# main script for dm users

# modules:
from selenium.webdriver.support.ui import Select
from main import wd_path, write_cookies
from modules import *
import pandas as pd

# function to load .csv file into the memory:
def file_read():

    file_loc = "users/users_list.csv"
    df = pd.read_csv(file_loc)

    list0 = list(df.org)
    org_list = list0

    list1 = list(df.user_email)
    user_email_list = list1

    list2 = list(df.user_role)
    user_role_list = list2

    return [org_list, user_email_list, user_role_list]

# main function for creation of the roles:
def users_bot(domain):

    for x, y, z in zip(file_read()[0], file_read()[1], file_read()[2]):
        org = x
        email = y
        role = z

        fixed_url = f"https://ttt.{domain}.xxx/{org}/organization_users"
        main_url = fixed_url
        wdpath = Service(wd_path())

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--kiosk")
        
        driver = webdriver.Firefox(service=wdpath, options=options)
        driver.get(main_url)
        
        cookies_file = "cookies.txt"
        cookies = json.load(open(cookies_file, "r"))

        for c in cookies:
            c['domain'] = f"xxx.{domain}.ttt"
            try:
                driver.add_cookie(c)
            except:
                pass
            main_url = fixed_url
            driver.get(main_url)
        time.sleep(0.5)

        # button "new user":
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/a"))).click()
        time.sleep(5)

        email = driver.find_element(By.ID, "user_email").send_keys(email)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID,
                                        "user_role_id"))).click()
        select = Select(driver.find_element(By.ID,
                                            "user_role_id"))
        select.select_by_visible_text(role)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME,
                                                "commit")))
            driver.find_element(By.NAME,
                                "commit").click()
        except:
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div[2]/div[2]/div/a"))).click()
            
    # outside the loops to quit the driver:
    driver.quit()
    print("Users created !!!")

# calling functions:
if __name__ == "__main__":
    write_cookies()
    # define parameter for domain:
    users_bot("dom")
