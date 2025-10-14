import pytest
from pages.user_management_page import UserManagementPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("username", ["Brucedeo221"])  # or any username you want to test
def test_search_user(page, username):
    # Login first
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")
    
    # Navigate to Admin → User Management
    user_mgmt = UserManagementPage(page)
    
    # Search for the username
    user_mgmt.search_user(username)
    
    # Verify that the username appears in the results
    assert page.locator(f"text={username}").first.is_visible()
