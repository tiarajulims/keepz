import allure
import unittest
import copy
from Utils.Data_Object.login_data import DataForLogin
from Utils.commonSteps import send_and_verify
from Utils.commonSteps import login


class LoginNegative(unittest.TestCase):

    @allure.suite("Login - Negative")
    @allure.title("Login with empty deviceToken - Individual")
    @allure.description("Login with empty deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_empty_devToken_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with None deviceToken - Individual")
    @allure.description("Login with None deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_None_devToken_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with space as deviceToken - Individual")
    @allure.description("Login with space as deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_space_devToken_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with empty deviceToken - Business")
    @allure.description("Login with empty deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_empty_devToken_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with None deviceToken - Business")
    @allure.description("Login with None deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_None_devToken_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with space as deviceToken - Business")
    @allure.description("Login with space as deviceToken, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_space_devToken_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["deviceToken"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[deviceToken-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileName - Individual")
    @allure.description("Login with empty mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_empty_mobileName_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileName - Business")
    @allure.description("Login with empty mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_empty_mobileName_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = ""
        payload["userType"] = "BUSINESS"
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileName - Individual")
    @allure.description("Login with None mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_None_mobileName_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileName - Business")
    @allure.description("Login with None mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_None_mobileName_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with space mobileName - Individual")
    @allure.description("Login with space mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_space_mobileName_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileName - Business")
    @allure.description("Login with None mobileName, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_empty_mobileName_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileName"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileName-Is required]")




    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileOS - Individual")
    @allure.description("Login with empty mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_empty_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")



    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileOS - Business")
    @allure.description("Login with empty mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_empty_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileOS - Individual")
    @allure.description("Login with None mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_None_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " [mobileOS-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileOS - Business")
    @allure.description("Login with empty mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_empty_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileOS-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with space mobileOS - Individual")
    @allure.description("Login with space mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_17_space_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "  can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")


    @allure.suite("Login - Negative")
    @allure.title("Login with space mobileOS - Business")
    @allure.description("Login with space mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_space_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")


    @allure.suite("Login - Negative")
    @allure.title("Login with lowercase mobileOS - Individual")
    @allure.description("Login with lowercase mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_19_lowercase_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "android"
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "android can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")


    @allure.suite("Login - Negative")
    @allure.title("Login with lowercase mobileOS - Business")
    @allure.description("Login with lowercase mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_lowercase_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "android"
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "android can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")


    @allure.suite("Login - Negative")
    @allure.title("Login with invalid mobileOS - Individual")
    @allure.description("Login with invalid mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_invalid_mobileOS_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "iOS"
        payload['mobileNumber'] = "996599989981"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "iOS can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")


    @allure.suite("Login - Negative")
    @allure.title("Login with invalid mobileOS - Business")
    @allure.description("Login with invalid mobileOS, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_22_invalid_mobileOS_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["mobileOS"] = "Android"
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userSMSId"] = user_sms_id
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "Android can't be parsed to MobileOS.MobileOS "
                                                "must be one of this: IOS, ANDROID, UNKNOWN")



    @allure.suite("Login - Negative")
    @allure.title("Login with empty userSMSId - Individual")
    @allure.description("Login with empty userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_23_empty_userSMSId_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = ""
        payload['mobileNumber'] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with empty userSMSId - Business")
    @allure.description("Login with empty userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_empty_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = ""
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")




    @allure.suite("Login - Negative")
    @allure.title("Login with None userSMSId - Individual")
    @allure.description("Login with None userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_None_userSMSId_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = None
        payload['mobileNumber'] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")


    @allure.suite("Login - Negative")
    @allure.title("Login with None userSMSId - Business")
    @allure.description("Login with None userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_26_None_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = None
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")




    @allure.suite("Login - Negative")
    @allure.title("Login with space userSMSId - Individual")
    @allure.description("Login with space userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_27_space_userSMSId_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = " "
        payload['mobileNumber'] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with space userSMSId - Business")
    @allure.description("Login with space userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_28_space_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = " "
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userSMSId-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with invalid userSMSId - Individual")
    @allure.description("Login with invalid userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_29_invalid_userSMSId_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = "invalid" + user_sms_id
        payload['mobileNumber'] = "996599989981"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], f'404 NOT_FOUND "Sms not send with i'
                                                f'd invalid{user_sms_id} "')



    @allure.suite("Login - Negative")
    @allure.title("Login with invalid userSMSId - Business")
    @allure.description("Login with invalid userSMSId, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_30_invalid_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = "invalid" + user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 404)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], f'404 NOT_FOUND "Sms not send with i'
                                                f'd invalid{user_sms_id} "')


    @allure.suite("Login - Negative")
    @allure.title("Login with empty userType - Individual")
    @allure.description("Login with empty userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_31_empty_userType_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = ""
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")




    @allure.suite("Login - Negative")
    @allure.title("Login with empty userType - Business")
    @allure.description("Login with empty userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_32_empty_userType_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userType"] = ""
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")


    @allure.suite("Login - Negative")
    @allure.title("Login with None userType - Individual")
    @allure.description("Login with None userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_33_None_userType_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = None
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[userType-Is required]")




    @allure.suite("Login - Negative")
    @allure.title("Login with None userType - Business")
    @allure.description("Login with NOne userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_34_invalid_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userType"] = None
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " [userType-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with space userType - Individual")
    @allure.description("Login with space userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_35_space_userType_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = " "
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")



    @allure.suite("Login - Negative")
    @allure.title("Login with space userType - Business")
    @allure.description("Login with space userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_36_space_userSMSId_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "BUSINESS"
        payload["userType"] = " "
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], " can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")

    @allure.suite("Login - Negative")
    @allure.title("Login with lowercase userType - Individual")
    @allure.description("Login with lowercase userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_37_lowercase_userType_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "Individual"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "Individual can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")

    @allure.suite("Login - Negative")
    @allure.title("Login with lowercase userType - Business")
    @allure.description("Login with lowercase userType, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_38_lowercase_userType_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "996599989981"
        payload["userType"] = "Business"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "Business can't be parsed to UserType.UserType "
                                                "must be one of this: INDIVIDUAL, BUSINESS")


    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileNumber - Individual")
    @allure.description("Login with empty mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_39_empty_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = ""
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ['[mobileNumber-Is required, must match "^\\d{12}$"]',
                                                 '[must match "^\\d{12}$", mobileNumber-Is required]'])



    @allure.suite("Login - Negative")
    @allure.title("Login with empty mobileNumber - Business")
    @allure.description("Login with empty mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_39_empty_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = ""
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ['[mobileNumber-Is required, must match "^\\d{12}$"]',
                                                 '[must match "^\\d{12}$", mobileNumber-Is required]'])

    @allure.suite("Login - Negative")
    @allure.title("Login with space mobileNumber - Individual")
    @allure.description("Login with space mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_40_space_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = " "
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ['[mobileNumber-Is required, must match "^\\d{12}$"]',
                                                 '[must match "^\\d{12}$", mobileNumber-Is required]'])

    @allure.suite("Login - Negative")
    @allure.title("Login with space mobileNumber - Business")
    @allure.description("Login with space mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_41_space_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = " "
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], ['[mobileNumber-Is required, must match "^\\d{12}$"]',
                                                 '[must match "^\\d{12}$", mobileNumber-Is required]'])

    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileNumber - Individual")
    @allure.description("Login with None mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_42_None_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = None
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileNumber-Is required]")



    @allure.suite("Login - Negative")
    @allure.title("Login with None mobileNumber - Business")
    @allure.description("Login with None mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_43_None_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = None
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], "[mobileNumber-Is required]")

    @allure.suite("Login - Negative")
    @allure.title("Login with text mobileNumber - Individual")
    @allure.description("Login with tet mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_44_text_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "string"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')

    @allure.suite("Login - Negative")
    @allure.title("Login with text mobileNumber - Business")
    @allure.description("Login with text mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_45_text_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "string"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')



    @allure.suite("Login - Negative")
    @allure.title("Login witt long mobileNumber - Individual")
    @allure.description("Login with long mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_46_long_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "5999899811231"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')

    @allure.suite("Login - Negative")
    @allure.title("Login witt long mobileNumber - Business")
    @allure.description("Login with long mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_47_long_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "5999899811231"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')

    @allure.suite("Login - Negative")
    @allure.title("Login witt long mobileNumber - Individual")
    @allure.description("Login with long mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_48_short_mobileNumber_login_ind(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "5999899"
        response = login(payload)
        json_response = response.json()
        print(json_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')

    @allure.suite("Login - Negative")
    @allure.title("Login witt short mobileNumber - Business")
    @allure.description("Login with short mobileNumber, other data is valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_49_short_mobileNumber_login_bus(self):
        payload_sms = copy.copy(DataForLogin.payload_send_sms)
        payload_sms["phone"] = "599989981"
        payload_verify = copy.copy(DataForLogin.payload_verify_sms)
        payload_verify["phone"] = "599989981"
        user_sms_id = send_and_verify(payload_sms, payload_verify)
        payload = copy.copy(DataForLogin.payload_login)
        payload["userSMSId"] = user_sms_id
        payload['mobileNumber'] = "59998998"
        payload["userType"] = "BUSINESS"
        response = login(payload)
        json_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_response)
        self.assertIn(json_response["message"], '[must match "^\\d{12}$"]')



