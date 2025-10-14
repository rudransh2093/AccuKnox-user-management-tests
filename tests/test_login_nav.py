from pages.login_page import LoginPage

def test_login_and_navigate_admin(page):
    login = LoginPage(page)
    login.goto()
    login.login("Admin", "admin123")

    page.wait_for_selector("h6:has-text('Dashboard')", timeout=5000)
    assert page.locator("h6:has-text('Dashboard')").is_visible()

    admin_link = page.locator("span.oxd-main-menu-item--name:has-text('Admin')")
    admin_link.click()

    page.wait_for_selector("h6:has-text('User Management')", timeout=5000)
    assert page.locator("h6:has-text('User Management')").is_visible()
    page.wait_for_timeout(2000)