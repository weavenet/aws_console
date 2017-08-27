#!/usr/bin/env python3.6

import json
import os
import sys, getopt
import getpass

import boto3

from aws_console.console import Console
from aws_console.sts import Sts

def get_url_via_assume_role(**kwargs):
    credentials_json = Sts().assume_role(**kwargs)
    url = Console().generate_console_url(credentials_json)
    return url

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

def help(action):
    if action == "actions":
        print("Usage: console [credentials|assume_role] OPTIONS")
        return

    if action == "assume_role":
        print("""Usage: console assume_role -d DURATION -e -h -m MFA_ARN -r ROLE_ARN""")
        return

def action_get_url_via_assume_role():
    try:
        opts, args = getopt.getopt(sys.argv[2:],
                "d:ehm:r:",
                ["duration", "external_id", "help", "mfa_arn", "role_arn"])
    except getopt.GetoptError as err:
        print(err)
        help("assume_role")
        sys.exit(1)

    duration = 3600
    external_id = None
    role_arn = None
    mfa_arn = None
    mfa_token = None
    for o, a in opts:
        if o in ("-d", "--duration"):
            duration = a
        elif o in ("-e", "--external_id"):
            external_id = getpass.getpass("External ID: ")
        elif o in ("-h", "--help"):
            help("assume_role")
            sys.exit(0)
        elif o in ("-m", "mfa_arn"):
            mfa_arn = a
            mfa_token = getpass.getpass("MFA Token: ")
        elif o in ("-r", "role_arn"):
            role_arn = a
        else:
            assert False, "unhandled option"

    if (role_arn == None):
        help("assume_role")
        sys.exit(1)

    url = get_url_via_assume_role(
        duration=duration,
        external_id=external_id,
        role_arn=role_arn,
        mfa_arn=mfa_arn,
        mfa_token=mfa_token)
    return url

def run():
    if (len(sys.argv) < 2):
        help("actions")
        sys.exit(1)
    action = sys.argv[1]
    args = sys.argv[2:]

    try:
        if (action == "credentials"):
            print(get_url_via_credentials())
            sys.exit(0)

        if (action == "assume_role"):
            url = action_get_url_via_assume_role()
            print(url)
            sys.exit(0)

    except Exception as e:
        print("Received error:", e)
        sys.exit(1)

    help("actions")
    sys.exit(1)
