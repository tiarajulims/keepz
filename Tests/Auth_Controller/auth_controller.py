# TODO
import copy
import unittest
from Utils.commonSteps import check_userType
from Utils.commonSteps import send_sms
from Utils.Data_Object.login_data import DataForLogin
import Utils.Data_Object.login_data
import Utils.Data_Object.signup_data
import Utils.api_endpoints
import allure
from Utils import data_generator
from Utils.commonSteps import send_and_verify
from Utils.commonSteps import register_account
from Utils.Data_Object.signup_data import Sign_Up_Data

class AuthController(unittest.TestCase):





    @allure.suite("Registration Functionality")
    @allure.title("Register individual user")
    @allure.description("Register individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_123_register_ind_user(self):
        phoneNumber = data_generator.generate_random_mobile_number()
        sms_payload = copy.copy(DataForLogin.payload_send_sms)
        sms_payload["phone"] = phoneNumber
        sms_payload["smsType"] = "REGISTRATION"
        verif_payload = copy.copy(DataForLogin.payload_verify_sms)
        verif_payload["phone"] = phoneNumber
        user_sms_id = send_and_verify(sms_payload, verif_payload)
        reg_payload = copy.copy(Sign_Up_Data.payload_registration)
        reg_payload["mobileNumber"] = "996" + phoneNumber
        reg_payload["userSMSId"] = user_sms_id
        reg_payload["userType"] = "BUSINESS"
        reg_payload.pop("birthDate", None)
        reg_payload["personalNumber"] = data_generator.generate_identification_number()
        reg_ind = register_account(reg_payload)
        print(sms_payload, verif_payload)
        print(reg_payload)
        print(reg_ind.text)
        # return reg_ind

    @allure.suite("Registration Functionality")
    @allure.title("Register individual user")
    @allure.description("Register individual user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_register_bus_user(self):

        user_sms_id = Utils.commonSteps.send_and_verify(Utils.Data_Generator.generate_random_mobile_number(),
                                                        Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
        reg_ind = Utils.commonSteps.register_account(deviceToken="string",
                                                     iban="GE13BG7252322426883581",
                                                     mobileOS="ANDROID",
                                                     name=Utils.Data_Generator.generate_fake_name(),
                                                     personalNumber=Utils.Data_Generator.generate_identification_number(),
                                                     userSMSId=user_sms_id,
                                                     userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
        print(reg_ind)
        return reg_ind


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
        phone_number = Utils.Data_Generator.generate_random_mobile_number()
        res = Utils.commonSteps.check_user(phone_number)
        check_res = res.json()
        if not check_res["businessExists"] and not check_res["individualExists"]:
            user_sms_id = Utils.commonSteps.send_and_verify(phone_number,
                                                            Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
            reg_res = Utils.commonSteps.register_account(birthDate=Utils.Data_Generator.generate_fake_birthDate(),
                                                         deviceToken="string",
                                                         iban="GE13BG7252322426883582",
                                                         mobileOS="ANDROID",
                                                         name=Utils.Data_Generator.generate_fake_name(),
                                                         personalNumber=Utils.Data_Generator.generate_personal_id(),
                                                         userSMSId=user_sms_id,
                                                         userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_individual)
            print(reg_res.json())
            return reg_res
        else:
            print("impossible to register such account")




    def test_11_register_bus_if_check_is_false_for_both(self):
        phone_number = Utils.Data_Generator.generate_random_mobile_number()
        res = Utils.commonSteps.check_user(phone_number)
        check_res = res.json()
        if not check_res["businessExists"] and not check_res["individualExists"]:
            user_sms_id = Utils.commonSteps.send_and_verify(phone_number,
                                                            Utils.Data_Object.login_data.DataForLogin.registration_send_sms)
            reg_res = Utils.commonSteps.register_account(
                                                         deviceToken="string",
                                                         iban="GE13BG7252322426883582",
                                                         mobileOS="ANDROID",
                                                         name=Utils.Data_Generator.generate_fake_name(),
                                                         personalNumber=Utils.Data_Generator.generate_identification_number(),
                                                         userSMSId=user_sms_id,
                                                         userType=Utils.Data_Object.signup_data.Sign_Up_Data.sms_type_business)
            print(reg_res.json())
            return reg_res
        else:
            print("impossible to register such account")
