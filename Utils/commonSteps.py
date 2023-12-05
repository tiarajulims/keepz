import json
import requests
from requests import Response
import Utils.Data_Object.auth_data
import Utils.api_endpoints


# METHOD WHICH SEND ONLY SMS
def send_sms(countrycode, otphash, phoneNumber, userType):
    payload_Send_sms = {
        "countryCode": countrycode,
        "otphash": otphash,
        "phone": phoneNumber,
        "smsType": userType
    }
    response = requests.post(url=Utils.api_endpoints.send_sms,
                             data=json.dumps(payload_Send_sms),
                             headers=Utils.Data_Object.auth_data.headers)
    return response


# METHOD WHICH VERIFIES AN OTP AND RETURNS USER_SMS_ID
def verify_otp_sms(code, countrycode, phoneNumber):
    payload_Verify_sms = {
        "code": code,
        "countryCode": countrycode,
        "phone": phoneNumber
    }
    response = requests.post(url=Utils.api_endpoints.verify_sms,
                             data=json.dumps(payload_Verify_sms),
                             headers=Utils.Data_Object.auth_data.headers)
    return response


# METHOD WHICH GENERATES A TOKEN AND RETURNS IT
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
                             headers=Utils.Data_Object.auth_data.headers)
    print(response)
    return response


# METHOD WHICH PERFORMS ALL ACTIONS TO GENERATE AND RETURN TOKEN, SEND SMS, VERIFY AND LOGIN
def get_auth_token(code, countrycode, otphash, phoneNumber, userType):
    # Send SMS
    send_sms(countrycode, otphash, phoneNumber, userType)
    # Verify SMS
    userSmsId = verify_otp_sms(code, countrycode, phoneNumber)
    # Update payload_login with userSMSId
    Utils.Data_Object.auth_data.payload_login["userSMSId"] = userSmsId.text
    # Perform login
    res_login = requests.post(url=Utils.api_endpoints.login,
                              data=json.dumps(Utils.Data_Object.auth_data.payload_login),
                              headers=Utils.Data_Object.auth_data.headers)
    data = json.loads(res_login.text)
    return data


# METHOD WHICH REGISTERS A NEW ACCOUNT , GENERATES TOKEN AND RETURNS IT, TO USE THESE FIRST SEND SMS AND VERIFY NEEDS TO BE SENT
def register_account(dob, devToken, iban, mobName, mobOS, name, persId, userSmsId, userType):
    payload_registration = {
        "birthDate": dob,
        "deviceToken": devToken,
        "iban": iban,
        "mobileName": mobName,
        "mobileOS": mobOS,
        "name": name,
        "personalNumber": persId,
        "userSMSId": userSmsId,
        "userType": userType
    }
    response = requests.post(url=Utils.api_endpoints.registration,
                             data=json.dumps(payload_registration),
                             headers=Utils.Data_Object.auth_data.headers)
    data = json.loads(response.text)
    return data
