import copy
import allure
import unittest
from Utils.commonSteps import send_and_verify
from Utils.commonSteps import login
from Utils.commonSteps import check_userType
from Utils.commonSteps import get_method
from Utils.Data_Object.login_data import DataForLogin



class LoginPositive(unittest.TestCase):

    @allure.suite("Login - Positive")
    @allure.title("Login as individual")
    @allure.description("Trying to Login as individual user and return access token")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_01_login_individual(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login as Business")
    @allure.description("Trying to Login as business user and return access token")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_02_login_business(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['userType'] = "BUSINESS"
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with text deviceToken - Individual")
    @allure.description("Login with text deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_string_devToken_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = "text_as_string"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with text deviceToken - Business")
    @allure.description("Login with text deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_string_devToken_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_sms["userType"] = "BUSINESS"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = "text_as_string"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with integer deviceToken - Individual")
    @allure.description("Login with integer deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_integer_devToken_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = 123456789
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with integer deviceToken - Business")
    @allure.description("Login with integer deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_integer_devToken_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_sms["userType"] = "BUSINESS"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = 1234545478
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with text mobileName - Individual")
    @allure.description("Login with text mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_string_mobileName_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = "string_as_text"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response



    @allure.suite("Login - Positive")
    @allure.title("Login with text mobileName - Business")
    @allure.description("Login with text mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_text_mobileName_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_sms["userType"] = "BUSINESS"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = "string_as_text"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with IOS as mobileOS - Individual")
    @allure.description("Login with IOS as mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_IOS_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "IOS"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response


    @allure.suite("Login - Positive")
    @allure.title("Login with IOS as mobileOS - Business")
    @allure.description("Login with IOS as mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_IOS_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_sms["userType"] = "BUSINESS"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "IOS"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response


    @allure.suite("Login - Positive")
    @allure.title("Login with UNKNOWN as mobileOS - Individual")
    @allure.description("Login with UNKNOWN as mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_UNKNOWN_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "UNKNOWN"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login with UNKNOWN as mobileOS - Business")
    @allure.description("Login with UNKNOWN as mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_UNKNOWN_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_sms["userType"] = "BUSINESS"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "UNKNOWN"
        payload["userSMSId"] = user_sms_id
        payload["mobileNumber"] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 200)
        self.assertIn("access_token", json_response)
        self.assertIsNotNone(json_response.get("access_token"))
        return json_response

    @allure.suite("Login - Positive")
    @allure.title("Login if check is true - Individual")
    @allure.description("Login if check is true for Individual , other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_login_as_ind_if_check_is_True(self):
        check_payload = copy.copy(DataForLogin.payload_check)
        check_payload["phone"] = "996599436774"
        response = check_userType(check_payload)
        check_response = response.json()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599436774"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599436774"
        if 'individualExists' in check_response and check_response['individualExists']:
            userSmSId = send_and_verify(payload_sms, payload_verify )
            payload_login = copy.copy(DataForLogin.payload_login)
            payload_login["userSMSId"] = userSmSId
            payload_login["mobileNumber"] = "996599436774"
            login_res = login(payload_login)
            json_response = login_res.json()
            access_token = json_response.get("access_token")
            profile_res = get_method(access_token)
            profile = profile_res.json()
            self.assertEquals(login_res.status_code, 200)
            self.assertIn("id", profile)
            self.assertIn("name", profile)
            self.assertIn(profile["id"], "7078961e-f59e-4710-b377-813b546c9d4e")
            self.assertIn(profile["name"], "James Hughes")
            return profile

        else:
            print("No individual account is present on this number 599436774")

    @allure.suite("Login - Positive")
    @allure.title("Login if check is true - Individual")
    @allure.description("Login if check is true for Individual , other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_login_as_bus_if_check_is_True(self):
        check_payload = copy.copy(DataForLogin.payload_check)
        check_payload["phone"] = "996599472555"
        response = check_userType(check_payload)
        check_response = response.json()
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599472555"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599472555"
        if 'businessExists' in check_response and check_response['businessExists']:
            userSmSId = send_and_verify(payload_sms, payload_verify )
            payload_login = copy.copy(DataForLogin.payload_login)
            payload_login["userSMSId"] = userSmSId
            payload_login["mobileNumber"] = "996599472555"
            payload_login["userType"] = "BUSINESS"
            login_res = login(payload_login)
            json_response = login_res.json()
            self.assertEquals(login_res.status_code, 200)
            self.assertIn("access_token", json_response)
            self.assertIsNotNone(json_response.get("access_token"), "The 'access_token' should not be None")

        else:
            print("No individual account is present on this number 599472555")
