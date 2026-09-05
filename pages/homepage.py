from playwright.sync_api import sync_playwright, expect, Page

class AmazonHomePage:

    def __init__(self, page: Page):
        self.signin_btn= page.locator("#nav-link-accountList")

    def clickon_signin_account_btn(self):
        self.signin_btn.click()
