from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def generate_random_email(domain='example.com', length=10):
    """Generate a random email address."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    full_email = random_string + '@' + domain
    return full_email

random_email = generate_random_email(domain='test.com')

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

    # Log out
    driver.find_element(By.LINK_TEXT, "Log out").click()

    driver.find_element(By.ID, "username").send_keys(random_email)
    driver.find_element(By.ID, "password").send_keys("Admin@1234")
    driver.find_element(By.NAME, 'login').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
    print("Test Case #3 (Login with Registered User): Passed")

    driver.get("http://demostore.supersqa.com/")
    add_to_cart_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".add_to_cart_button"))
    )
    if add_to_cart_buttons:
        add_to_cart_buttons[0].click()

        view_cart_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".added_to_cart"))
        )
        view_cart_link.click()
        print("Test Case #4 (Add to Cart): Passed")

        quantity_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".quantity input"))
        )
        quantity_input.clear()
        quantity_input.send_keys("6")
        driver.find_element(By.NAME, "update_cart").click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
        ).click()

        checkout_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert "Checkout" in checkout_heading.text
        print("Test Case #5 (Proceed to Checkout): Passed")
    else:
        print("No Add to Cart buttons found.")

finally:
    # Close the browser window
    driver.quit()
