import unittest

import json

from console import Console

class ResponseStub():
    def __init__(self):
        self.status_code = 200
        self.text = json.dumps({'SigninToken': "abc"})

class RequestsStub():
    def get(self, url):
        return ResponseStub()

class TestConsole(unittest.TestCase):
    def test_success(self):
        credentials_json = json.dumps({
                'sessionId': 'id',
                'sessionKey': 'key',
                'sessionToken': 'token'
                })
        issuer = "example.org"
        c = Console()
        c.requests = RequestsStub()
        result = c.generate_console_url(credentials_json)
        expected = "https://signin.aws.amazon.com/federation?Action=login&Issuer=https://github.com/weavenet/aws_console&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2F&SigninToken=abc"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
