import copy
import json
import os
import sys
import requests

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import Utils.api_endpoints
import Utils.Data_Object.merchant_data
import Utils.commonSteps
import Utils.data_generator
from Utils.Data_Object.merchant_data import Merchant_data

"""Methods to get Token """


def send_and_verify(country_code, phone, smsType):
    Utils.commonSteps.send_sms(country_code, "string", phone, smsType)

    response = Utils.commonSteps.verify_otp_sms("123456", country_code, phone)
    userSmsId = response.text
    return userSmsId


def get_auth_token():
    userSmsId = send_and_verify("351", "802156392", "LOGIN")
    res_login = Utils.commonSteps.login("string",
                                        "string",
                                        "ANDROID",
                                        userSmsId,
                                        Utils.Data_Object.login_data.DataForLogin.sms_type_business)
    print(res_login)
    return res_login


""" Method to create a Merchant account """

access_token = get_auth_token()

def test_create_empty_branch():
    payload = {
        "numberOfUsers": 1
    }

    response = requests.post(url=Utils.api_endpoints.create_empty_branch,
                             data=json.dumps(payload),
                             headers=Utils.Data_Object.merchant_data.Merchant_data.header(access_token))

    response_data = response.json()
    qrcode = response_data[0]["qrCode"]

    return qrcode


def create_merchant(payload):

    response = requests.post(url=Utils.api_endpoints.add_merchant,
                             data=json.dumps(payload),
                             headers=Merchant_data.header(access_token))

    return response


