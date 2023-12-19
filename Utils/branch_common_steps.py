import json
import os
import sys
import requests
import Utils.api_endpoints
import Utils.Data_Object.merchant_data
import Utils.commonSteps
import Utils.data_generator

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

"""Token Generation"""


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



access_token = get_auth_token()

def add_branch(**data):

    payload = [
  {
    "address": data.get("address"),
    "contactPhone": data.get("contactPhone"),
    "iban": data.get("iban"),
    "image_path": "",
    "isMaster": data.get("isMaster"),
    "merchantId": "e613e523-20b0-488d-bc7f-6059399a5ef0",
    "name": "string",
    "qrCodeBranch": 10237
  }
]

