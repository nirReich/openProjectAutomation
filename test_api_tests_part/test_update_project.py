import pytest

from test_api_tests_part.api_utils import update_project, load_json_file

json = load_json_file()
project_id = json["api"]["proj_by_id"]["project_id"]
test_url = json["api"]["proj_by_id"]["base_url"]
auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
payload = {"description": {"raw": "this is the new description!!"}}


@pytest.mark.project_api_sanity
def test_002_update_project():
    response = update_project(test_url, project_id, auth_params, payload)
    print("new description change: ", response.json()["description"]["raw"])

    assert response.json()["description"]["raw"] == payload["description"][
        "raw"], f"test update project fail. expected result {payload['description']['raw']}"
