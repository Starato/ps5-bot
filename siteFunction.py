from telnetlib import STATUS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "/Library/chromedriver"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 10)

def bestbuy(bestBuy):
    try:
        driver.get(bestBuy)

        title = driver.find_element(By.XPATH, "//div[@class='sku-title']//h1")
        price = driver.find_element(By.XPATH, "//span[@class='sr-only']")
        status = driver.find_element(By.XPATH, "//div[@class='fulfillment-add-to-cart-button']//button")

        print(f"{title.text} {price.text} {status.text}")
    except Exception as e:
        print(f"Error: {e}.")
        driver.quit()
    finally:
        time.sleep(10)
        driver.quit()
   
def amazon(amazon):
    try:
        driver.get(amazon)

        title = driver.find_element(By.XPATH, "//div[@id='titleSection']/h1//span")
        price = driver.find_element(By.ID, "priceblock_ourprice")
        if price == None:
            return print("Item does not have a price, most likely sold out at the moment.")

        print(f"{title.text} {price.text}")
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
    finally:
        time.sleep(10)
        driver.quit()