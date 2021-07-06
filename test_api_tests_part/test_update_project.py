from test_api_tests_part.api_utils import update_project
from test_api_tests_part.rest_client import HttpClient

project_id = "34"
test_url = "http://localhost:8080/api/v3"
auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
payload = {"description": {"raw": "this is the new description!!"}}


def test_002_update_project():
    response = update_project(test_url, project_id, auth_params, payload)
    print("new description change: ", response.json()["description"]["raw"])

    assert response.json()["description"]["raw"] == payload["description"][
        "raw"], f"test update project fail. expected result {payload['description']['raw']}"
