from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import psycopg2

conn = psycopg2.connect(database="pg_db_dy", user="postgres", password="1234567", host="localhost", port="5432")  # 创建数据库连接
cursor = conn.cursor()  #  获取游标

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
        cursor.execute('select str_desc from dy_aweme_hj')
        text = cursor.fetchall()
        # ((12,),(12,))
        from itertools import chain
        self.awemes = list(chain.from_iterable(text))  # 把text转成列表
        # self.awemes = ['教你一招认识欧盟餐酒，这种红酒超过50块就别买了！#酒#红酒 @抖音小助手']
        self.awemes.append('获取名称失败')
        # print(port, '=' * 30)

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

    def driverWait(self, text, xpORid='xpath'):
        try:
            if xpORid == 'xpath':
                if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_xpath(text)):
                    return True
            else:
                if WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_id(text)):
                    return True
        except Exception as e:
            print('driverWait: {}'.format(e.args))
            return False

    def driverClick(self, text, xy=[], xpORid='xpath'):
        try:
            if xpORid == 'xpath':
                self.driver.find_element_by_xpath(text).click()
            else:
                self.driver.find_element_by_id(text).click()
        except Exception as e:
            print('driverClick:【{}】-【{}】'.format(text, e.args))
            self.driver.tap(xy, 500)  # 报错的时候自动点击

    def driverSendKey(self, text, value, xpORid='xpath'):
        try:
            if xpORid == 'xpath':
                self.driver.find_element_by_xpath(text).send_keys(value)
            else:
                self.driver.find_element_by_id(text).send_keys(value)
        except Exception as e:
            print('driverSendKey:{}-{}'.format(text, e.args))

    def driverText(self, text, xpORid='xpath'):
        try:
            if xpORid == 'xpath':
                return self.driver.find_element_by_xpath(text).text
            else:
                return self.driver.find_element_by_id(text).text
        except Exception as e:
            return ""

    def search(self):
        """点击搜索按钮"""
        # 等待一秒
        time.sleep(1)
        if self.driverWait('//android.widget.ImageView[@content-desc="搜索"]'):
            self.driverClick('//android.widget.ImageView[@content-desc="搜索"]', [(9, 44), (63, 98)])

    def clickInput(self, value):
        """搜索框输入内容"""
        time.sleep(1)
        if self.driverWait('com.ss.android.ugc.aweme:id/a9d', xpORid='id'):
            self.driverClick('com.ss.android.ugc.aweme:id/a9d', xpORid='id')
            self.driverSendKey('com.ss.android.ugc.aweme:id/a9d', value, xpORid='id')

    def searchClick(self):
        """点击搜索按钮"""
        time.sleep(1)
        if self.driverWait('com.ss.android.ugc.aweme:id/d_b', xpORid='id'):
            self.driverClick('com.ss.android.ugc.aweme:id/d_b', xpORid='id')

    def userClick(self):
        """点击用户tab"""
        time.sleep(1)
        try:
            self.driver.tap([(241,130),(287,162)], 500)
            time.sleep(1)
        except Exception as e:
            print('userClick', e)

    def user(self):
        """循环执行点击抖音号"""
        time.sleep(5)
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
        if self.driverWait('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i):
            dy = self.driverText('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i)
            if dy not in self.DYH:
                self.DYH.append(dy)
                self.driverClick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]' % i)

    def clickVideo(self):
        """点击视频信息"""
        time.sleep(1)
        old_aweme_name = ""
        for i in range(1, 5):
            if self.driverWait('//android.widget.ImageView[@content-desc="视频%s"]' % i):
                self.driverClick('//android.widget.ImageView[@content-desc="视频%s"]' % i)
                break

        while True:
            time.sleep(3)
            self.driver.tap([(673,878)], 500) # 点击评论
            time.sleep(2)
            try:
                aweme_name = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a25').text
                print(aweme_name)
            except Exception as e:
                print('1'+e)
            time.sleep(2)
            # self.driverClick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView')
            if self.closeComment():
                print('【{}】没有评论。'.format(aweme_name))
                #  如果没有评论窗 关闭评论窗
                time.sleep(3)
                self.driverClick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView')
                time.sleep(2)
            else:
                comI = 1
                while True:
                    if aweme_name in self.awemes:
                        print('【{}】已经获取过。'.format(aweme_name))
                        self.driverClick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView')
                        time.sleep(3)
                        break
                    self.swipe_up(name='滑动【{}】第{}页评论评论中'.format(aweme_name, comI))
                    comI += 1
                    time.sleep(1)

                    pl = self.driverText('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[9]/android.widget.TextView')
                    if "没有更多了" in self.driver.page_source or "没有更多了" in pl:  # 评论到底
                        print('【{}】没有评论了'.format(aweme_name))
                        time.sleep(3)
                        self.driverClick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView')
                        break
            # print(aweme_name+'--'+old_aweme_name)
            if aweme_name == old_aweme_name:
                print('视频没有了')
                time.sleep(3)
                self.driver.tap([(34, 79.9)], 500)  # 关闭视频
                time.sleep(3)
                self.driverClick('com.ss.android.ugc.aweme:id/ix', xpORid='id')
                time.sleep(2)
                break
            else:
                old_aweme_name = aweme_name
            self.swipe_up(t=300, name='更换下一个视频')

    def closeComment(self):
        try:
            commentValue = self.driverText('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView')
            if '暂无评论' in commentValue:
                return True
        except Exception as e:
            pass

        page_source = self.driver.page_source
        if "评论并转发" in page_source:  # 没有评论 將自动打开的评论框关闭
            return True

        if "暂无评论" in page_source:  # 没有评论 关闭评论窗
            return True

        if '暂无评论，来抢沙发' in page_source:
            return True

        return False




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
    main('127.0.0.1:62025', 4723,['红酒']).start()