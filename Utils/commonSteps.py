import json
import os
import sys

import allure

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import requests
from Utils.Data_Object.login_data import DataForLogin
from Utils.api_endpoints import check_user
from Utils.api_endpoints import send_sms_url
from Utils.api_endpoints import verify_sms_url
from Utils.api_endpoints import login_url
from Utils.api_endpoints import profile
from Utils.api_endpoints import registration_url

""" METHOD TO CHECK IF USER HAS ACCOUNT ASA INDIVIDUAL OR BUSINESS"""


@allure.step
def check_userType(payload_check):
    response = requests.post(url=check_user,
                             data=json.dumps(payload_check),
                             headers=DataForLogin.headers)
    return response


"""METHOD WHICH SEND ONLY SMS"""


@allure.step
def send_sms(payload_send_sms):
    response = requests.post(url=send_sms_url,
                             data=json.dumps(payload_send_sms),
                             headers=DataForLogin.headers)
    return response


"""METHOD WHICH VERIFIES AN OTP AND RETURNS USER_SMS_ID"""


@allure.step
def verify_otp_sms(payload_verify_sms):
    response = requests.post(url=verify_sms_url,
                             data=json.dumps(payload_verify_sms),
                             headers=DataForLogin.headers)
    return response


"""METHOD WHICH GENERATES A TOKEN AND RETURNS IT"""


@allure.step
def login(payload_login):
    response = requests.post(url=login_url,
                             data=json.dumps(payload_login),
                             headers=DataForLogin.headers)
    return response


@allure.step  # METHOD WHICH SENDS AND VERIFIES OTP AND RETURNS USER SMS ID
def send_and_verify(payload_sms, payload_verify):
    send_sms(payload_sms)
    response = verify_otp_sms(payload_verify)
    userSmsId = response.text
    return userSmsId


"""METHOD WHICH PERFORMS ALL ACTIONS TO GENERATE AND RETURN TOKEN, SEND SMS, VERIFY AND LOGIN"""


def get_auth_token():
    userSmsId = send_and_verify("599989981",
                                DataForLogin.individual_send_sms)

    res_login = login("string",
                      "string",
                      "ANDROID",
                      userSmsId,
                      DataForLogin.sms_type_individual)
    data = res_login.json()
    access_token = data.get('access_token')
    return access_token


""" METHOD WHICH REGISTERS A NEW ACCOUNT , GENERATES TOKEN AND RETURNS IT, TO USE THESE FIRST SEND SMS AND VERIFY NEEDS TO BE SENT"""

@allure.step
def register_account(payload_registration):
    response = requests.post(url=registration_url,
                             data=json.dumps(payload_registration),
                             headers=DataForLogin.headers)
    return response


@allure.step
def get_method(access_token):
    header = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    info = requests.get(url=profile,
                        headers=header)
    return info
