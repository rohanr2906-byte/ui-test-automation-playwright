from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("rohan")
    page.locator("#password").fill("12345")
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match"
    )