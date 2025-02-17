from playwright.sync_api import Page, BrowserContext
from support.common_functions import CommonFunctions
from support.random_utils import click_random_option_by_text
from datetime import date, timedelta


class HomePage:

    def __init__(self, page: Page, context: BrowserContext, base_url: str):
        self.page = page
        self.base_url = base_url
        
        # page instances
        self.common_functions = CommonFunctions(page)

        # Locators
        self.initial_options_btn = page.locator("label.option-button.primary")
        self.home_page_header_selector = page.locator("div.banner-text:has-text('Welcome to the live Further demo!')")
        self.next_btn = page.get_by_role("button", name="Next")
        self.confirm_selections = page.get_by_role("button", name="Confirm selections (1)")
        self.close_chat_btn = page.locator("span:has-text('Close Chat')")
        self.input_name = page.get_by_placeholder("Type here...")
        self.submit_btn = page.locator("div.user-input-wrapper button[type='submit']")
        self.please_wait_banner = page.locator("div.please-wait")
        self.error_message = page.locator("div[class='error-message']")
        self.info_message = page.locator("div.bubble-conatiner p")
        self.schedule_a_visit_btn = page.locator("label.option-button.primary:has-text('Schedule A Visit')")
        self.tour_options_locator = "label.option-button.primary"
        self.activities_locator = "label.option-button"
        self.time_locator = "div.time"


        # Arrays

        self.schedule_a_tour_options = ["Parent", "Spouse", "Family Member", "Friend", "Other"]

        self.level_of_care_options = [
            "Independent Living",
            "Assisted Living",
            "Memory Care",
            "Respite Care",
            "Not Sure",
        ]

        self.relationship_options = [
            "Parent",
            "Spouse",
            "Myself",
            "Relative",
            "Friend",
        ]

        self.timeline_options = [
            "Immediately",
            "1 to 3 Months",
            "3 Months +",
            "Just Researching"
        ]

        self.time_options = [
            "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM",
            "12:00 PM", "1:00 PM", "3:00 PM",
            "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM"
        ]

        self.activities = [
            "Happy Hour",
            "Music Activities",
            "Exercise Classes",
            "Game Night & Bingo",
            "Cooking",
            "Group Outings",
            "No, thank you"
        ]

    # Functions

    def navigate_to_home_page(self):
        """Navigate to the homepage."""
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")
        self.home_page_header_selector.wait_for(state="visible")

    def select_random_option(self, options: list, locator):
        """
        Randomly selects an option from a given list.
        """
        click_random_option_by_text(self.page, options, locator)


    def select_initial_option(self, option_text: str):
        """Clicks on a specified option using dynamic text filtering."""
        locator = self.initial_options_btn.filter(has_text=option_text) 
        self.common_functions.click_button(locator)
    
    
    def select_tour_date_and_time(self): 
        
        """ Date calculation logic, select 2 days ahead since one day ahead is already selected by default
        """
        tomorrow = date.today() + timedelta(days=2)
        tomorrow_day_str = str(tomorrow.day)

        day_locator = self.page.locator(f"div.day-in-month:has-text('{tomorrow_day_str}')")

        day_locator.wait_for(state="visible")
        day_locator.click()
        click_random_option_by_text(self.page, self.time_options, self.time_locator)
        
    
    def click_next(self):
        """
        Click on Next button
        """
        self.common_functions.click_button(self.next_btn)
    
    def click_confirm_selections(self):
        """
        Click on Confirm selection button
        """
        self.common_functions.click_button(self.confirm_selections)


    def personal_data_input(self, data):
        """
        Populates personal data based on the input requirement e.g email , first , last name etc.. 
        """
        self.common_functions.input_text(self.input_name, data)
        
    def click_submit(self):
        """
        Click on submit button
        """
        self.common_functions.click_button(self.submit_btn)

    def click_schedule_a_visit(self):
        """
        Click on scheduel a visit button
        """
        self.common_functions.click_button(self.schedule_a_visit_btn)

    def close_chat(self):
        """
        Click close chat button
        """
        self.common_functions.click_button(self.close_chat_btn)

    def wait(self): 
        self.page.wait_for_timeout(10000)
