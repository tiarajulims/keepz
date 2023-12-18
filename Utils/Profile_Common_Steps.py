import os
import sys

import allure
import requests

import Utils.api_endpoints

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


# Get Methods
@allure.step
def get_logged_profile(access_token):
    header = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.get(url=Utils.api_endpoints.profile, headers=header)
    return response


@allure.step
def get_profile_details(access_token):
    header = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.get(url=Utils.api_endpoints.profile_details, headers=header)
    return response


@allure.step
def get_tiny_url(access_token: str):
    header = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.get(url=Utils.api_endpoints.tiny_url, headers=header)
    return response


# Post Methods
@allure.step
def post_profile_update(birth_date: str, completed_by: int, document: str, email: str, iban: str, profile_id: str,
                        mobile_number: str, name: str, official_name: str, personal_number: str, user_group_id: int,
                        user_type: str, verified: bool, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    body = {
        "birthDate": birth_date,
        "completedBy": completed_by,
        "document": document,
        "email": email,
        "iban": iban,
        "id": profile_id,
        "mobileNumber": mobile_number,
        "name": name,
        "official_name": official_name,
        "personalNumber": personal_number,
        "userGroupId": user_group_id,
        "userType": user_type,
        "verified": verified
    }

    response = requests.post(url=Utils.api_endpoints.complete_or_update_user, json=body, headers=header)
    return response


@allure.step
def post_empty_users(number_of_users: int, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    body = {
        "numberOfUsers": number_of_users
    }

    response = requests.post(url=Utils.api_endpoints.empty_user, json=body, headers=header)
    return response


@allure.step
def post_profile_image(image_path, access_token):
    header = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(access_token)
    }
    files = {'file': ('image.jpg', open(image_path, 'rb'), 'image/jpeg')}

    response = requests.post(url=Utils.api_endpoints.profile_image, headers=header, files=files)
    return response


@allure.step
def post_profile_logout(access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.post(url=Utils.api_endpoints.profile_logout, headers=header)
    return response


@allure.step
def post_logout_all(access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.post(url=Utils.api_endpoints.logout_all, headers=header)
    return response


@allure.step
def post_logout_from_session(session_id: str, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.post(url=Utils.api_endpoints.logout_from_session(session_id), headers=header)
    return response


# Put Methods
@allure.step
def add_profile_details(birth_date: str, iban: str, name: str, personal_num: str, user_type: str, access_token):
    body = {
        "birthDate": birth_date,
        "iban": iban,
        "name": name,
        "personalNumber": personal_num,
        "userType": user_type
    }
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.put(url=Utils.api_endpoints.put_profile_details, json=body, headers=header)
    return response


@allure.step
def profile_phone(user_sms_id: str, access_token):
    body = {
        "userSMSId": user_sms_id
    }
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.put(url=Utils.api_endpoints.profile_phone, json=body, headers=header)
    return response


# Delete Methods
@allure.step
def soft_delete(access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.delete(url=Utils.api_endpoints.delete_profile_soft_delete, headers=header)
    return response


@allure.step
def soft_delete_by_id(user_id: str, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.delete(url=Utils.api_endpoints.delete_profile_by_id(user_id), headers=header)
    return response
