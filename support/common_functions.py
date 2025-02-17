import logging
from playwright.sync_api import Page, Locator, expect

# Logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CommonFunctions:
    def __init__(self, page: Page):
        self.page = page

    def click_button(self, locator: Locator, index: int = 0, timeout: int = 60000):
        """Scroll to and click a button or element."""
        try:
            element = locator.nth(index)
            logger.info(f"Clicking button at index {index}.")
            element.scroll_into_view_if_needed(timeout=timeout)
            element.click(timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to click button: {e}")
            raise

    def click_element_by_text(self, base_locator: str, text: str, timeout: int = 60000):
        """
        Clicks on an element based on the base locator and text content.
        :param base_locator: Base locator (e.g., 'button', 'div').
        :param text: Text content of the element to match.
        """
        try:
            target_element = self.page.locator(f"{base_locator}:has-text('{text}')")
            logger.info(f"Clicking element with text '{text}' using base locator '{base_locator}'.")
            expect(target_element).to_be_visible(timeout=timeout)
            target_element.click(timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to click element by text: {e}")
            raise

    def input_text(self, locator: Locator, text: str, index: int = 0, timeout: int = 60000):
        """Input text into a given element."""
        try:
            element = locator.nth(index)
            logger.info(f"Filling text '{text}' into element at index {index}.")
            element.fill(text, timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to input text: {e}")
            raise

    def element_is_visible(self, locator: Locator, timeout: int = 60000):
        """Check if an element is visible."""
        try:
            logger.info("Checking element visibility.")
            expect(locator).to_be_visible(timeout=timeout)
            visibility = locator.is_visible(timeout=timeout)
            logger.info(f"Element is visible: {visibility}")
            return visibility
        except Exception as e:
            logger.error(f"Error checking element visibility: {e}")
            return False

    def element_is_not_visible(self, locator: Locator, timeout: int = 60000):
        """Check if an element is NOT visible (hidden or detached)."""
        try:
            logger.info("Checking if element is NOT visible.")
            expect(locator).not_to_be_visible(timeout=timeout)
            visibility = not locator.is_visible(timeout=timeout)
            logger.info(f"Element is NOT visible: {visibility}")
            return visibility
        except Exception as e:
            logger.error(f"Error checking element non-visibility: {e}")
            return False

    def is_text_visible(self, locator: Locator, expected_text: str, index: int = 0, timeout: int = 60000) -> None:
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

    def is_text_present_on_page(self, expected_text: str, timeout: int = 60000):
        """
        Verify if the expected text is visible anywhere on the page.
        :param expected_text: The text to validate.
        :param timeout: Timeout for waiting.
        """
        try:
            logger.info(f"Verifying text '{expected_text}' is visible anywhere on the page.")
            self.page.wait_for_selector(f"text={expected_text}", timeout=timeout)
            logger.info(f"Text '{expected_text}' is present on the page.")
        except Exception as e:
            logger.error(f"Text visibility verification failed: {e}")
            raise
