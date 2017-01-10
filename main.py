# -*- coding:utf-8 -*-
from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.quit()
