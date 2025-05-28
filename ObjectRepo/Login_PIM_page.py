import time
from selenium.webdriver.common.by import By
import json
from conf_test import Config

with open('Data.json', 'r') as f:
    data = json.load(f)
employees = data['employees']

class BaseClass:
    def __init__(self, driver=None):
        self.driver = Config.config()

    def quit_driver(self):
        self.driver.quit()


class LoginPIM(BaseClass):

    def test_login_negative(self):
        print("logging in...")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin@123")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123!@#")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        validation = self.driver.find_element(By.XPATH, "//p[.='Invalid credentials']").text
        assert validation == "Invalid credentials"

    def test_login_positive(self):
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.implicitly_wait(10)
        dashboard = self.driver.find_element(By.XPATH, "//h6[.='Dashboard']").text
        assert dashboard == "Dashboard", f"login failed"

    def add_employees(self):
        # PIM = self.driver.find_element(By.XPATH)
        # dashboard = self.driver.find_element(By.XPATH, "(//span[.='PIM'])[1]").text
        # hover = ActionChains
        # hover.move_to_element(to_element=PIM).perform()

        self.driver.find_element(By.XPATH, "(//span[.='PIM'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[.= 'Add Employee']").click()
        time.sleep(2)

        # running a loop to add 4 employees
        for first_name, middle_name, last_name, emp_id in employees:
            # entering employee details
            first_name_input = self.driver.find_element(By.XPATH, "//input[@name='firstName']")
            first_name_input.clear()
            first_name_input.send_keys(first_name)

            middle_name_input = self.driver.find_element(By.XPATH, "//input[@name='middleName']")
            middle_name_input.clear()
            middle_name_input.send_keys(middle_name)

            last_name_input = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
            last_name_input.clear()
            last_name_input.send_keys(last_name)

            emp_id_input = self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
            emp_id_input.clear()
            emp_id_input.send_keys(emp_id)

        # clicks on submit and comes back to add employee page
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, "//a[.= 'Add Employee']").click()
            time.sleep(2)
        # opens the employee listing page
        self.driver.find_element(By.XPATH, "//a[. ='Employee List']").click()
        self.driver.implicitly_wait(10)


    def verify_added_employees(self):
        # running a loop to verify added employee name using their ID
        for first_name, middle_name, last_name, emp_id in [employees[3]]:
            self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[2]").clear()
            self.driver.find_element(By.XPATH, "(//input[@class ='oxd-input oxd-input--active'])[2]").send_keys(emp_id)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            employee_id = self.driver.find_element(By.XPATH, "(//div[@class='oxd-table-cell oxd-padding-cell'])[2]").text
            assert employee_id == emp_id, f"assert failed, employee not added"
            print("Name Verified")
            self.driver.execute_script("window.scrollTo(0, 0);")









