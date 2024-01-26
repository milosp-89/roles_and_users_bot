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
