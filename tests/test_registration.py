from playwright.sync_api import sync_playwright

def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
        email_input.fill('user.name@gmail.com')

        username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
        username_input.fill('username')

        password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
        password_input.fill('password')

        registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        page.wait_for_timeout(5000)