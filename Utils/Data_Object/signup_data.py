import random
from faker import Faker


def generate_random_number():
    random_number = ''.join(random.choices('1234567890', k=6))
    return random_number


def generate_personal_id():
    random_number = ''.join(random.choices('1234567890', k=11))
    return random_number


def generate_random_mobile_number() -> str:
    response = generate_random_number()
    mob_number = "599" + response
    return mob_number


def generate_fake_name() -> str:
    fake = Faker()
    name = fake.name()
    return name


def generate_fake_birthDate():
    fake = Faker()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    formatted_birthdate = birth_date.strftime("%Y-%m-%d")
    return formatted_birthdate


def generate_identification_number():
    random_number = ''.join(random.choices('1234567890', k=9))
    return random_number


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
