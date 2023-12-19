import os
import sys

import allure
import requests

from Utils.api_endpoints import ApiEndpoints

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


# Get Methods
@allure.step
def get_logged_profile(access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }
    response = requests.get(url=ApiEndpoints.profile, headers=header)
    return response


@allure.step
def get_profile_details(access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }
    response = requests.get(url=ApiEndpoints.profile_details, headers=header)
    return response


@allure.step
def get_tiny_url(access_token: str):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }
    response = requests.get(url=ApiEndpoints.base_url, headers=header)
    return response


# Post Methods
@allure.step
def post_profile_update(birth_date: str, completed_by: int, document: str, email: str, iban: str, profile_id: str,
                        mobile_number: str, name: str, official_name: str, personal_number: str, user_group_id: int,
                        user_type: str, verified: bool, access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
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

    response = requests.post(url=ApiEndpoints.complete_or_update_user, json=body, headers=header)
    return response


@allure.step
def post_empty_users(number_of_users: int, access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }

    body = {
        "numberOfUsers": number_of_users
    }

    response = requests.post(url=ApiEndpoints.empty_user, json=body, headers=header)
    return response


@allure.step
def post_profile_image(image_path, access_token):
    script_directory = os.path.dirname(os.path.realpath(__file__))

    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }

    image_path_absolute = os.path.abspath(os.path.join(script_directory, image_path))

    files = {'file': ('image.jpg', open(image_path_absolute, 'rb'), 'image/jpeg')}

    response = requests.post(url=ApiEndpoints.profile_image, headers=header, files=files)
    return response


@allure.step
def post_profile_logout(access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Authorization': 'Bearer ' + str(access_token)
        }
    response = requests.post(url=ApiEndpoints.profile_logout, headers=header)
    return response


@allure.step
def post_logout_all(access_token):
    if len(access_token) < 10:
        header = {
            'accept': '*/*',
        }
    else:
        header = {
            'accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(access_token)
        }
    response = requests.post(url=ApiEndpoints.logout_all, headers=header)
    return response


@allure.step
def post_logout_from_session(session_id: str, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }
    response = requests.post(url=ApiEndpoints.logout_from_session(session_id), headers=header)
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

    response = requests.put(url=ApiEndpoints.put_profile_details, json=body, headers=header)
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

    response = requests.put(url=ApiEndpoints.profile_phone, json=body, headers=header)
    return response


# Delete Methods
@allure.step
def soft_delete(access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.delete(url=ApiEndpoints.delete_profile_soft_delete, headers=header)
    return response


@allure.step
def soft_delete_by_id(user_id: str, access_token):
    header = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
    }

    response = requests.delete(url=ApiEndpoints.delete_profile_by_id(user_id), headers=header)
    return response
