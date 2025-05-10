from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from faker import Faker


def init_driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    return driver


def login(driver):
    time.sleep(4)  # Wait for page load
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    ).click()
    time.sleep(3)


def navigate_to_add_employee(driver):
    # Click PIM in sidebar
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
            '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
        ))
    ).click()
    time.sleep(2)

    # Click "Add Employee"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
            "//a[contains(text(),'Add Employee')]"
        ))
    ).click()
    time.sleep(3)


def add_employee_basic_info(driver):
    driver.find_element(By.NAME, 'firstName').send_keys("Mm")
    driver.find_element(By.NAME, 'middleName').send_keys("M")
    driver.find_element(By.NAME, 'lastName').send_keys("Mm")

    input_field = driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    )
    input_field.clear()
    input_field.send_keys('0470')

    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    ).click()

    fake = Faker()
    username = fake.user_name()

    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    ).send_keys(username)

    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    ).send_keys("maliha@123")

    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    ).send_keys("maliha@123")

    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    ).click()
    time.sleep(10)


def fill_employee_personal_details(driver):
    driver.find_element(By.XPATH,
        "//body/div[@id='app']/div/div/div/div/div/div/div/div/form/div/div/div[2]/div[1]/div[2]/input[1]"
    ).send_keys('01234')

    driver.find_element(By.XPATH,
        "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[2]/div[1]/div[1]/div[2]/input[1]"
    ).send_keys('234567890')

    # Calendar for License Expiry
    driver.find_element(By.XPATH,
        "//i[contains(@class,'oxd-icon bi-calendar')]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH,
        "//div[@class='oxd-calendar-date' and text()='3']"
    ).click()
    time.sleep(2)

    # Nationality
    driver.find_element(By.XPATH,
        "//div[@class='oxd-select-text--after']"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH,
        "//div[@role='option']/span[text()='Indian']"
    ).click()

    # Marital Status
    driver.find_element(By.XPATH,
        "(//div[@class='oxd-select-text--after'])[2]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH,
        "//div[@role='option']/span[text()='Single']"
    ).click()
    time.sleep(2)

    # Date of Birth
    driver.find_element(By.XPATH,
        "//label[text()='Date of Birth']/following::input[1]"
    ).click()
    time.sleep(2)
    driver.find_element(By.XPATH,
        "//div[@class='oxd-calendar-date' and text()='3']"
    ).click()

    # Gender
    driver.find_element(By.XPATH,
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    ).click()

    time.sleep(2)
    driver.find_element(By.XPATH,
        "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"
    ).click()
    time.sleep(5)


def main():
    driver = init_driver()
    login(driver)
    navigate_to_add_employee(driver)
    add_employee_basic_info(driver)
    fill_employee_personal_details(driver)
    input("Press Enter to close...")
    driver.quit()


if __name__ == "__main__":
    main()
