
# Rest API Test Framework (Gorest API0


The project is a comprehensive API testing framework designed to ensure the reliability and security of Gorest APIs. Gorest APIs are freely accessible APIs that require a Bearer access token for certain operations. The framework is built with Python and Pytest, and it uses the Requests library for making HTTP requests.
The framework supports data-driven testing, positive/negative tests validation, and Pytest parameterizations for efficient testing of multiple data sets. It also includes a retry mechanism for handling limited request failures. The framework validates various aspects of the API responses, such as authentication, content-type, response time, pagination parameters, status codes, response structure, and response validation. Custom assertions are used to enhance test coverage.
The project also includes logging and detailed reporting features, providing insights into test results. Reports can be generated in HTML format or using Allure reports. The project is designed to be run locally, with dependencies managed through a `requirements.txt` file. The project also includes instructions for running the tests and generating reports.
In summary, this project is a robust and comprehensive framework for testing Gorest APIs, providing a range of features to ensure the reliability and security of the APIs.

## Points to know before running the project locally
- Signup to go rest for the access token https://gorest.co.in/
- store the access token in `conf.properties` file in `token` variable
- Access token is required for POST, PUT, PATCH and DELETE methods.
- Created data with a particular access token will only be available for same user and not to the rest.
- According to gorest we can access the GET request without Bearer token but the data created during tests won't be available to validate, Hence used Bearer token for GET requests also.
- Data will be removed on daily basis.
- Do check the website https://gorest.co.in for more details on `request-rate-limits` `pagination parameters` `status codes` `curl example for REST API`

## Run Locally 
- Clone the Project
```bash
git clone https://github.com/ankgupta16/RestApiAutomation.git
```
- Go to the project directory

```bash
cd RestApiAutomation
```

- Install dependencies

```bash
pip install -r requirements.txt
```
- Navigate to tests directory
```bash
cd tests
```

- Run all the tests

```bash
pytest -s -v
```


## Generating HTML reports


#### Pytest Html report
Dependensies
`pytest-html`
- Run the tests using following command
```bash
pytest test_filename.py -s -v -m "marker_name" --html=path_to_save_report/report.html
```
Generated Pytest HTML report.

### Details of arguments

| Parameter | Option     | Description                |
| :-------- |:-----------| :------------------------- |
| `pytest` | `required` | Pytest command to run the tests from terminal |
| `test_filename.py` | `optional` | To run the tests from specific file if not provided all the files with 'test_' or '_test' will be considered |
| `-s` | `optional` | for displaying console logs|
| `-v` | `optional` | for displaying additional details |
| `-m "marker_name"` | `optional` | To run the customised markers \| **Accepted values**: [positive, negative]|
| `--html="Path/file_name.html"` | `optional` | To generate the html report at given path  |

## Features

- GET, POST, PUT, PATCH, DELETE APIs Tested 
- API Test Automation
- RESTapis Testing
- Schema Validation
- Response data Validation
- Data driven tests 
- End-to-end tests 
- Positive/negative tests
- Pytest Parameterizations
- Logging 
- Interactive reporting [ HTML Reporting | Allure Reporting ]
- Retry mechanisam for limited requests
- Auth validations using Bearer token
- status code validation
- Searching | Pagination validation
- content-type | environment | response time validations
- Auth token verification
- Response body validation
- Custom assertions


## Developed using

- Python
- Pytest
- Requests library
- Allure reports
- Docker

## 🛠 Skills

`Python` `Pytest` `Allure reports` `Docker` `HTML reports` `Automation Testing` `API Testing`  `RESTapi`