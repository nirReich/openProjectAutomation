import requests


class HttpClient:
    '''class that handles http requests. includes 4 requests: get,post,patch and delete.'''

    def __init__(self, base_url: str, base_headers: tuple):
        self.base_url = base_url
        self.base_headers = base_headers

    def get_request(self):
        response = requests.get(url=self.base_url, auth=self.base_headers)
        return response

    def post_request(self, data: dict):
        response = requests.post(url=self.base_url, auth=self.base_headers, data=data)
        return response

    def patch_request(self, data, json):
        response = requests.patch(url=self.base_url, auth=self.base_headers, data=data)
        return response

    def delete_request(self, data: dict):
        response = requests.delete(url=self.base_url, auth=self.base_headers, data=data)
