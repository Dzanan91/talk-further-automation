import logging
from playwright.sync_api import Page, Locator, expect

# logger config
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CommonFunctions:
    def __init__(self, page: Page):
        self.page = page

    def click_button(self, locator: Locator, index: int = 0):
        """Scroll to and click a button or element."""
        try:
            element = locator.nth(index)
            logger.info(f"Clicking button at index {index}.")
            element.scroll_into_view_if_needed()
            element.click()
        except Exception as e:
            logger.error(f"Failed to click button: {e}")
            raise

    def click_element_by_text(self, base_locator: str, text: str):
        """
        Clicks on an element based on the base locator and text content.
        :param base_locator: Base locator (e.g., 'button', 'div').
        :param text: Text content of the element to match.
        """
        try:
            target_element = self.page.locator(f"{base_locator}:has-text('{text}')")
            logger.info(f"Clicking element with text '{text}' using base locator '{base_locator}'.")
            expect(target_element).to_be_visible(timeout=5000)
            target_element.click()
        except Exception as e:
            logger.error(f"Failed to click element by text: {e}")
            raise

    def input_text(self, locator: Locator, text: str, index: int = 0):
        """Input text into a given element."""
        try:
            element = locator.nth(index)
            logger.info(f"Filling text '{text}' into element at index {index}.")
            element.fill(text)
        except Exception as e:
            logger.error(f"Failed to input text: {e}")
            raise

    def element_is_visible(self, locator: Locator, timeout: int = 30000):
        """Check if an element is visible."""
        try:
            logger.info("Checking element visibility.")
            expect(locator).to_be_visible(timeout=timeout)
            visibility = locator.is_visible()
            logger.info(f"Element is visible: {visibility}")
            return visibility
        except Exception as e:
            logger.error(f"Error checking element visibility: {e}")
            return False

    def element_is_not_visible(self, locator: Locator, timeout: int = 30000):
        
        """Check if an element is NOT visible (hidden or detached)."""
        try:
            logger.info("Checking if element is NOT visible.")
            expect(locator).not_to_be_visible(timeout=timeout)
            visibility = not locator.is_visible()
            logger.info(f"Element is NOT visible: {visibility}")
            return visibility
        except Exception as e:
            logger.error(f"Error checking element non-visibility: {e}")
            return False

    def get_text(self, selector: str):
        """Retrieve the text of an element by selector."""
        try:
            text = self.page.locator(selector).inner_text()
            logger.info(f"Retrieved text from '{selector}': {text}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from '{selector}': {e}")
            raise

    def hover_over_element(self, locator: Locator) -> None:
        """Hover over an element."""
        try:
            logger.info("Hovering over element.")
            locator.hover()
        except Exception as e:
            logger.error(f"Failed to hover over element: {e}")
            raise

    def is_text_visible(self, locator: Locator, expected_text: str, index: int = 0, timeout: int = 30000) -> None:
        """
        Verify if the expected text is visible in a specific element.
        :param locator: The Playwright locator object.
        :param expected_text: The expected text.
        :param index: Index if there are multiple matching elements.
        :param timeout: Timeout for waiting.
        """
        try:
            element = locator.nth(index)
            logger.info(f"Verifying text '{expected_text}' is visible in element at index {index}.")
            element.wait_for(state="visible", timeout=timeout)
            actual_text = element.inner_text().strip()
            if actual_text != expected_text.strip():
                logger.error(f"Text mismatch: Expected '{expected_text}', got '{actual_text}'.")
            assert actual_text == expected_text.strip(), f"Expected: '{expected_text}', but got: '{actual_text}'"
        except Exception as e:
            logger.error(f"Text visibility verification failed: {e}")
            raise
    def is_text_present_on_page(self, expected_text: str, timeout: int = 30000):
        """
        Verify if the expected text is visible anywhere on the page.
        
        :param expected_text: The text to validate.
        :param timeout: Timeout for waiting (default 30s).
        """
        try:
            logger.info(f"Verifying text '{expected_text}' is visible anywhere on the page.")
            
            # Wait for the text to be visible anywhere on the page
            self.page.wait_for_selector(f"text={expected_text}", timeout=timeout)
            
            logger.info(f"Text '{expected_text}' is present on the page.")
        except Exception as e:
            logger.error(f"Text visibility verification failed: {e}")
            raise


    def validate_url(self, expected_url: str, match_type: str = "exact"):
        """
        Validates the current URL.
        :param expected_url: The expected URL or part of the URL.
        :param match_type: 'exact' for an exact match or 'contains' for a partial match.
        """
        try:
            current_url = self.page.url
            logger.info(f"Validating URL. Expected: '{expected_url}', Got: '{current_url}', Match type: '{match_type}'.")
            if match_type == "exact":
                assert current_url == expected_url, f"Expected URL: '{expected_url}', but got: '{current_url}'"
            elif match_type == "contains":
                assert expected_url in current_url, f"URL does not contain: '{expected_url}'"
            else:
                raise ValueError(f"Invalid match type: {match_type}")
        except Exception as e:
            logger.error(f"URL validation failed: {e}")
            raise
