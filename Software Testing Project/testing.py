from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pyautogui 

driver = webdriver.Chrome()

def valid_mainpage(driver):
    driver.get("https://irctc.co.in")
    driver.fullscreen_window()

    from_station = driver.find_element(By.XPATH , '//*[@id="origin"]/span/input')
    from_station.send_keys("KSR BENGALURU - SBC")

    to_station = driver.find_element(By.XPATH , '//*[@id="destination"]/span/input')
    to_station.send_keys("KOLKATA - KOAA (Howrah / Kolkata)")

    journey_date = driver.find_element(By.XPATH , '//*[@id="jDate"]/span/input')

    search = driver.find_element(By.XPATH , '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div[1]/button')
    search.click()

def pnr_status(driver):
    driver.get("https://irctc.co.in")
    time.sleep(1)
    driver.fullscreen_window()
    pnr_link = driver.find_element(By.XPATH , '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/a')
    pnr_link.click()

def vacancy_list(driver):
    driver.get("https://irctc.co.in")
    time.sleep(10)
    driver.fullscreen_window()
    char_link = driver.find_element(By.XPATH , '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/a')
    char_link.click()

def cookies_irctc(driver):
    driver.get("https://irctc.co.in")
    driver.fullscreen_window()
    cookies = driver.get_cookies() 

    for cookie in cookies:
        print(f"Name: {cookie['name']}")
        print(f"Value: {cookie['value']}")
        print(f"Domain: {cookie['domain']}")
        print(f"Path: {cookie['path']}")
        print(f"Expiry: {cookie['expiry'] if 'expiry' in cookie else 'Session cookie'}") 
        print(f"Secure: {cookie['secure']}")
        print(f"HttpOnly: {cookie['httpOnly']}")
        print(f"SameSite: {cookie['sameSite']}")

def reservation_chart(driver):
    driver.get("https://www.irctc.co.in/online-charts/")
    driver.fullscreen_window()
    time.sleep(5)
    pyautogui.moveTo(336,  411)
    pyautogui.leftClick()
    pyautogui.write("22201 - DURONTO EXPRESS")
    pyautogui.press("Enter")
    time.sleep(5)
    pyautogui.moveTo(301 , 574)
    pyautogui.leftClick()
    pyautogui.write("PURI (PURI)")
    pyautogui.press("Enter")
    time.sleep(1)
    get_info = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/div[1]/div/div/div/div/div[2]/button')
    get_info.click()

def invalidreservation_chart(driver):
    driver.get("https://www.irctc.co.in/online-charts/")
    driver.fullscreen_window()
    time.sleep(30)
    pyautogui.moveTo(336,  411)
    pyautogui.leftClick()
    pyautogui.write("22201 - ABC")
    pyautogui.press("Enter")
    time.sleep(20)
    pyautogui.moveTo(301 , 574)
    pyautogui.leftClick()
    pyautogui.write("PURI (PURI)")
    pyautogui.press("Enter")
    time.sleep(20)
    get_info = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/div[1]/div/div/div/div/div[2]/button')
    get_info.click()


def invalid_mainpage(driver):
    driver.get("https://irctc.co.in")
    driver.fullscreen_window()

    from_station = driver.find_element(By.XPATH , '//*[@id="origin"]/span/input')
    from_station.send_keys("XYZ BENGALURU - SBC")

    to_station = driver.find_element(By.XPATH , '//*[@id="destination"]/span/input')
    to_station.send_keys("KOLKATA - KOAA (Howrah / Kolkata)")

    journey_date = driver.find_element(By.XPATH , '//*[@id="jDate"]/span/input')

    search = driver.find_element(By.XPATH , '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div[1]/button')
    search.click()


def Website(driver):
    driver.get("https://irctc.co.in")

def Scroll(driver):
    driver.get("https://irctc.co.in")

    driver.fullscreen_window()

    time.sleep(30)

    driver.execute_script("window.scrollTo(0 , 1000)")


#Website(driver)
# reservation_chart(driver)
#cookies_irctc(driver)
#vacancy_list(driver)
# pnr_status(driver)
#valid_mainpage(driver)
#invalid_mainpage(driver)
#invalidreservation_chart(driver)

# Scroll(driver)

time.sleep(10)