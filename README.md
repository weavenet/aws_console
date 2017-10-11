# AWS Console

Generate signed AWS console links.

# Installation

```shell
pip3 install git+https://github.com/weavenet/aws_console@v1.0.1
```

# Usage

## Generating URL from AWS credential providers

Reads the standard [AWS credential providers](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials) and genertes URL.

```shell
$ aws_console
https://signin.aws.amazon.com/federation?Action=login&Issuer=https://github.com/weavenet/aws_console&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2F&SigninToken=AY_....
```

## Dev / Test

Clone down this repo and run the following

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install .
```

Run the tests

```shell
python3 aws_console/test.py
```
