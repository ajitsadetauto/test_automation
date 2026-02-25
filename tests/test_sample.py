import time
from playwright.sync_api import Playwright
import pytest 


@pytest.mark.sanity
def test_open_browser(open_obj):
    print('Browser opened successfully.')
    open_obj.open_browser()

