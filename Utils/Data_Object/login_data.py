class DataForLogin:


    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    payload_send_sms = {
        "countryCode": "996",
        "otphash": "string",
        "phone": "599989981",
        "smsType": "LOGIN_AS_INDIVIDUAL"
    }

    payload_verify_sms = {
        "code": "123456",
        "countryCode": "996",
        "phone": "599989981"
    }

    payload_login = {
        "deviceToken": "string",
        "mobileName": "string",
        "mobileOS": "ANDROID",
        "userSMSId": "",  # Placeholder, will be updated later
        "userType": "INDIVIDUAL"
    }





    individual_send_sms = "LOGIN"
    business_sens_sms = "LOGIN"
    registration_send_sms = "REGISTRATION"

    sms_type_individual = "INDIVIDUAL"
    sms_type_business = "BUSINESS"
