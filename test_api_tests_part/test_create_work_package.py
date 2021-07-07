import pytest

from test_api_tests_part.api_utils import create_work_pack, search_work_pack_in_project_by_subject, load_json_file

json = load_json_file()


@pytest.mark.work_pack_api_sanity
def test_create_work_pack():
    project_id = json["api"]["proj_by_id"]["project_id"]
    auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
    url_for_test = f'{json["api"]["proj_by_id"]["url_for_testing"]}/{project_id}/work_packages'
    body_for_test = {
        "subject": "newly created work pack for test"
    }
    response = create_work_pack(url_for_test, auth_params, body_for_test)
    print("work package creation status: ", response.status_code)
    check_if_exc = search_work_pack_in_project_by_subject(url_for_test, auth_params, body_for_test["subject"])
    print("work pack created in project: ", check_if_exc)
    assert check_if_exc, f"create work pack test fail!, work pack created: {check_if_exc}"
