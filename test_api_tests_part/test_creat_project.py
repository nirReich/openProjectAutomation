import json
import random
import string

import requests


def test_003_create_project():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    rand_str_letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    project_rand_name = str("project " + rand_str_numbers + ' ' + rand_str_letters)
    project_rand_expected_name = project_rand_name.replace(" ", "-")

    payload = json.dumps({
        "description": {
            "raw": "this is a new test project.."
        },
        "name": project_rand_name
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YXBpa2V5OjY5Zjk2YmIzZWI0NjY5ODM5YzQ0NWM0MzgzNDZjOTJmZTk0MzNkMDEyOThmMjJkNjBkYTczNTMyMWJiYjRhOTM='
    }
    response = requests.post("http://localhost:8080/api/v3/projects", headers=headers, data=payload)

    print(response.text)
    print(f"response status: {response.status_code}")

    assert response.json()["identifier"] == project_rand_expected_name, \
        f"faild creat project test!" f" expected name result{project_rand_expected_name}"
