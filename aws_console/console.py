#!/usr/bin/env python3.6

import json
import os
import requests
import sys
import urllib

class Console():
    def __generate_federation_request_parameters(self, credentials_json):
        request_parameters = "?Action=getSigninToken"
        request_parameters += "&SessionDuration=3600"
        request_parameters += "&Session=" + urllib.parse.quote_plus(credentials_json)
        return request_parameters

    def __generate_sign_in_token(self, credentials_json):
        request_parameters = self.__generate_federation_request_parameters(credentials_json)
        request_url = "https://signin.aws.amazon.com/federation" + request_parameters
        r = requests.get(request_url)
        if (r.status_code != 200):
            raise Exception("Error getting sigin in token", r.status_code, r.text)
        return json.loads(r.text)['SigninToken']

    def __generate_signin_request_parameters(self, signin_token, issuer):
        request_parameters = "?Action=login" 
        request_parameters += "&Issuer=" + issuer
        request_parameters += "&Destination=" + urllib.parse.quote_plus("https://console.aws.amazon.com/")
        request_parameters += "&SigninToken=" + signin_token
        return request_parameters

    def __generate_signed_url(self, signin_token, issuer):
        request_parameters = self.__generate_signin_request_parameters(signin_token, issuer)
        return "https://signin.aws.amazon.com/federation" + request_parameters

    def generate_console_url(self, issuer, credentials_json):
        signin_token = self.__generate_sign_in_token(credentials_json)
        return self.__generate_signed_url(signin_token, issuer)
