from test_api_tests_part.api_utils import create_random_project_name, \
    create_work_pack, search_work_pack_in_project_by_subject, \
    delete_work_pack_by_id, get_work_package_by_id, change_project_description, load_json_file, \
    update_project, get_work_pack_by_id, get_project_lock_version, change_task_description, \
    create_project_by_name, delete_project_by_id, get_project_by_id, \
    check_project_until_delete

from test_api_tests_part.rest_client import HttpClient
import random

json = load_json_file()
test_url = json["api"]["proj_by_id"]["url_for_testing"]
package_id = "38"
package_type = "Task"
package_description = "My Task 1"
headers = {
    'Content-Type': 'application/json',
}
url_for_testing = "http://localhost:8080//api/v3/"
project_id = "34"
test_url = "http://localhost:8080/api/v3"
payload = {"description": {"raw": "this is the new description!!"}}
work_pack_id = "38"
base_url = "http://localhost:8080/api/v3"
json = load_json_file()
project_name = json["api"]["proj_by_id"]["project_name"]
project_desc = json["api"]["proj_by_id"]["project_desc"]
auth_params = (json["api"]["proj_by_id"]["auth_params"][0], json["api"]["proj_by_id"]["auth_params"][1])
headers = json["api"]["proj_by_id"]["headers"]
response = HttpClient(f"http://localhost:8080/api/v3/projects/{project_id}/", auth_params).get_request()

project_id = "34"
auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
test_url = f"http://localhost:8080/api/v3/projects"
delete_url = "http://localhost:8080/api/v3/work_packages"
body_for_test = {
    "subject": "newly created work pack for deletion"
}
headers_for_test = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YXBpa2V5OjY5Zjk2YmIzZWI0NjY5ODM5YzQ0NWM0MzgzNDZjOTJmZTk0MzNkMDEyOThmMjJkNjBkYTczNTMyMWJiYjRhOTM='
}
full_creation_url = f"{test_url}/{project_id}//work_packages"
test_url = "http://localhost:8080//api/v3/projects"


def test_update_work_pack():
    work_pack = get_work_pack_by_id(url_for_testing, auth_params, package_id)
    lock_ver = get_project_lock_version(work_pack)
    payload = {
        "lockVersion": str(lock_ver),
        "description": {"raw": "this is the new task description!"}
    }
    change_task_description(url_for_testing, auth_params, payload, package_id)
    response = get_work_pack_by_id(url_for_testing, auth_params, package_id)
    new_description = response.json()["description"]["raw"]
    print("new task description: ", new_description)
    assert new_description == payload["description"][
        "raw"], f" update work package test fail!, current task description {new_description}"


def test_002_update_project():
    response_for_test = update_project(test_url, project_id, auth_params, payload)
    print("new description change: ", response_for_test.json()["description"]["raw"])

    assert response_for_test.json()["description"]["raw"] == payload["description"][
        "raw"], f"test update project fail. expected result {payload['description']['raw']}"


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


def test_delete_work_package():
    create_response = create_work_pack(full_creation_url, auth_params, body_for_test)
    print("work pack create response: ", create_response)
    work_pack_id = search_work_pack_in_project_by_subject(full_creation_url, auth_params, body_for_test["subject"])[
        "id"]
    delete_wp = delete_work_pack_by_id(delete_url, headers_for_test, work_pack_id)
    assert delete_wp.status_code == 204, f"delete process failed! response:{delete_wp}"
    check_if_deleted = get_work_package_by_id(test_url, auth_params, project_id)
    print(f"deletion check: search response for WP: {check_if_deleted.status_code}")
    assert check_if_deleted != 404, f"test_delete_work_package faild!, chack deleterd WP response not 404! current response:{check_if_deleted.status_code}"


def test_004_delete_project():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    payload_for_test = {
        "name": f"project to delete{rand_str_numbers}"
    }

    create_response = create_project_by_name(test_url, auth_params, payload_for_test)
    print(f"created new project named: {create_response.json()['identifier']}")
    project_id_to_delete = create_response.json()["id"]
    delete_request = delete_project_by_id(test_url, headers_for_test, project_id_to_delete)
    print("delete request response: ", delete_request)
    delete_check = check_project_until_delete(test_url, auth_params, project_id_to_delete)
    assert not delete_check, f"delete project test failed, delete request status:{delete_request.status_code}"


def test_create_work_pack():
    url_for_this_test = f"http://localhost:8080/api/v3/projects/{project_id}/work_packages"
    body_for_the_test = {
        "subject": "newly created work pack for test"
    }
    response = create_work_pack(url_for_this_test, auth_params, body_for_the_test)
    print("work package creation status: ", response.status_code)
    check_if_exc = search_work_pack_in_project_by_subject(url_for_this_test, auth_params, body_for_the_test["subject"])
    print("work pack created in project: ", check_if_exc)
    assert check_if_exc, f"create work pack test fail!, work pack created: {check_if_exc}"


def test_003_create_project():
    project_rand_name = create_random_project_name()
    project_rand_expected_name = project_rand_name.replace(" ", "-")
    payload_for_test = {"description": {"raw": "this is a new test project"}, "name": project_rand_name}
    res = create_project_by_name(test_url, auth_params, payload_for_test)

    print(f"response status: {res.status_code}")

    assert res.json()["identifier"] == project_rand_expected_name, \
        f"failed create project test!" f" expected name result{project_rand_expected_name}"
