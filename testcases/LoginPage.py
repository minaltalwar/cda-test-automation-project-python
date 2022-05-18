def loginSession(loginURL, UName, PWord):
    import time
    from selenium import webdriver

    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    driver.get(loginURL)
    driver.maximize_window()

    btnProceed = driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]")

    btnProceed.click()
    txtusername = driver.find_element(By.ID, "username")
    txtpassword = driver.find_element(By.ID, "password")
    time.sleep(1)
    txtusername.send_keys(UName + Keys.ENTER)
    txtpassword.send_keys(PWord + Keys.ENTER)
    time.sleep(20)
    cookies = driver.get_cookies()
    session = cookies[0]['value']
    sessionID = 'SESSION=' + session
    return sessionID