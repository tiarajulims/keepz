import unittest
import allure
import sys
import os
import copy

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from Utils.commonSteps import send_sms
from Utils.commonSteps import verify_otp_sms
from Utils.Data_Object.login_data import DataForLogin
from Utils.commonSteps import check_userType
from Utils import data_generator


class SendVerifyNegative(unittest.TestCase):
    # ALLURE SUITE TITLES FOR VERIFY SMS
    verify_sms_login_individual = "Login Functionality - Verify Sms -  Individual"
    verify_sms_login_business = "Login Functionality - Verify Sms -  Business"
    verify_sms_registration = "Registration Functionality - Verify Sms"

    @allure.suite("Check - Negative")
    @allure.title("Check with None phone")
    @allure.description("Check response by passing None as value")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_check_with_None_phone(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = None
        response = check_userType(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[must not be blank]")

    @allure.suite("Check - Negative")
    @allure.title("Check with empty phone")
    @allure.description("Check response by passing empty value")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_check_with_empty_phone(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = ""
        response = check_userType(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ["[must not be blank, Invalid format of phone]",
                                                 "[Invalid format of phone, must not be blank]"])


    @allure.suite("Check - Negative")
    @allure.title("Check with space phone")
    @allure.description("Check response by passing space as value")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_check_with_space_phone(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = " "
        response = check_userType(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ["[must not be blank, Invalid format of phone]",
                                                 "[Invalid format of phone, must not be blank]"])



    @allure.suite("Check - Negative")
    @allure.title("Check with test as phone")
    @allure.description("Check response by passing text as value")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_check_with_text_phone(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = "string"
        response = check_userType(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[Invalid format of phone]")



    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with empty countryCode")
    @allure.description("Send Sms with empty countryCode and all other with valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_sendSms_empty_countyCode(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["countryCode"] = ""
        response = send_sms(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[Invalid format of countryCode]")


    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with None countryCode")
    @allure.description("Send Sms with None countryCode and all other with valid data")
    @allure.severity(allure.severity_level.NORMAL)
    # TODO the assert must be changed after https://makingscience.atlassian.net/browse/EX07198-754 will be fixed
    def test_06_sendSms_None_countyCode(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["countryCode"] = None
        response = send_sms(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[Invalid Country Code]")


    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with space countryCode")
    @allure.description("Send Sms with space as countryCode and all other with valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_sendSms_space_countyCode(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["countryCode"] = " "
        response = send_sms(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[Invalid format of countryCode]")

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with text as countryCode")
    @allure.description("Send Sms with text as countryCode and all other with valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_sendSms_text_countyCode(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["countryCode"] = "string"
        response = send_sms(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[Invalid format of countryCode]")




    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with empty phone - Login")
    @allure.description("Send sms with empty phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_sendSms_empty_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = ""
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone, must not be blank]",
                       "[must not be blank, Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with space as phone - Login")
    @allure.description("Send sms with space as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_sendSms_space_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = " "
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone, must not be blank]",
                       "[must not be blank, Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with None as phone - Login")
    @allure.description("Send sms with None phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_sendSms_None_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = None
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[must not be blank]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with short phone - Login")
    @allure.description("Send sms with short phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_sendSms_short_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "345"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with long phone - Login")
    @allure.description("Send sms with long phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_sendSms_long_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "3451231231231321"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with text as phone - Login")
    @allure.description("Send sms with text as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_sendSms_text_phone_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "string"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with empty phone - Registration")
    @allure.description("Send sms with empty phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_sendSms_empty_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = ""
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone, must not be blank]",
                                           "[must not be blank, Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with space as phone - Registration")
    @allure.description("Send sms with space as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_sendSms_space_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = " "
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone, must not be blank]",
                                           "[must not be blank, Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with None as phone - Registration")
    @allure.description("Send sms with None phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_17_sendSms_None_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = None
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[must not be blank]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with short phone - Registration")
    @allure.description("Send sms with short phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_sendSms_short_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "345"
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with long phone - Registration")
    @allure.description("Send sms with long phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_19_sendSms_long_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "3451231231231321"
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with text as phone - Registration")
    @allure.description("Send sms with text as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_sendSms_text_phone_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "string"
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[Invalid format of phone]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with empty smsType")
    @allure.description("Send sms with empty smsType all other valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_sendSms_empty_smsType(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = ""
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], [" can't be parsed to SMSType.SMSType must be one of this: "
                                           "REGISTRATION, LOGIN, PASSWORD_RESET, PHONE_CHANGE"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with space as smsType")
    @allure.description("Send sms with space as smsType all other valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_22_sendSms_space_smsType(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = " "
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], [" can't be parsed to SMSType.SMSType must be one of this: "
                                           "REGISTRATION, LOGIN, PASSWORD_RESET, PHONE_CHANGE"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with None smsType")
    @allure.description("Send sms with None smsType all other valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_23_sendSms_None_smsType(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = None
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["[must not be null]"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with incorrect smsType - Login")
    @allure.description("Send sms with incorrect smsType, all other valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_sendSms_None_smsType(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = "LOGI"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["LOGI can't be parsed to SMSType.SMSType must be one of this: "
                                           "REGISTRATION, LOGIN, PASSWORD_RESET, PHONE_CHANGE"])

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with incorrect smsType - Registration")
    @allure.description("Send sms with incorrect smsType, all other valid data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_sendSms_None_smsType(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = "REGISTRATion"
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], ["REGISTRATion can't be parsed to SMSType.SMSType must be one of this: "
                                           "REGISTRATION, LOGIN, PASSWORD_RESET, PHONE_CHANGE"])

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty OTP - Login")
    @allure.description("Verify with empty OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_26_verify_empty_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = ""
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space as OTP - Login")
    @allure.description("Verify with space as OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_27_verify_space_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = " "
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms None OTP - Login")
    @allure.description("Verify with None OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_28_verify_None_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = None
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms short OTP - Login")
    @allure.description("Verify with short OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    # TODO the assertion must be changed when https://makingscience.atlassian.net/browse/EX07198-720 will be fixed
    def test_29_verify_short_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "1"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], f'428 PRECONDITION_REQUIRED '
                                          f'"SMS not send on phone 996{fake_number} "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms long OTP - Login")
    @allure.description("Verify with long OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    # TODO the assertion must be changed when https://makingscience.atlassian.net/browse/EX07198-720 will be fixed
    def test_30_verify_long_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "12345678"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], f'428 PRECONDITION_REQUIRED '
                                          f'"SMS not send on phone 996{fake_number} "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms text as OTP - Login")
    @allure.description("Verify with text as OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_31_verify_text_otp_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "string"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], f'428 PRECONDITION_REQUIRED '
                                          f'"SMS not send on phone 996{fake_number} "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty OTP - Registration")
    @allure.description("Verify with empty OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_32_verify_empty_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = ""
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space as OTP - Registration")
    @allure.description("Verify with space as OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_33_verify_space_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = " "
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms None OTP - Registration")
    @allure.description("Verify with None OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_34_verify_None_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = None
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '[must not be blank]')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms short OTP - Registration")
    @allure.description("Verify with short OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_35_verify_short_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "1"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms long OTP - Registration")
    @allure.description("Verify with long OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_36_verify_long_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "12345678"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms text as OTP - Registration")
    @allure.description("Verify with text as OTP , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_37_verify_text_otp_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["code"] = "string"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 406)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '406 NOT_ACCEPTABLE "Invalid SMS Code"')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty countryCode - Login")
    @allure.description("Verify with empty countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_38_verify_empty_countryCode_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = ""
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space countryCode - Login")
    @allure.description("Verify with space countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_39_verify_space_countryCode_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = " "
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with None countryCode - Login")
    @allure.description("Verify with None countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_40_verify_None_countryCode_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = None
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with text as countryCode - Login")
    @allure.description("Verify with text as countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_41_verify_text_countryCode_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = "string"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], f'428 PRECONDITION_REQUIRED '
                                          f'"SMS not send on phone string{fake_number} "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty countryCode - Registration")
    @allure.description("Verify with empty countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_42_verify_empty_countryCode_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = ""
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space countryCode - Registration")
    @allure.description("Verify with space countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_43_verify_space_countryCode_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = " "
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with None countryCode - Registration")
    @allure.description("Verify with None countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_44_verify_None_countryCode_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = None
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with text as countryCode - Registration")
    @allure.description("Verify with text as countryCode , all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_45_verify_text_countryCode_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["countryCode"] = "string"
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], f'428 PRECONDITION_REQUIRED '
                                          f'"SMS not send on phone string{fake_number} "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty phone - Login")
    @allure.description("Verify with empty phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_46_verify_empty_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = ""
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space as phone - Login")
    @allure.description("Verify with space as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_47_verify_space_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = " "
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with None as phone - Login")
    @allure.description("Verify with None as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_48_verify_None_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = None
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with short phone - Login")
    @allure.description("Verify with short phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_49_verify_short_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "5932"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 9965932 "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with long phone - Login")
    @allure.description("Verify with long phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_50_verify_long_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599123432442342"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 996599123432442342 "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with text as phone - Login")
    @allure.description("Verify with text as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_51_verify_text_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "string"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 996string "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with empty phone - Registration")
    @allure.description("Verify with empty phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_52_verify_empty_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = ""
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with space as phone - Registration")
    @allure.description("Verify with space as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_53_verify_space_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = " "
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with None as phone - Registration")
    @allure.description("Verify with None as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_54_verify_None_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = None
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], "[must not be blank]")

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with short phone - Registration")
    @allure.description("Verify with short phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_55_verify_short_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "5932"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 9965932 "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with long phone - Registration")
    @allure.description("Verify with long phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_56_verify_long_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599123432442342"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 996599123432442342 "')

    @allure.suite("Verify sms - Negative")
    @allure.title("Verify sms with text as phone - Registration")
    @allure.description("Verify with text as phone, all other with correct data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_57_verify_text_phone_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "string"
        response = verify_otp_sms(payload_verify)
        sendSms = response.json()
        self.assertEquals(response.status_code, 428)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"], '428 PRECONDITION_REQUIRED'
                                          ' "SMS not send on phone 996string "')

    @allure.suite("Send sms - Negative")
    @allure.title("Send sms with unregistered phone - Login")
    @allure.description("Send sms with text as phone number and country code 996")
    @allure.severity(allure.severity_level.NORMAL)
    def test_58_sendSms_unregistered_phone_login(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = fake_number
        response = send_sms(payload)
        sendSms = response.json()
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", sendSms)
        self.assertIn(sendSms["message"],
                      [f'404 NOT_FOUND "Account does not exist for mobile number: 996{fake_number}"'])
