import copy
import unittest

import allure

from Utils import data_generator
from Utils.Data_Object.login_data import DataForLogin
from Utils.Data_Object.signup_data import Sign_Up_Data
from Utils.commonSteps import send_and_verify, register_account
from Utils.data_generator import generate_random_mobile_number, generate_identification_number


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



    @allure.suite("Registration Functionality")
    @allure.title("Register ind user with empty date of birth - Business")
    @allure.description("Trying to register individual user with empty date of birth, all other with valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_register_bus_user_empty_dob(self):
        phoneNumber = generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = phoneNumber
        payload_sms["smsType"] = "REGISTRATION"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = phoneNumber
        userSmsId = send_and_verify(payload_sms, payload_verify)
        reg_payload = copy.copy(Sign_Up_Data.payload_registration)
        reg_payload["birthDate"] = ""
        reg_payload["personalNumber"] = generate_identification_number()
        reg_payload["userSMSId"] = userSmsId
        reg_payload["userType"] = "BUSINESS"
        reg_payload["mobileNumber"] = "996" + phoneNumber
        response = register_account(reg_payload)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[birthDate-Is required]")