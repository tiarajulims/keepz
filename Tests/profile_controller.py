import json
import unittest

import allure

import Utils.Profile_Common_Steps as profileSteps
import Utils.commonSteps as commonSteps
from Utils.Data_Object.signup_data import generate_random_mobile_number


class ProfileController(unittest.TestCase):
    user_sms_id = commonSteps.send_and_verify(generate_random_mobile_number(),
                                              "REGISTRATION")
    registration = commonSteps.register_account(birthDate="2020-11-27",
                                                deviceToken="string",
                                                iban="GE13BG7252322433283581",
                                                mobileOS="ANDROID",
                                                name="TestUser",
                                                personalNumber="01002030200",
                                                userSMSId=user_sms_id,
                                                userType="INDIVIDUAL")

    access_token = json.loads(registration.text).get("access_token")

    @allure.suite("Profile controller positive tests")
    @allure.title("Get Profile")
    @allure.description("Get Logged in profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_get_profile(self):
        response = profileSteps.get_logged_profile(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Profile details")
    @allure.description("Get Logged in profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_logged_in_profile_details(self):
        response = profileSteps.get_profile_details(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Tiny URL")
    @allure.description("Get Tiny URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_get_tiny_url(self):
        response = profileSteps.get_tiny_url(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Profile Picture")
    @allure.description("Add profile picture")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_post_profile_image(self):
        response = profileSteps.post_profile_image(
            "../../keepz/resources/Images/w11.jpeg",
            self.access_token)

        # script_directory = os.path.dirname(os.path.realpath(__file__))
        #
        # image_path_relative = os.path.join('resources', 'Images', 'w11.jpeg')
        #
        # image_path_absolute = os.path.join(script_directory, image_path_relative)
        #
        # print(image_path_absolute)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Profile Picture")
    @allure.description("Add profile picture")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_post_empty_users(self):
        response = profileSteps.post_empty_users(7, self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Profile details")
    @allure.description("Add profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_put_profile_details(self):
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252322333283581", "TestUser2",
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

    @allure.suite("Profile controller positive tests")
    @allure.title("Delete profile")
    @allure.description("Delete profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_soft_delete(self):
        response = profileSteps.soft_delete(self.access_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Delete profile by id")
    @allure.description("Delete profile using users id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_delete_by_id(self):
        user_sms_id = commonSteps.send_and_verify(generate_random_mobile_number(),
                                                  "REGISTRATION")
        registration = commonSteps.register_account(birthDate="2022-11-27",
                                                    deviceToken="string",
                                                    iban="GE13BG7262322433283581",
                                                    mobileOS="ANDROID",
                                                    name="UserTest",
                                                    personalNumber="01002030200",
                                                    userSMSId=user_sms_id,
                                                    userType="INDIVIDUAL")

        access_token = json.loads(registration.text).get("access_token")

        user_id = json.loads(profileSteps.get_profile_details(access_token).text).get("userId")

        response = profileSteps.soft_delete_by_id(user_id, access_token)

        self.assertEqual(200, response.status_code)
