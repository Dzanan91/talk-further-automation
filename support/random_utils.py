import random
from playwright.sync_api import Page
from  faker import Faker
import re

def click_random_option_by_text(page: Page, text_options: list[str], locator_prefix: str = "label.option-button.primary") -> str:
    """
    Randomly selects one text from `text_options` and clicks an element 
    matching the combined locator (locator_prefix + :has-text('<selected>')).

    :param page: The Playwright page object.
    :param text_options: A list of possible text labels to choose from.
    :param locator_prefix: The base locator string (defaults to "label.option-button.primary").
    """
    selected_text = random.choice(text_options)
    
    locator = page.locator(f"{locator_prefix}:has-text('{selected_text}')")
    
    locator.click()
    
    print(f"Selected option: {selected_text}")
    return selected_text

def generate_user_details():
    """
    Generates random user details: first name, last name, and email.
    """
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    full_name = f"{first_name} {last_name}"

    # Generate a phone number and remove non-digit characters
    raw_phone = fake.phone_number()
    digits_only = re.sub(r'\D', '', raw_phone) 

    # Ensure 10 digits for a valid number
    if len(digits_only) == 10:
        phone = f"+1-{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
    else:
        phone = "+1-555-555-5555"  # Fallback in case Faker generates invalid phone number format

    return {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "email": email,
        "phone": phone
    }

def generate_author_payload() -> dict:
    """
    Generates a payload for creating a new author.
    """
    fake = Faker('en_US')
    author_id = random.randint(10000, 99999)
    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
        "id": author_id,
        "idBook": 0,
        "firstName": first_name,
        "lastName": last_name
    }