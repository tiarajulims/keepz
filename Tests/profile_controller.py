import json
import random
import unittest

import allure

import Utils.Profile_Common_Steps as profileSteps
from Utils.register_user import register_business
from Utils.register_user import register_individual


class ProfileController(unittest.TestCase):
    ind_token = register_individual()
    biz_token = register_business()

    # Tests on INDIVIDUAL user
    @allure.suite("Profile controller positive tests")
    @allure.title("Get INDIVIDUAL Profile")
    @allure.description("Get Logged in INDIVIDUAL profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_get_profile(self):
        response = profileSteps.get_logged_profile(self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("INDIVIDUAL Profile details")
    @allure.description("Get Logged in INDIVIDUAL profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_logged_in_profile_details(self):
        response = profileSteps.get_profile_details(self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("INDIVIDUAL's Tiny URL")
    @allure.description("Get INDIVIDUAL's Tiny URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_get_tiny_url(self):
        response = profileSteps.get_tiny_url(self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("INDIVIDUAL's Profile Picture")
    @allure.description("Add profile picture for INDIVIDUAL user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_post_profile_image(self):
        response = profileSteps.post_profile_image(
            "../../keepz/resources/Images/w11.jpeg",
            self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Post empty users")
    @allure.description("Post empty users")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_post_empty_users(self):
        response = profileSteps.post_empty_users(random.randint(1, 12), self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Update INDIVIDUAL's Profile details")
    @allure.description("Update INDIVIDUAL's Profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_put_profile_details(self):
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252322333283581", "TestUser4",
                                                    "02004411203", "INDIVIDUAL", self.ind_token)

        response_json = json.loads(response.text)

        expected_data = {
            "birthdate": "1993-12-18",
            "iban": "GE13BG7252322333283581",
            "name": "TestUser4",
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
    @allure.title("logout INDIVIDUAL profile")
    @allure.description("logout INDIVIDUAL profile from session using session id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_session_logout(self):
        token = register_individual()
        session = register_individual(user_param="session state")

        response = profileSteps.post_logout_from_session(session, token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Delete INDIVIDUAL's profile")
    @allure.description("Delete INDIVIDUAL's profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_soft_delete(self):
        response = profileSteps.soft_delete(self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Delete INDIVIDUAL's profile by id")
    @allure.description("Delete INDIVIDUAL's profile using id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_delete_by_id(self):
        access_token = register_individual()

        user_id = json.loads(profileSteps.get_profile_details(access_token).text).get("userId")

        response = profileSteps.soft_delete_by_id(user_id, access_token)

        self.assertEqual(200, response.status_code)

    # Tests on BUSINESS user
    @allure.suite("Profile controller positive tests")
    @allure.title("Get BUSINESS Profile")
    @allure.description("Get Logged in BUSINESS profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_get_profile(self):
        response = profileSteps.get_logged_profile(self.biz_token())

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("BUSINESS Profile details")
    @allure.description("Get Logged in BUSINESS profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_get_logged_in_profile_details(self):
        response = profileSteps.get_profile_details(self.biz_token())

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("BUSINESS Tiny URL")
    @allure.description("Get BUSINESS Tiny URL")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_get_tiny_url(self):
        response = profileSteps.get_tiny_url(self.biz_token())

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("BUSINESS Profile Picture")
    @allure.description("Add BUSINESS profile picture")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_post_profile_image(self):
        response = profileSteps.post_profile_image(
            "../../keepz/resources/Images/w11.jpeg",
            self.ind_token)

        self.assertEqual(200, response.status_code)

    @allure.suite("Profile controller positive tests")
    @allure.title("Update BUSINESS Profile details")
    @allure.description("Update BUSINESS profile details")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_put_profile_details(self):
        response = profileSteps.add_profile_details("", "GE13BG7252322333283581", "TestUser4",
                                                    "020044112", "BUSINESS", self.ind_token)

        response_json = json.loads(response.text)

        expected_data = {
            "birthdate": None,
            "iban": "GE13BG7252322333283581",
            "name": "TestUser4",
            "personalNumber": "020044112",
            "userType": "BUSINESS"
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
    @allure.title("Delete BUSINESS profile")
    @allure.description("Delete BUSINESS profile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_soft_delete(self):
        response = profileSteps.soft_delete(self.biz_token())

        self.assertEqual(200, response.status_code)
