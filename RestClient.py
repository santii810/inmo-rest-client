import logging

import requests


class RestClient:
    def __init__(self, backend_url):
        self.server_url = backend_url
        self.headers = {"Content-Type": "application/json", "Host": "127.0.0.1:8080"}

    def send_ad(self, json: dict):
        method = "PUT"
        url = f"{self.server_url}/inmo/ad"
        logging.info(f"Sending {method} {url} body: {json}")
        response = requests.request(method=method, url=url, json=json, headers=self.headers)
        if response.status_code == 201:
            logging.info("Add request Ok")
        else:
            logging.error(f"Error in API connection code:{response.status_code} error:{response.content} ")
