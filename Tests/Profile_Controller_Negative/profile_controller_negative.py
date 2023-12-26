import json
import unittest

import allure

import Utils.Profile_Common_Steps as profileSteps
from Utils.register_user import register_business
from Utils.register_user import register_individual


class ProfileControllerNegative(unittest.TestCase):
    invalid_access_token = "NoToken"
    individual_token = register_individual()
    business_token = register_business()
    invalid_session_state = "InvalidSessionState"

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Profile")
    @allure.description("Get logged out/non-logged in profile by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_get_profile(self):
        response = profileSteps.get_logged_profile(self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Profile details")
    @allure.description("Get logged out/non-logged in profile details by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_profile_details(self):
        response = profileSteps.get_profile_details(self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Tiny URL")
    @allure.description("Get Tiny URL by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_get_tiny_url(self):
        response = profileSteps.get_tiny_url(self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Post user log out with invalid token")
    @allure.description("logging out user with invalid token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_get_log_out(self):
        response = profileSteps.post_profile_logout(self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Post log out all users with invalid token")
    @allure.description("logging out all user with invalid token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_05_get_log_out_all(self):
        response = profileSteps.post_logout_all(self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Post empty users with invalid token")
    @allure.description("posts empty users with invalid token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_post_empty_users(self):
        response = profileSteps.post_empty_users(1, self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Post log out all users with invalid token")
    @allure.description("logging out all user with invalid token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_log_out_from_session(self):
        response = profileSteps.post_logout_from_session(self.invalid_session_state, self.invalid_access_token)

        self.assertEqual(400, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put INDIVIDUAL user profile update : birth date")
    @allure.description("Passing incorrect birthdate format to put INDIVIDUAL user profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_update_INDV_profile_birth_date(self):
        response = profileSteps.add_profile_details("93-12-18", "GE13BG7252322333283581", "TestUser2",
                                                    "02004411203", "INDIVIDUAL", self.individual_token)

        message = json.loads(response.text)
        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Cannot deserialize value of type `java.time.LocalDate`", message["message"])

        profileSteps.soft_delete(self.individual_token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put INDIVIDUAL user profile update : future birth date")
    @allure.description("Passing future birthdate to post INDIVIDUAL user profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_update_INDV_profile_birth_date(self):
        response = profileSteps.add_profile_details("2093-12-18", "GE13BG7252322333283581", "TestUser2",
                                                    "02004411203", "INDIVIDUAL", self.individual_token)

        message = json.loads(response.text)
        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("birthDate-Must be past", message["message"])

        profileSteps.soft_delete(self.individual_token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put profile update : iban")
    @allure.description("Passing incorrect iban format to post profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_update_INDV_profile_iban(self):
        token = register_individual()
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252323383581", "TestUser2",
                                                    "02004411203", "INDIVIDUAL", token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("iban-Invalid Format", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put profile update : iban")
    @allure.description("Passing incorrect iban format to post profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_11_update_INDV_profile_name(self):
        token = register_individual()
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252323383581", "",
                                                    "02004411203", "INDIVIDUAL", token)

        message = json.loads(response.text)
        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("name-Is required", message["message"])

        profileSteps.soft_delete(self.individual_token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put INDIVIDUAL user profile update : Personal number")
    @allure.description("Passing invalid personal number to post INDIVIDUAL user profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_12_update_INDV_profile_personal_number(self):
        token = register_individual()
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252322333283581", "TestUser2",
                                                    "02011203", "INDIVIDUAL", token)

        message = json.loads(response.text)
        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Invalid format of personalNumber", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Put INDIVIDUAL user profile update : Personal number")
    @allure.description("Passing invalid personal number to post INDIVIDUAL user profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_13_update_INDV_profile_personal_number(self):
        token = register_individual()
        response = profileSteps.add_profile_details("1993-12-18", "GE13BG7252322333283581", "TestUser2",
                                                    "90013245678", "Reno", token)

        message = json.loads(response.text)
        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("UserType must be one of this: INDIVIDUAL, BUSINESS", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : birthdate")
    @allure.description("Passing incorrect birthdate format to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_14_complete_INDV_profile_birth_date(self):
        token = register_individual()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("93-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("JSON parse error: Cannot deserialize value of type `java.time.LocalDate`", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : birthdate")
    @allure.description("Passing future date of birth to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_15_complete_INDV_profile_birth_date(self):
        token = register_individual()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2093-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("birthDate-Must be past", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : name")
    @allure.description("Passing empty name to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_16_complete_INDV_profile_name(self):
        token = register_individual()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "", "Avto", "01002020300", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("name-Is required", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : iban")
    @allure.description("Passing invalid format of iban to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_17_complete_INDV_profile_iban(self):
        token = register_individual()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7253283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("iban-Invalid Format", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : mobile number")
    @allure.description("Passing invalid format of mobile number post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_18_complete_INDV_profile_mobile_num(self):
        token = register_individual()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187",
                                                    "", "Avto", "01002020300", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Invalid format of mobileNumber", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : personal number")
    @allure.description("Passing invalid personal number to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_19_complete_INDV_profile_personal_num(self):
        token = register_individual()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187123",
                                                    "Porsche", "Avto", "0100", 0,
                                                    "INDIVIDUAL", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Invalid format of personalNumber", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : user type")
    @allure.description("Passing invalid user type to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_20_complete_INDV_profile_type(self):
        token = register_individual()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187789",
                                                    "Porsche", "Avto", "01002010456", 0,
                                                    "Bob", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("UserType must be one of this: INDIVIDUAL, BUSINESS", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update INDIVIDUAL user - negative : access token")
    @allure.description("Passing incorrect token to post INDIVIDUAL user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_21_complete_INDV_profile_token(self):
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", "user_id", "588187789",
                                                    "Porsche", "Avto", "01002010456", 0,
                                                    "INDIVIDUAL", True, self.invalid_access_token)

        self.assertEqual(401, response.status_code)

    # @allure.suite("Profile controller negative tests")
    # @allure.title("Complete or update INDIVIDUAL user - negative : profile picture")
    # @allure.description("Passing incorrect picture  to post INDIVIDUAL user profile complete and update")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_18_complete_INDV_profile_picture(self):
    #     token = register_individual()
    #     response = profileSteps.post_profile_image("../../keepz/resources/Images/image.gif",token)
    #     self.assertEqual(405, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : birthdate")
    @allure.description("Passing birthdate to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_22_update_BIZ_profile_birth_date(self):
        token = register_business()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("93-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("JSON parse error: Cannot deserialize value of type `java.time.LocalDate`", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : birthdate")
    @allure.description("Passing future date of birth to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_23_update_BIZ_profile_birth_date(self):
        token = register_business()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2093-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("birthDate-Must be past", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : name")
    @allure.description("Passing empty name to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_24_update_BIZ_profile_name(self):
        token = register_business()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588123287",
                                                    "", "Avto", "01002020300", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("name-Is required", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : iban")
    @allure.description("Passing invalid format of iban to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_25_update_BIZ_profile_iban(self):
        token = register_business()
        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7253283581", user_id, "588123287",
                                                    "Geralt", "Avto", "01002020300", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("iban-Invalid Format", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : mobile number")
    @allure.description("Passing invalid format of mobile number post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_26_update_BIZ_profile_mobile_number(self):
        token = register_business()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187",
                                                    "", "Avto", "01002020300", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Invalid format of mobileNumber", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : personal number ")
    @allure.description("Passing invalid personal number to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_27_update_BIZ_profile_personal_num(self):
        token = register_business()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187",
                                                    "Porsche", "Avto", "0100", 0,
                                                    "BUSINESS", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("Invalid format of personalNumber", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : user type")
    @allure.description("Passing invalid user type to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_28_update_BIZ_profile_type(self):
        token = register_business()

        user_id = json.loads(profileSteps.get_profile_details(token).text).get("userId")
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", user_id, "588187789",
                                                    "Porsche", "Avto", "01002010456", 0,
                                                    "Bob", True, token)

        message = json.loads(response.text)

        self.assertEqual(400, response.status_code)
        self.assertIn("message", message)
        self.assertIn("UserType must be one of this: INDIVIDUAL, BUSINESS", message["message"])

        profileSteps.soft_delete(token)

    @allure.suite("Profile controller negative tests")
    @allure.title("Complete or update BUSINESS user - negative : access token")
    @allure.description("Passing incorrect token to post BUSINESS user profile complete and update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_29_update_BIZ_profile_token(self):
        response = profileSteps.post_profile_update("2013-12-18", 0, "string",
                                                    "test@gmail.com", "GE13BG7252322333283581", "user_id", "588187789",
                                                    "Porsche", "Avto", "01002010456", 0,
                                                    "BUSINESS", True, self.invalid_access_token)

        self.assertEqual(401, response.status_code)
