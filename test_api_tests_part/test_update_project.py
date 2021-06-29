import json

import requests


def test_002_update_project():
    auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')

    payload = {"description": {"raw": "this is the new description!!"}}
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.patch("http://localhost:8080/api/v3/projects/34/", auth=auth_params, headers=headers,
                              data=json.dumps(payload))
    print(response.json())
    print(response.json()["description"]["raw"])

    assert response.json()["description"]["raw"] == payload["description"][
        "raw"], f"test update project fail. expected result {payload['description']['raw']}"
