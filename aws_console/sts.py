#!/usr/bin/env python3.6

import json
import boto3

class Sts():
    def __init__(self, region='us-west-2'):
        self.sts_client = boto3.client('sts', region)

    def assume_role(self, **kwargs):
        role_arn = kwargs.get('role_arn')
        mfa_arn = kwargs.get('mfa_arn')
        duration = kwargs.get('duration')
        external_id = kwargs.get('external_id')
        mfa_token = kwargs.get('mfa_token')

        args = {
                'RoleSessionName': "AssumeRoleAwsConsoleSession",
                'RoleArn': role_arn,
                'DurationSeconds': duration
                }
        if (mfa_arn != None) and (mfa_token != None):
            args['SerialNumber'] = mfa_arn
            args['TokenCode'] = mfa_token

        if external_id != None:
            args['ExternalId'] = external_id

        response = self.sts_client.assume_role(**args)

        tmp_credentials = {
                'sessionId': response['Credentials']['AccessKeyId'],
                'sessionKey': response['Credentials']['SecretAccessKey'],
                'sessionToken': response['Credentials']['SessionToken']
                }

        return json.dumps(tmp_credentials)
