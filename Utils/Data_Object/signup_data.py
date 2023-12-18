import random


def generate_random_number():
    random_number = ''.join(random.choices('1234567890', k=6))
    return random_number


def generate_random_mobile_number():
    response = generate_random_number()
    mob_number = "599" + response
    return mob_number


class Sign_Up_Data:
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    payload_registration = {
        "birthDate": "2020-11-27",
        "deviceToken": "string",
        "iban": "GE16TB1544777371444667",
        "mobileName": "string",
        "mobileOS": "ANDROID",
        "name": "Jijelava",
        "personalNumber": "62014008420",
        "userSMSId": "40f84c1a-1de0-4a33-9b16-d634cf760a03",
        "userType": "INDIVIDUAL"
    }

    sms_type_individual = "INDIVIDUAL"
    sms_type_business = "BUSINESS"
