#!/usr/bin/env python3.6

import json
import sys
import boto3

from aws_console.console import Console

def get_url_via_credentials():
    session = boto3.Session()        
    credentials = session.get_credentials()        
    frozen_credentials = credentials.get_frozen_credentials()        
    credentials_json = json.dumps({
           'sessionId': frozen_credentials.access_key,        
           'sessionKey': frozen_credentials.secret_key,        
           'sessionToken': frozen_credentials.token        
           })
    return Console().generate_console_url(credentials_json)

def run():
    try:
        print(get_url_via_credentials())
    except Exception as e:
        print("Received error:", e)
        sys.exit(1)
