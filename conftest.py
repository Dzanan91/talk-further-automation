from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

# UI Imports
from pages.home_page import HomePage
from support.common_functions import CommonFunctions
from config.config import BASE_URL 

# API imports
from config.config import BASE_API_URL
from api_utils.authors_api import AuthorsAPI

@pytest.fixture
def browser():
    """Set up the Playwright browser."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True, 
            args=["--window-size=1920,1080"]
        )
        yield browser
        browser.close()

@pytest.fixture
def browser_context(browser):
    """Set up a fresh browser context for each test to avoid shared session data."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos"  # This tells Playwright to record videos in the "videos" folder
    )
    yield context
    context.close()  # Ensures cookies, cache, and storage are cleared

@pytest.fixture
def page(browser_context):
    """Provide a new page for each test, ensuring isolation."""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def common_functions(page):
    """Initialize and provide the CommonFunctions class."""
    return CommonFunctions(page)

@pytest.fixture
def home_page(page, browser_context):
    """Initialize and provide the HomePage class."""
    return HomePage(page, browser_context, BASE_URL)

@pytest.fixture
def authors_api():
    """
    Returns an instance of AuthorsAPI which extends BaseAPI.
    """
    return AuthorsAPI(BASE_API_URL)
