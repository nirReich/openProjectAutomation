import json
import random
import string
import time
from test_api_tests_part.rest_client import HttpClient


def load_json_file():
    with open("general_variables_api.json") as json_file:
        json_object = json.load(json_file)
        json_file.close()
        return json_object


def get_project_by_id(req_url: str, auth: tuple, proj_id: int):
    full_url = f"{req_url}/{proj_id}"
    proj_res = HttpClient(full_url, auth).get_request()
    return proj_res


def change_project_description(url, proj_id, auth, new_desc):
    full_url = f"{url}/{proj_id}"
    response = HttpClient(full_url, auth).patch_request(new_desc)
    print(f"change_project_description func: description change response: {response}")
    return response


def update_project(url, proj_id, auth, data):
    response = HttpClient(f"{url}/projects/{proj_id}/", auth).patch_request(data)
    print(f"update_project func: project updated status: {response}")
    return response


def create_random_project_name():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    rand_str_letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    project_rand_name = str("project " + rand_str_numbers + ' ' + rand_str_letters)
    return project_rand_name


def create_project_by_name(url, auth, payload: dict):
    response = HttpClient(url, auth).post_request(payload)
    print(f'create_project_by_name func: new project named {payload["name"]} created!')
    return response


def delete_project_by_id(url: str, headers: dict, proj_id: int):
    delete_request = HttpClient(f"{url}/{proj_id}", headers).delete_request()
    print(f"delete_project_by_id func: delete request status: {delete_request.status_code}")
    return delete_request


def get_work_pack_by_id(req_url, auth, pack_id):
    full_url = f"{req_url}/work_packages/{pack_id}"
    response = HttpClient(full_url, auth).get_request()
    print(f"get_work_package_by_id_func: getting WP, status: {response.status_code}")
    return response


def get_project_lock_version(package):
    lock_ver = package.json()["lockVersion"]
    print("lock version is:", lock_ver)
    return lock_ver


def change_task_description(url, auth, data, pack_id):
    full_url = f"{url}/work_packages/{pack_id}"
    response = HttpClient(full_url, auth).patch_request(data)
    print(f"change_task_description func: change description request status: {response}")


def create_work_pack(url: str, auth: tuple, json: dict):
    response_create = HttpClient(url, auth).post_request(json)
    print(print("work package creation status: ", response_create.status_code))
    return response_create


def search_work_pack_in_project_by_subject(url: str, auth: tuple, subject: str) -> bool:
    res_check_get = HttpClient(url, auth).get_request()
    work_packs = res_check_get.json()['_embedded']['elements']
    for pack in work_packs:
        if pack['subject'] == subject:
            return pack


def delete_work_pack_by_id(url, auth, wp_id):
    full_url = f"{url}/{wp_id}"
    delete_res = HttpClient(full_url, auth).delete_request()
    print(f"delete work pack by id func: deleting WP {wp_id} sent. status {delete_res.status_code}")
    return delete_res


def get_work_package_by_id(req_url, auth, proj_id):
    full_url = f"{req_url}/projects/{proj_id}/work_packages"
    response = HttpClient(full_url, auth).get_request()
    print(f"get_work_package_by_id_func: getting WP, status: {response.status_code}")
    return response


def check_project_until_delete(url, auth, proj_id) -> "returns false if deleted or true if not":
    condition = True
    counter = 0
    while condition:
        delete_check = get_project_by_id(url, auth, proj_id)
        if delete_check.status_code == 200 and counter <= 20:
            time.sleep(0.5)
            counter += 1
            status = delete_check.status_code
        else:
            condition = False
    message = f"check_project_until_delete func: project still exist?:{condition}"
    print(message)
    return condition
