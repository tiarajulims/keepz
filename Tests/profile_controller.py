import json
import unittest

import Utils.Data_Object.login_data
import Utils.Data_Object.signup_data
import Utils.Profile_Common_Steps
import Utils.api_endpoints
import Utils.commonSteps
import allure


class ProfileController(unittest.TestCase):
    user_sms_id = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                    "REGISTRATION")
    registration = Utils.commonSteps.register_account(birthDate="2020-11-27",
                                                      deviceToken="string",
                                                      iban="GE13BG7252322433283581",
                                                      mobileOS="ANDROID",
                                                      name="TestUser",
                                                      personalNumber="01002030200",
                                                      userSMSId=user_sms_id,
                                                      userType="INDIVIDUAL")

    access_token = json.loads(registration.text).get("access_token")

    @allure.suite("Profile functionality")
    @allure.title("Get Profile")
    @allure.description("Get Logged in profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_get_profile(self):
        response = Utils.Profile_Common_Steps.get_logged_profile(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Profile details")
    @allure.description("Get Logged in profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_logged_in_profile_details(self):
        response = Utils.Profile_Common_Steps.get_profile_details(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Tiny URL")
    @allure.description("Get Tiny URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_get_tiny_url(self):
        response = Utils.Profile_Common_Steps.get_tiny_url(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Profile Picture")
    @allure.description("Add profile picture")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_post_profile_image(self):
        response = Utils.Profile_Common_Steps.post_profile_image(
            "../resources/Images/w11.jpeg",
            self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Profile Picture")
    @allure.description("Add profile picture")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_post_empty_users(self):
        response = Utils.Profile_Common_Steps.post_empty_users(7, self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Profile details")
    @allure.description("Add profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_put_profile_details(self):
        response = Utils.Profile_Common_Steps.add_profile_details("1993-12-18", "GE13BG7252322333283581", "TestUser2",
                                                                  "02004411203", "INDIVIDUAL", self.access_token)

        response_json = json.loads(response.text)

        expected_data = {
            "birthdate": "1993-12-18",
            "iban": "GE13BG7252322333283581",
            "name": "TestUser2",
            "personalNumber": "02004411203",
            "userType": "INDIVIDUAL"
        }

        response_json_dict = {
            "birthdate": response_json.get("birthdate"),
            "iban": response_json.get("iban"),
            "name": response_json.get("name"),
            "personalNumber": response_json.get("personalNumber"),
            "userType": response_json.get("userType")
        }

        self.assertDictEqual(expected_data, response_json_dict)

    @allure.suite("Profile functionality")
    @allure.title("Delete profile")
    @allure.description("Delete profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_soft_delete(self):
        response = Utils.Profile_Common_Steps.soft_delete(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile functionality")
    @allure.title("Delete profile by id")
    @allure.description("Delete profile using users id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_delete_by_id(self):
        user_sms_id = Utils.commonSteps.send_and_verify(Utils.Data_Object.signup_data.generate_random_mobile_number(),
                                                        "REGISTRATION")
        registration = Utils.commonSteps.register_account(birthDate="2022-11-27",
                                                          deviceToken="string",
                                                          iban="GE13BG7262322433283581",
                                                          mobileOS="ANDROID",
                                                          name="Chxeto",
                                                          personalNumber="01002030200",
                                                          userSMSId=user_sms_id,
                                                          userType="INDIVIDUAL")

        access_token = json.loads(registration.text).get("access_token")

        user_id = json.loads(Utils.Profile_Common_Steps.get_profile_details(access_token).text).get("userId")

        response = Utils.Profile_Common_Steps.soft_delete_by_id(user_id, access_token)

        self.assertEqual(200, response.status_code)
