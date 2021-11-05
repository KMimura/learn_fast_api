import requests
import unittest

BASE_URL='http://127.0.0.1:8000/'

class api_test(unittest.TestCase):
    def test_post(self):
        request_url = BASE_URL + 'items'
        request_body = {'name':'test','price':100}
        response = requests.post(request_url,json=request_body)
        print(response.json())

unittest.main()