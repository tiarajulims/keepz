
headers = {
    'Accept': '*/*',
    'Content-Type': '*/*'
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

payload_registration = {
  "birthDate": "2020-11-27",
  "deviceToken": "string",
  "iban": "GE16TB1544777371444667",
  "mobileName": "string",
  "mobileOS": "ANDROID",
  "name": "Jijelava",
  "personalNumber": "62014008420",
  "userSMSId": "40f84c1a-1de0-4a33-9b16-d634cf760a03",
  "userType": "INDIVIDUAL"
}


individual = "LOGIN_AS_INDIVIDUAL"
business = "LOGIN_AS_BUSINESS"
registration = "REGISTRATION"
