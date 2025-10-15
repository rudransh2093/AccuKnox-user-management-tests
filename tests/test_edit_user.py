import pytest
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

@pytest.mark.parametrize("username,new_status", [("Brucedeo123", "Disabled")])
def test_edit_user(page, username, new_status):
    login_page = LoginPage(page)
    user_page = UserManagementPage(page)

    login_page.goto()
    login_page.login("Admin", "admin123")
    user_page.go_to_user_management()

    user_page.edit_user(username, new_status)

    user_page.search_user(username)
    status_locator = page.locator(f"div.oxd-table-cell:has-text('{new_status}')").first
    assert status_locator.is_visible(), f"User '{username}' status was not updated"
