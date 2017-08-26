# AWS Console Scripts

Generate signed AWS console links.

# Installation

```
pip3 install git+https://github.com/weavenet/aws_console
```

# Usage

## Generating URL from environment variables

Reads the standard AWS env variables and generates console link.

```
export AWS_SESSION_TOKEN=xxx
export AWS_SECRET_ACCESS_KEY=yyy
export AWS_ACCESS_KEY_ID=zzz

console_via_env_variables
```

## Assuming role (with MFA and external id)

Will assume a role, with external id and MFA, and generate signed console URL.

```
console_via_assume_role 111122223333 user arn:aws:iam::444455556666:mfa/user
```

## Dev

Clone down this repo and run the following

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```
