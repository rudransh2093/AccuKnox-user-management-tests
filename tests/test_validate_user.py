import pytest
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

@pytest.mark.parametrize("username", ["Brucedeo123"])
def test_search_user(page, username):
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")
    
    page.locator("span.oxd-text:has-text('Admin')").click()
    page.wait_for_timeout(2000)

    user_mgmt = UserManagementPage(page)
    user_mgmt.search_user(username)
    
    assert page.locator(f"text={username}").first.is_visible()