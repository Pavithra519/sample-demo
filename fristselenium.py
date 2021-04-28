from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.facebook.com")
driver.find_element_by_xpath("//*[@id='email']").send_keys('pavithra')
print("Application title is",driver.title)
print("Application url is",driver.current_url)
driver.quit()
driver.close()
