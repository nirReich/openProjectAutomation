import requests


class TestGetWorkPackage:
    project_id = "34"
    package_type = "Task"
    package_description = "My Task 1"
    auth_params = ('apikey', '69f96bb3eb4669839c445c438346c92fe9433d01298f22d60da735321bbb4a93')

    response = requests.get(f"http://localhost:8080//api/v3/work_packages/{project_id}/", auth=auth_params)

    def test_response_status_code(self):
        print(self.response.json())
        print("response status: ", self.response.status_code)
        assert self.response.status_code == 200, f"get work package test fail!, request status: {self.response.status_code}"

    def test_packedge_type(self):
        current_pack_type = self.response.json()["_embedded"]["type"]["name"]
        print(current_pack_type)
        assert current_pack_type == self.package_type, f"package type test fail!, current type: {current_pack_type}"

    def test_work_package_subject(self):
        current_pack_subject = self.response.json()["_links"]["self"]["title"]
        print(f"Work package subject is:{current_pack_subject}")
        assert current_pack_subject == self.package_description, f"package subject test fail! current subject: {current_pack_subject}"
