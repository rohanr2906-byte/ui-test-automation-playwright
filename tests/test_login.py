from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

    expect(page.locator("h1")).to_contain_text("Logged In Successfully")