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
        """点击搜索按钮"""
        # 等待一秒
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(
                    lambda driver: driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]')):
                print(self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]'))
                self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
        except Exception as e:
            print('search', e)
            self.driver.tap([(9, 44), (63, 98)], 500) #报错的时候自动点击

    def clickInput(self, value):
        """搜索框输入内容"""
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9d')):
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9d').click()
                time.sleep(2)
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9d').send_keys(value)
        except Exception as e:
            print('clickInput', e)

    def searchClick(self):
        """点击搜索按钮"""
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver:driver.find_element_by_id('com.ss.android.ugc.aweme:id/d_b')):
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/d_b').click()
        except Exception as e:
            print('searchClick', e)

    def userClick(self):
        """点击用户tab"""
        time.sleep(1)
        try:
            self.driver.tap([(241,130),(287,162)], 500)
            time.sleep(1)
            # self.driver.tap([(241, 130), (287, 162)], 500)
            # self.driver.find_element_by_xpath(
            #     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').click()
        except Exception as e:
            print('userClick', e)

    def user(self):
        """循环执行点击抖音号"""
        time.sleep(5)
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').click()

        try:
            while True:
                for i in range(1, 10):
                    self.userInfo(i)
                    time.sleep(3)
                    self.clickVideo()
                self.swipe_up(500, 1, 'user')
                if "暂时没有更多了" in self.driver.page_source:
                    print('用户暂时没有更多了')
                    break
        except Exception as e:
            print('user',e)

    def userInfo(self, i):
        """点击抖音号"""
        time.sleep(1)
        try:
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[9]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i)):
                try:
                    dy = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i).text
                    if dy not in self.DYH:
                        self.DYH.append(dy)
                        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i).click()
                except Exception as e:
                    print('userInfo2', e)
        except Exception as e:
            print('userInfo1', e)

    def clickVideo(self):
        """点击视频信息"""
        time.sleep(1)
        try:
            for i in range(1, 5):
                try:
                    if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="视频%s"]' % i)):
                        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="视频%s"]' % i).click()
                        break
                except Exception as e:
                    print('clickVideo', e)

            while True:
                time.sleep(3)
                self.driver.tap([(673,878)], 500) # 点击评论
                time.sleep(5)
                try:
                    i = True
                    page_source = self.driver.page_source
                    if "评论并转发" in page_source:  # 没有评论 將自动打开的评论框关闭
                        print('当前视频没有评论')
                        i = False
                        self.driver.tap([(0, 38), (720, 1079)], 500)

                    if "暂无评论" in page_source:  # 没有评论 关闭评论窗
                        print('暂无评论')
                        i = False
                        # self.driver.tap([(0, 38)(720, 1079)], 500)
                        self.driver.find_element_by_xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView').click()
                    print(i)
                except Exception as e:
                    i = False
                if i:
                    while True:
                        self.swipe_up(name='clickVideo1')
                        time.sleep(1)
                        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView
                        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView
                        try:
                            pl = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[9]/android.widget.TextView').text
                        except Exception as e:
                            pl = ""
                        if "暂时没有更多了" in self.driver.page_source or "暂时没有更多了" in pl:  # 评论到底
                            print('暂时没有更多了')
                            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
                            break
                    time.sleep(5)
                    self.swipe_up(t=100,name='clickVideo2')

                if "没有更多了" in self.driver.page_source:
                    self.driver.tap([(34, 79.9)], 500) # 关闭视频
                    break


                # 673 878

        except Exception as e:
            print(e)

    # 向上滑动
    def swipe_up(self, t=500, n=1, name=""):
        """
        :param t: 滑动时长
        :param n: 滑动次数
        :return: 模拟滑动
        """
        try:
            print(name)
            s = self.driver.get_window_size()
            x1 = s['width'] * 0.5  # x坐标
            y1 = s['height'] * 0.75  # 起点y坐标
            y2 = s['height'] * 0.25  # 终点y坐标
            for i in range(n):
                self.driver.swipe(x1 + random.randint(0, 100), y1 + random.randint(0, 100), x1 + random.randint(0, 100),
                                  y2 + random.randint(0, 100), t)
        except Exception as e:
            print('swipe_up', e)
            time.sleep(1)
            self.swipe_up()


if __name__ == '__main__':
    main('127.0.0.1:62025', 4723,['红酒','戒指', '旅游', '就业', '考研', '环境','人工智能','商业','白酒']).start()