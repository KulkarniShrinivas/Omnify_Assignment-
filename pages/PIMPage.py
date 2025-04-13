from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.employee_id_input = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_link = (By.LINK_TEXT, "Employee List")
        self.search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.next_page_button = (By.XPATH, "//button[@aria-label='Next Page']")

    def add_employee(self, first_name, last_name):
        print(f"➡️ Adding employee: {first_name} {last_name}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_employee_button)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

        unique_id = str(int(time.time()))[-6:]
        employee_id_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.employee_id_input)
        )
        employee_id_field.clear()
        employee_id_field.send_keys(unique_id)

        self.driver.find_element(*self.save_button).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.employee_list_link))
        print(f"Added employee: {first_name} {last_name} with ID {unique_id}")

    def go_to_employee_list(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.employee_list_link)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input))
        print(" Navigated to Employee List")

    def verify_employee(self, name):
        print(f" Verifying employee: {name} through scrolling")
        found = False
        while True:
            rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")
            for row in rows:
                self.driver.execute_script("arguments[0].scrollIntoView();", row)
                time.sleep(0.5)
                if name in row.text:
                    print(f" {name} - Name Verified")
                    found = True
                    break

            if found:
                break

            try:
                next_button = self.driver.find_element(*self.next_page_button)
                if "disabled" in next_button.get_attribute("class"):
                    break  # No more pages
                next_button.click()
                time.sleep(2)
            except:
                break

        if not found:
            print(f" {name} - Not Found")
