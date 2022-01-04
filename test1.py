from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='D:\\exefile\\chromedriver.exe')
driver.get("http://automationpractice.com/index.phpery=t+shirt&submit_search=")
assert "Search - My Store" in driver.title
elem = driver.find_element("search_query")
elem.clear()
elem.send_keys("t  shirt")
elem.send_keys(Keys.RETURN)
assert "no results found" not in driver.page_source
driver.quit()