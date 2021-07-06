from test_api_tests_part.api_utils import get_work_pack_by_id

package_type = "Task"
package_description = "My Task 1"
work_pack_id = "38"
auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
base_url = "http://localhost:8080/api/v3"


def test_response_status_code():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    print("response status: ", response.status_code)
    assert response.status_code == 200, f"get work package test fail!, request status: {response.status_code}"


def test_package_type():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    current_pack_type = response.json()["_embedded"]["type"]['name']
    print(f"pack type: {current_pack_type}")
    assert current_pack_type == package_type, f"package type test fail!, current type: {current_pack_type}"


def test_work_package_subject():
    response = get_work_pack_by_id(base_url, auth_params, work_pack_id)
    current_pack_subject = response.json()["subject"]
    print(f"work package subject is:{current_pack_subject}")
    assert current_pack_subject == package_description, f"package subject test fail! current subject: {current_pack_subject}"
