import Utils.data_generator


class Merchant_data:

    def header(access_token):
        return {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }


    branch_address = Utils.data_generator.generate_fake_address()
    branch_phone = Utils.data_generator.generate_random_mobile_number()
    branch_name = Utils.data_generator.fake_company() + " 1"
    branch_iban = Utils.data_generator.iban_generator()

    merchant_email = Utils.data_generator.test_get_fake_email()
    merchant_phone = Utils.data_generator.generate_random_mobile_number()
    merchant_name = Utils.data_generator.fake_company()
    merchant_identification = Utils.data_generator.generate_identification_number()
    merchant_groupId = Utils.data_generator.random_merchantGroup()
    merchant_iban = Utils.data_generator.iban_generator()

    payload = {
        "branches": [
            {
                "address": branch_address,
                "completedBy": 0,
                "contactPhone": branch_phone,
                "iban": branch_iban,
                "image_path": "string",
                "isMaster": "true",
                "merchantId": "",
                "name": branch_name,
                "qrCodeBranch": ""
            }
        ],
        "completedBy": 0,
        "document": "",
        "email": merchant_email ,
        "iban": merchant_iban, # M
        "image_path": "string",
        "merchantGroupId": merchant_groupId,
        "merchant_charging_fee": 0,
        "mobileNumber": merchant_phone, # M
        "name": merchant_name,   # M
        "personalNumber": merchant_identification,
        "verified": "true"
    }
