# Base URL
base_url = "https://appdev.keepz.me:8888/common-service"

"""End Points Auth controller"""

check_user = base_url + "/api/v1/auth/check"

send_sms = base_url + "/api/v1/auth/send-sms"

verify_sms = base_url + "/api/v1/auth/verify-sms"

login = base_url + "/api/v1/auth/login"

registration = base_url + "/api/v1/auth/registration"

# TODO "upgradeOrDowngrade" end point needs to be added once everything will be clear


"""End Points Profile controller """

# Get Endpoints

profile = base_url + "/api/v1/profile"

profile_details = base_url + "/api/v1/profile/details"

tiny_url = base_url + "/api/v1/profile/tiny-url"

# Post Endpoints

complete_or_update_user = base_url + "api/v1/profile/admin"

empty_user = base_url + "/api/v1/profile/bulk/create"

profile_image = base_url + "/api/v1/profile/image"

profile_logout = base_url + "/api/v1/profile/logout"

logout_all = base_url + "/api/v1/profile/logout-all"


def logout_from_session(session_id):
    return base_url + f"/api/v1/profile/logout/{session_id}"


# Put Endpoints

put_profile_details = base_url + "api/v1/profile/details"

profile_phone = base_url + "/api/v1/profile/phone"


# Delete Endpoints

delete_profile_soft_delete = base_url + "/api/v1/profile/soft-delete"


def delete_profile_by_id(user_id):
    return base_url + f"/api/v1/profile/soft-delete/{user_id}"


""""End Points Merchant Controller ------------------------------------------------------------------------------------"""


add_merchant = base_url + "/api/v1/merchant"


def update_merchant(merchantId):
    return base_url + f"/api/v1/merchant/{merchantId}"


def delete_merchant(merchantId):
    return base_url + f"/api/v1/merchant/{merchantId}"


def activate_merchant(merchantId):
    return base_url + f"/api/v1/merchant/activate/{merchantId}"


def deactivate_merchant(merchantId):
    return base_url + f"/api/v1/merchant/deactivate/{merchantId}"


""" End points Branch Controller ------------------------------------------------------------------------------------ """


add_branch = base_url + "/api/v1/branch"


def update_branch(branchId):
    return base_url + f"/api/v1/branch/{branchId}"


def delete_branch(branchId):
    return base_url + f"/api/v1/branch/{branchId}"


def activate_branch(branchId):
    return base_url + f"/api/v1/branch/activate/{branchId}"


create_empty_branch = base_url + "/api/v1/branch/bulk"


def deactivate_branch(branchId):
    return base_url + f"/api/v1/branch/deactivate/{branchId}"



def set_master_branch(branchId):
    return base_url + f"/api/v1/branch/setMaster/{branchId}"

