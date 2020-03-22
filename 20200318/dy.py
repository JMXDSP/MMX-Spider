from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing
import os
import time
import random

class main():
    def __init__(self, device, port, listValue):
        self.device = device
        self.port = port
        self.cap = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": self.device,
            # "udid": self.device,
            'newCommandTimeout': "20000",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetkeyboard": True
        }

        self.driver = webdriver.Remote("http://localhost:" + str(port) + "/wd/hub", self.cap)
        self.LISTVALUE = listValue
        self.DYH = []

    def start(self):
        self.search()
        time.sleep(3)
        for value in self.LISTVALUE:
            self.clickInput(value)
            time.sleep(1)
            self.searchClick()
            time.sleep(5)
            self.userClick()
            time.sleep(3)
            self.user()



    def search(self):
        """µã»÷ËÑË÷°´Å¥"""
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(
                    lambda driver: driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="ËÑË÷"]')):
                print(self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="ËÑË÷"]'))
                self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="ËÑË÷"]').click()
        except Exception as e:
            print('search', e)
            self.driver.tap([(9, 44), (63, 98)], 500) #±¨´íµÄÊ±ºò×Ô¶¯µã»÷

    def clickInput(self, value):
        """ËÑË÷¿òÊäÈëÄÚÈÝ"""
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView')):
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView').click()
            time.sleep(1)
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText')):
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText').send_keys(
                    value)
        except Exception as e:
            print('clickInput', e)
            # self.driver.tap([(75,50),(633,104)],500)

    def searchClick(self):
        """µã»÷ËÑË÷°´Å¥"""
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver:driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView').click();
        except Exception as e:
            print('searchClick', e)
        self.driver.tap([(624, 38), (720, 116)], 500)

    def userClick(self):
        """µã»÷ÓÃ»§tab"""
        time.sleep(1)
        try:
            self.driver.tap([(316,130),(362,162)], 500)
        except Exception as e:
            print('userClick', e)
        self.driver.tap([(241, 130), (287, 162)], 500)

if __name__ == '__main__':
    main('127.0.0.1:62025', 4723, ['ºì¾Æ', '°×¾Æ']).start()

