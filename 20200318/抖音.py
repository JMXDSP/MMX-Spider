from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing
import os
import time
import random


class automation:
    def __init__(self, device, port, listValue):
        self.device = device
        self.port = port
        self.cap = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": self.device,
            #"udid": self.device,
            'newCommandTimeout': "20000",
            # "automationName": "uiautomator2",
            # 'ANDROID_UIAUTOMATOR': 'uiautomator2',
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
        try:
            time.sleep(2)
            self.search()  # 点击搜索
            time.sleep(2)
            for v in self.LISTVALUE:
                self.inputValue(v)  # 输入内容
                time.sleep(2)
                self.baiduClick()  # 点击搜索
                time.sleep(5)
                self.userClick()  # 点击用户tab
                time.sleep(2)
                self.users()  # 点击用户抖音号
                time.sleep(5)
        except Exception as e:
            print('start', e)

    # 点击搜索
    def search(self):
        # 等待一秒
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver:driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]')):
                self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="搜索"]').click()
        except Exception as e:
            print('search', e)
            self.driver.tap([(9, 44), (63, 98)], 500)

    # 输入内容
    def inputValue(self, value):
        time.sleep(1)
        try:
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View')):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View').click()

            if WebDriverWait(self.driver,60).until(lambda driver:driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText')):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText').send_keys(value)
        except Exception as e:
            print('inputValue', e)

    # 点击搜索框
    def searchClick(self):
        time.sleep(1)
        try:
            if WebDriverWait(self.driver, 60).until(lambda driver:driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView').click();
        except Exception as e:
            print('searchClick', e)

    # 点击用户tab
    def userClick(self):
        time.sleep(1)
        try:
            self.driver.tap([(336, 146)], 500)
        except Exception as e:
            print('userClick', e)
            time.sleep(1)
            self.userClick()

    # 点击用户抖音号
    def users(self):
        time.sleep(1)
        try:
            while True:
                for i in range(1, 10):
                    self.userInfo(i)
                self.swipe_up(500, 1)
                if "暂时没有更多了" in self.driver.page_source:
                    print('用户暂时没有更多了')
                    break
        except Exception as e:
            print('users', e)

    def userInfo(self, i):
        try:
            # 	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
            if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView' % i)):
                try:
                    dy = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView' % i).text
                    print(dy)
                    if dy not in self.DYH:
                        try:
                            self.DYH.append(dy)
                            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView' % i).click()
                            time.sleep(5)
                            self.swipes()  # 滑动做品
                            time.sleep(2)
                            self.returnWork()  # 返回做品
                            time.sleep(5)
                        except Exception as e:
                            print('--', e)
                except Exception as e:
                    print('-', e)
            else:
                print('页面没有这个元素')
        except Exception as e:
            print('----', e)
            time.sleep(1)
            self.userInfo(i)

    # 点击作品tab
    def works(self):
        try:
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.TextView
            # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.TextView
            for i in range(1, 5):
                if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[%s]/android.widget.RelativeLayout/android.widget.TextView' % (
                                i,))):
                    zp = self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[%s]/android.widget.RelativeLayout/android.widget.TextView' % (
                            i,)).text

                    print(zp)
                    if '作品' in str(zp):
                        self.driver.find_element_by_xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[%s]/android.widget.RelativeLayout/android.widget.TextView' % (
                                i,)).click()
                        break
                    else:
                        print(i, '没有')
                        time.sleep(2)
                else:
                    print('没有==')
        except Exception as e:
            print('works', e)

    # 滑动作品
    def swipes(self):
        try:
            while True:
                self.swipe_up(500, 1)
                if "没有更多了" in self.driver.page_source:
                    print('视频暂时没有更多了')
                    break
                # time.sleep(1)
        except Exception as e:
            print('swipes', e)

    # 返回作品
    # def returnWork(self):
    #     try:
    #         self.driver.find_element_by_xpath('	//android.widget.ImageView[@content-desc="返回"]').click()
    #     except Exception as e:
    #         print('returnWork', e)

    # 切换成百度输入法
    # def baidu(self):
    #     time.sleep(1)
    #     try:
    #         os.system("adb -s %s shell ime set com.baidu.input/.ImeService" % (self.device,))
    #     except Exception as e:
    #         print('baidu', e)

    # 点击百度搜索按钮
    # def baiduClick(self):
    #     time.sleep(1)
    #     try:
    #         # self.driver.tap([(664, 1217)], 200)
    #         if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_id('com.ss.android.ugc.aweme:id/dt2')):
    #             self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/dt2').click()
    #     except Exception as e:
    #         print('baiduClick', e)
    #         time.sleep(1)
    #         self.baiduClick()

    # 切换成appium输入法
    # def appium(self):
    #     time.sleep(1)
    #     try:
    #         os.system('adb -s %s shell ime set io.appium.settings/.UnicodeIME' % (self.device,))
    #     except Exception as e:
    #         print('appium', e)

    # 向上滑动
    #def swipe_up(self, t=500, n=1):
    #     try:
    #         s = self.driver.get_window_size()
    #         x1 = s['width'] * 0.5  # x坐标
    #         y1 = s['height'] * 0.75  # 起点y坐标
    #         y2 = s['height'] * 0.25  # 终点y坐标
    #         for i in range(n):
    #             self.driver.swipe(x1 + random.randint(0, 100), y1 + random.randint(0, 100), x1 + random.randint(0, 100),
    #                               y2 + random.randint(0, 100), t)
    #     except Exception as e:
    #         print('swipe_up', e)
    #         time.sleep(1)
    #         self.swipe_up()


#   /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
# 	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
# 	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
#   /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView
#   /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView


if __name__ == '__main__':
    #
    automation('127.0.0.1:62025', 4723,['红酒', '戒指', '旅游', '就业', '考研', '环境','人工智能']).start()
    # # 不用动 除非开多个模拟器
    # devicesList = ["127.0.0.1:62025"]  # "127.0.0.1:62034",
    # mulList = []
    # for device in range(len(devicesList)):
    #     # 循环创建线程
    #     port = 4723 + 2 * device
    #     mulList.append(multiprocessing.Process(target=automation(devicesList[device], port,
    #                                                              ['牛奶', '车', '房地产', '上学', '就业', '考研', '环境',
    #                                                               '人工智能']).start()))
    #
    # # 开始执行线程
    # for mul in mulList:
    #     mul.start()
    #
    # # 关闭线程
    # for mul in mulList:
    #     mul.join()
