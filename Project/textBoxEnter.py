from selenium import webdriver
#pip install selenium
#https://github.com/rivermont/spidy/    𝗕𝗲𝗮𝘂𝘁𝗶𝗳𝘂𝗹 𝗦𝗼𝘂𝗽 𝟰
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Ensure chromedriver.exe is installed if using Chrome)
driver = webdriver.Firefox()  # Use webdriver.Chrome() for Chrome
overflow_input = "10" * 10000  # Adjust length based on target application
try:
    # Open the local test login page
    driver.get("https://the-internet.herokuapp.com/login")  # Adjust based on your local server

    # Wait for the input fields to load
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    # Type into the fields
    username_field.send_keys(overflow_input)
    password_field.send_keys(overflow_input)

    # Locate and click the login button
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    # Wait for login process
    wait.until(EC.url_changes(driver.current_url))
    print("✅ Login attempt completed.")

except Exception as e:
    print(f"❌ Error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
