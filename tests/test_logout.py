import pytest
from pages.login_page import LoginPage

def test_logout(page):
    login = LoginPage(page)

    # 1. Prerequisite: Login
    login.goto()
    login.login("Admin", "admin123")
    
    # Wait for Dashboard to confirm successful login before logging out
    page.wait_for_selector("h6:has-text('Dashboard')", timeout=5000)

    # 2. Perform Logout
    login.logout()

    # 3. Verify Logout (Check if the login form is visible)
    assert login.login_button.is_visible(), "Logout failed: Login button is not visible."
    assert "login" in page.url, "Logout failed: Not redirected to the login URL."