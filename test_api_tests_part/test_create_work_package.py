from test_api_tests_part.rest_client import HttpClient
from test_api_tests_part.api_utils import create_work_pack, search_work_pack_in_project_by_subject

def test_create_work_pack():
    project_id = "34"
    auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
    url_for_test = f"http://localhost:8080/api/v3/projects/{project_id}/work_packages"
    body_for_test = {
        "subject": "newly created work pack for test"
    }
    response = create_work_pack(url_for_test, auth_params, body_for_test)
    print("work package creation status: ", response.status_code)
    check_if_exc = search_work_pack_in_project_by_subject(url_for_test, auth_params, body_for_test["subject"])
    print("work pack created in project: ", check_if_exc)
    assert check_if_exc, f"create work pack test fail!, work pack created: {check_if_exc}"
