import random
import requests
from faker import Faker
import io
from PIL import Image

fake = Faker()


def generate_random_number() -> str:
    return ''.join(random.choices('1234567890', k=6))


def generate_personal_id() -> str:
    return ''.join(random.choices('1234567890', k=11))


def generate_random_mobile_number() -> str:
    response = generate_random_number()
    return "996599" + response


def generate_fake_name() -> str:
    return fake.name()


def generate_fake_birthDate() -> str:
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    return birth_date.strftime("%Y-%m-%d")


def generate_identification_number() -> str:
    return ''.join(random.choices('1234567890', k=9))


def generate_fake_address() -> str:
    return fake.address()


def test_generate_fake_iban() -> int:
    return fake.iban()


def test_get_fake_image_url(width=300, height=200) -> str:
    return f'https://picsum.photos/{width}/{height}/?random'


def test_download_image(url) -> Image:
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))


def test_get_fake_email() -> str:
    return fake.email()


def fake_company() -> str:
    return fake.company()


def random_merchantGroup() -> str:
    numbers = [3, 28, 1, 10, 31]
    return random.choice(numbers)


def iban_generator() -> int:
    country_code = "GE"
    bank_initial_char = ["TB", "BG"]
    bank_code = random.choice(bank_initial_char)
    check_digit = ''.join(random.choices('1234567890', k=2))
    bank_account = ''.join(random.choices('1234567890', k=16))
    return country_code + check_digit + bank_code + bank_account
