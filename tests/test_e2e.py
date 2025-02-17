from support.random_utils import generate_user_details
import pytest



#@pytest.mark.skip(reason="Skip test")
def test_schedule_a_tour(home_page, common_functions):

    user_details = generate_user_details()
    empty_email_error_message = (
    "segment_1 must be a `string` type, but the final value was: `null`. "
    "If \"null\" is intended as an empty value be sure to mark the schema as `.nullable()`"
)
    invalid_email_error_message = 'Please use a valid email address'
    invalid_phone_number_format_error_message = 'Sorry but that is an invalid phone number. Please check it is 10 digits long and does not contain letters or symbols.'
    
    # Navigate to home page 
    home_page.navigate_to_home_page()

    # Select Schedule A Tour and fill in required data
    home_page.select_initial_option('Schedule A Tour')

    # Randomly select one of the tour options
    home_page.select_random_option(home_page.schedule_a_tour_options, home_page.tour_options_locator)
    home_page.select_tour_date_and_time()
    home_page.click_next()

    # Randomly select one of the activities
    home_page.select_random_option(home_page.activities, home_page.activities_locator)
    home_page.click_confirm_selections()

    # Fill in personal data
    home_page.personal_data_input(user_details['full_name'])
    home_page.click_submit()

    # Validate error message for empty email field
    home_page.click_submit()
    common_functions.is_text_visible(home_page.error_message, empty_email_error_message)

    # Validate error message for invalid email format
    home_page.personal_data_input('Invalidemailaddress')
    common_functions.is_text_visible(home_page.error_message, invalid_email_error_message)

    # Enter valid email address and proceed 
    home_page.personal_data_input(user_details['email'])
    home_page.click_submit()

    # Validate error message for invalid phone number
    home_page.personal_data_input('12457zzz')
    home_page.click_submit()
    common_functions.is_text_visible(home_page.error_message, invalid_phone_number_format_error_message)

    # Enter valid phone and proceed
    home_page.personal_data_input(user_details['phone'])
    home_page.click_submit()

    # Validate tour was requested
    common_functions.element_is_visible(home_page.please_wait_banner)
    common_functions.element_is_not_visible(home_page.please_wait_banner)

    # Close chat
    home_page.close_chat()

#@pytest.mark.skip(reason="Skip test")
def test_pricing_flow(home_page, common_functions):

    user_details = generate_user_details()

    empty_email_error_message = (
    "segment_1 must be a `string` type, but the final value was: `null`. "
    "If \"null\" is intended as an empty value be sure to mark the schema as `.nullable()`"
)
    invalid_email_error_message = 'Please use a valid email address'
    invalid_phone_number_format_error_message = 'Sorry but that is an invalid phone number. Please check it is 10 digits long and does not contain letters or symbols.'

    # Navigate to home page 
    home_page.navigate_to_home_page()

    # Select Pricing and level of care random options
    home_page.select_initial_option('Pricing')
    home_page.select_random_option(home_page.level_of_care_options, home_page.tour_options_locator)
    
    # Select random person for level of care
    home_page.select_random_option(home_page.relationship_options, home_page.tour_options_locator)
    
    # Select timeline options
    home_page.select_random_option(home_page.timeline_options, home_page.tour_options_locator)

    # Fill in personal data
    home_page.personal_data_input(user_details['full_name'])
    home_page.click_submit()

    # Validate error message for invalid phone number
    home_page.personal_data_input('12457zzz')
    home_page.click_submit()
    common_functions.is_text_visible(home_page.error_message, invalid_phone_number_format_error_message)

    # Enter valid phone and proceed
    home_page.personal_data_input(user_details['phone'])
    home_page.click_submit()

    # Validate error message for empty email field
    home_page.click_submit()
    common_functions.is_text_visible(home_page.error_message, empty_email_error_message)

    # Validate error message for invalid email format
    home_page.personal_data_input('Invalidemailaddress')
    common_functions.is_text_visible(home_page.error_message, invalid_email_error_message)

    # Enter valid email address and proceed 
    home_page.personal_data_input(user_details['email'])
    home_page.click_submit()

    # Validate tour was requested
    common_functions.element_is_visible(home_page.please_wait_banner)
    common_functions.element_is_not_visible(home_page.please_wait_banner)

    # Select Schedule a visit
    home_page.click_schedule_a_visit()
    home_page.select_tour_date_and_time()
    home_page.click_next()

    # Randomly select one of the activities
    home_page.select_random_option(home_page.activities, home_page.activities_locator)
    home_page.click_confirm_selections()

    # Validate first and last name are prepopulated
    common_functions.is_text_present_on_page(user_details['full_name'])
    home_page.click_submit()

    # Validate email is prepopulated
    common_functions.is_text_present_on_page(user_details['email'])
    home_page.click_submit()

    # Validate phone is prepopulated
    common_functions.is_text_present_on_page(user_details['phone'])
    home_page.click_submit()

    # Close chat
    home_page.close_chat()