import json
import pytest
import requests
import unittest
import allure
import sys
import os
import Utils.api_endpoints
import Utils.commonSteps
import Utils.Data_Object.auth_data

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


class AuthControllerNegative(unittest.TestCase):
    headers = {
        'content-type': 'application/json',
        'Accept': '*/*'
    }


    # ALLURE SUITE TITLES FOR SEND SMS
    send_sms_login_individual = "Login Functionality - Send Sms -  Individual"
    send_sms_login_business = "Login Functionality - Send Sms - Business"
    registration_send_sms = "Registration Functionality - Send Sms"

    # ALLURE SUITE TITLES FOR VERIFY SMS
    verify_sms_login_individual = "Login Functionality - Verify Sms -  Individual"
    verify_sms_login_business = "Login Functionality - Verify Sms -  Business"
    verify_sms_registration = "Registration Functionality - Verify Sms"



    @allure.suite(send_sms_login_individual)
    @allure.title("Login with empty phone")
    @allure.description("Login for individual person with empty phone number and country code 996")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_empty_phone_login_individual(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "",
                                              Utils.Data_Object.auth_data.individual)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone, must not be blank]",
                       "[must not be blank, Invalid format of phone]"])

    @allure.suite(send_sms_login_business)
    @allure.title("Login with empty phone")
    @allure.description("Login for individual person with empty phone number and country code 996")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_empty_phone_business_login(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "",
                                              Utils.Data_Object.auth_data.business)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone, must not be blank]",
                       "[must not be blank, Invalid format of phone]"])

    @allure.suite(registration_send_sms)
    @allure.title("registration with empty phone")
    @allure.description("Registration with empty phone number and country code 996")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_empty_phone_registration(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "",
                                              Utils.Data_Object.auth_data.registration)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone, must not be blank]",
                       "[must not be blank, Invalid format of phone]"])

    @allure.suite(send_sms_login_individual)
    @allure.title("Login with empty country code")
    @allure.description("login for individual person with empty country code, phone number 599989981")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_empty_country_code_individual(self):
        response = Utils.commonSteps.send_sms("",
                                              "string",
                                              "599989981",
                                              Utils.Data_Object.auth_data.individual)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid Country Code]"])

    @allure.suite(send_sms_login_business)
    @allure.title("Login with empty country code")
    @allure.description("login for individual person with empty country code, phone number 599989981")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_empty_country_code_business(self):
        response = Utils.commonSteps.send_sms("",
                                              "string",
                                              "599989981",
                                              Utils.Data_Object.auth_data.business)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid Country Code]"])

    @allure.suite(registration_send_sms)
    @allure.title("Registration with empty country code")
    @allure.description("Registration with empty country code, phone number 599989981")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_empty_country_code_registration(self):
        response = Utils.commonSteps.send_sms("",
                                              "string",
                                              "599989981",
                                              Utils.Data_Object.auth_data.registration)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid Country Code]"])

    @allure.suite(send_sms_login_individual)
    @allure.title("Login with string phone")
    @allure.description("Login for individual person entering string as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_string_phone_login_individual(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "string",
                                              Utils.Data_Object.auth_data.individual)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite(send_sms_login_business)
    @allure.title("Login with string phone")
    @allure.description("Login for individual person entering string as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_string_phone_business_login(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "string",
                                              Utils.Data_Object.auth_data.business)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite(registration_send_sms)
    @allure.title("Registration string as a number")
    @allure.description("Enter string as a phone number during registration")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_string_phone_registration(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "string",
                                              Utils.Data_Object.auth_data.registration)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite(send_sms_login_individual)
    @allure.title("Login with invalid phone")
    @allure.description("Login for individual person entering an invalid phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_invalid_phone_login_individual(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "821989981",
                                              Utils.Data_Object.auth_data.individual)
        sendSms = response.json()
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ['404 NOT_FOUND "Individual user does not exist for mobile number: 996821989981"'])

    @allure.suite(send_sms_login_business)
    @allure.title("Login with invalid phone")
    @allure.description("Login for business person entering an invalid phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_invalid_phone_login_business(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "821989981",
                                              Utils.Data_Object.auth_data.business)
        sendSms = response.json()
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ['404 NOT_FOUND "Business user does not exist for mobile number: 996821989981"'])

    @allure.suite(registration_send_sms)
    @allure.title("register with invalid phone")
    @allure.description("register entering an invalid phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_invalid_phone_registration(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "ass821989981",
                                              Utils.Data_Object.auth_data.registration)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone]"])

    @allure.suite("Login Functionality")
    @allure.title("Login with empty smsType")
    @allure.description("Login leaving empty smsType , with phone 599989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_empty_smsType_login(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "599989981",
                                              "")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], [" can't be parsed to SMSType.SMSType must be one of this: REGISTRATION, "
                                           "LOGIN_AS_INDIVIDUAL, LOGIN_AS_BUSINESS, PASSWORD_RESET, PHONE_CHANGE"])

    @allure.suite(verify_sms_login_individual)
    @allure.title("Login with empty OTP")
    @allure.description("Login for individual person leaving empty OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_empty_otp_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.individual)
        response = Utils.commonSteps.verify_otp_sms("",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite(verify_sms_login_business)
    @allure.title("Login with empty OTP")
    @allure.description("Login for business person leaving empty OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_empty_otp_business(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.business)
        response = Utils.commonSteps.verify_otp_sms("",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite(verify_sms_registration)
    @allure.title("Register with empty OTP")
    @allure.description("Register leaving empty OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_empty_otp_registration(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.registration)
        response = Utils.commonSteps.verify_otp_sms("",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite(verify_sms_login_individual)
    @allure.title("Login with wrong OTP")
    @allure.description("Login for individual person entering wrong OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_17_wrong_otp_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.individual)
        response = Utils.commonSteps.verify_otp_sms("654221",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '"406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite(verify_sms_login_business)
    @allure.title("Login with wrong OTP")
    @allure.description("Login for business person entering wrong OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_wrong_otp_business(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.business)
        response = Utils.commonSteps.verify_otp_sms("654221",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '"406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite(verify_sms_registration)
    @allure.title("Register with wrong OTP")
    @allure.description("Register entering wrong OTP , phone number 5999989981 and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_19_wrong_otp_registration(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.registration)
        response = Utils.commonSteps.verify_otp_sms("654221",
                                                    "996",
                                                    "599989981")
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '"406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite(verify_sms_login_individual)
    @allure.title("Login with wrong OTP")
    @allure.description("Login for individual person entering invalid country code , phone number 5999989981 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_invalid_country_code_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.individual)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "997",
                                                    "599989981")
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 997599989981 "')

    @allure.suite(verify_sms_login_business)
    @allure.title("Login with wrong Country Code ")
    @allure.description("Login for individual person entering invalid country code , phone number 5999989981 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_invalid_country_code_business(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.business)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "997",
                                                    "599989981")
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 997599989981 "')

    @allure.suite(registration_send_sms)
    @allure.title("Register with wrong OTP")
    @allure.description("Register account entering invalid country code , phone number 5999989981 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_22_invalid_country_code_registration(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.registration)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "997",
                                                    "599989981")
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 997599989981 "')

    @allure.suite(verify_sms_login_individual)
    @allure.title("login with empty number")
    @allure.description("Login as individual leaving the number field empty , with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_23_login_empty_phone_number_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.individual)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite(verify_sms_login_business)
    @allure.title("login with empty number")
    @allure.description("Login as business leaving the number field empty , with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_empty_phone_number_login_business(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.business)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite(verify_sms_registration)
    @allure.title("Register with empty number")
    @allure.description("Register user leaving the number field empty , with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_empty_phone_number_registration(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.registration)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "")
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite(verify_sms_login_individual)
    @allure.title("login with wrong number")
    @allure.description("Login as individual leaving the number field empty , with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_26_login_wrong_phone_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.individual)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "499989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 996499989981 "')

    @allure.suite(verify_sms_login_individual)
    @allure.title("login with wrong number")
    @allure.description("Login as business leaving the number field empty , with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_27_login_wrong_phone_business(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.business)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "499989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 996499989981 "')

    @allure.suite(verify_sms_registration)
    @allure.title("Registration with wrong number")
    @allure.description("register with wrong number, with correct otp and country code 996 ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_28_register_wrong_phone_(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   Utils.Data_Object.auth_data.registration)
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "499989981")
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED "SMS not send on phone 996499989981 "')







