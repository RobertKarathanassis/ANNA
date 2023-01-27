from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def click_phone_login(): 
    # init selenium
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
     # Variables   
    URL_tinder = "https://tinder.com/"
    # logging in 
    driver.get(URL_tinder)
    driver.fullscreen_window()
    decline_cookies_button = driver.find_element(By.XPATH,'//div[text()="I decline"]' )
    decline_cookies_button.click()
    # I don't know what is wrong with this login/phone button but sometimes it just doesn't love life
    # TLDR loop till it works. Sloppy but hey
    login_button_found = False
    while(not login_button_found):
        try:
            login_button = driver.find_element(By.XPATH, '//div[text()="Log in"]')
            login_button.click()
        except: 
            print("Login button 404")
        else: 
            login_button_found = True
    # I don't know what is wrong with this login/phone button but sometimes it just doesn't love life
    # TLDR loop till it works. Sloppy but hey
    phone_button_found = False
    while(not phone_button_found):
        try:
            phone_login_button = driver.find_element(By.XPATH,'//div[text()="Log in with phone number"]' )
            phone_login_button.click() 
        except: 
            print("Phone button 404")
        else: 
            phone_button_found = True

    return driver