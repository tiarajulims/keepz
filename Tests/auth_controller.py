import json

import pytest
import requests
# TODO
import unittest
from Utils import get_token

check_mobile = "https://appdev.keepz.me:8888/common-service/api/v1/auth/check"
class AuthController(unittest.TestCase):

    # @pytest.mark.xfail
    def test_01_check(self):
        payload = {
            'phone': '995551554599'
        }

        headers = {
            'content-type': 'application/json',
            # 'Authorization': get_token.get_auth_token(),
            'Accept': '*/*'
        }

        res = requests.post(url=check_mobile, data=json.dumps(payload), headers=headers)

        self.assertEquals(res.status_code, 200)

    def test_02_countries_code(self):
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJDQ2xaTFhra1NHaEMxWkp2bkl0ZXNRdnFUUC0wbjVfQ0VLOTFBbUNndkZZIn0.eyJleHAiOjE2OTk5NzE1MTgsImlhdCI6MTY5OTk2NzkxOCwianRpIjoiMmZmMzUyZDMtNzVhOS00MzdjLWIxOGMtMDU5ODRkZDBlMGU5IiwiaXNzIjoiaHR0cHM6Ly9hcHBkZXYua2VlcHoubWU6ODA4MC9hdXRoL3JlYWxtcy9zd2VlZnQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZmM4ZGMyMmQtZmVmNS00MzdiLTllMmUtNWEyNzA2YWJjODRjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoic3dlZWZ0LWFwaS1nYXRld2F5Iiwic2Vzc2lvbl9zdGF0ZSI6IjZiNTU1ZjM4LTVlMzktNDVlOC1iMjNkLTM2MjM3NWZiZDU5OSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1zd2VlZnQiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGluZGl2aWR1YWxfdXNlciBlbWFpbCB0ZXN0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJkYXRhYmFzZV9pZCI6IntcInVzZXJJZFwiOlwiN2Q3ZWIzYmUtMmNlYi00OGJmLTlmMDUtMTZmYjhkNDcwZWM3XCJ9IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiOTk1NTk5OTg5OTgxIn0.Igd1CIruooAjI5tk7auVpMQ1hoKouaDKx_neJKhjdUO6oWN9yYrDsbV5Qap1pTktx8naf9vs9wMUCpFIgd6y4EfwDHlh3MkwvTZpKcP8-3EBZlVZfxESMshZVxlbT4zByYsHT1ubWirQFsyLATeRzr7kw5Dc-aQtJzyusya6HUwVy8I-RV4wuIyhvlt1OeS0RUBMf0TQS4XOiK8nlJqjj94oZKYODV-ei3JQCWLR5FGvjBkLKv-GITSKDuRFC7Bko9vCS3SWZqZ_9zP0Y6okoJEXpDQeQeYIHaF5R7Q8DykJ3r4xAA_aYgPn39Qvdm73VgwU9VWd5dRLw4jnBTr6jg',
            'Accept': 'application/json'
        }
        res = requests.get(url="https://appdev.keepz.me:8888/common-service/api/v1/profile", headers=headers)

        # print(res.status_code, res.text)
        res = res.text
        print(res)
        # self.assertEquals(res["name"], "იური")
