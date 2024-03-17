from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


random_email = generate_random_string() + '@example.com'
random_first_name = "Ezz"
random_last_name = "Eldin"
random_address = generate_random_string()
random_city = generate_random_string()
random_zip = str(random.randint(10000, 99999))
phone_number = "+2011495162997"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.get("http://demostore.supersqa.com/")
    driver.find_element(By.LINK_TEXT, "My account").click()
    driver.find_element(By.ID, "username").send_keys("fakename")
    driver.find_element(By.ID, "password").send_keys("fakepassword")
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.woocommerce-error li')))
    print("Test Case #1 (Invalid Login): Passed")

    driver.find_element(By.ID, "reg_email").send_keys(random_email)
    driver.find_element(By.ID, "reg_password").send_keys("Admin@1234")
    driver.find_element(By.NAME, 'register').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    print("Test Case #2 (Registration): Passed")

    driver.find_element(By.LINK_TEXT, "Log out").click()

    driver.find_element(By.ID, "username").send_keys(random_email)
    driver.find_element(By.ID, "password").send_keys("Admin@1234")
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    print("Test Case #3 (Login with Registered User): Passed")

    driver.get("http://demostore.supersqa.com/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_to_cart_button"))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".added_to_cart"))).click()
    print("Test Case #4 (Add to Cart): Passed")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))).click()
    assert "Checkout" in driver.find_element(By.TAG_NAME, "h1").text
    print("Test Case #5 (Proceed to Checkout): Passed")

    driver.find_element(By.ID, "billing_first_name").send_keys(random_first_name)
    driver.find_element(By.ID, "billing_last_name").send_keys(random_last_name)
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Germany")
    driver.find_element(By.ID, "billing_address_1").send_keys(random_address)
    driver.find_element(By.ID, "billing_city").send_keys(random_city)
    Select(driver.find_element(By.ID, "billing_state")).select_by_visible_text("Berlin")
    driver.find_element(By.ID, "billing_postcode").send_keys(random_zip)
    driver.find_element(By.ID, "billing_phone").send_keys(phone_number)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "place_order"))).click()
    confirmation_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-order-received"))
    )
    assert "Invalid payment method." in confirmation_message.text
    print("Test Case #6 (Place Order): Passed")

finally:
    driver.quit()
