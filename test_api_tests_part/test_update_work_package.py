import json

import requests

from test_api_tests_part import rest_client

project_id = "34"
package_type = "Task"
package_description = "My Task 1"
lock_version = ''
auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
headers = {
    'Content-Type': 'application/json',
}
url_for_testing = f"http://localhost:8080//api/v3/work_packages/{project_id}/"


def get_project_lockversion(url, auth) -> lock_version:
    # getting the lockversion of the project
    response_lock_version = rest_client.HttpClient(url, auth).get_request()
    print("lockversion is:", response_lock_version.json()["lockVersion"])
    return str(response_lock_version.json()["lockVersion"])


lock_version = get_project_lockversion(url_for_testing, auth_params)
payload = {
    "lockVersion": lock_version,
    "description": {"raw": "this is the new task description!"}
}


def change_task_description(url, auth, req_head, data=json):
    requests.patch(url=url, auth=auth, headers=req_head, data=data)


def test_update_work_pack():
    get_project_lockversion(url_for_testing, auth_params)
    change_task_description(url_for_testing, auth_params, headers, json.dumps(payload))
    response = rest_client.HttpClient(url_for_testing, auth_params).get_request()
    new_description=response.json()["description"]["raw"]
    print("new task description: ",new_description)
    assert new_description == payload["description"]["raw"], f" update work package test fail!, current task description {new_description}"
