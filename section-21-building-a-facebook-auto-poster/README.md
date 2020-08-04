# Section 21: Building A Facebook Auto Poster
## Lesson overview
- Learn about auto post facebook
### Coding
    ```
    from selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.common.exceptions import NoSuchElementException

    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    a = driver.find_element_by_id('email')
    a.send_keys('cuonglieu3256@gmail.com')
    b = driver.find_element_by_id('pass')
    b.send_keys('khoa03052000')
    c = driver.find_element_by_id('loginbutton')
    c.click()
    post_box = driver.find_element_by_xpath("//*[@name='xhpc_message']")
    time.sleep(5)
    post_box.click()
    time.sleep(5)
    post_box.send_keys("Testing using Name not ID.Selenium is easy.")
    time.sleep(5)
    post_it = driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
    post_it.click()
    ```