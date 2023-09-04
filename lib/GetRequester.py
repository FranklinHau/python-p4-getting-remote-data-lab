import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        '''Fetch the raw response content (as bytes) from the URL.'''
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        '''Fetch the response content, parse it as JSON, and return the resulting object.'''
        response = requests.get(self.url)
        return response.json()