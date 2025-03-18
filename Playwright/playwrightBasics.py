import time

from playwright.sync_api import Page

def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)      # Launch the browser
    context = browser.new_context()       # Create a new context      # Create a new page
    page = context.new_page()       # Create a new page
    page.goto("https://rahulshettyacademy.com/")

# page fixture is used for chromium browser headless mode,1 single context and 1 single page
def test_playwrightshortcut(page : Page):
    page.goto("https://rahulshettyacademy.com/")


def test_corelocators(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    time.sleep(5)
    page.get_by_role("button",name= "Sign In").click()
    time.sleep(5)





