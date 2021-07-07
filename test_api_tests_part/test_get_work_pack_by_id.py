import pytest

from test_api_tests_part.api_utils import get_work_pack_by_id, load_json_file

json = load_json_file()
package_type = json["api"]["work_pac"]["package_type"]
package_description = json["api"]["work_pac"]["package_description"]
work_pack_id = json["api"]["work_pac"]["work_pack_id"]
auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
base_url = json["api"]["proj_by_id"]["base_url"]


@pytest.mark.work_pack_api_sanity
def test_response_status_code():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    print("response status: ", response.status_code)
    assert response.status_code == 200, f"get work package test fail!, request status: {response.status_code}"


@pytest.mark.work_pack_api_sanity
def test_package_type():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    current_pack_type = response.json()["_embedded"]["type"]['name']
    print(f"pack type: {current_pack_type}")
    assert current_pack_type == package_type, f"package type test fail!, current type: {current_pack_type}"


@pytest.mark.work_pack_api_sanity
def test_work_package_subject():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    current_pack_subject = response.json()["subject"]
    print(f"work package subject is:{current_pack_subject}")
    assert current_pack_subject == package_description, f"package subject test fail! current subject: {current_pack_subject}"
