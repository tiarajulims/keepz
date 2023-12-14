# TODO
import unittest

import faker

import Utils.commonSteps
import Utils.Data_Object.login_data
import Utils.Data_Object.signup_data
import Utils.api_endpoints
import allure


class AuthController(unittest.TestCase):



    @allure.suite("Auth controller - Positive")
    @allure.title("check registered user type ")
    @allure.description("check the phone number if it is registered and the type of user under")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_check(self):

        response = Utils.commonSteps.check_user("599602065")
        self.assertEquals(response.status_code, 200)
        print(response.text)

    @allure.suite("Auth controller - Positive")
    @allure.title("send sms for login ")
    @allure.description("send sms for login purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_send_sms(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              "599989981",
                                              Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
        self.assertEquals(response.status_code, 200)
        return response

    @allure.suite("Auth controller - Positive")
    @allure.title("send sms for Registration ")
    @allure.description("send sms for Registration purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_send_sms(self):
        response = Utils.commonSteps.send_sms("996",
                                              "string",
                                              Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                              Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
        self.assertEquals(response.status_code, 200)
        return response

    @allure.suite("Auth controller - Positive")
    @allure.title("Verify OTP ")
    @allure.description("Verify for Login purposes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_verify_sms(self):
        response = Utils.commonSteps.verify_otp_sms("123456",
                                                    "996",
                                                    "599989981")
        self.assertEquals(response.status_code, 202)
        return response

    @allure.suite("Auth controller - Positive")
    @allure.title("Login as individual")
    @allure.description("Login as individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_Login(self):
        response = Utils.commonSteps.send_and_verify("599989981",
                                                     Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
        response_1 = Utils.commonSteps.login("string",
                                             "string",
                                             "ANDROID",
                                             response,
                                             Utils.Data_Object.login_data.DataForLogin.sms_type_individual)
        return response_1

    @allure.suite("Auth controller - Positive")
    @allure.title("Login as business")
    @allure.description("Login as individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_Login(self):
        response = Utils.commonSteps.send_and_verify("599989981",
                                                     Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
        response_1 = Utils.commonSteps.login("string",
                                             "string",
                                             "ANDROID",
                                             response,
                                             Utils.Data_Object.login_data.DataForLogin.sms_type_business)
        print(response_1)
        return response_1

    @allure.suite("Registration Functionality")
    @allure.title("Register individual user")
    @allure.description("Register individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_register_ind_user(self):
        user_sms_id = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                        Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
        reg_ind = Utils.commonSteps.register_account(birthDate=Utils.Data_Object.signup_data.generate_fake_birthDate(),
                                                     deviceToken="string",
                                                     iban="GE13BG7252322426883581",
                                                     mobileOS="ANDROID",
                                                     name=Utils.Data_Object.signup_data.generate_fake_name(),
                                                     personalNumber=Utils.Data_Object.signup_data.generate_personal_id(),
                                                     userSMSId=user_sms_id,
                                                     userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
        print(reg_ind)
        return reg_ind

    @allure.suite("Registration Functionality")
    @allure.title("Register individual user")
    @allure.description("Register individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_register_bus_user(self):
        user_sms_id = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                        Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
        reg_ind = Utils.commonSteps.register_account(deviceToken="string",
                                                     iban="GE13BG7252322426883581",
                                                     mobileOS="ANDROID",
                                                     name=Utils.Data_Object.signup_data.generate_fake_name(),
                                                     personalNumber=Utils.Data_Object.signup_data.generate_identification_number(),
                                                     userSMSId=user_sms_id,
                                                     userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        print(reg_ind)
        return reg_ind

    def test_08_login_as_ind_if_check_is_True(self):
        res = Utils.commonSteps.check_user("599683762")
        check_res = res.json()
        if check_res["individualExists"]:
            userSmSId = Utils.commonSteps.send_and_verify("599683762",
                                                          Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
            login_res = Utils.commonSteps.login("string",
                                                "string",
                                                "ANDROID",
                                                userSmSId,
                                                Utils.Data_Object.login_data.DataForLogin.sms_type_individual)
            profile_res = Utils.commonSteps.get_method(login_res)
            profile = profile_res.json()
            print(profile_res.json())
            self.assertEquals(profile_res.status_code, 200)
            self.assertIn("name", profile)
            self.assertIn("birthdate", profile)
            self.assertIn("personalNumber", profile)
            self.assertIn("phoneNumber", profile)
            self.assertIn(profile["name"], "Automation")
            self.assertIn(profile["birthdate"], "2014-12-12")
            self.assertIn(profile["personalNumber"], "92014008420")
            self.assertIn(profile["phoneNumber"], "599683762")


        else:
            print("No individual account is present on this number 599683762")

    def test_09_login_as_bus_if_check_is_True(self):
        res = Utils.commonSteps.check_user("599602065")
        check_res = res.json()
        if check_res["businessExists"]:
            userSmSId = Utils.commonSteps.send_and_verify("599602065",
                                                          Utils.Data_Object.login_data.DataForLogin.individual_send_sms)
            login_res = Utils.commonSteps.login("string",
                                                "string",
                                                "ANDROID",
                                                userSmSId,
                                                Utils.Data_Object.login_data.DataForLogin.sms_type_business)
            profile_res = Utils.commonSteps.get_method(login_res)
            profile = profile_res.json()

            self.assertEquals(profile_res.status_code, 200)
            self.assertIn("name", profile)
            self.assertIn("personalNumber", profile)
            self.assertIn("phoneNumber", profile)
            self.assertIn(profile["name"], "James Bond")
            self.assertIn(profile["personalNumber"], "720140084")
            self.assertIn(profile["phoneNumber"], "599602065")
        else:
            print("No individual account is present on this number 599683762")

    def test_10_register_ind_if_check_is_false_for_both(self):
        phone_number = Utils.Data_Object.signup_data.generate_random_mobile_number()
        res = Utils.commonSteps.check_user(phone_number)
        check_res = res.json()
        if not check_res["businessExists"] and not check_res["individualExists"]:
            user_sms_id = Utils.commonSteps.send_and_verify(phone_number,
                                                            Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
            reg_res = Utils.commonSteps.register_account(birthDate=Utils.Data_Object.signup_data.generate_fake_birthDate(),
                                                         deviceToken="string",
                                                         iban="GE13BG7252322426883582",
                                                         mobileOS="ANDROID",
                                                         name=Utils.Data_Object.signup_data.generate_fake_name(),
                                                         personalNumber=Utils.Data_Object.signup_data.generate_personal_id(),
                                                         userSMSId=user_sms_id,
                                                         userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
            print(reg_res.json())
            return reg_res
        else:
            print("impossible to register such account")




    def test_11_register_bus_if_check_is_false_for_both(self):
        phone_number = Utils.Data_Object.signup_data.generate_random_mobile_number()
        res = Utils.commonSteps.check_user(phone_number)
        check_res = res.json()
        if not check_res["businessExists"] and not check_res["individualExists"]:
            user_sms_id = Utils.commonSteps.send_and_verify(phone_number,
                                                            Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
            reg_res = Utils.commonSteps.register_account(
                                                         deviceToken="string",
                                                         iban="GE13BG7252322426883582",
                                                         mobileOS="ANDROID",
                                                         name=Utils.Data_Object.signup_data.generate_fake_name(),
                                                         personalNumber=Utils.Data_Object.signup_data.generate_identification_number(),
                                                         userSMSId=user_sms_id,
                                                         userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
            print(reg_res.json())
            return reg_res
        else:
            print("impossible to register such account")
