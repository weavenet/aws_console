#!/usr/bin/env python3.6

import getpass
import json
import sys

from aws_console.console import Console
from aws_console.sts import Sts

def validate_input(argv):
    if (len(argv) < 3):
        return False

    if (argv[1] == "") or (argv[2] == "") or (argv[3] == ""):
        return False

    return True

def run():
    # --- Start of CLI parsing ---
    if (validate_input(sys.argv) != True):
        print("console_via_assume_role.py ACCOUNT_ID ROLE_NAME MFA_ARN")
        sys.exit(1)

    account_id = sys.argv[1] # Account id of target account
    role_name = sys.argv[2] # Name of role to assume in target account
    mfa_arn = sys.argv[3] # MFA users' ARN. More info: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html

    duration = 3600 # 1 Hour
    issuer = "example.org" # issuer name for signin url
    external_id = getpass.getpass("External ID: ")
    mfa_token = getpass.getpass("MFA Token: ")

    try:
        credentials_json = Sts().assume_role(account_id, role_name, duration, external_id, mfa_arn, mfa_token)
        url = Console().generate_console_url(issuer, credentials_json)
        print(url)
    except Exception as e:
        print("Received error:", e)
        sys.exit(1)
