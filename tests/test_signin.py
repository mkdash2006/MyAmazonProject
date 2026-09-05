from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.signInpage import SignInHome
from pages.homepage import AmazonHomePage

@pytest.mark.smoke5
def test_signin(page:Page, navigate_to_amazon):
    home_page_obj= AmazonHomePage(page)
    signin_page_obj= SignInHome(page)
    home_page_obj.clickon_signin_account_btn()
    signin_page_obj.fill_email_or_mobile_text_field()
    signin_page_obj.click_on_continue_btn()
    signin_page_obj.validatenextsignpage()