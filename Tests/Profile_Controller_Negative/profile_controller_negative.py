import unittest

import allure

import Utils.Profile_Common_Steps as profileSteps


class ProfileControllerNegative(unittest.TestCase):
    wrong_access_token = "NoToken"

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Profile")
    @allure.description("Get logged out/non-logged in profile by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_get_profile(self):
        response = profileSteps.get_logged_profile(self.wrong_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Profile details")
    @allure.description("Get logged out/non-logged in profile details by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_profile_details(self):
        response = profileSteps.get_profile_details(self.wrong_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Get Tiny URL")
    @allure.description("Get Tiny URL by passing wrong token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_profile_details(self):
        response = profileSteps.get_tiny_url(self.wrong_access_token)

        self.assertEqual(401, response.status_code)

    @allure.suite("Profile controller negative tests")
    @allure.title("Post profile update : birth date")
    @allure.description("passing incorrect birthdate format to post profile update")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_get_profile_details(self):

        response = profileSteps.add_profile_details("93-12-18", "GE13BG7252322333283581", "TestUser2",
                                                               "02004411203", "INDIVIDUAL", )
        pass
