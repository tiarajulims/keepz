import json
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import requests
import Utils.Data_Object.login_data
import Utils.api_endpoints

""" METHOD TO CHECK IF USER HAS ACCOUNT ASA INDIVIDUAL OR BUSINESS"""


def check_user(phoneNumber):
    payload_check = {
        "phone": "996" + phoneNumber
    }
    response = requests.post(url=Utils.api_endpoints.check_user,
                             data=json.dumps(payload_check),
                             headers=Utils.Data_Object.login_data.DataForLogin.headers)
    return response


"""METHOD WHICH SEND ONLY SMS"""


def send_sms(countrycode, otphash, phoneNumber, userType):
    payload_Send_sms = {
        "countryCode": countrycode,
        "otphash": otphash,
        "phone": phoneNumber,
        "smsType": userType
    }
    response = requests.post(url=Utils.api_endpoints.send_sms,
                             data=json.dumps(payload_Send_sms),
                             headers=Utils.Data_Object.login_data.DataForLogin.headers)
    return response


"""METHOD WHICH VERIFIES AN OTP AND RETURNS USER_SMS_ID"""


def verify_otp_sms(code, countrycode, phoneNumber):
    payload_Verify_sms = {
        "code": code,
        "countryCode": countrycode,
        "phone": phoneNumber
    }
    response = requests.post(url=Utils.api_endpoints.verify_sms,
                             data=json.dumps(payload_Verify_sms),
                             headers=Utils.Data_Object.login_data.DataForLogin.headers)
    return response




"""METHOD WHICH GENERATES A TOKEN AND RETURNS IT"""


def login(devToken, mobName, mobOS, userSmsId, userType):
    payload_Login = {
        "deviceToken": devToken,
        "mobileName": mobName,
        "mobileOS": mobOS,
        "userSMSId": userSmsId,
        "userType": userType
    }
    response = requests.post(url=Utils.api_endpoints.login,
                             data=json.dumps(payload_Login),
                             headers=Utils.Data_Object.login_data.DataForLogin.headers)
    data = response.json()
    access_token = data.get('access_token')
    return access_token


""" METHOD WHICH SENDS AND VERIFIES OTP AND RETURNS USER SMS ID"""


def send_and_verify(phone, smsType):
    send_sms("996", "string", phone, smsType)

    response = verify_otp_sms("123456", "996", phone)

    userSmsId = response.text
    return userSmsId


"""METHOD WHICH PERFORMS ALL ACTIONS TO GENERATE AND RETURN TOKEN, SEND SMS, VERIFY AND LOGIN"""


def get_auth_token():
    userSmsId = Utils.commonSteps.send_and_verify("599989981",
                                                  Utils.Data_Object.login_data.DataForLogin.individual_send_sms)

    res_login = Utils.commonSteps.login("string",
                                        "string",
                                        "ANDROID",
                                        userSmsId,
                                        Utils.Data_Object.login_data.DataForLogin.sms_type_individual)
    data = res_login.json()
    access_token = data.get('access_token')
    return access_token


""" METHOD WHICH REGISTERS A NEW ACCOUNT , GENERATES TOKEN AND RETURNS IT, TO USE THESE FIRST SEND SMS AND VERIFY NEEDS TO BE SENT"""


def register_account(**data):
    payload_registration = {
        "birthDate": data.get("birthDate"),
        "deviceToken": data.get("deviceToken"),
        "iban": data.get("iban"),
        "mobileName": "string",
        "mobileOS": data.get("mobileOS"),
        "name": data.get("name"),
        "personalNumber": data.get("personalNumber"),
        "userSMSId": data.get("userSMSId"),
        "userType": data.get("userType"),
    }
    response = requests.post(url=Utils.api_endpoints.registration,
                             data=json.dumps(payload_registration),
                             headers=Utils.Data_Object.login_data.DataForLogin.headers)

    return response


def get_method(access_token):
    header = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    info = requests.get(url=Utils.api_endpoints.profile, headers=header)
    return info
