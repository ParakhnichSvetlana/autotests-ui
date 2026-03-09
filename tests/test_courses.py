from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
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
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title_courses = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')
        expect(title_courses).to_have_text('Courses')

        empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        title_courses_empty_list = page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
        expect(title_courses_empty_list).to_have_text('There is no results')

        empty_list_description = page.locator('//p[@data-testid="courses-list-empty-view-description-text"]')
        expect(empty_list_description).to_have_text('Results from the load test pipeline will be displayed here')