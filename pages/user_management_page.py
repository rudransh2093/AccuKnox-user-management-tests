from playwright.sync_api import Page

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator("button:has-text('Add')")
        self.user_role_dropdown = page.locator("(//div[contains(@class,'oxd-select-text-input')])[1]")
        self.employee_name_input = page.locator("input[placeholder='Type for hints...']")
        self.status_dropdown = page.locator("(//div[contains(@class,'oxd-select-text-input')])[2]")
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.confirm_password_input = page.locator("input[name='confirmPassword']")
        self.save_button = page.locator("button:has-text('Save')")

    def click_add(self):
        self.add_button.click()

    def fill_user_form(self, user_role, employee_name, status, username, password):
        self.user_role_dropdown.click()
        self.page.locator(f"div[role='option']:has-text('{user_role}')").click()

        self.employee_name_input.fill("a")      
        self.page.wait_for_selector("div.oxd-autocomplete-option", timeout=5000)  # waits up to 5 sec
        self.page.locator("div.oxd-autocomplete-option").first.click()


        self.status_dropdown.click()
        self.page.locator(f"div[role='option']:has-text('{status}')").click()

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)


    def save_user(self):
        self.save_button.click()
