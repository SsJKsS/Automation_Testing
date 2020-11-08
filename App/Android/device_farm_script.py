from selenium import webdriver as chrome_driver
from appium import webdriver
from time import sleep
import time
import random
import datetime
import unittest
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android import app_pocket_s8plus


class SuperTaste(unittest.TestCase):

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    # initial setting
    def setUp(self):
        desired_caps = {
            'autoGrantPermissions': True
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 連接Appium
        self.driver.implicitly_wait(8)

    # 初次進入APP，新手教學相關功能驗證
    def test_open(self):
        # 新手教學
        for i in range(3):
            self.driver.find_element_by_class_name('android.widget.ImageView').click()
            self.driver.implicitly_wait(3)

        # 立即逛逛btn
        self.driver.find_element_by_id(
            'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
        self.driver.implicitly_wait(3)
        print('\n新手教學功能正常且進入APP首頁順利')

        # 檢查tab名稱
        index_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_featured')
        self.assertEqual(index_tab.get_attribute('content-desc'), '首頁')
        store_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_store')
        self.assertEqual(store_tab.get_attribute('content-desc'), '購物')
        pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
        self.assertEqual(pocket_tab.get_attribute('content-desc'), '口袋')
        search_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_search')
        self.assertEqual(search_tab.get_attribute('content-desc'), '熱搜')
        member_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_member')
        self.assertEqual(member_tab.get_attribute('content-desc'), '我的')
        print('Tab Bar名稱正確')

        # 檢查tab selected狀態
        index_tab_selected = index_tab.is_selected()
        self.assertTrue(index_tab_selected, '首頁icon經點選後未被填滿')  # 判斷首頁icon經點選後有無填滿
        store_tab.click()
        self.driver.implicitly_wait(3)
        store_tab_selected = store_tab.is_selected()
        self.assertTrue(store_tab_selected, '購物icon經點選後未被填滿')  # 判斷購物icon經點選後有無填滿
        search_tab.click()
        self.driver.implicitly_wait(3)
        search_tab_selected = search_tab.is_selected()
        self.assertTrue(search_tab_selected, '熱搜icon經點選後未被填滿')  # 判斷熱搜icon經點選後有無填滿
        member_tab.click()
        self.driver.implicitly_wait(3)
        member_tab_selected = member_tab.is_selected()
        self.assertTrue(member_tab_selected, '我的icon經點選後未被填滿')  # 判斷我的icon經點選後有無填滿
        print('Tab Bar icon經點選後有被填滿')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SuperTaste('test_open'))  # 首頁底部Tab驗證
    # suite.addTest(SuperTaste('test_index'))  # 搖一搖、banner、節目即時看、上方Tab跳轉
    # suite.addTest(SuperTaste('test_hotRecommend'))  # 熱門推薦
    # suite.addTest(SuperTaste('test_relatedNews'))  # 相關報導
    # suite.addTest(SuperTaste('test_collectSearch'))  # 收藏後、取消收藏後搜尋
    # suite.addTest(SuperTaste('test_loginFeature'))  # 大頭貼、登入btn進入登入頁面
    # suite.addTest(SuperTaste('test_memberCenterLoginPageCheck'))  # 登入頁面欄位、邏輯
    # suite.addTest(SuperTaste('test_memberCenterLoginTVBS'))  # 登入TVBS會員
    # suite.addTest(SuperTaste('test_memberCenterLoginFB'))  # 登入FB會員(APP登出狀態)
    # suite.addTest(SuperTaste('test_memberCenterRegisterPageCheck'))  # 註冊頁面欄位、邏輯
    # suite.addTest(SuperTaste('test_memberCenterRegisterTVBS'))  # 註冊TVBS會員
    # suite.addTest(SuperTaste('test_memberCenterRegisterFB'))  # 註冊FB會員
    # suite.addTest(SuperTaste('test_hotSearch'))  # 熱搜
    # suite.addTest(SuperTaste('test_profileEdit'))  # 個人資料編輯(施工中)
    # suite.addTest(SuperTaste('test_myCollection'))  # 口袋
    # suite.addTest(SuperTaste('test_myNotification'))  # 我的通知
    # suite.addTest(SuperTaste('test_officialAccount'))  # 官方帳號
    # suite.addTest(SuperTaste('test_otherSettings'))  # 其他設定
    # suite.addTest(SuperTaste('test_pocket'))  # 口袋清單(Freyja)
    suite.run()
