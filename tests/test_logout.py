import pytest
from pages.login_page import LoginPage

def test_logout(page):
    login = LoginPage(page)

    login.goto()
    login.login("Admin", "admin123")
    
    page.wait_for_selector("h6:has-text('Dashboard')", timeout=5000)

    login.logout()

    assert login.login_button.is_visible(), "Logout failed: Login button is not visible."
    assert "login" in page.url, "Logout failed: Not redirected to the login URL."