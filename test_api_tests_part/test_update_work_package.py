from test_api_tests_part.api_utils import get_work_pack_by_id, get_project_lock_version, change_task_description

package_id = "38"
package_type = "Task"
package_description = "My Task 1"
auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')
headers = {
    'Content-Type': 'application/json',
}
url_for_testing = "http://localhost:8080//api/v3/"


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
