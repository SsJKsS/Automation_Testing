from appium import webdriver
import time
from time import sleep
import unittest
import HTMLTestRunner
from selenium.webdriver.support.wait import WebDriverWait


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
            'platformName': 'iOS',
            'platformVersion': '13.3',
            "deviceName": "iPhone 11 Pro",
            "app": "/Users/TVBS/Desktop/supertastemvp dev.app",
            "automationName": 'XCUITest',
            'autoAcceptAlerts': True,
            'clearSystemFiles': True,
            'newCommandTimeout': 80,
            # 'noReset': True,  # 不重新安裝app
            "permissions": "{\"tw.com.tvbs.supertastemvp.dev\":"
                           "{\"camera\":\"YES\","
                           "\"medialibrary\":\"YES\","
                           "\"microphone\":\"YES\","
                           "\"notifications\":\"YES\","
                           "\"photos\":\"YES\","
                           "\"location\":\"always\"}}"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 連接Appium
        self.driver.implicitly_wait(8)

    # 初次進入APP，新手教學相關功能驗證
    def test_open(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            print('\n=======新手教學=======')
            for i in range(3):
                # diretion = up | down | left | right
                self.driver.execute_script('mobile: swipe', {'direction': 'left'})
                self.driver.implicitly_wait(3)
            self.driver.execute_script('mobile: swipe', {'direction': 'right'})
            self.driver.implicitly_wait(3)
            self.driver.execute_script('mobile: swipe', {'direction': 'left'})
            self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.tap([(200, 750)])
            self.driver.implicitly_wait(3)
            print('新手教學功能正常且進入APP首頁順利')

            # 關閉 App 後重啟不再出現新手教學
            self.driver.terminate_app('tw.com.tvbs.supertastemvp.dev')
            sleep(2)
            self.driver.activate_app('tw.com.tvbs.supertastemvp.dev')
            print('關閉 App 後重啟不再出現新手教學')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('首頁'))

            # tab名稱
            index_tab = self.driver.find_element_by_name('首頁')
            store_tab = self.driver.find_element_by_name('購物')
            pocket_tab = self.driver.find_element_by_name('口袋')
            search_tab = self.driver.find_element_by_name('熱搜')
            member_tab = self.driver.find_element_by_name('我的')

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
            # member_tab.click()
            # sleep(1)

            # member_tab_selected = member_tab.is_selected()
            # self.assertTrue(member_tab_selected, '我的icon經點選後未被填滿')  # 判斷我的icon經點選後有無填滿
            print('Tab Bar名稱正確且點選後有被填滿')

            # 檢查Tab Bar跳轉
            index_tab.click()  # 首頁
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('hand'))
            store_tab.click()
            sleep(1)
            self.driver.tap([(337, 64)])  # 購物車按鈕
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('login_fb'))
            self.driver.find_element_by_name('close').click()  # Ｘ按鈕
            pocket_tab.click()  # 口袋
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('login_fb'))
            self.driver.find_element_by_name('close').click()  # Ｘ按鈕
            search_tab.click()  # 熱搜
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('熱門搜尋'))
            member_tab.click()  # 我的
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name('我的'))
            print('Tab Bar跳轉功能正常')
            self.driver.quit()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 搖一搖
    def test_shake(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 新手教學
            for i in range(3):
                # diretion = up | down | left | right
                self.driver.execute_script('mobile: swipe', {'direction': 'left'})
                self.driver.implicitly_wait(3)
            self.driver.tap([(200, 750)])  # 立即逛逛btn
            sleep(2)

            # 搖一搖（Email會員）
            print('\n=======搖一搖（Email會員）=======')
            self.driver.tap([(40, 70)])  # 搖一搖icon
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_ios_predicate("value = '請輸入註冊Email'")
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_ios_predicate("value = '請輸入密碼'")
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_name('登入').click()
            sleep(5)
            self.driver.tap([(40, 70)])  # 搖一搖icon

            # 沒活動
            if self.is_element_exist('XCUIElementTypeAlert') is True:
                self.driver.find_element_by_ios_predicate("type = 'XCUIElementTypeButton'").click()
                print('搖一搖目前沒活動')

            # 有活動
            else:
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeImage'"))
                self.driver.shake()  # 實際搖動
                print('搖動後可進入活動頁面')
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeButton'"))
                print('Title列有返回鍵 ＜')
                sleep(3)
                for i in range(2):
                    # diretion = up | down | left | right
                    self.driver.execute_script('mobile: swipe', {'direction': 'up'})
                # 分享btn
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                    '//XCUIElementTypeOther[@name="2020夜市新人氣王"]/XCUIElementTypeOther[1]'))
                # 返頂btn
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                    '//XCUIElementTypeOther[@name="2020夜市新人氣王"]/XCUIElementTypeOther[2]'))
                print('拉至底部會跳出Button Bar')

            # 登出
            self.driver.find_element_by_ios_predicate("type = 'XCUIElementTypeButton'").click()
            sleep(1)
            index_tab = self.driver.find_element_by_name('首頁')
            member_tab = self.driver.find_element_by_name('我的')
            member_tab.click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeNavigationBar'"))
            for i in range(3):
                # diretion = up | down | left | right
                self.driver.execute_script('mobile: swipe', {'direction': 'up'})
                sleep(1)
            self.driver.tap([(200, 700)])  # 登出
            self.driver.find_element_by_ios_predicate("name = '含淚登出'").click()
            sleep(1)
            index_tab.click()
            sleep(1)

            # 搖一搖（FB會員）
            print('\n=======搖一搖（FB會員）=======')
            self.driver.tap([(40, 70)])  # 搖一搖icon
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_ios_predicate("name = 'login_fb'"))
            self.driver.tap([(200, 150)])  # FB icon
            sleep(1)
            self.driver.tap([(257, 470)])  # FB 權限Continue
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeButton'"))
            self.driver.find_element_by_ios_predicate("name = '繼續'").click()
            sleep(5)
            self.driver.tap([(40, 70)])  # 搖一搖icon

            # 沒活動
            if self.is_element_exist('XCUIElementTypeAlert') is True:
                self.driver.find_element_by_ios_predicate("type = 'XCUIElementTypeButton'").click()
                print('搖一搖目前沒活動')

            # 有活動
            else:
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeImage'"))
                self.driver.shake()  # 實際搖動
                sleep(2)
                print('搖動後可進入活動頁面')
            self.driver.quit()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../screenshot/supertasteAppFail/shake_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 商城
    def test_shop(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 新手教學
            for i in range(3):
                # diretion = up | down | left | right
                self.driver.execute_script('mobile: swipe', {'direction': 'left'})
                self.driver.implicitly_wait(3)
            self.driver.tap([(200, 750)])  # 立即逛逛btn
            sleep(2)

            # 購物車
            WebDriverWait(self.driver, 40).until(lambda x: x.find_element_by_ios_predicate("name = 'shop icon2'"))
            self.driver.find_element_by_ios_predicate("name = 'shop icon2'").click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_ios_predicate("value = '請輸入註冊Email'")
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_ios_predicate("value = '請輸入密碼'")
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_name('登入').click()
            WebDriverWait(self.driver, 40).until(lambda x: x.find_element_by_ios_predicate("name = 'shop icon2'"))

            # 購物車無收藏
            self.driver.find_element_by_ios_predicate("name = 'shop icon2'").click()
            sleep(8)
            self.driver.tap([(300, 430)])  # 確定btn
            WebDriverWait(self.driver, 40).until(
                lambda x: x.find_element_by_ios_predicate("type = 'XCUIElementTypeTabBar'"))

            # 收藏商品
            self.driver.tap([(270, 750)])  # 熱搜
            WebDriverWait(self.driver, 40).until(lambda x: x.find_element_by_ios_predicate("name = '請搜尋你感興趣的內容'"))
            search_blank = self.driver.find_element_by_ios_predicate("name = '請搜尋你感興趣的內容'")
            search_blank.send_keys('巧克力')
            self.driver.tap([(300, 700)])  # 鍵盤搜尋
            self.driver.find_elements_by_ios_predicate("type = 'XCUIElementTypeStaticText'")[3].click()  # 買東西
            self.driver.find_element_by_ios_predicate("name = '(測試不出貨)【排第1個主商品1】巧克力棒'").click()
            self.driver.find_element_by_ios_predicate("name = '放入購物車'").click()
            self.driver.tap([(300, 280)])  # 關閉確認收藏提醒
            self.driver.quit()

            # 購物車無收藏

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../screenshot/supertasteAppFail/shake_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        pass


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../report/supertasteAppReport/supertaste_App_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(SuperTaste('test_open'))  # 首頁底部Tab驗證
    # suite.addTest(SuperTaste('test_shake'))  # 搖一搖
    suite.addTest(SuperTaste('test_shop'))  # 商城
    # suite.addTest(SuperTaste('test_index'))  # banner、節目即時看、上方Tab跳轉
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
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)
