import json
import string

import pytest
import requests
# TODO
import unittest

import Utils.api_endpoints
from Utils import get_token


class AuthController(unittest.TestCase):

    # @pytest.mark.xfail
    def test_01_check(self):
        payload = {
            'phone': '996599989981'
        }
        headers = {
            'content-type': 'application/json',
            'Accept': '*/*'
        }
        response = requests.post(url=Utils.api_endpoints.check_user, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
        print(response.text)

    def test_2_send_sms(self):
        headers = {
            'content-type': 'application/json',
            'Accept': '*/*'
        }
        payload = {
            "countryCode": "996",
            "otphash": "string",
            "phone": "599989981",
            "smsType": "LOGIN_AS_INDIVIDUAL"
        }
        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200

    def test_03_verify_sms(self):
        headers = {
            'content-type': 'application/json',
            'Accept': '*/*'
        }
        payload = {
            "code": "123456",
            "countryCode": "996",
            "phone": "599989981"
        }
        requests.post()
        response = requests.post(url=Utils.api_endpoints.verify_sms, data= json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 202 or 200

    def test_04_Login(self):
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json'
        }
        payload_sms = {
            "countryCode": "996",
            "otphash": "string",
            "phone": "599989981",
            "smsType": "LOGIN_AS_INDIVIDUAL"
        }
        requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload_sms), headers=headers)
        payload_verify = {
            "code": "123456",
            "countryCode": "996",
            "phone": "599989981"
        }
        verify_response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload_verify), headers=headers)
        userSmsid = verify_response.text
        payload_login = {
            "deviceToken": "string",
            "mobileName": "string",
            "mobileOS": "ANDROID",
            "userSMSId": userSmsid,
            "userType": "INDIVIDUAL"
        }
        response = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_login), headers=headers)
        assert response.status_code == 200
        response_json = json.loads(response.text)
        access_token = response_json.get("access_token")
        return access_token





