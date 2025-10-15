import pytest
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

@pytest.mark.parametrize("username_to_delete", ["Renu_1524"])
def test_delete_user(page, username_to_delete):
    login = LoginPage(page)
    user_mgmt = UserManagementPage(page)
    
    login.goto()
    login.login("Admin", "admin123")
    user_mgmt.go_to_user_management()

    user_mgmt.delete_user(username_to_delete)

    
    user_mgmt.search_user(username_to_delete)
    
    no_records_locator = page.locator("span.oxd-text:has-text('No Records Found')")
    
    no_records_locator.wait_for(state="visible", timeout=5000)
    
    assert no_records_locator.is_visible(), f"User '{username_to_delete}' was found after deletion attempt."