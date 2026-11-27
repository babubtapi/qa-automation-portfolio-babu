from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # 1. Navigate to the practice e-commerce site
    page.goto("https://www.saucedemo.com/")

    # 2. Enter valid username and password
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # 3. Click the Login button
    page.locator("#login-button").click()

    # 4. Assert we landed on the Products inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")