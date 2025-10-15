from playwright.sync_api import Page

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page

        # Admin panel elements
        self.username_box = page.locator("div.oxd-input-group input[name='username']")
        self.search_button = page.locator("button:has-text('Search')")
        self.add_button = page.locator("button:has-text('Add')")

        # Add User form elements
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
        self.page.wait_for_selector("div.oxd-autocomplete-option", timeout=5000)
        self.page.locator("div.oxd-autocomplete-option").first.click()

        self.status_dropdown.click()
        self.page.locator(f"div[role='option']:has-text('{status}')").click()

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)

    def go_to_user_management(self):
        self.page.click("a:has-text('Admin')")
        self.page.wait_for_timeout(2000)

    def search_user(self, username):
        # Using exact XPaths from your inspection
        username_input_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        search_button_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'

        self.page.locator(f'xpath={username_input_xpath}').click()
        self.page.fill(f'xpath={username_input_xpath}', username)
        self.page.wait_for_timeout(1500)
        self.page.locator(f'xpath={search_button_xpath}').click()
        self.page.wait_for_timeout(3000)

    def save_user(self):
        self.save_button.click()
