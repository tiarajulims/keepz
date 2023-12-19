import json
import allure
import unittest
import Utils.commonSteps
import Utils.api_endpoints
from Utils.Data_Object.login_data import DataForLogin


class LoginNegative(unittest.TestCase):

    @allure.suite("Login functionality")
    @allure.title("empty device token, case - 1")
    @allure.description("empty device token, smsType individual, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_login_empty_dev_token_STI_UTI(self):
        """Login method with empty device token, Sms type individual & UserType Individual
         STI - Sms Type individual, UTI - User Type Individual """
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        response = Utils.commonSteps.login("",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           DataForLogin.sms_type_individual)
        login_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login functionality")
    @allure.title("empty device token, case - 2")
    @allure.description("empty device token, smsType individual, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_login_empty_dev_token_STI_UTB(self):
        """Login method with empty device token, Sms type individual & UserType Business
         STI - Sms Type individual, UTB - User Type Business"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.individual_send_sms)
        response = Utils.commonSteps.login("",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           DataForLogin.sms_type_business)
        login_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login functionality")
    @allure.title("empty device token, case - 3 ")
    @allure.description("empty device token, smsType business, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_login_empty_dev_token_STB_UTB(self):
        """Login method with empty device token, Sms type Business & UserType Business
         STB - Sms Type Business, UTB - User Type Business """
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_business)
        response = Utils.commonSteps.login("",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           DataForLogin.sms_type_business)
        login_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login functionality")
    @allure.title("empty device token, case - 4 ")
    @allure.description("empty device token, smsType business, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_login_empty_dev_token_STB_UTI(self):
        """Login method with empty device token, Sms type Business & UserType Individual
         STB - Sms Type Business, UTI - User Type Individual"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_business)
        response = Utils.commonSteps.login("",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           DataForLogin.sms_type_individual)
        login_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login functionality")
    @allure.title("login with empty mobile OS - case 1")
    @allure.description("empty Mobile OS, smsType individual, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_login_empty_mobileOS_STI_UTI(self):
        """Login with empty mobile OS , Sms Type individual & User Type Individual
        STI - Sms Type individual, UTI - User Type Individual"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        userSmsId = json.dumps(response)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "",
                                            userSmsId,
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Login functionality")
    @allure.title("login with empty mobile OS - case 2")
    @allure.description("empty Mobile OS, smsType individual, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_login_empty_mobile_OS_STI_UTB(self):
        """Login with empty mobile OS , Sms Type individual & User Type Business
        STI - Sms Type individual, UTB - User Type Business"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        userSmsId = json.dumps(response)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "",
                                            userSmsId,
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Login functionality")
    @allure.title("login with empty mobile OS - case 3")
    @allure.description("empty Mobile OS, smsType business, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_login_empty_mobile_OS_STB_UTB(self):
        """Login with empty mobile OS , Sms Type business & User Type Business
        STB - Sms Type business, UTB - User Type Business """
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_business)
        userSmsId = json.dumps(response)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "",
                                            userSmsId,
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Login functionality")
    @allure.title("login with empty mobile OS - case 4")
    @allure.description("empty Mobile OS, smsType business, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_login_empty_mobile_OS_STB_UTI(self):
        """Login with empty mobile OS , Sms Type business & User Type Business
        STB - Sms Type business, UTI - User Type individual """
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        userSmsId = json.dumps(response)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "",
                                            userSmsId,
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Login functionality")
    @allure.title("login with empty UserSmsId - case 1")
    @allure.description("empty User Sms Id,  smsType individual, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_login_empty_userSmsId_STI_UTI(self):
        """Login with empty userSmsId, Sms Type individual & User Type individual
        STI - Sms Type individual, UTI - User Type individual"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            "",
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        print(response1)
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login functionality")
    @allure.title("login with empty UserSmsId - case 2")
    @allure.description("empty User Sms Id,  smsType individual, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_login_empty_userSmsId_STI_UTB(self):
        """Login with empty userSmsId, Sms Type individual & User Type Business
        STI - Sms Type individual, UTB - User Type Business"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_individual)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            "",
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        print(response1)
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login functionality")
    @allure.title("login with empty UserSmsId - case 3")
    @allure.description("empty User Sms Id,  smsType business, user type business ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_login_empty_userSmsId_STB_UTB(self):
        """Login with empty userSmsId, Sms Type Business & User Type Business
        STB - Sms Type Business, UTB - User Type Business"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_business)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            "",
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        print(response1)
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login functionality")
    @allure.title("login with empty UserSmsId - case 4")
    @allure.description("empty User Sms Id,  smsType business, user type individual ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_login_empty_userSmsId_STB_UTI(self):
        """Login with empty userSmsId, Sms Type Business & User Type individual
        STB - Sms Type Business, UTI - User Type individual"""
        Utils.commonSteps.send_and_verify("599989981", DataForLogin.sms_type_business)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            "",
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        print(response1)
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login functionality")
    @allure.title("login with wrong UserSmsId - case 1")
    @allure.description("wrong User Sms Id,  smsType individual, user type individual ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_login_empty_userSmsId_STI_UTI(self):
        """Login with wrong userSmsId, Sms Type individual & User Type individual
        STB - Sms Type Business, UTI - User Type individual"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.individual_send_sms)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            response + "test",
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 404)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], '404 NOT_FOUND "Sms not send with id ' + response + 'test "')

    @allure.suite("Login functionality")
    @allure.title("login with wrong UserSmsId - case 2")
    @allure.description("wrong User Sms Id,  smsType business, user type individual ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_14_login_empty_userSmsId_STB_UTI(self):
        """Login with wrong userSmsId, Sms Type business & User Type individual
        STB - Sms Type Business, UTI - User Type individual"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.business_sens_sms)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            response + "test",
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 404)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], '404 NOT_FOUND "Sms not send with id ' + response + 'test "')

    @allure.suite("Login functionality")
    @allure.title("login with wrong UserSmsId - case 3")
    @allure.description("wrong User Sms Id,  smsType business, user type business ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_15_login_empty_userSmsId_STB_UTB(self):
        """Login with wrong userSmsId, Sms Type business & User Type business
        STB - Sms Type business, UTB - User Type business"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.individual_send_sms)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            response + "test",
                                            DataForLogin.sms_type_individual)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 404)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], '404 NOT_FOUND "Sms not send with id ' + response + 'test "')

    @allure.suite("Login functionality")
    @allure.title("login with wrong UserSmsId - case 4")
    @allure.description("wrong User Sms Id,  smsType individual, user type business ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_16_login_empty_userSmsId_STI_UTB(self):
        """Login with wrong userSmsId, Sms Type business & User Type business
        STI - Sms Type individual, UTI - User Type business"""
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.individual_send_sms)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            response + "test",
                                            DataForLogin.sms_type_business)
        login_response = response1.json()
        self.assertEquals(response1.status_code, 404)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"], '404 NOT_FOUND "Sms not send with id ' + response + 'test "')

    @allure.suite("Login functionality")
    @allure.title("login with empty user type")
    @allure.description("Login without entering user type, else data is correct")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_17_login_with_empty_userType(self):
        response = Utils.commonSteps.send_and_verify("599989981", DataForLogin.individual_send_sms)
        response1 = Utils.commonSteps.login("string",
                                            "string",
                                            "ANDROID",
                                            response,
                                            "")
        login_response = response1.json()
        self.assertEquals(response1.status_code, 400)
        self.assertIn("message", login_response)
        self.assertIn(login_response["message"],
                      " can't be parsed to UserType.UserType must be one of this: INDIVIDUAL, BUSINESS")


def test_30():
    token = Utils.commonSteps.get_auth_token()
    response = Utils.commonSteps.get_method(token)
    print(response.text)
