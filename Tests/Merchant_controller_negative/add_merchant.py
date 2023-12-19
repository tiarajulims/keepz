import copy
from Utils.Data_Object import merchant_data
from Utils import merchant_common_steps
from Utils.merchant_common_steps import test_create_empty_branch
from Utils.merchant_common_steps import create_merchant
from Utils.Data_Object.merchant_data import Merchant_data
import Utils.data_generator
import allure
import sys
import os
import unittest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


class Add_merchant_negative(unittest.TestCase):

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch address")
    @allure.description("trying to create a merchant and branch without entering an address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_add_merchant_empty_address(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["address"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[address-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None  branch address")
    @allure.description("trying to create a merchant and branch with none entering an address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_add_merchant_None_address(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["address"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[address-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch contactPhone")
    @allure.description("trying to create a merchant and branch without entering branch contactPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_add_merchant_empty_contactPhone(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["contactPhone"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], ["[Invalid format of mobileNumber, mobileNumber-Is required]",
                                             "[mobileNumber-Is required, Invalid format of mobileNumber]"])

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None branch contactPhone")
    @allure.description("trying to create a merchant and branch with None branch contactPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_add_merchant_None_contactPhone(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["contactPhone"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[mobileNumber-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with string branch contactPhone")
    @allure.description("trying to create a merchant and branch with string branch contactPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_add_merchant_string_contactPhone(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["contactPhone"] = "string"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[Invalid format of mobileNumber]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with short branch contactPhone")
    @allure.description("trying to create a merchant and branch with short branch contactPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_06_add_merchant_short_contactPhone(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["contactPhone"] = "123"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[Invalid format of mobileNumber]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with long branch contactPhone")
    @allure.description("trying to create a merchant and branch with long branch contactPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_add_merchant_long_contactPhone(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["contactPhone"] = "12345678912345678"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[Invalid format of mobileNumber]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch iban")
    @allure.description("trying to create a merchant and branch with empty branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_08_add_merchant_empty_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with none branch iban")
    @allure.description("trying to create a merchant and branch with none branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_09_add_merchant_none_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with short branch iban")
    @allure.description("trying to create a merchant and branch with short branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_10_add_merchant_short_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = "GE12TB223"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with long branch iban")
    @allure.description("trying to create a merchant and branch with long branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_11_add_merchant_long_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = "GE12TB22312312312312153534534645568568879786785"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with string branch iban")
    @allure.description("trying to create a merchant and branch with string branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_12_add_merchant_string_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = "string"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with non Georgian branch iban")
    @allure.description("trying to create a merchant and branch with non Georgian branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_add_merchant_non_geo_iban(self):
        # TODO after goLive the iban will not be mandatory
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["iban"] = "IT26K0300203280772241396784"
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch isMaster")
    @allure.description("trying to create a merchant and branch with empty branch isMaster")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_14_add_merchant_empty_isMaster(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["isMaster"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 500)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with non Georgian branch iban")
    @allure.description("trying to create a merchant and branch with non Georgian branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_15_add_merchant_none_isMaster(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["isMaster"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 500)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with non Georgian branch iban")
    @allure.description("trying to create a merchant and branch with non Georgian branch iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_16_add_merchant_non_geo_iban(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["isMaster"] = False
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 403)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], '403 FORBIDDEN "Please choose master branch!"')


    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty merchantId")
    @allure.description("trying to create a merchant and branch with empty merchantId")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_17_add_merchant_empty_merchantId(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["merchantId"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None merchantId")
    @allure.description("trying to create a merchant and branch with None merchantId")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_18_add_merchant_None_merchantId(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["merchantId"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch name")
    @allure.description("trying to create a merchant and branch with empty name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_19_add_merchant_empty_name(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["name"] = ""
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[name-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty branch name")
    @allure.description("trying to create a merchant and branch with empty name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_20_add_merchant_None_name(self):
        qr_code = test_create_empty_branch()
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["name"] = None
        payload["branches"][0]["qrCodeBranch"] = qr_code

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[name-Is required]")


    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty qrCodeBranch ")
    @allure.description("trying to create a merchant and branch with empty qrCodeBranch")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_21_add_merchant_empty_qrCodeBranch(self):
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["qrCodeBranch"] = ""

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with wrong qrCodeBranch ")
    @allure.description("trying to create a merchant and branch with wrong qrCodeBranch")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_22_add_merchant_wrong_qrCodeBranch(self):
        payload = copy.deepcopy(Merchant_data.payload)
        payload["branches"][0]["qrCodeBranch"] = 123

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 403)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "403 FORBIDDEN \"Branch with qr code 123is already completed!\"")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty document")
    @allure.description("trying to create a merchant and branch with empty document")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_add_merchant_empty_document(self):  # POS
        payload = copy.deepcopy(Merchant_data.payload)
        payload["document"] = ""

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None document")
    @allure.description("trying to create a merchant and branch with None document")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_add_merchant_empty_document(self):  # POS
        payload = copy.deepcopy(Merchant_data.payload)
        payload["document"] = None

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty email")
    @allure.description("trying to create a merchant and branch with empty email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_add_merchant_empty_email(self):  # POS
        payload = copy.deepcopy(Merchant_data.payload)
        payload["email"] = ""

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None email")
    @allure.description("trying to create a merchant and branch with None email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_13_add_merchant_None_email(self):  # POS
        payload = copy.deepcopy(Merchant_data.payload)
        payload["email"] = None

        response = create_merchant(payload)
        print(response.text)
        self.assertEquals(response.status_code, 201)

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty merchant iban")
    @allure.description("trying to create a merchant and branch with empty merchant iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_empty_iban(self):  # POS
        payload = copy.copy(Merchant_data.payload)
        payload["iban"] = ""

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], ["[iban-Invalid Format, iban-Is required]",
                                             "[iban-Is required, iban-Invalid Format]"])

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with None merchant iban")
    @allure.description("trying to create a merchant and branch with None merchant iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_empty_iban(self):  # POS
        payload = copy.copy(Merchant_data.payload)
        payload["iban"] = None

        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with short merchant iban")
    @allure.description("trying to create a merchant and branch with short merchant iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_short_iban(self):
        payload = copy.copy(Merchant_data.payload)
        payload["iban"] = "GE23TB123"
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Invalid Format]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with long merchant iban")
    @allure.description("trying to create a merchant and branch with long merchant iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_long_iban(self):
        payload = copy.copy(Merchant_data.payload)
        payload["iban"] = "GE23TB12312312312312312313131231"
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Invalid Format]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with Non Geo merchant iban")
    @allure.description("trying to create a merchant and branch with Non Geo merchant iban")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_non_Geo_iban(self):
        payload = copy.copy(Merchant_data.payload)
        payload["iban"] = "IT18M0300203280147975291319"
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[iban-Invalid Format]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty merchant mobile number")
    @allure.description("trying to create a merchant and branch with empty merchant mobile number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_empty_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["mobileNumber"] = ""
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], ["[mobileNumber-Is required, Invalid format of mobileNumber]",
                                             "[Invalid format of mobileNumber, mobileNumber-Is required]"])

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with none merchant mobile number")
    @allure.description("trying to create a merchant and branch with none merchant mobile number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_None_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["mobileNumber"] = None
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[mobileNumber-Is required]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with short merchant mobile number")
    @allure.description("trying to create a merchant and branch with short merchant mobile number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_short_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["mobileNumber"] = 599123
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[Invalid format of mobileNumber]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with long merchant mobile number")
    @allure.description("trying to create a merchant and branch with long merchant mobile number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_long_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["mobileNumber"] = 2341241241234123412341234123412341234123
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "[Invalid format of mobileNumber]")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with registered merchant mobile number")
    @allure.description("trying to create a merchant and branch with registered merchant mobile number")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_registered_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["mobileNumber"] = 667790233
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 409)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"], "409 CONFLICT \"Individual or Business user already exists for mobile number: 995667790233\"")

    @allure.suite("Create Merchant Functionality")
    @allure.title("create merchant with empty merchant name")
    @allure.description("trying to create a merchant and branch with empty merchant name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_24_add_merchant_registered_mobileNumber(self):
        payload = copy.copy(Merchant_data.payload)
        payload["name"] = ""
        response = create_merchant(payload)
        json_resp = response.json()
        print(response.text)
        self.assertEquals(response.status_code, 400)
        self.assertIn("message", json_resp)
        self.assertIn(json_resp["message"],
                      "409 CONFLICT \"Individual or Business user already exists for mobile number: 995667790233\"")
