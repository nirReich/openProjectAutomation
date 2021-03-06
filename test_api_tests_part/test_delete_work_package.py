import pytest

from test_api_tests_part.api_utils import create_work_pack, search_work_pack_in_project_by_subject, \
    delete_work_pack_by_id, get_work_package_by_id,load_json_file

json = load_json_file()
project_id = json["api"]["proj_by_id"]["project_id"]
auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
test_url = json["api"]["proj_by_id"]["url_for_testing"]
delete_url = json["api"]["proj_by_id"]["delete_url"]
body_for_test = {
    "subject": "newly created work pack for deletion"
}
headers = json["api"]["work_pac"]["headers_for_delete"]
full_creation_url = f"{test_url}/{project_id}//work_packages"


@pytest.mark.work_pack_api_sanity
def test_delete_work_package():
    create_response = create_work_pack(full_creation_url, auth_params, body_for_test)
    print("work pack create response: ", create_response)
    work_pack_id = search_work_pack_in_project_by_subject(full_creation_url, auth_params, body_for_test["subject"])[
        "id"]
    delete_wp = delete_work_pack_by_id(delete_url, headers, work_pack_id)
    assert delete_wp.status_code == 204, f"delete process failed! response:{delete_wp}"
    check_if_deleted = get_work_package_by_id(test_url, auth_params, project_id)
    print(f"deletion check: search response for WP: {check_if_deleted.status_code}")
    assert check_if_deleted != 404, f"test_delete_work_package faild!, chack deleterd WP response not 404! current response:{check_if_deleted.status_code}"
