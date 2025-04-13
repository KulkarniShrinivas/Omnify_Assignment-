from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_link = (By.LINK_TEXT, "PIM")

    def navigate_to_pim(self):
        pim_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pim_link))
        actions = ActionChains(self.driver)
        actions.move_to_element(pim_element).click().perform()
