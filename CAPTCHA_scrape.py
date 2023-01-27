from selenium.webdriver.common.by import By
import time
import urllib
import login_tinder

# Function to navigate the iframes .-. we have to go deeper 
def iframe_inception(iframe_bedrock): 
    driver.switch_to.default_content()
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframes[0])
    driver.switch_to.frame(driver.find_element(By.ID, "fc-iframe-wrap"))
    if(iframe_bedrock):
       driver.switch_to.frame(driver.find_element(By.ID, "CaptchaFrame"))

# Function to hit the reload button
def reload_button():
    iframe_inception(False)
    reload_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Start over with a different challenge']")
    reload_button.click()

# Function finds the CAPTCHA img and saves it 
def save_image():
    #Saving images 
    iframe_inception(True)
    capatcha_image = driver.find_element(By.TAG_NAME, "img")
    capatcha_image_src = capatcha_image.get_attribute('src')
    now = time.strftime('%Y_%H_%M_%S')

    captcha_image_name = "captcha_images/captcha_" + now + ".png"
    urllib.request.urlretrieve(capatcha_image_src, captcha_image_name)

# The function finds the verify button and clicks it
def verify_button():
    try: 
        iframe_inception(True)
        verify_button = driver.find_element(By.XPATH,'//button[text()="Verify"]' )
        verify_button.click()
    except:
        print("verify button not found")
        return False
    else: 
        return True
    

# Function refreshes the page obsolete at the moment
def refresh_page():
    #actions.send_keys(Keys.CONTROL + Keys.F5)
    #actions.perform()
    print("nothing")

# This function is for detecting if the verify button needs to be clicked because tinder sometimes wants it after you hit the login button 
def detect_verify_button():
    verify_button()

# The main procedure for capturing the CAPTCHA. Save the image, hit the reload button, hit the verify button, repeat. 
def capture_CAPTCHA():
    save_image()
    reload_button()
    verify_button_found = verify_button()
    while(not verify_button_found):
        verify_button_found = verify_button()
    

refresh_counter = 0
driver = login_tinder.click_phone_login()
time.sleep(3)
detect_verify_button()
while(refresh_counter < 9):
    capture_CAPTCHA()
    refresh_counter += 1
    if(refresh_counter == 9):
        refresh_counter = 0
        driver.close()
        driver = login_tinder.click_phone_login()
        time.sleep(3)
        detect_verify_button()

