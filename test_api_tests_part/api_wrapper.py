import json

from test_api_tests_part import rest_client


def get_project_by_id(url, proj_id, auth):
    full_url = f"{url}{proj_id}/"
    response = rest_client.HttpClient(full_url, json.dumps(auth)).get_request()
    return response.json()


testing = get_project_by_id("http://localhost:8080//api/v3/projects/", "34",
                  ("apikey", "69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93"))
print(testing)