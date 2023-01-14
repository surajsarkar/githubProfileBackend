import requests


# test with valid username shold have a key user_present with value ture


def test_correct_username():
    url = "http://localhost:5000/api/user?name=surajsarkar"
    response = requests.get(url)
    assert response.status_code == 200
    user_details = response.json()
    assert "user_present" in user_details
    assert user_details["user_present"] == True


def test_incorrect_username():
    url = "http://localhost:5000/api/user?name=dlfjdlkfkjdlkfj"
    response = requests.get(url)
    assert response.status_code == 200
    user_details = response.json()
    assert "user_present" in user_details
    assert user_details["user_present"] == False
    assert len(user_details) == 1

