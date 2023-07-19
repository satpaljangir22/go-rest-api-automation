import requests


class APICalls:

    def __init__(self):
        self.base_url = "https://gorest.co.in"
        self.request_header = {
            "Authorization": "Bearer 61189c08b723b85b8787fa3296e5b0efa8eae0d46ff79463d84a834683ad119d"
        }

    def get_request(self, user_id=""):
        request_url = self.base_url + f"/public/v2/users/{user_id}"
        response = requests.get(request_url, headers=self.request_header)
        status = response.status_code
        content = response.json()
        return status, content

    def post_request(self, payload: dict):
        request_url = self.base_url + "/public/v2/users"
        response = requests.post(request_url, json=payload, headers=self.request_header)
        status = response.status_code
        content = response.json()
        return status, content

    def put_request(self, payload: dict, user_id):
        request_url = self.base_url + f"/public/v2/users/{user_id}"
        response = requests.put(request_url, json=payload, headers=self.request_header)
        status = response.status_code
        content = response.json()
        return status, content

    def delete_request(self, user_id):
        request_url = self.base_url + f"/public/v2/users/{user_id}"
        response = requests.delete(request_url, headers=self.request_header)
        status = response.status_code
        content = response.json()
        return status, content


def config_context(context):
    context.api_operations = APICalls()


def tear_down(context):
    context.api_operations = None
