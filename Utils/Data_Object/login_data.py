
from Utils import data_generator


class DataForLogin:

    phoneNumber = data_generator.generate_random_mobile_number()

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    payload_check = {
        "phone": phoneNumber
    }

    payload_send_sms = {
        "countryCode": "996",
        "otphash": "string",
        "phone": phoneNumber,
        "smsType": "LOGIN"
    }

    payload_verify_sms = {
        "code": "123456",
        "countryCode": "996",
        "phone": phoneNumber
    }

    payload_login = {
        "deviceToken": "string",
        "mobileName": "string",
        "mobileOS": "ANDROID",
        "mobileNumber": "string",
        "userSMSId": "string",
        "userType": "INDIVIDUAL"
    }



