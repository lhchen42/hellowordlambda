import unittest
from unittest import mock
from unittest.mock import patch
import os

import moto
import boto3

import json

from datetime import datetime

import importlib

import pytest

@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    os.environ['LOGGING_MODE'] = 'DEBUG'


def test_Crediential(aws_credentials):
    assert os.environ['AWS_ACCESS_KEY_ID'] == 'testing'
    assert os.environ['AWS_SECRET_ACCESS_KEY'] == 'testing'
    assert os.environ['AWS_SECURITY_TOKEN'] == 'testing'
    assert os.environ['AWS_SESSION_TOKEN'] == 'testing'
    assert os.environ['AWS_DEFAULT_REGION'] == 'us-east-1'

# @moto.mock_dynamodb
def test_HelloWorld(aws_credentials):
    helloworld = importlib.import_module("hello_world.app")
    with open("events/event.json", 'rb') as f:
        payload = f.read()
    response = helloworld.lambda_handler(payload, {})
    body = json.loads(response['body'])
    assert response['statusCode'] == 200
    assert body['message'] == "hello world new version"




