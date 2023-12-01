import json
import pytest
import requests
import unittest
import Utils.api_endpoints



class AuthControllerNegative(unittest.TestCase):

    headers = {
            'content-type': 'application/json',
            'Accept': '*/*'
        }

    def test_01_empty_phone(self):

        payload = {
            "countryCode": "995",
            "otphash": "string",
            "phone": "",
            "smsType": "LOGIN_AS_BUSINESS"
        }

        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 400
        assert "message" in json_data
        assert json_data["message"] == "[Invalid format of phone, must not be blank]" or "[must not be blank, Invalid format of phone]"

    def test_02_string_phone(self):

        payload = {
            "countryCode": "995",
            "otphash": "string",
            "phone": "string",
            "smsType": "LOGIN_AS_BUSINESS"
        }

        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 400
        assert "message" in json_data
        assert json_data["message"] == "[Invalid format of phone]"
        #
    def test_03_invalid_phone(self):

        payload = {
            "countryCode": "995",
            "otphash": "string",
            "phone": "544989981",
            "smsType": "LOGIN_AS_BUSINESS"
        }

        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 404
        assert "message" in json_data
        assert json_data["message"] == '404 NOT_FOUND "Business user does not exist for mobile number: 995544989981"'



    def test_04_empty_smsType(self):

        payload = {
            "countryCode": "995",
            "otphash": "string",
            "phone": "544989981",
            "smsType": ""
        }

        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 400
        assert "message" in json_data
        assert (json_data["message"] == " can't be parsed to SMSType.SMSType must be one of this: REGISTRATION, "
                                        "LOGIN_AS_INDIVIDUAL, LOGIN_AS_BUSINESS, PASSWORD_RESET, PHONE_CHANGE")


    def test_05_invalid_business_number(self):

        payload = {
            "countryCode": "995",
            "otphash": "string",
            "phone": "5999899811",
            "smsType": "LOGIN_AS_BUSINESS"
        }

        response = requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 404
        assert "message" in json_data
        assert json_data["message"] == '404 NOT_FOUND "Business user does not exist for mobile number: 9955999899811"'



    @pytest.mark.parametrize("invalidCode", [("899230"), ("899231"), ("899232")], )
    def test_06_invalid_sms_code(self):

        payload = {
            "code": "899230",
            "countryCode": "995",
            "phone": "599989981"
        }

        response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 428
        assert "message" in json_data
        assert json_data["message"] == '428 PRECONDITION_REQUIRED "SMS not send on phone 995599989981 "'



    def test_07_incorrect_phone(self):

        payload = {
            "code": "899230",
            "countryCode": "995",
            "phone": "59998998121231"
        }
        response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload), headers=AuthControllerNegative.headers)
        json_data = response.json()
        assert response.status_code == 428
        assert "message" in json_data
        assert json_data["message"] == '428 PRECONDITION_REQUIRED "SMS not send on phone 99559998998121231 "'


    def test_06_invalid_sms_code(self, ):
        payload = {
            "code": "422102",
            "countryCode": "995",
            "phone": "599989981"
        }
        response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload),
                                 headers=AuthControllerNegative.headers)
        json_data = response.json()

        assert response.status_code == 428
        assert "message" in json_data
        assert json_data["message"] == '428 PRECONDITION_REQUIRED "SMS not send on phone 995599989981 "'
