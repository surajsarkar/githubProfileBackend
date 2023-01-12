from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


def request_user_details(username: str):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        info = response.json()
        return {
            "name": info["name"],
            "avatar_url": info["avatar_url"],
            "bio": info["bio"],
            "profile_link": info["html_url"],
            "location": info["location"],
            "twitter_username": info["twitter_username"],
            "repos": info["repos_url"],
        }
    return response.json()


def filter_repo_detail(userdata: dict):
    response = requests.get(userdata["repos"])
    filtered_repos = []
    if response.status_code == 200:
        repos = response.json()
        total_no_of_repo = len(repos)

        for repo in repos:
            filtered_repo = {
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "topics": repo["topics"],
            }
            filtered_repos.append(filtered_repo)
    userdata["repos"] = filtered_repos
    return userdata


def filter_repo_language(languages_url: str):
    # todo: filter topoics intead of language
    response = requests.get(languages_url)
    if response.status_code == 200:
        return response.json()


def fetch_and_organise_data(username: str):
    user_details = request_user_details(username)

    if not user_details.get("message") == "Not Found":
        prepared_user_and_repo_details = filter_repo_detail(userdata=user_details)
        prepared_user_and_repo_details["user_present"] = True
        return prepared_user_and_repo_details
    return {"user_present": False}


@app.route("/api/user", methods=["GET"])
def get_user_details():
    username = request.args["name"]
    user_github_details = fetch_and_organise_data(username=username)

    return jsonify(user_github_details)


if __name__ == "__main__":
    app.run(debug=True)
