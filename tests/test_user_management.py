from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

def test_add_user(page):
    login = LoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    um = UserManagementPage(page)
    page.wait_for_selector('text=User Management')
    um.add_user("TestUser123", "Password123!")
    page.wait_for_timeout(2000)
    assert page.locator("text=TestUser123").is_visible()
