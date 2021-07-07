import pytest

from test_api_tests_part.api_utils import create_random_project_name, create_project_by_name, load_json_file

json = load_json_file()
test_url = json["api"]["proj_by_id"]["url_for_testing"]


@pytest.mark.project_api_sanity
def test_003_create_project():
    project_rand_name = create_random_project_name()
    project_rand_expected_name = project_rand_name.replace(" ", "-")

    payload = {"description": {"raw": "this is a new test project.."}, "name": project_rand_name}
    headers = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
    response = create_project_by_name(test_url, headers, payload)
    print(f"response status: {response.status_code}")

    assert response.json()["identifier"] == project_rand_expected_name, \
        f"failed create project test!" f" expected name result{project_rand_expected_name}"
