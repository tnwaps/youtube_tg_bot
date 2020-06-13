from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from selenium import webdriver
from telegram.ext import Filters
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram.ext import MessageHandler
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests

token = 'lololo'

driver = webdriver.Chrome()


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if 'youtube' in text or 'youtu.be' in text:
        driver.get(text)
        browser.switch_to.frame(browser.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    
    
    if(text=='!'):
        driver.get()


     


def main():
    updater = Updater(
        token = token,
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

