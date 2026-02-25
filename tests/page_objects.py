from playwright.sync_api import Playwright, expect, Locator
class PageObjects:
    
    def __init__(self, page):
        self.page = page



    def open_browser(self):
        self.page.locator(".toggle").click()
        print('toogle clicking successfully.')
        self.page.wait_for_timeout(3000)