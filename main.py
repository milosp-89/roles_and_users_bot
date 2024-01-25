# main script for web driver and cookies


# modules:
from modules import *


# function for web driver path
def wd_path():

    path = "wdriver/geckodriver.exe"
    return path


# function to log in and fetch cookies:
def login_and_fetch_cookies(email, password, domain):

    login_url = f"https://devicemagic.{domain}.icrc.org/users/login"
    wdpath = Service(wd_path())

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--kiosk")

    driver = webdriver.Firefox(service=wdpath, options=options)
    driver.get(login_url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "user_remember_me_1")))
    driver.find_element(By.ID, "user_remember_me_1").click()

    mail_enter = driver.find_element(By.ID, "user_email")
    mail_enter.send_keys(email)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "user_password")))
    pswd_enter = driver.find_element(By.ID, "user_password")
    pswd_enter.send_keys(password)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()

    return driver


# function to write fetched cookies:
def write_cookies():

    cookies_file_location = "cookies.txt"
    # define parameters for email, password and domain (ext or uat):
    driver = login_and_fetch_cookies("mpopovic@icrc.org",
                                     "ICRCmp1989",
                                     "ext")
    time.sleep(0.5)
    cookies_after_login = driver.get_cookies()
    json.dump(cookies_after_login,
              open(f"{cookies_file_location}", "w"))
    driver.quit()
