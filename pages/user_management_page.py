from playwright.sync_api import Page

class UserManagementPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_box = page.locator("div.oxd-input-group input[name='username']")
        self.search_button = page.locator("button:has-text('Search')")
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
        username_input_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        search_button_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'

        self.page.locator(f'xpath={username_input_xpath}').click()
        self.page.fill(f'xpath={username_input_xpath}', username)
        self.page.wait_for_timeout(1500)
        self.page.locator(f'xpath={search_button_xpath}').click()
        self.page.wait_for_timeout(3000)
        
    def edit_user(self, username, new_role=None, new_status=None, new_employee_name=None, new_password=None):
        
        self.search_user(username) 

        self.page.wait_for_selector(f"//div[text()='{username}']", timeout=5000)

        edit_icon_xpath = f"//div[text()='{username}']/ancestor::div[@role='row']//button/i[@class='oxd-icon bi-pencil-fill']"
        
        self.page.locator(f'xpath={edit_icon_xpath}').click()
        
        self.page.wait_for_selector("h6:has-text('Edit User')", timeout=5000)

        if new_role:
            self.page.locator("(//div[contains(@class,'oxd-select-text-input')])[1]").click()
            self.page.locator(f"div[role='option']:has-text('{new_role}')").click()

        if new_employee_name:
            self.employee_name_input.fill(new_employee_name[:1])
            self.page.wait_for_selector("div.oxd-autocomplete-option", timeout=5000)
            self.page.locator(f"div.oxd-autocomplete-option span:has-text('{new_employee_name}')").first.click()

        if new_status:
            self.page.locator("(//div[contains(@class,'oxd-select-text-input')])[2]").click()
            self.page.locator(f"div[role='option']:has-text('{new_status}')").click()

        if new_password:
            self.page.locator("label:has-text('Change Password ?')").click()
            self.password_input.fill(new_password)
            self.confirm_password_input.fill(new_password)

        self.save_button.click()
        self.page.wait_for_selector("div.oxd-toast.oxd-toast--success", timeout=10000)
    def delete_user(self, username):
            # 1. Search for the user to make the row visible
            self.search_user(username) 
            
            # Wait for the user's row to appear
            self.page.wait_for_selector(f"//div[text()='{username}']", timeout=5000)

            # 2. Click the individual Delete (trash) icon in the user's row
            # Locator targets the trash icon within the row containing the username
            delete_icon_xpath = f"//div[text()='{username}']/ancestor::div[@role='row']//button/i[@class='oxd-icon bi-trash']"
            self.page.locator(f'xpath={delete_icon_xpath}').click()
            
            # 3. Confirm the deletion in the modal dialog ("Are You Sure?")
            # Wait for the modal button to appear
            self.page.wait_for_selector("button:has-text('Yes, Delete')", timeout=5000)
            self.page.locator("button:has-text('Yes, Delete')").click()
            
            # Wait for the success toast message
            self.page.wait_for_selector("div.oxd-toast.oxd-toast--success", timeout=10000)

    def save_user(self):
        self.save_button.click()
