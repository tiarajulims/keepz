import unittest
import allure
import Utils.commonSteps
import Utils.Data_Object.signup_data
import Utils.api_endpoints


class SignUpNegative(unittest.TestCase):

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_register_ind_user_none_dob(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate=None,
                                                      deviceToken="string",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[birthDate-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_register_ind_user_empty_dob(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="",
                                                      deviceToken="string",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[birthDate-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with future date of birth")
    @allure.description("Trying to register individual user with future date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_register_ind_user_future_dob(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2025-11-11",
                                                      deviceToken="string",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[birthDate-Must be past]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_register_bus_user_future_dob(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2025-11-11",
                                                      deviceToken="string",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[birthDate-Must not be provided, birthDate-Must be past]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_register_ind_user_empty_devToken(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2008-11-11",
                                                      deviceToken="",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[deviceToken-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_register_ind_user_none_devToken(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2021-11-11",
                                                      deviceToken=None,
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[deviceToken-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual without date of birth")
    @allure.description("Trying to register individual user without entering date of birth")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_register_bus_user_empty_devToken(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="",
                                                      iban="GE30TB4445352926927826",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[deviceToken-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with empty iban")
    @allure.description("Trying to register individual user without entering iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_08_register_ind_user_empty_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="1995-11-11",
                                                      deviceToken="string",
                                                      iban="",  # GE30TB4445352926927826
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], ['[iban-Is required, iban-Invalid Format]',
                      '[iban-Invalid Format, iban-Is required]'])

    @allure.suite("Registration Functionality")
    @allure.title("Register business with empty iban")
    @allure.description("Trying to register business user without entering iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_09_register_bus_user_empty_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="",  # GE30TB4445352926927826
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Is required, iban-Invalid Format]' or
                      '[iban-Invalid Format, iban-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with no iban")
    @allure.description("Trying to register individual user without entering iban")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_register_ind_user_none_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2010-12-11", deviceToken="string",
                                                      iban=None,  # GE30TB4445352926927826
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register business with no iban")
    @allure.description("Trying to register business user without entering iban")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_register_bus_user_none_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban=None,
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Is required]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with short iban")
    @allure.description("Trying to register individual user entering short iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_12_register_ind_user_short_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2010-12-11",
                                                      deviceToken="string",
                                                      iban="GE30TB4445",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register business with short iban")
    @allure.description("Trying to register business user entering short iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_register_ind_user_short_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE30TB4445",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with long iban")
    @allure.description("Trying to register individual user entering long iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_14_register_ind_user_long_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2018-11-11",
                                                      deviceToken="string",
                                                      iban="GE30TB44453529269278261",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register business with long iban")
    @allure.description("Trying to register business user entering long iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_15_register_bus_user_long_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE30TB44453529269278261",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with invalid iban")
    @allure.description("Trying to register individual user entering invalid iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_16_register_ind_user_invalid_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2017-12-11",
                                                      deviceToken="string",
                                                      iban="GE13157252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register business with invalid iban")
    @allure.description("Trying to register business user entering invalid iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_17_register_bus_user_invalid_iban(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13157252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], '[iban-Invalid Format]')

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with empty mobileOS")
    @allure.description("Trying to register individual user leaving empty mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_register_ind_user_empty_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2017-12-11",
                                                      deviceToken="string",
                                                      iban="GE13TB7252322426883581",
                                                      mobileOS="",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with empty mobileOS")
    @allure.description("Trying to register business user leaving empty mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_19_register_bus_user_empty_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      " can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with none mobileOS")
    @allure.description("Trying to register individual user with none mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_register_ind_user_none_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2017-12-11",
                                                      deviceToken="string",
                                                      iban="GE13TB7252322426883581",
                                                      mobileOS=None,
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[mobileOS-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with none mobileOS")
    @allure.description("Trying to register business user with none mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_register_bus_user_none_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS=None,
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[mobileOS-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with wrong mobileOS")
    @allure.description("Trying to register individual user with wrong mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_22_register_ind_user_wrong_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2017-12-11",
                                                      deviceToken="string",
                                                      iban="GE13TB7252322426883581",
                                                      mobileOS="andoid",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "andoid can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with wrong mobileOS")
    @allure.description("Trying to register business user with wrong mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_23_register_bus_user_wrong_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ios",
                                                      name="testName",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "ios can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with wrong mobileOS")
    @allure.description("Trying to register individual user with wrong mobileOS")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_register_ind_user_wrong_mobOS(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2017-12-11",
                                                      deviceToken="string",
                                                      iban="GE13TB7252322426883581",
                                                      mobileOS="andoid",
                                                      name="testName",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "andoid can't be parsed to MobileOS.MobileOS must be one of this: IOS, ANDROID, UNKNOWN")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with empty name")
    @allure.description("Trying to register individual user leaving empty name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_25_register_ind_user_empty_name(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2012-12-11",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="IOS",
                                                      name="",
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[name-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with empty name")
    @allure.description("Trying to register business user with empty name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_26_register_bus_user_empty_name(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="",
                                                      personalNumber="920140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[name-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with none name")
    @allure.description("Trying to register individual user with none name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_27_register_ind_user_none_name(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2014-11-11",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="IOS",
                                                      name=None,
                                                      personalNumber="92014008420",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[name-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with none name")
    @allure.description("Trying to register business user with none name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_28_register_bus_user_none_name(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name=None,
                                                      personalNumber="820140084",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      "[name-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with empty Personal Number")
    @allure.description("Trying to register individual user with leaving empty personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_29_register_ind_user_empty_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2013-12-13",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"],
                      ["[personalNumber-Length must be 11, personalNumber-Is required]", "[personalNumber-Is required, personalNumber-Length must be 11]"])

    @allure.suite("Registration Functionality")
    @allure.title("Register business with empty Personal Number")
    @allure.description("Trying to register business user with leaving empty personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_30_register_bus_user_empty_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], ["[personalNumber-Is required, personalNumber-Length must be 9]",
                                                "[personalNumber-Length must be 9, personalNumber-Is required]"])

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with none Personal Number")
    @allure.description("Trying to register individual user with none personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_31_register_ind_user_none_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2014-12-12",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber=None,
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with none Personal Number")
    @allure.description("Trying to register business user with none personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_32_register_bus_user_none_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber=None,
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Is required]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with 10 char Personal Number")
    @allure.description("Trying to register individual user with 10 char personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_33_register_ind_user_10_char_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2014-12-12",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="9201400842",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 11]")

    @allure.suite("Registration Functionality")
    @allure.title("Register individual with 12 char Personal Number")
    @allure.description("Trying to register individual user with 12 char personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_34_register_ind_user_10_char_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2014-12-12",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="920140084200",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 11]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with 8 char Personal Number")
    @allure.description("Trying to register business user with none personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_35_register_bus_user_8_char_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="elevench",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        print(reg_response)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 9]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with 10 char Personal Number")
    @allure.description("Trying to register business user with none personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_36_register_bus_user_10_char_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="9201400842",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 9]")


    @allure.suite("Registration Functionality")
    @allure.title("Register individual with string as Personal Number")
    @allure.description("Trying to register individual user with string as personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_37_register_ind_user_invalid_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(birthDate="2014-12-12",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="elevencharr",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 11]")

    @allure.suite("Registration Functionality")
    @allure.title("Register business with string as  Personal Number")
    @allure.description("Trying to register business user with string as personal Number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_38_register_bus_user_8_char_personalNum(self):
        userSmsId = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                      "REGISTRATION")
        response = Utils.commonSteps.register_account(deviceToken="string",
                                                      iban="GE13BG7252322426883581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="elevencha",
                                                      userSMSId=userSmsId,
                                                      userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        reg_response = response.json()
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", reg_response)
        self.assertIn(reg_response["message"], "[personalNumber-Length must be 9]")
