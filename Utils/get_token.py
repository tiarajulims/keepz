import json

import requests

send_sms = "https://appdev.keepz.me:8888/common-service/api/v1/auth/send-sms"
verify_sms = "https://appdev.keepz.me:8888/common-service/api/v1/auth/verify-sms"
login = "https://appdev.keepz.me:8888/common-service/api/v1/auth/login"

def get_auth_token() -> str:
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

    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    res_send_sms = requests.post(url=send_sms, data=json.dumps(payload_send_sms), headers=headers)
    res_verify_sms = requests.post(url=verify_sms, data=json.dumps(payload_verify_sms), headers=headers)


    payload_login = {
        "deviceToken": "string",
        "mobileName": "string",
        "mobileOS": "ANDROID",
        "userSMSId": f"{res_verify_sms.text}",
        "userType": "INDIVIDUAL"
    }

    res_login = requests.post(url=login, data=json.dumps(payload_login), headers=headers)
    data = json.loads(res_login.text)

    return f'Bearer {data["access_token"]}'

