import json
import requests
import unittest
import Utils.commonSteps
import Utils.api_endpoints


class LoginNegative(unittest.TestCase):

    def test_01_Login_invalid_userSmsId_individual(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   "LOGIN_AS_INDIVIDUAL")
        Utils.commonSteps.verify_otp_sms("123456",
                                         "996",
                                         "599989981")
        response = Utils.commonSteps.login("123567",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           "INDIVIDUAL")
        login_response = response.json()
        print(login_response)
        assert response.status_code == 404
        assert "message" in login_response
        assert login_response["message"] == '404 NOT_FOUND "Sms not send with id testtest "'










    def test_02_Login_invalid_mobileOS(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   "LOGIN_AS_INDIVIDUAL")
        Utils.commonSteps.verify_otp_sms("123456",
                                         "996",
                                         "599989981")
        response = Utils.commonSteps.login("string",
                                           "string",
                                           "invalidMobOS",
                                           "testtest",
                                           "INDIVIDUAL")
        login_response = response.json()
        assert response.status_code == 400
        assert "message" in login_response
        assert login_response[
                   "message"] == "invalidMobOS can't be parsed to MobileOS.MobileOS must be one of this: "'IOS, ANDROID, UNKNOWN'
        print(response.text)


    def test_03_Login_empty_deviceToken(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   "LOGIN_AS_INDIVIDUAL")
        Utils.commonSteps.verify_otp_sms("123456",
                                         "996",
                                         "599989981")
        response = Utils.commonSteps.login("",
                                           "string",
                                           "ANDROID",
                                           "testtest",
                                           "INDIVIDUAL")
        login_response = response.json()
        assert response.status_code == 400
        assert "message" in login_response
        assert login_response["message"] == "[deviceToken-Is required]"
        print(response.text)


    def test_04_Login_mobileName_empty(self):
        Utils.commonSteps.send_sms("996",
                                   "string",
                                   "599989981",
                                   "LOGIN_AS_INDIVIDUAL")
        response1 = Utils.commonSteps.verify_otp_sms("123456",
                                                     "996",
                                                     "599989981")
        userSmsId = response1.text
        response = Utils.commonSteps.login("string",
                                           None,
                                           "ANDROID", userSmsId ,
                                           "INDIVIDUAL")
        login_response = response.json()
        assert response.status_code == 400
        assert "message" in login_response
        assert login_response["message"] == "[mobileName-Is required]"



    def test0001_123(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "599989981",
                                              Utils..auth_data.individual)
        response1 = Utils.commonSteps.verify_otp_sms("654321",
                                                     "996",
                                                     "499989981", )
        print(response1.text)