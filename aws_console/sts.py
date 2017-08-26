#!/usr/bin/env python3.6

import json

import boto3

class Sts():
    def __init__(self, region='us-west-2'):
        self.sts_client = boto3.client('sts', region)

    def assume_role(self, account_id, role_name, duration, external_id, mfa_arn, mfa_token):
        role_arn = "arn:aws:iam::" + account_id + ":role/" + role_name
        role_session_name = "AssumeRoleSession"

        response = self.sts_client.assume_role(RoleArn=role_arn,
                RoleSessionName=role_session_name,
                DurationSeconds=duration,
                ExternalId=external_id,
                SerialNumber=mfa_arn,
                TokenCode=mfa_token)

        tmp_credentials = {
                'sessionId': response['Credentials']['AccessKeyId'],
                'sessionKey': response['Credentials']['SecretAccessKey'],
                'sessionToken':response['Credentials']['SessionToken']
                }

        return json.dumps(tmp_credentials)
