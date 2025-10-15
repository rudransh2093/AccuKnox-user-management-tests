from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button:has-text("Login")')

    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
            profile_button_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p'
            self.page.locator(f'xpath={profile_button_xpath}').click()
            
            logout_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'
            
            logout_link = self.page.locator(f'xpath={logout_link_xpath}')
            logout_link.wait_for(state="visible", timeout=5000)
            logout_link.click()
            

            self.page.wait_for_selector("button[type='submit']", timeout=5000)
