import pytest
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

# Assuming the user 'Brucedeo221' was created and edited in previous tests
@pytest.mark.parametrize("username_to_delete", ["Renu_1524"])
def test_delete_user(page, username_to_delete):
    login = LoginPage(page)
    user_mgmt = UserManagementPage(page)
    
    # 1. Login and Navigate
    login.goto()
    login.login("Admin", "admin123")
    user_mgmt.go_to_user_management()

    # 2. Delete the User
    user_mgmt.delete_user(username_to_delete)

    # --- Verification (Test Case: Verify the User is Deleted) ---
    
    # 3. Search again for the deleted username
    user_mgmt.search_user(username_to_delete)
    
    # 4. Assert "No Records Found" message appears
    no_records_locator = page.locator("span.oxd-text:has-text('No Records Found')")
    
    # Wait for the "No Records Found" message to be visible
    no_records_locator.wait_for(state="visible", timeout=5000)
    
    assert no_records_locator.is_visible(), f"User '{username_to_delete}' was found after deletion attempt."