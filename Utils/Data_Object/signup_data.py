import random

from Utils import data_generator


class Sign_Up_Data:

    mobOS = ["ANDROID", "IOS", "UNKNOWN"]


    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    payload_registration = {
        "birthDate": data_generator.generate_fake_birthDate(),
        "deviceToken": "string",
        "iban": data_generator.iban_generator(),
        "mobileName": "string",
        "mobileNumber": data_generator.generate_random_mobile_number(),
        "mobileOS": random.choice(mobOS),
        "name": data_generator.generate_fake_name(),
        "personalNumber": data_generator.generate_personal_id(),
        "userSMSId": "string",
        "userType": "INDIVIDUAL"
    }

    sms_type_individual = "INDIVIDUAL"
    sms_type_business = "BUSINESS"
