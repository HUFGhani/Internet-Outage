from selenium import webdriver
import time


def disconnect():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                              options=chrome_options)  # Optional argument, if not specified will search path
    driver.get('http://192.168.0.1/0000016400/gui/#/main/')
    driver.find_element_by_name("Go To Advanced Settings Tile").click()
    driver.find_element_by_name("Broadband Tile").click()
    time.sleep(5)
    Password = driver.find_element_by_name("password")
    Password.send_keys("hg6thbtq")
    driver.find_element_by_id("submitButton").click()
    time.sleep(5)
    driver.find_element_by_name("Connect Button").click()
    driver.quit()



def connect():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',
                              options=chrome_options)  # Optional argument, if not specified will search path
    driver.get('http://192.168.0.1/0000016400/gui/#/main/')
    driver.find_element_by_name("Go To Advanced Settings Tile").click()
    driver.find_element_by_name("Broadband Tile").click()
    time.sleep(5)
    Password = driver.find_element_by_name("password")
    Password.send_keys("hg6thbtq")
    driver.find_element_by_id("submitButton").click()
    time.sleep(5)
    driver.find_element_by_name("Connect Button").click()
    driver.quit()


if __name__ == '__main__':
    main()