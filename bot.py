from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Library/chromedriver"
driver = webdriver.Chrome(PATH)

def bestbuy(bestBuy):
    try:
        driver.get(bestBuy)

        title = driver.find_element(By.XPATH, "//div[@class='sku-title']//h1")
        price = driver.find_element(By.XPATH, "//span[@class='sr-only']")
        status = driver.find_element(By.XPATH, "//div[@class='fulfillment-add-to-cart-button']//button")

        print(f"{title.text} {price.text} {status.text}")
        time.sleep(5)
        driver.quit()
    except Exception as e:
        print(f"Error: {e}.")
def main():
    bestBuy = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
    bestbuy(bestBuy)
main()
