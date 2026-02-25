import pytest
import re
from playwright.sync_api import Playwright
from tests.page_objects import PageObjects

@pytest.fixture(scope="session")
def open_obj(setup_teardown):

    return PageObjects(setup_teardown)


@pytest.fixture(scope="session") 
def setup_teardown(playwright:Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context(record_video_dir="./video/")
    page = context.new_page()
    page.goto("https://www.automationtesting.co.uk/", wait_until="domcontentloaded", timeout=60000)
    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(60000)
    yield page


    


