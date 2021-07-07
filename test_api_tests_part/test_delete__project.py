import random

import pytest

from test_api_tests_part.api_utils import create_project_by_name, delete_project_by_id, check_project_until_delete

test_url = "http://localhost:8080//api/v3/projects"


@pytest.mark.project_api_sanity
def test_004_delete_project():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    payload = {
        "name": f"project to delete{rand_str_numbers}"
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YXBpa2V5OjY5Zjk2YmIzZWI0NjY5ODM5YzQ0NWM0MzgzNDZjOTJmZTk0MzNkMDEyOThmMjJkNjBkYTczNTMyMWJiYjRhOTM='
    }
    auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')

    create_response = create_project_by_name(test_url, auth_params, payload)
    print(f"created new project named: {create_response.json()['identifier']}")
    project_id_to_delete = create_response.json()["id"]
    delete_request = delete_project_by_id(test_url, headers, project_id_to_delete)
    print("delete request response: ", delete_request)
    delete_check = check_project_until_delete(test_url, auth_params, project_id_to_delete)
    assert not delete_check, f"delete project test failed, delete request status:{delete_request.status_code}"
