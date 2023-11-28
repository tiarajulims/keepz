import json
import requests
import unittest
import Utils.api_endpoints


class AuthControllerNegative(unittest.TestCase):

    def test_01_Login_invalid_usersmsId(self):
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
        payload_login = {
            "deviceToken": "string",
            "mobileName": "string",
            "mobileOS": "ANDROID",
            "userSMSId": "userSmsid",
            "userType": "INDIVIDUAL"
        }

        response = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_login), headers=headers)
        json_data = response.json()
        assert response.status_code == 404
        assert "message" in json_data
        assert json_data["message"] == '404 NOT_FOUND "Sms not send with id userSmsid "'


    def test_02_Login_invalid_mobileOS(self):
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
        usersmsId = verify_response.text
        payload_login = {
            "deviceToken": "string",
            "mobileName": "string",
            "mobileOS": "asdasdasdasdas",
            "userSMSId": usersmsId,
            "userType": "INDIVIDUAL"
            }

        response = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_login), headers=headers)
        json_data = response.json()
        assert response.status_code == 400
        assert "message" in json_data
        assert json_data["message"] == "asdasdasdasdas can't be parsed to MobileOS.MobileOS must be one of this: "'IOS, ANDROID, UNKNOWN'
        print(response.text)

    def test_03_Login_empty_deviceToken(self):
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
        verify_response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload_verify),
                                        headers=headers)
        usersmsId = verify_response.text
        payload_login = {
            "deviceToken": "",
            "mobileName": "string",
            "mobileOS": "ANDROID",
            "userSMSId": usersmsId,
            "userType": "INDIVIDUAL"
        }

        response = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_login), headers=headers)
        json_data = response.json()
        assert response.status_code == 400
        assert "message" in json_data
        assert json_data["message"] == "[deviceToken-Is required]"
        print(response.text)

