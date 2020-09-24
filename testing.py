# Testing Selenium scraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = r"C:\Users\Arttu Lehtola\Desktop\apps\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://nvidia.com/fi-fi/geforce/graphics-cards/30-series/")
print(driver.title)

search = driver.find_element_by_class_name("oos-btn")

#print(search.get_attribute('innerHTML'))

if not search.get_attribute('innerHTML') == "Loppuunmyyty":
    print('On saatavilla!')
else:
    print("Ei ole saatavilla.")


driver.quit()


#searchableClass = r"oos-btn"
# <span class="oos-btn"> Loppuunmyyty </span>
# Hae ton sisältä arvo