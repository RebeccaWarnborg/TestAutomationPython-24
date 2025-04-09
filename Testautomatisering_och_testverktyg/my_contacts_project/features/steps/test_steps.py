from behave import given, when, then
from playwright.sync_api import sync_playwright

@given("att jag är på kontaktsidan")
def step_go_to_contact_page(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://forverkliga.se/JavaScript/my-contacts/#/")
    
    # Sparar för att kunna använda i andra steg
    context.playwright = playwright
    context.browser = browser
    context.page = page

@when("sidan laddas")
def step_wait_for_load(context):
    context.page.click("text=Vänlista")
    context.page.wait_for_selector("text=Ändra")

@then("ska jag se en lista med kontakter")
def step_see_contacts_list(context):
    assert context.page.query_selector("text=Ändra") is not None
    context.browser.close()
    context.playwright.stop()

