# Api

<a href="https://surajsarkar.pythonanywhere.com/api/user?name=surajsarkar">https://surajsarkar.pythonanywhere.com/api/user?name=surajsarkar </a>

* Right now it only has 1 endpoint (the above one mentioned, passing my username as argument).
* It filters every required data and sends it as json
* It is deployed on **pythonanywhere**


### Endpoint ⬇️  
 Only supports `GET` request
```python
https://surajsarkar.pythonanywhere.com/api/user?name=<github_username>
```
### Run test cases
```commandline
pytest <test_file_path>
#eg
pytest ./tests/test.py
```
