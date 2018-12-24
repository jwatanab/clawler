
import urllib.parse
import sys
from utils import *

LIMIT = 50
INTERVAL = 50

driver = None
sys.argv.pop(0)

if len(sys.argv) != 3:
  print(("usage:   python crawler.py [username] [password] [*keywords]\n"
         "example: python crawler.py user c8can1!!0_ python3"))
  sys.exit(1)
  
username, password, *keywords = sys.argv

try:
  driver = get_logged_driver(username, password)

  tag_search_url= "https://www.instagram.com/explore/tags/{}/?hl=ja"
  
  for keyword in keywords:
    driver.get(tag_search_url.format(
      urllib.parse.quote(keyword)
    ))

    sleep()
    driver.implicitly_wait(10)

    target = driver.find_element_by_css_selector('a div img').get_attribute('class')
    driver.find_element_by_xpath(f"//img[@class='{target}']/ancestor-or-self::a").click()

    driver.find_element_by_css_selector("[role=dialog] button [aria-label=いいね！]").click()
    time.sleep(2)

    for c in range(LIMIT):
      driver.find_element_by_css_selector(".coreSpriteRightPaginationArrow").click()
      time.sleep(2)
      driver.find_element_by_css_selector("[role=dialog] button [aria-label=いいね！]").click()
      time.sleep(2)
      if c != 0 and c % INTERVAL == 0:
        time.sleep(120)
except Exception as e:
  raise e
finally:
  if driver != None:
    driver.quit()
    
