import json
import requests
from requests import Response

import Utils.api_endpoints

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json'
}

payload_send_sms = {
    "countryCode": "996",
    "otphash": "string",
    "phone": "599989981",
    "smsType": "LOGIN_AS_INDIVIDUAL"
}

payload_verify_sms = {
    "code": "123456",
    "countryCode": "996",
    "phone": "599989981"
}

payload_login = {
    "deviceToken": "string",
    "mobileName": "string",
    "mobileOS": "ANDROID",
    "userSMSId": "",  # Placeholder, will be updated later
    "userType": "INDIVIDUAL"
}

individual = "LOGIN_AS_INDIVIDUAL"
business = "LOGIN_AS_BUSINESS"


def send_sms(countrycode, otphash, phoneNumber, userType):
    payload_Send_sms = {
        "countryCode": countrycode,
        "otphash": otphash,
        "phone": phoneNumber,
        "smsType": userType
    }
    requests.post(url=Utils.api_endpoints.send_sms, data=json.dumps(payload_Send_sms), headers=headers)


def verify_otp_sms(code, countrycode, phoneNumber):
    payload_Verify_sms = {
        "code": code,
        "countryCode": countrycode,
        "phone": phoneNumber
    }
    response = requests.post(url=Utils.api_endpoints.verify_sms, data=json.dumps(payload_Verify_sms), headers=headers)
    return response


def login(devToken, mobName, mobOS, userSmsId, userType):
    payload_Login = {
        "deviceToken": devToken,
        "mobileName": mobName,
        "mobileOS": mobOS,
        "userSMSId": userSmsId,
        "userType": userType
    }
    response = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_Login), headers=headers)
    print(response)
    return response


def get_auth_token(countrycode, phoneNumber, userType):
    # Send SMS
    send_sms(countrycode, phoneNumber, userType)
    # Verify SMS
    userSmsId = verify_otp_sms(countrycode, phoneNumber)
    # Update payload_login with userSMSId
    payload_login["userSMSId"] = userSmsId.text
    # Perform login
    res_login = requests.post(url=Utils.api_endpoints.login, data=json.dumps(payload_login), headers=headers)
    data = json.loads(res_login.text)
    print(data)
