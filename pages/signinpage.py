from playwright.sync_api import sync_playwright, expect, Page

class SignInHome:

    def __init__(self, page):
        self.email_mobile_text_field= page.locator("input[name='email']")
        self.continue_btn= page.locator("#continue")
        self.password_text_field= page.locator("#ap_password") 
        self.signin_submit_btn= page.locator("input#signInSubmit")
        self.otpcode_text_field= page.locator("input#input-box-otp")
        self.submitcode_btn= page.locator("input.a-button-input")

    def fill_email_or_mobile_text_field(self):
        self.email_mobile_text_field.fill("mkdash2003@gmail.com")

    def click_on_continue_btn(self):
        self.continue_btn.click()
                        
    def validatenextsignpage(self):
        # Verify that the next sign-in step is displayed
        expect(self.password_text_field).to_be_visible()
    