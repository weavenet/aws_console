#!/usr/bin/env python3.6

import json
import os
import sys

from aws_console.console import Console

def run():
    try:
        credentials_json = json.dumps({
                'sessionId': os.environ['AWS_ACCESS_KEY_ID'],
                'sessionKey': os.environ['AWS_SECRET_ACCESS_KEY'],
                'sessionToken': os.environ['AWS_SESSION_TOKEN']
                })
        issuer = "example.org"
        url = Console().generate_console_url(issuer, credentials_json)
        print(url)
    except Exception as e:
        print("Received error:", e)
        sys.exit(1)
