import requests

project_id = "34"
url_for_test = f"http://localhost:8080//api/v3/work_packages/{project_id}/"

response = requests.post(url_for_test)