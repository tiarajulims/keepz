from Utils.data_generator import *


class Merchant_data:

    def header(self, access_token) -> dict:
        return {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

    payload = {
        "branches": [
            {
                "address": generate_fake_address(),
                "completedBy": 0,
                "contactPhone": generate_random_mobile_number(),
                "iban": iban_generator(),
                "image_path": "string",
                "isMaster": "true",
                "merchantId": "",
                "name": fake_company(),
                "qrCodeBranch": ""
            }
        ],
        "completedBy": 0,
        "document": "",
        "email": test_get_fake_email(),
        "iban": iban_generator(),  # M
        "image_path": "string",
        "merchantGroupId": random_merchantGroup(),
        "merchant_charging_fee": 0,
        "mobileNumber": generate_random_mobile_number(),  # M
        "name": fake_company(),  # M
        "personalNumber": generate_identification_number(),
        "verified": "true"
    }
