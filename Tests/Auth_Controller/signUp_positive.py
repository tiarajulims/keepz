import copy
import unittest

import allure

from Utils import data_generator
from Utils.Data_Object.login_data import DataForLogin
from Utils.Data_Object.signup_data import Sign_Up_Data
from Utils.commonSteps import send_and_verify, register_account


class SignUpPositive(unittest.TestCase):

    @allure.suite("Registration Functionality")
    @allure.title("Register individual user")
    @allure.description("Register individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_register_ind_user(self):
        phoneNumber = data_generator.generate_random_mobile_number()
        sms_payload = copy.copy(DataForLogin.payload_send_sms)
        sms_payload["phone"] = phoneNumber
        sms_payload["smsType"] = "REGISTRATION"
        verif_payload = copy.copy(DataForLogin.payload_verify_sms)
        verif_payload["phone"] = phoneNumber
        user_sms_id = send_and_verify(sms_payload, verif_payload)
        reg_payload = copy.copy(Sign_Up_Data.payload_registration)
        reg_payload["mobileNumber"] = "996" + phoneNumber
        reg_payload["userSMSId"] = user_sms_id
        reg_payload["userType"] = "BUSINESS"
        reg_payload.pop("birthDate", None)
        reg_payload["personalNumber"] = data_generator.generate_identification_number()
        reg_ind = register_account(reg_payload)
        print(sms_payload, verif_payload)
        print(reg_payload)
        print(reg_ind.text)
