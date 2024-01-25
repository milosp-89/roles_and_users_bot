# main script for dm roles

# modules:
from main import wd_path, write_cookies
from modules import *

# main function to load cookies and to create roles using bot:
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
        x['domain'] = f"yyy.{domain}.xxx"
        try:
            driver.add_cookie(x)
        except:
            pass
        main_url = main_url
        driver.get(main_url)
    time.sleep(5)

    ##########################################################################
    # administrator role:
    name = "Administrator"
    # button "new role":
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/a"))).click()
    time.sleep(0.5)
    # name of the role:
    role_name = driver.find_element(By.ID, "user_role_name").send_keys(name)
    # online forms:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_45"))).click()
    # forms (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_2"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_3"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_4"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_5"))).click()
    # Destinations (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_6"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_7"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_8"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_9"))).click()
    # Form submissions and DM database (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_10"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_11"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_12"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_46"))).click()
    # Submissions errors (all 5):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_13"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_14"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_15"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_16"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_17"))).click()
    # Devices (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_18"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_19"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_20"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_21"))).click()
    # Resources (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_22"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_23"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_24"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_25"))).click()
    # Dispatches (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_26"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_27"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_28"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_29"))).click()
    # Groups (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_30"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_31"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_32"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_33"))).click()
    # Even log read:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_34"))).click()
    # Users (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_35"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_36"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_37"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_38"))).click()
    # User roles (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_39"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_41"))).click()
    # go back at top and click create button
    driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()

    ##########################################################################
    # manager role:
    name = "Manager"
    # button "new role":
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/a"))).click()
    time.sleep(0.5)
    # name of the role:
    role_name = driver.find_element(By.ID, "user_role_name").send_keys(name)
    # online forms:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_45"))).click()
    # forms (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_2"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_3"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_4"))).click()
    # Destinations (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_6"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_7"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_8"))).click()
    # Form submissions and DM database (2):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_10"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_12"))).click()
    # Submissions errors (4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_13"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_14"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_16"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_17"))).click()
    # Devices (all 4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_18"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_19"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_20"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_21"))).click()
    # Resources (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_22"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_23"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_24"))).click()
    # Dispatches (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_26"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_27"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_28"))).click()
    # Groups (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_30"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_31"))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_32"))).click()
    # Users (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_35"))).click()
    # go back at top and click create button
    driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()

    ##########################################################################
    # data entry assistant role:
    name = "Data entry assistant"
    # button "new role":
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/a"))).click()
    time.sleep(0.5)
    # name of the role:
    role_name = driver.find_element(By.ID, "user_role_name").send_keys(name)
    # online forms:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_45"))).click()
    # forms (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_2"))).click()
    # Destinations (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_6"))).click()
    # Form submissions and DM database (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_10"))).click()
    # Submissions errors (4):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_13"))).click()
    # Resources (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_22"))).click()
    # Dispatches (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_26"))).click()
    # Groups (3):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_30"))).click()
    # Users (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_35"))).click()
    # go back at top and click create button
    driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()

    ##########################################################################
    # enumerator role:
    name = "Enumerator"
    # button "new role":
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/a"))).click()
    time.sleep(0.5)
    # name of the role:
    role_name = driver.find_element(By.ID, "user_role_name").send_keys(name)
    # forms (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_2"))).click()
    # Destinations (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_6"))).click()
    # Form submissions and DM database (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_10"))).click()
    # Submissions errors (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_13"))).click()
    # Resources (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_22"))).click()
    # Users (1):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID,
                                    "user_role_permission_ids_35"))).click()
    # go back at top and click create button
    driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "commit")))
    driver.find_element(By.NAME, "commit").click()
    
    time.sleep(1)
    driver.quit()
    print(f"Roles created for organization id: {org_name} !!!")


# calling functions:
if __name__ == "__main__":
    write_cookies()
    # define parameters for org id and domain:
    roles_bot(n, "dom")
