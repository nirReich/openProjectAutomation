import json
import random
import time

import requests

from test_api_tests_part import rest_client


def test_004_delete_project():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    payload = json.dumps({
        "description": {
            "raw": f"this is a project {rand_str_numbers} to delete."
        },
        "name": f"project to delete{rand_str_numbers}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YXBpa2V5OjY5Zjk2YmIzZWI0NjY5ODM5YzQ0NWM0MzgzNDZjOTJmZTk0MzNkMDEyOThmMjJkNjBkYTczNTMyMWJiYjRhOTM='
    }

    create_response = requests.post("http://localhost:8080/api/v3/projects", headers=headers, data=payload)
    project_id_to_delete = create_response.json()["id"]
    print(create_response.json())
    delete_request = requests.delete(f"http://localhost:8080//api/v3/projects/{project_id_to_delete}",
                                     headers=headers)
    print("delete request response: ", delete_request)
    assert delete_request, f"delete project test failed, delete request status:{delete_request.status_code}"









# the rest client class usage example:
# get = rest_client.HttpClient("http://localhost:8080/api/v3/projects/61").get_request(auth=(('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')))
