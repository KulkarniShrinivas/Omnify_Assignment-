import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import get_driver
from pages.LoginPage import LoginPage
import time

def test_login():
    print("Launching browser...")
    driver = get_driver()

    print("Opening login page...")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    print("Performing login...")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    print("Waiting before closing...")
    time.sleep(5)

    driver.quit()
    print("Test completed and browser closed.")

if __name__ == "__main__":
    test_login()
