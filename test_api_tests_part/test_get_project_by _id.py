import pytest

import requests

from test_api_tests_part import rest_client


class TestGetProjectById:
    project_id = "34"
    project_name = "testproject1"
    project_desc = 'This is the first test project'
    auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
    response = rest_client.HttpClient(f"http://localhost:8080//api/v3/projects/{project_id}/", auth_params).get_request()
    print(response)

    def test_project_status_code(self):
        assert self.response.status_code == 200, f"status code test fail!, current status:{self.response.status_code}"
        print(self.response)

    def test_project_name(self):
        res_project_name = self.response.json()["identifier"]
        print(f"project name: {res_project_name}")

        assert res_project_name == str(self.project_name), f"project name test fail! current name: {res_project_name}"

    def test_project_description(self):
        res_project_description = self.response.json()["description"]["raw"]
        print(f"project description: {res_project_description}")

        assert res_project_description == self.project_desc, f"project description test fail! current description{res_project_description}"
