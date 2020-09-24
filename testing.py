# Testing Selenium scraping
from selenium import webdriver

PATH = r"C:\Users\Arttu Lehtola\Desktop\apps\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://is.fi")
print(driver.title)
driver.quit()

