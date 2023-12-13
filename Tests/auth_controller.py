import json
# TODO
import unittest
import Utils.commonSteps
import Utils.Data_Object.login_data
import Utils.commonSteps
import Utils.api_endpoints
import allure


class AuthController(unittest.TestCase):


    def test_01_check(self):

        response = Utils.commonSteps.check_user("599989981")
        self.assertEquals(response.status_code, 200)
        print(response.text)



    def test_2_send_sms(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "599989981",
                                              Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
        self.assertEquals(response.status_code, 200)
        return response

    def test_03_verify_sms(self):
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "599989981")
        self.assertEquals(response.status_code, 202)
        return response

    def test_04_Login(self):
        response = Utils.commonSteps.send_and_verify(Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
        response_1 = Utils.commonSteps.login("string",
                                             "string",
                                             "ANDROID",
                                             response,
                                             Utils.Data_Object.login_data.DataForLogin.sms_type_individual)
        self.assertEquals(response_1.status_code, 200)
        response_json = json.loads(response_1.text)
        access_token = response_json.get("access_token")
        return access_token


    @allure.suite("Login Functionality - Check")
    @allure.title("login  with empty phone for check")
    @allure.description("try to login without inserting number in check endpoint")
    @allure.severity(allure.severity_level.NORMAL)
    def test_29_login_with_empty_phone(self):
        response = Utils.commonSteps.check_user("599989981")
        sendSms = response.json()
        print(sendSms)
        self.assertEquals(response.status_code, 200)
        self.assertIn("individualExists", sendSms)
        self.assertIn("businessExists", sendSms)
        self.assertIn(str(sendSms["individualExists"]), "True")
        self.assertIn(str(sendSms["businessExists"]), "True")
