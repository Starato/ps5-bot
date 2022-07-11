from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.message import EmailMessage
import siteFunction

def main():

    #Notes: Only works with websites listed below    
    # enter full website url here
    # comment out the website you will not be using
    amazon = "https://www.amazon.com/PlayStation-5-Console/dp/B09DFCB66S/ref=sr_1_3?crid=UI9WZ1J3FU8T&keywords=playstation+5&qid=1657579758&sprefix=playstation+5%2Caps%2C98&sr=8-3"
    bestBuy = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
    gameStop = "https://www.gamestop.com/"
    nintendo = "https://www.nintendo.com/"
    # newegg = ""
    target = "https://www.target.com/"
    walmart = "https://www.walmart.com/"

    websites = {amazon, bestBuy, gameStop, nintendo, target, walmart}

    for site in websites:
        siteTitle = site.split(".")

        match siteTitle[1]:
            case "amazon":
                siteFunction.amazon(amazon)
            case "bestbuy":
                siteFunction.bestbuy(bestBuy)
            case "gamestop":
                print("This is gamestop")
            case "nintendo":
                print("this is nintendo")
            case "target":
                print("this is target")
            case "walmart":
                print("This is walmart")
            case _:
                print("none found")

main()
