from test_api_tests_part.api_utils import get_project_by_id, change_project_description,load_json_file
from test_api_tests_part.rest_client import HttpClient

json= load_json_file()
project_id = json["api"]["proj_by_id"]["project_id"]
project_name = json["api"]["proj_by_id"]["project_name"]
project_desc = json["api"]["proj_by_id"]["project_desc"]
auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
headers = json["api"]["proj_by_id"]["headers"]
url_for_testing = json["api"]["proj_by_id"]["url_for_testing"]
response = HttpClient(f"http://localhost:8080/api/v3/projects/{project_id}/", auth_params).get_request()


def test_project_status_code():
    res_call_proj = get_project_by_id(url_for_testing, auth_params, project_id)
    assert res_call_proj.status_code == 200, f"status code test fail!, current status:{response.status_code}"
    print(response)


def test_project_name():
    res_call_proj = get_project_by_id(url_for_testing, auth_params, project_id)
    res_project_name = res_call_proj.json()["identifier"]
    print(f"project name: {res_project_name}")

    assert res_project_name == str(project_name), f"project name test fail! current name: {res_project_name}"


def test_project_description():
    res_call_proj = get_project_by_id(url_for_testing, auth_params, project_id)
    res_project_description = res_call_proj.json()["description"]["raw"]
    print(f"project description: {res_project_description}")

    assert res_project_description == project_desc, f"project description test fail! current description{res_project_description}"


# -----updating project part-----:

def test_002_update_project():
    payload = {"description": {"raw": "this is the new description!!"}}
    res = change_project_description(url_for_testing, project_id, auth_params, payload)
    print(res.json()["description"]["raw"])

    assert response.json()["description"]["raw"] == payload["description"][
        "raw"], f"test update project fail. expected result {payload['description']['raw']}"
    # changing back to previous description
    change_project_description(url_for_testing, project_id, auth_params, {"description": {"raw": project_desc}})
