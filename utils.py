from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
import re

def sleep():
  time.sleep(3)

def save(driver, fn = 'test.png'):
  sleep()
  driver.save_screenshot(fn)

def get_logged_driver(username, password):
  try:
    options = Options()

    for e in ('--headless', '--no-sandbox', '--disable-gpu', '--window-size=1280,1024', '--disable-setuid-sandbox'):
      options.add_argument(e)

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

    sleep()

    username_field = driver.find_element_by_css_selector('#react-root [name=username]')
    username_field.send_keys(username)

    password_field = driver.find_element_by_css_selector('#react-root [name=password]')
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    sleep()

    try:
      driver.find_element_by_css_selector(f"nav a[href*='{username}']")
    except:
      raise "Could not log in"

  except Exception as e:
    driver.quit()
    raise e

  return driver
