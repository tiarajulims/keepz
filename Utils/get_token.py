import requests

send_sms = "https://appdev.keepz.me:8888/common-service/api/v1/auth/send-sms"


def get_auth_token():
    payload = {
        "countryCode": 996,
        "otphash": "string",
        "phone": "551554599",
        "smsType": "LOGIN_AS_INDIVIDUAL"
    }

    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }
    res = requests.post(url=send_sms, data=payload, headers=headers)
    print(res.content)

get_auth_token()
