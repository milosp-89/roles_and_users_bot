# main script for dm roles

# modules:
from main import wd_path, write_cookies
from modules import *

# function for creation of the roles:
def create_role(web_driver,
                role_name,
                permissions):

    WebDriverWait(web_driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[2]/div[2]/div/a"))).click()
    time.sleep(0.5)

    web_driver.find_element(By.ID,
                            "user_role_name").send_keys(role_name)

    for p in permissions:
        WebDriverWait(web_driver, 15).until(
            EC.element_to_be_clickable((By.ID, f"user_role_permission_ids_{p}"))).click()

    web_driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")

    WebDriverWait(web_driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    web_driver.find_element(By.NAME, "commit").click()

# main function to load cookies and to create roles using the bot:
def roles_bot(org_name, domain):

    main_url = f"https://ttt.{domain}.xxx/{org_name}/user_roles"
    wdpath = Service(wd_path())

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--kiosk")

    driver = webdriver.Firefox(service=wdpath, options=options)
    driver.get(main_url)

    cookies_file = "cookies.txt"
    cookies = json.load(open(cookies_file, "r"))
    for x in cookies:
        x['domain'] = f"ttt.{domain}.xxx"
        try:
            driver.add_cookie(x)
        except:
            pass
        main_url = main_url
        driver.get(main_url)
    time.sleep(5)

    # roles:

    # administrator role:
    create_role(driver, "Administrator", [45, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                          11, 12, 46, 13, 14, 15, 16, 17,
                                          18, 19, 20, 21, 22, 23, 24, 25,
                                          26, 27, 28, 29, 30, 31, 32, 33,
                                          34, 35, 36, 37, 38, 39, 41])

    # manager role:
    create_role(driver, "Manager", [45, 2, 3, 4, 6, 7, 8, 10, 12, 13,
                                    14, 16, 17, 18, 19, 20, 21, 22, 23,
                                    24, 26, 27, 28, 30, 31, 32, 35])

    # data entry assistant role:
    create_role(driver, "Data entry assistant", [45, 2, 6, 10, 13, 22, 26, 30, 35])

    # enumerator role:
    create_role(driver, "Enumerator", [2, 6, 10, 13, 22, 35])

    time.sleep(1)
    driver.quit()
    print(f"Roles created for organization id: {org_name} !!!")


# calling functions:
if __name__ == "__main__":
    write_cookies()
    # define parameters for org id and domain::
    roles_bot(int, "dom")
