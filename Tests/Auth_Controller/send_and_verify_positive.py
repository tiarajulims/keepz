import copy
import unittest
import allure
from Utils.commonSteps import check_userType
from Utils.commonSteps import send_sms
from Utils.commonSteps import verify_otp_sms
from Utils import data_generator
from Utils.Data_Object.login_data import DataForLogin


class SendVerifyPositive(unittest.TestCase):


    @allure.suite("Check - Positive")
    @allure.title("Both user type true ")
    @allure.description("Check, if phone number has both accounts")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_check_both_true(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = "996599989981"
        response = check_userType(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_response["individualExists"], True)
        self.assertEquals(json_response["businessExists"], True)


    @allure.suite("Check- Positive")
    @allure.title("Only individual account True")
    @allure.description("Check, if phone number has only individual True")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_check_ind_true(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = "996599989982"
        response = check_userType(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_response["individualExists"], True)
        self.assertEquals(json_response["businessExists"], False)


    @allure.suite("Check - Positive")
    @allure.title("Both user type false")
    @allure.description("Check, if phone number has None accounts")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_check_both_false(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = "996599989983"
        response = check_userType(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_response["individualExists"], False)
        self.assertEquals(json_response["businessExists"], False)


    @allure.suite("Check - Positive")
    @allure.title("Only business account True")
    @allure.description("Check, if phone number has only business True")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_check_bus_true(self):
        payload = copy.copy(DataForLogin.payload_check)
        payload["phone"] = "996599328692"
        response = check_userType(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_response["businessExists"], True)
        self.assertEquals(json_response["individualExists"], False)

    @allure.suite("Send sms - Positive")
    @allure.title("Send sms for login ")
    @allure.description("Send sms for login purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_send_sms_login(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["phone"] = "599989981"
        response = send_sms(payload)
        self.assertEquals(response.status_code, 200)
        return response

    @allure.suite("Send sms - Positive")
    @allure.title("Send sms for registration")
    @allure.description("Send sms for registration purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_send_sms_registration(self):
        payload = copy.copy(DataForLogin.payload_send_sms)
        payload["smsType"] = "REGISTRATION"
        response = send_sms(payload)
        self.assertEquals(response.status_code, 200)
        return response

    @allure.suite("Send sms - Positive")
    @allure.title("Verify OTP for login ")
    @allure.description("Verify OTP for Login purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_verify_sms_login(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        response = verify_otp_sms(payload_verify)
        self.assertEquals(response.status_code, 202)
        return response


    @allure.suite("Send sms - Positive")
    @allure.title("Verify OTP for registration ")
    @allure.description("Verify OTP for Login purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_verify_sms_registration(self):
        fake_number = data_generator.generate_random_mobile_number()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = fake_number
        payload_sms["smsType"] = "REGISTRATION"
        send_sms(payload_sms)
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = fake_number
        response = verify_otp_sms(payload_verify)
        self.assertEquals(response.status_code, 202)
        return response




