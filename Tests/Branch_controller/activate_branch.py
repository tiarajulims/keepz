import copy

import allure

from Utils.Data_Object.login_data import DataForLogin
from Utils.commonSteps import check_userType, send_sms


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
