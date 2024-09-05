import hashlib
import platform

# Function to generate a unique device ID
def get_device_id():
    # Example: Using platform and hashlib to generate a device ID based on platform details
    platform_info = platform.uname()
    device_info = f"{platform_info.system}-{platform_info.node}-{platform_info.processor}".encode()
    device_id = hashlib.sha256(device_info).hexdigest()
    return device_id




# Get the device ID of the current machine
current_device_id = get_device_id()
print(current_device_id)
# List of allowed device IDs (replace with actual allowed IDs)
allowed_device_ids = [
    "f39ae3683a66c3f3b258b3c8ab3ef0d9780a7bbbaf432bef2f960be3143487c8",
    "d9e451e17e7558c05f5c3617c9448ec792765a3e8721f32faa42f2a45883990c"    # Example device ID
    # Add more allowed device IDs as needed
]
# Check if the current device is allowed to run the script
if current_device_id in allowed_device_ids:
    print("Device authorized. Proceeding with script execution.")
    
    # Put your existing script code here...
    # This could include login logic, web scraping, etc.

    # For example:
    import time
    from itertools import chain
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException
    from cryptography.fernet import Fernet
    import getpass

    # Function to log in to Twitter (x.com)
    def login_to_twitter(driver, username, password):
        driver.get('https://x.com/i/flow/login')
        time.sleep(5)  # Wait for the login page to load

        try:
            # Enter username
            username_input = driver.find_element(By.NAME, 'text')
            username_input.send_keys(username)
            username_input.send_keys(Keys.RETURN)
            time.sleep(5)  # Wait for the password input to appear

            # Enter password
            password_input = driver.find_element(By.NAME, 'password')
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            time.sleep(5)  # Wait for the login process to complete
        except Exception as e:
            print("An error occurred during login:", str(e))
            driver.quit()
            return False

        return True

    # Read keywords from file
    partition = input("Enter Partition Letter: ")
    keyWordsFile = open(f'{partition}://Teg.Whts//telegram//keywords.txt', encoding='utf-8')
    keyWords = keyWordsFile.readlines()

    # Read usernames and passwords from log.txt
    with open('log.txt', 'r') as log_file:
        credentials = log_file.readlines()

    # Process each username and password pair
    for i in range(0, len(credentials), 2):
        username = credentials[i].strip()
        password = credentials[i + 1].strip()

        # Initialize WebDriver for each login attempt
        driver = webdriver.Chrome()

        # Perform login
        if login_to_twitter(driver, username, password):
            for keyWord in keyWords:
                driver.get('https://x.com/search-advanced/')
                time.sleep(5)  # Wait for the page to load

                try:
                    # Wait for the search input fields to be visible
                    searchKeysInput = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, 'allOfTheseWords'))
                    )

                    searchPhraseInput = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, 'thisExactPhrase'))
                    )
                except TimeoutException as e:
                    print(f"An error occurred while searching for element: {str(e)}")
                    continue

                searchPhraseInput.clear()
                searchPhraseInput.send_keys("t.me/joinchat")
                time.sleep(2)
                searchKeysInput.clear()
                searchKeysInput.send_keys(keyWord.strip())
                time.sleep(2)

                try:
                    searchKeysInput.send_keys(Keys.RETURN)
                    time.sleep(5)  # Wait for the search results to load
                except Exception as e:
                    print("An error occurred during search:", str(e))

                print(keyWord)

                for i in range(1, 15):
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    time.sleep(2)
                    try:
                        # Find all article elements containing links
                        links = driver.find_elements(By.TAG_NAME, "a")
                        urls2 = WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
                        )
                        results = set(links + urls2)  # Use set to avoid duplicates
                    except TimeoutException as e:
                        print(keyWord + " لا يوجد نتائج لهذه الكلمة ")
                        break

                    for i, url2 in enumerate(results, start=1):
                        extracteddata = url2.get_attribute("title") or ""
                        extracteddata += url2.get_attribute("href") or ""

                        WAString = "join"
                        WAString2 = "//t.co/"

                        if WAString in extracteddata:
                            with open(f'{partition}://Teg.Whts//telegram//extractedTEGLinks.txt', 'a', encoding='utf-8') as extractedLinks:
                                print('This link number is ' + str(i) + '==' + extracteddata)
                                extractedLinks.write(extracteddata + "\n")
                        elif WAString2 in extracteddata:
                            with open(f'{partition}://Teg.Whts//telegram//extractedTEGLinks2.txt', 'a', encoding='utf-8') as extractedLinks:
                                print('This link number is ' + str(i) + '==' + extracteddata)
                                extractedLinks.write(extracteddata + "\n")

        # Close the WebDriver
        driver.quit()

    # Close files
    keyWordsFile.close()

    # Wait for user input before exiting to keep the console window open
    input("Press Enter to exit...")

else:
    print("Unauthorized device. Script execution aborted.")