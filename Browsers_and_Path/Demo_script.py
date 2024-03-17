from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

def generate_random_email(domain='example.com', length=10):
    """Generate a random email address and username."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    full_email = random_string + '@' + domain
    username = random_string
    return full_email, username

# Generate a unique email and username for registration
random_email, random_username = generate_random_email(domain='test.com')

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

try:
    # Open the demo store website
    driver.get("http://demostore.supersqa.com/")
    time.sleep(3)

    # Navigate to My Account for login attempt
    my_account_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
    my_account_link.click()

    # Attempt to log in with a non-existing account
    u_name_field = driver.find_element(By.ID, "username")
    u_name_field.send_keys("fakename")

    p_field = driver.find_element(By.ID, "password")
    p_field.send_keys("aaaaaaa")

    # Click login button
    login_btn = driver.find_element(By.NAME, 'login')
    login_btn.click()
    time.sleep(3)

    # Get and assert the displayed error
    first_error_elm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.woocommerce-error li')))
    displayed_error_text = first_error_elm.text

    expected_error = "Error: The username fakename is not registered on this site. If you are unsure of your username, try your email address instead."
    assert expected_error in displayed_error_text, "Displayed error is not as expected."
    print("Test Case #1 (Invalid Login): Passed")

    # Navigate back to My Account for registration
    driver.get("http://demostore.supersqa.com/my-account/")

    # Fill the registration form with the generated email
    email_field = driver.find_element(By.ID, "reg_email")
    email_field.send_keys(random_email)

    password_field = driver.find_element(By.ID, "reg_password")
    password_field.send_keys("Admin@1234")  # Use a safe, test-specific password

    # Click the register button
    register_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button')
    register_btn.click()

    # Wait for registration to complete and assert on the logout link
    logout_link = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]/a'))
    )
    assert "Log out" in logout_link.text, "Log out link was not found after registration."
    print("Test Case #2 (Registration): Passed")

    # Click on the logout link
    logout_link.click()

    # Log in with the new user credentials
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
    username_field.send_keys(random_email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Admin@1234")

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
    login_button.click()

    # Assert on the logout link again to verify that login was successful
    logout_link = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]/a'))
    )
    assert "Log out" in logout_link.text, "Log out link was not found after re-login."
    print("Test Case #3 (Login with Registered User): Passed")

    # Test Case #4 (Add to Cart and Verify Cart)
    # Navigate to Home
    home_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[1]/a'))
    )
    home_button.click()

    # Add to Cart from the list of items
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/ul/li[1]/a[2]'))
    )
    add_to_cart_button.click()

    # Wait for the 'View Cart' button to be visible
    view_cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/ul/li[1]/a[3]'))
    )

    # Assert 'View Cart' button is visible
    assert view_cart_button.is_displayed(), "View Cart button is not displayed after adding to cart."

    # Navigate to Cart to confirm the item was added
    view_cart_button.click()

    # Assert the presence of 'Apply Coupon' button in the cart
    apply_coupon_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'apply_coupon'))
    )
    assert apply_coupon_button.is_displayed(), "Apply Coupon button is not displayed in the cart."

    print("Test Case #4 (Add to Cart): Passed")

finally:
    driver.quit()
