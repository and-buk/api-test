[![tests](https://github.com/and-buk/api-test/actions/workflows/tests.yml/badge.svg)](https://github.com/and-buk/api-test/actions/workflows/tests.yml)

This repository contains REST API Testing automation code using Python

The project uses:
1. Python 3.9 and higher
2. Pytest
3. Requests
4. Allure Framework for reports
5. CI (GitHub actions)

Testing application:

git: https://github.com/berpress/flask-restful-api

url: https://stores-tests-api.herokuapp.com

swagger: https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0

### How to start

By using Windows Terminal, Python and pip
1. Place the repository files into the directory of your choice
2. Create virtual environment
```
py -m venv env
```
2. Activate created virtual environment  
```
env\Scripts\activate
```
3. Install project's dependencies  
```
pip install -r requirements.txt
```
4. Install [pre-commit](https://pre-commit.com/)
```
pip install pre-commit 
```
5. Install [Allure Framework](https://docs.qameta.io/allure/)
6. Install [Java](https://www.java.com/en/download/help/windows_manual_download.html)

### How to run tests

- **Without Allure Test report**

All tests:
```
pytest
```
Positive tests:
```
pytest -m positive
```
Negative tests:
```
pytest -m negative
```
- **With Allure Test report**
```
pytest --alluredir=allure_reports
```
Show generated report in browser:
```
allure serve allure_reports
```
