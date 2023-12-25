import random
import requests
from faker import Faker
import io
from PIL import Image




def generate_random_number():
    random_number = ''.join(random.choices('1234567890', k=6))
    return random_number


def generate_personal_id():
    random_number = ''.join(random.choices('1234567890', k=11))
    return random_number


def generate_random_mobile_number() -> str:
    response = generate_random_number()
    mob_number = "599" + response
    return mob_number


def generate_fake_name() -> str:
    fake = Faker()
    name = fake.name()
    return name


def generate_fake_birthDate():
    fake = Faker()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    formatted_birthdate = birth_date.strftime("%Y-%m-%d")
    return formatted_birthdate


def generate_identification_number():
    random_number = ''.join(random.choices('1234567890', k=9))
    return random_number


def generate_fake_address():
    faker = Faker()
    address = faker.address()
    return address


def test_generate_fake_iban():
    faker = Faker()
    iban = faker.iban()
    return iban


fake = Faker()


def test_get_fake_image_url(width=300, height=200):
    return f'https://picsum.photos/{width}/{height}/?random'


def test_download_image():
    response = requests.get()
    return Image.open(io.BytesIO(response.content))


def test_get_fake_email():
    faker = Faker()
    email = faker.email()
    return email


def fake_company():
    faker = Faker()
    company = faker.company()
    return company


def random_merchantGroup():
    numbers = [3, 28, 1, 10, 31]
    randon_number = random.choice(numbers)
    print(randon_number)
    return randon_number



def iban_generator():
    country_code = "GE"
    bank_initial_char = ["TB", "BG"]
    bank_code = random.choice(bank_initial_char)
    check_digit = ''.join(random.choices('1234567890', k=2))
    bank_account = ''.join(random.choices('1234567890', k=16))
    iban = country_code + check_digit + bank_code + bank_account
    return iban

