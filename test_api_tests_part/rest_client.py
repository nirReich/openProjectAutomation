import requests


class HttpClient:
    """
     This class call handles http requests. includes 4 requests: get,post,patch and delete.
    """

    def __init__(self, base_url: str, base_headers: tuple):
        self.url = base_url
        self.headers = base_headers

    def get_request(self):
        response = requests.get(url=self.url, auth=self.headers)
        return response

    def post_request(self, data: dict):
        response = requests.post(url=self.url, auth=self.headers, json=data)
        return response

    def patch_request(self, data):
        response = requests.patch(url=self.url, auth=self.headers, json=data)
        return response

    def delete_request(self):
        response = requests.delete(url=self.url, headers=self.headers)
        return response
