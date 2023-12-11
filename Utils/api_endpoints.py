import json

# Base URL
base_url = "https://appdev.keepz.me:8888/common-service"

# End Points Auth controller

check_user = base_url + "/api/v1/auth/check"

send_sms = base_url + "/api/v1/auth/send-sms"

verify_sms = base_url + "/api/v1/auth/verify-sms"

login = base_url + "/api/v1/auth/login"

registration = base_url + "/api/v1/auth/registration"

#TODO "upgradeOrDowngrade" end point needs to be added once everything will be clear


get_profile = base_url + "/api/v1/profile/details"

