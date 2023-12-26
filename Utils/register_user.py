import json
import random

import Utils.commonSteps as commonSteps
from Utils.data_generator import generate_fake_birthDate
from Utils.data_generator import generate_fake_name
from Utils.data_generator import generate_identification_number
from Utils.data_generator import generate_personal_id
from Utils.data_generator import generate_random_mobile_number
from Utils.data_generator import iban_generator


def register_individual(user_param="access token"):
    user_sms_id = commonSteps.send_and_verify(generate_random_mobile_number(),
                                              "REGISTRATION")
    registration = commonSteps.register_account(birthDate=generate_fake_birthDate(),
                                                deviceToken="string",
                                                iban=iban_generator(),
                                                mobileOS=random.choice(["ANDROID", "IOS"]),
                                                mobileNumber=f"996{generate_random_mobile_number()}",
                                                name=generate_fake_name(),
                                                personalNumber=generate_personal_id(),
                                                userSMSId=user_sms_id,
                                                userType="INDIVIDUAL")

    access_token = json.loads(registration.text).get("access_token")
    session_state = json.loads(registration.text).get("session_state")
    return_values = {
        "access token": access_token,
        "session state": session_state
    }
    return return_values.get(user_param, "Default Option")


def register_business(user_param="access token"):
    user_sms_id = commonSteps.send_and_verify(generate_random_mobile_number(),
                                              "REGISTRATION")
    registration = commonSteps.register_account(birthDate="",
                                                deviceToken="string",
                                                iban=iban_generator(),
                                                mobileOS=random.choice(["ANDROID", "IOS", "UNKNOWN"]),
                                                mobileNumber=f"996{generate_random_mobile_number()}",
                                                name=generate_fake_name(),
                                                personalNumber=generate_identification_number(),
                                                userSMSId=user_sms_id,
                                                userType="BUSINESS")

    access_token = json.loads(registration.text).get("access_token")
    session_state = json.loads(registration.text).get("session_state")
    return_values = {
        "access token": access_token,
        "session state": session_state
    }
    return return_values.get(user_param, "Default Option")
