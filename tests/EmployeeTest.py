import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.driver_setup import get_driver
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.PIMPage import PIMPage
from pages.LogoutPage import LogoutPage


def test_employee_workflow():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Navigate to PIM
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_pim()

    # Add Employees
    pim = PIMPage(driver)
    employees = ["Alice Smith", "Bob Johnson", "Charlie Davis"]
    for emp in employees:
        first, last = emp.split()
        pim.add_employee(first, last)

    # Verify Employees
    pim.go_to_employee_list()
    for emp in employees:
        pim.verify_employee(emp)

    # Logout
    logout_page = LogoutPage(driver)
    logout_page.logout()
    driver.quit()


if __name__ == "__main__":
    test_employee_workflow()