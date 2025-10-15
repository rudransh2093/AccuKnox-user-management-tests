from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

def test_add_new_user(page):
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")

    page.locator("span.oxd-main-menu-item--name:has-text('Admin')").click()
    page.wait_for_selector("h6:has-text('User Management')", timeout=5000)
    page.wait_for_timeout(2000)

    admin = UserManagementPage(page)
    admin.click_add()
    admin.fill_user_form(
        user_role="ESS",
        employee_name="Davonte Bruen",
        status="Enabled",
        username="Brucedeo123",
        password="Davonte123"
    )
    admin.save_user()

    page.wait_for_selector(f"text=Brucedeo123", timeout=5000)
    assert page.locator(f"text=Brucedeo123").is_visible()
