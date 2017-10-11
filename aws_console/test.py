import unittest

import json

from console import Console

class ResponseStub():
    def __init__(self):
        self.status_code = 200
        self.text = json.dumps({'SigninToken': "abc"})

class ResponseErrorStub():
    def __init__(self):
        self.status_code = 400
        self.text = "an error"

class RequestsStub():
    def get(self, url):
        if url != "https://signin.aws.amazon.com/federation?Action=getSigninToken&Session=%7B%22sessionId%22%3A+%22id%22%2C+%22sessionKey%22%3A+%22key%22%2C+%22sessionToken%22%3A+%22token%22%7D":
            raise Exception("Unexpected url {}".format(url))
        return ResponseStub()

class RequestsErrorStub():
    def get(self, url):
        return ResponseErrorStub()

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.credentials_json = json.dumps({
                'sessionId': 'id',
                'sessionKey': 'key',
                'sessionToken': 'token'
                })
        self.c = Console()

    def test_success(self):
        self.c.requests = RequestsStub()
        result = self.c.generate_console_url(self.credentials_json)
        expected = "https://signin.aws.amazon.com/federation?Action=login&Issuer=https://github.com/weavenet/aws_console&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2F&SigninToken=abc"
        self.assertEqual(result, expected)

    def test_error(self):
        try:
            self.c.requests = RequestsErrorStub()
            self.c.generate_console_url(self.credentials_json)
        except Exception as e:
            self.assertEqual("Error getting sigin in token (code 400): an error", str(e))

if __name__ == '__main__':
    unittest.main()
