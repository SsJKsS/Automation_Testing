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
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'G7AZCY018534PKE',  # S8+(8.0) : ce031713bc2694670d, HTC(9.0) NE9CF1S01374
            'appPackage': 'com.tvbs.supertastemvppack',
            'appActivity': 'com.tvbs.supertaste.ui.activity.SplashActivity',
            'autoGrantPermissions': True
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

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_index(self):
        # # 網頁自動化設定
        # chrome_path = 'C:/workspace/selenium_driver_chrome/chromedriver.exe'
        # self.chrome_driver = chrome_driver.Chrome(chrome_path)
        # self.chrome_driver.maximize_window()
        #
        # # 後台 - 頭條管理
        # self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
        # self.chrome_driver.maximize_window()
        # self.chrome_driver.implicitly_wait(6)
        # login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
        # login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
        # login_adm_name.send_keys('jacktsao')
        # login_adm_pw.send_keys('TVBS2020')
        # self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
        # self.chrome_driver.implicitly_wait(6)
        #
        # # 新開一個視窗，通過執行js來新開一個視窗
        # js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_app_activities");'
        # self.chrome_driver.execute_script(js)
        #
        # # 獲取當前視窗控制代碼集合（列表型別）
        # handles = self.chrome_driver.window_handles
        # self.chrome_driver.switch_to.window(handles[-1])
        # time.sleep(2)
        #
        # add_page_btn = self.chrome_driver.find_element_by_id('add_page')
        # add_page_btn.click()
        #
        # title = self.chrome_driver.find_element_by_id('title')
        # url = self.chrome_driver.find_element_by_id('url')
        # link = self.chrome_driver.find_element_by_id('link')
        # released = self.chrome_driver.find_element_by_id('released')
        # end = self.chrome_driver.find_element_by_id('end')
        # save = self.chrome_driver.find_element_by_id('save')
        #
        # now = datetime.datetime.now()
        # delta = datetime.timedelta(seconds=10)
        # new_time = (now + delta).strftime('%Y/%m/%d %H:%M:%S')
        # title.send_keys('Automation ' + new_time)
        # url.send_keys('https://supertaste.tvbs.com.tw/')
        # link.send_keys('/program_piwigo/piwigo/upload/2020/05/22/20200522214613-422e6a1d.jpg')
        # released.clear()
        # released.send_keys(new_time)
        # end.clear()
        # end.send_keys('2020/12/31 12:00:00')
        # save.click()
        # self.chrome_driver.switch_to.alert.accept()


        # 新手教學
        flag = True
        # noinspection PyBroadException
        try:
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 搖一搖
            print('\n=======搖一搖=======')
            shake_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_shake')
            shake_btn.click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_shake'))
            shake_btn.click()
            if self.is_element_exist('android:id/message') is True:
                print('搖一搖目前沒活動')
                self.driver.find_element_by_id('android:id/button1').click()
            else:
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_Shake_Background'))
                # self.driver.shake()
                # 網頁自動化設定
                chrome_path = 'C:/workspace/selenium_driver_chrome/chromedriver.exe'
                self.chrome_driver = chrome_driver.Chrome(chrome_path)

                # 後台 - 頭條管理
                self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
                self.chrome_driver.implicitly_wait(6)
                login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
                login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
                login_adm_name.send_keys('jacktsao')
                login_adm_pw.send_keys('TVBS2020')
                self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
                self.chrome_driver.implicitly_wait(6)

                # 新開一個視窗，通過執行js來新開一個視窗
                js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_shake");'
                self.chrome_driver.execute_script(js)

                # 獲取當前視窗控制代碼集合（列表型別）
                handles = self.chrome_driver.window_handles
                self.chrome_driver.switch_to.window(handles[-1])
                web_shake_title = self.chrome_driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]').text
                web_shake_content = self.chrome_driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
                print('搖一搖目前有活動')
                shake_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Title').text
                shake_content = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Content').text
                self.assertEqual(web_shake_title, shake_title)
                print('後台設定與前台顯示標題一樣為 : ' + shake_title)
                self.assertEqual(web_shake_content, shake_content)
                print('後台設定與前台顯示內文一樣為 : ' + shake_content)
                self.driver.back()

            # 輪播圖
            banner = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            banner.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            self.driver.back()
            print('\n=======Banner=======')
            print('跳轉Banner正常')

            # 節目即時看
            print('\n=======節目即時看=======')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[3])
            channel_watch = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[3]
            channel_watch_text = channel_watch.text
            print('節目即時看文章標題為 :' + channel_watch_text)
            channel_watch.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            direct_channel_watch_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            print('節目即時看跳轉文章標題為 :' + direct_channel_watch_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            channel_watch_pic = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            channel_watch_pic.click()
            print('點選圖片可跳轉' + direct_channel_watch_text)
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))

            # 來討論
            print('\n=======來討論=======')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/llMessage').click()
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_class_name(
                'android.widget.EditText'))
            print('來討論跳轉正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivBack').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/llMessage'))

            # 去分享
            print('\n=======去分享=======')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/llShare').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/title'))
            print('去分享跳轉正常')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/llMessage'))

            # 藏口袋
            print('\n=======藏口袋=======')
            # 點選收藏
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').text
            self.assertEqual(collect_btn_text, '藏口袋')
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            print('收藏文章後愛心有填滿')

            # 判斷收藏按鈕文字變化
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            collected_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            self.assertEqual(collected_btn.text, '已收藏')
            print('收藏按鈕文字變化正確 ')

            # 取消收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏文章後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 再次收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            article_title = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/smallLabel'))

            # 返回收藏頁面
            self.driver.find_element_by_xpath("//*[@text='口袋']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            news_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more_article'))
            collected_article_title = self.driver.find_elements_by_class_name('android.widget.TextView')[4].text
            self.assertEqual(article_title, collected_article_title)
            print('已收藏的標題為 : ' + collected_article_title)
            print('確認為剛剛收藏的文章標題，收藏文章功能正常。')

            # 刪除收藏
            action = TouchAction(self.driver)  # 創建TouchAction物件
            action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
            action.perform()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            self.driver.find_element_by_id('android:id/button1').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 節目即時看下方店家資訊
            print('\n=======節目即時看下方店家資訊=======')
            self.driver.swipe(900, 730, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('收藏下方店家後愛心有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 取消收藏
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏下方店家後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 節目即時看下方店家跳轉
            store_title = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            print('節目即時看下方店家: ' + store_title)
            store = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            direct_store_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.assertEqual(store_title, direct_store_title)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            print('節目即時看下方店家跳轉正常')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))

            # # More
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_more').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            # self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')  # 判斷More按鈕
            # print('More按鈕功能正常')
            #
            # # 資訊卡
            # print('\n=======資訊卡=======')
            # index_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[0]
            # index_tab.click()
            # sleep(5)
            # self.driver.swipe(900, 1400, 900, 300)
            # info_card = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            # info_card.click()
            # print('資訊卡跳轉功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # sleep(5)
            #
            # # 推薦商品
            # print('\n=======推薦商品=======')
            # self.driver.swipe(900, 1200, 900, 300)
            # item = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            # item.click()
            # WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))  # 未來要改
            # self.driver.back()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # print('推薦商品跳轉功能正常')
            #
            # # 節目
            # print('\n=======分頁跳轉=======')
            # channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            # channel_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')
            # print('跳轉至節目頁正常')
            #
            # # 好喝
            # drink_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2]
            # drink_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(drink_tab.is_selected(), '未跳轉至好喝頁')
            # print('跳轉至好喝頁正常')
            #
            # # 熱門
            # hot_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[3]
            # hot_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(hot_tab.is_selected(), '未跳轉至熱門頁')
            # print('跳轉至熱門頁正常')
            #
            # # 美食
            # foods_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[3]
            # foods_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(foods_tab.is_selected(), '未跳轉至美食頁')
            # print('跳轉至美食頁正常')
            #
            # # 旅行
            # travel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[4]
            # travel_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(travel_tab.is_selected(), '未跳轉至旅行頁')

        except:
            flag = False
            if flag is False or Exception or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/index_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

        # com.tvbs.supertastemvppack: id / iv_more
        # # 後台新增美食資訊卡
        # self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
        # self.chrome_driver.maximize_window()
        # self.chrome_driver.implicitly_wait(6)
        # login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
        # login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
        # login_adm_name.send_keys('jacktsao')
        # login_adm_pw.send_keys('TVBS2020')
        # self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
        # sleep(3)
        # js = "var action=document.documentElement.scrollTop=10000"
        # self.chrome_driver.execute_script(js)
        # self.chrome_driver.implicitly_wait(3)
        # self.chrome_driver.find_element_by_xpath('/html/body/div/div/div/ul/li[17]/span').click()
        # self.chrome_driver.implicitly_wait(3)
        # self.chrome_driver.find_element_by_link_text('景點管理').click()
        # sleep(3)
    def test_hotRecommend(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 節目
            print('\n=======熱門推薦=======')
            channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            channel_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')
            print('跳轉至節目頁正常')

            # 文章
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            sleep(3)
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_tip') is False:
                    self.driver.swipe(900, 1300, 900, 300)
                else:
                    self.driver.swipe(900, 1300, 900, 300)
                    break
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d')
            print('文章時間格式正確')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            print('熱門推薦文章跳轉正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/hotRecommend_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_relatedNews(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 資訊卡
            self.driver.swipe(900, 1400, 900, 600)
            info_card = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/iv_channel')[1]
            info_card.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            self.driver.swipe(900, 1400, 900, 600)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
            print('\n=======相關報導=======')
            print('文章縮圖時間格式正確')
            related_news = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            related_news.click()
            print('相關報導跳轉正常')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_author').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
            print('文章時間格式正確')

            # 藏口袋
            # 點選收藏
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').text
            self.assertEqual(collect_btn_text, '藏口袋')
            collect_article.click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))

            # 判斷愛心有無填滿
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            print('收藏文章後愛心有填滿')

            # 判斷收藏按鈕文字變化
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            collected_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            self.assertEqual(collected_btn.text, '已收藏')
            print('收藏按鈕文字變化正確 ')

            # 取消收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏文章後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # # 返回收藏頁面
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/smallLabel'))
            # self.driver.find_element_by_xpath("//*[@text='口袋']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_more'))
            # news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            # news_tab.click()

            # # 確認無收藏
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/relatedNews_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_collectSearch(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            sleep(2)

            # 節目即時看下方店家資訊
            print('\n=======收藏驗證=======')
            self.driver.swipe(900, 730, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store.click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            #  搜尋節目即時看下方店家名稱
            store_name = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '已收藏')
            print('搜尋已收藏的節目即時看下方店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '藏口袋')
            print('搜尋未收藏的節目即時看下方店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='首頁']").click()
            sleep(3)

            # 搜尋資訊卡店家名稱
            self.driver.swipe(900, 1400, 900, 300)
            info_card = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            info_card.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            store_name = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '已收藏')
            print('搜尋已收藏的資訊卡店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '藏口袋')
            print('搜尋未收藏的資訊卡店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='首頁']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 文章底部功能列
            channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            channel_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            article_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(article_title[0:4])
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                'android.support.v7.app.ActionBar$Tab'))
            self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            status = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            status_checked = bool(status.get_attribute("checked"))
            self.assertTrue(status_checked, '收藏後仍未填滿')
            print('搜尋已收藏的文章收藏按鈕有填滿')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(article_title[0:4])
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                'android.support.v7.app.ActionBar$Tab'))
            self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1].click()
            self.assertFalse(status.is_selected(), '取消收藏後仍填滿')
            print('搜尋未收藏的文章收藏按鈕未填滿')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/collectSearch_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 進入登入頁面相關功能檢查
    def test_loginFeature(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            print('\n大頭貼按鈕功能正常')

            # 想先瀏覽看看
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tvPass').click()
            self.driver.implicitly_wait(3)
            print('想先瀏覽看看功能正常')

            # 判斷頁面是否有大頭貼btn且可點選
            profile_assert = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').is_enabled()
            # 判斷頁面是否有點擊登入文字且可點選
            login_text_assert = self.driver.find_element_by_xpath("//*[@text='點擊登入']").is_enabled()
            self.assertTrue(profile_assert)
            print('點選想先瀏覽看看功能正常 - 偵測頁面是否有大頭貼按鈕且enable')
            self.assertTrue(login_text_assert)
            print('點選想先瀏覽看看功能正常 - 偵測頁面是否有點擊登入按鈕且enable')
            self.driver.swipe(900, 1500, 900, 200)
            sleep(2)
            self.driver.tap([(500, 1700)])  # 登入btn
            print('點選底部登入按鈕功能正常')
            self.driver.implicitly_wait(3)

        except:
            flag = False
            profile_assert = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/loginFeature_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 登入頁面欄位檢查
    def test_memberCenterLoginPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            account_blank_text = account_blank.text
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            password_blank_text = password_blank.text

            self.assertEqual(account_blank_text, '請輸入註冊Email')  # 判斷欄位placeholder
            print('\n登入帳號欄位placeholder為 : ' + account_blank_text)
            self.assertEqual(password_blank_text, '請輸入密碼')  # 判斷欄位placeholder
            print('登入密碼欄位placeholder為 : ' + password_blank_text)

            # 不輸入帳號、密碼登入
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼')
            print('不輸入帳號密碼登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))

            # 不輸入帳號登入
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email')
            print('不輸入帳號登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            password_blank.clear()

            # 不輸入密碼登入
            account_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼')
            print('不輸入密碼登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()

            # 輸入非Email格式帳號進行登入
            account_blank.send_keys('tvbstest')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '帳號格式錯誤，請填寫完整Email！')
            print('輸入非Email格式帳號登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 輸入不存在帳號進行登入
            account_blank.send_keys('tvbstest@gmail.com')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '查無此帳號！')
            print('輸入不存在帳號登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 輸入錯誤密碼進行登入
            account_blank.send_keys('s0932748681@gmail.com')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '帳號或密碼錯誤，請重新輸入！')
            print('輸入錯誤密碼登入跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))

            # # 忘記密碼
            # forgot_mail = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvForgetPassWord')
            # forgot_mail.click()
            # forgot_mail_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etEmail').text
            # self.assertEqual(forgot_mail_text, '請輸入註冊Email')
            # print('忘記密碼placeholder為 : ' + forgot_mail_text)
            # forgot_mail.send_keys('s23321286')
            # send_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btSend')
            # send_btn.click()
            # message = self.driver.find_element_by_id('android:id/message')
            # message_text = message.text
            #
        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterLoginPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # TVBS會員登入
    def test_memberCenterLoginTVBS(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_Title'))
            self.driver.swipe(900, 1500, 900, 200)
            self.driver.swipe(900, 1500, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout'))
            print('\nTVBS登入功能正常')

            # 驗證登出相關文字
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout').click()
            self.driver.implicitly_wait(10)
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '你確定要登出嗎？')
            print('登出跳出dialog : ' + dialog_text)
            confirm_btn_text = self.driver.find_element_by_id('android:id/button1').text
            self.assertEqual(confirm_btn_text, '含淚登出')
            print('確定登出按鈕wording : ' + confirm_btn_text)
            cancel_btn_text = self.driver.find_element_by_id('android:id/button2').text
            self.assertEqual(cancel_btn_text, '再想一下')
            print('取消登出按鈕wording : ' + cancel_btn_text)

            # 驗證登出相關行為
            self.driver.find_element_by_id('android:id/button2').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout'))
            print('取消登出按鈕功能正常')
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('android:id/button1').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Login'))
            print('確定登出按鈕功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/test_memberCenterLoginTVB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # FB登入
    def test_memberCenterLoginFB(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            # FB登入
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/ivFbLogin').click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('android.view.ViewGroup'))
            self.driver.tap([(480, 870)])
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('android.widget.EditText'))
            self.driver.find_element_by_xpath("//*[@text='手機號碼或電子郵件地址']").send_keys('s23321286@gmail.com')
            self.driver.find_element_by_xpath("//*[@text='密碼']").send_keys('Tvbs2020')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.view.ViewGroup'))
            self.driver.find_elements_by_class_name('android.view.ViewGroup')[1].click()  # FB登入btn
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_Title'))
            sleep(3)

            # 驗證FB會員名字
            fb_member_name = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_member_name')
            fb_member_name_text = fb_member_name.text
            self.assertEqual(fb_member_name_text, 'Jack Tsao')
            print('\nFB會員登入成功且名字正確，此次登入用戶名稱為 : ' + fb_member_name_text)
            self.driver.implicitly_wait(3)
            self.driver.swipe(900, 1500, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout'))

            # 驗證登出相關文字
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout').click()
            self.driver.implicitly_wait(10)
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '你確定要登出嗎？')
            print('登出跳出dialog : ' + dialog_text)
            confirm_btn_text = self.driver.find_element_by_id('android:id/button1').text
            self.assertEqual(confirm_btn_text, '含淚登出')
            print('確定登出按鈕wording : ' + confirm_btn_text)
            cancel_btn_text = self.driver.find_element_by_id('android:id/button2').text
            self.assertEqual(cancel_btn_text, '再想一下')
            print('取消登出按鈕wording : ' + cancel_btn_text)

            # 驗證登出相關行為
            self.driver.find_element_by_id('android:id/button2').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout'))
            print('取消登出按鈕功能正常')
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('android:id/button1').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Login'))
            print('確定登出按鈕功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterLoginFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 註冊頁面欄位檢查
    def test_memberCenterRegisterPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            self.driver.find_element_by_xpath("//*[@text='我還沒有TVBS帳號，註冊去']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            # 註冊帳號欄位
            register_account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            register_account_blank_text = register_account_blank.text
            # 註冊密碼欄位
            register_password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            register_password_blank_text = register_password_blank.text
            # 確認密碼欄位
            password_confirm_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWordCheck')
            password_confirm_blank_text = password_confirm_blank.text
            # checkbox
            notification_checkbox = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbNotification')
            notification_checkbox_checked = bool(notification_checkbox.get_attribute("checked"))

            # 註冊欄位驗證
            self.assertEqual(register_account_blank_text, '請輸入註冊Email')  # 判斷欄位placeholder
            print('\n註冊帳號欄位placeholder為 : ' + register_password_blank_text)
            self.assertEqual(register_password_blank_text, '請設定密碼(6~12個英數字)')  # 判斷欄位placeholder
            print('註冊密碼欄位placeholder為 : ' + register_password_blank_text)
            self.assertEqual(password_confirm_blank_text, '請再次輸入密碼')  # 判斷欄位placeholder
            print('註冊密碼欄位placeholder為 : ' + password_confirm_blank_text)
            self.assertTrue(notification_checkbox_checked, 'Checkbox預設並未勾選! ')  # 判斷Checkbox預設是否已勾選
            print('Checkbox預設為已勾選')

            # 判斷Checkbox預設是否已勾選
            notification_checkbox = self.driver.find_element_by_class_name('android.widget.CheckBox')
            notification_checkbox.click()
            self.assertFalse(notification_checkbox.is_selected(), 'Checkbox點擊後仍為勾選狀態!')
            print('Checkbox點擊後可取消勾選狀態')
            self.driver.implicitly_wait(3)

            # 不輸入Email、密碼、確認密碼註冊
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼、確認密碼')
            print('不輸入Email、密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))

            # 不輸入密碼、確認密碼註冊
            register_account_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼、確認密碼')
            print('不輸入密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()

            # 不輸入Email、密碼註冊
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼')
            print('不輸入Email、密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            password_confirm_blank.clear()

            # 不輸入Email、確認密碼註冊
            register_password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、確認密碼')
            print('不輸入Email、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_password_blank.clear()

            # 不輸入確認密碼註冊
            register_account_blank.send_keys('tvbstest')
            register_password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入確認密碼')
            print('不輸入確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()

            # 不輸入Email註冊
            register_password_blank.send_keys('tvbstest')
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email')
            print('不輸入Email註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 不輸入密碼註冊
            register_account_blank.send_keys('tvbstest')
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入不一樣密碼、確認密碼註冊
            register_account_blank.send_keys('tvbstest@gmail.com')
            register_password_blank.send_keys('tvbstest1')
            password_confirm_blank.send_keys('tvbstest2')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '密碼與確認密碼不符，請重新確認！')
            print('輸入不一樣密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入不符合密碼、確認密碼規則註冊
            register_account_blank.send_keys('tvbstest@gmail.com')
            register_password_blank.send_keys('tvbstvbs')
            password_confirm_blank.send_keys('tvbstvbs')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '密碼建議為 6~12 位數，必須是英文數字混合！')
            print('輸入不符合密碼、確認密碼規則註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入已註冊為TVBS會員的帳號註冊
            register_account_blank.send_keys('s0932748681@gmail.com')
            register_password_blank.send_keys('tvbstvbs123')
            password_confirm_blank.send_keys('tvbstvbs123')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號已透過 Email 註冊為會員！')
            print('輸入已註冊為TVBS會員的帳號註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入已註冊為FB會員的帳號註冊
            register_account_blank.send_keys('s23321286@gmail.com')
            register_password_blank.send_keys('tvbstvbs123')
            password_confirm_blank.send_keys('tvbstvbs123')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號已透過 FB 註冊為會員！')
            print('輸入已註冊為FB會員的帳號註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterRegisterPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_memberCenterRegisterTVBS(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath("//*[@text='我還沒有TVBS帳號，註冊去']").click()
            self.driver.implicitly_wait(3)
            register_account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            register_password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            password_confirm_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWordCheck')

            # 註冊欄位傳值
            random_account = random.choice('abcdefg') + str(random.randint(0, 9999))
            print('\n此次註冊帳號為 : ' + random_account + '@gmail.com')
            register_account = random_account + '@gmail.com'
            register_account_blank.send_keys(register_account)
            self.driver.implicitly_wait(3)
            register_password_blank.send_keys('a00000')
            password_confirm_blank.send_keys('a00000')
            print('此次註冊密碼為 : a00000')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()

            # 判斷男性RadioButton預設是否已勾選
            male_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbMale')
            male_radiobtn_checked = male_radiobtn.is_selected()
            self.assertFalse(male_radiobtn_checked, '男性RadioButton預設已經被勾選! ')
            print('男性RadioButton預設為未勾選')

            # 判斷女性RadioButton預設是否已勾選
            female_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbFemale')
            female_radiobtn_checked = female_radiobtn.is_selected()
            self.assertFalse(female_radiobtn_checked, '女性RadioButton預設已經被勾選! ')  # 判斷女性RadioButton預設是否已勾選
            print('女性RadioButton預設為未勾選')

            # 判斷未勾選性別直接送出
            next_btn = self.driver.find_element_by_xpath("//*[@text='下一步']")  # 下一步btn
            next_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入性別')
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rbMale'))
            print('未勾選性別直接送出跳出wording : ' + dialog_text)

            # 判斷男性RadioButton點擊後是否已勾選
            male_radiobtn.click()
            male_radiobtn_checked = bool(male_radiobtn.get_attribute("checked"))
            self.assertTrue(male_radiobtn_checked, '男性RadioButton點擊後仍為未勾選狀態!')
            print('男性RadioButton點擊後為勾選狀態')
            self.driver.implicitly_wait(3)

            # 判斷女性RadioButton點擊後是否已勾選
            female_radiobtn.click()
            female_radiobtn_checked = bool(female_radiobtn.get_attribute("checked"))
            self.assertTrue(female_radiobtn_checked, '女性RadioButton點擊後仍為未勾選狀態!')
            print('女性RadioButton點擊後為勾選狀態')
            self.driver.implicitly_wait(3)

            # 生日功能驗證
            birthday_btn = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/ivBirthday')
            birthday_btn.click()
            birthday_btn_alert_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/alertTitle').text
            self.assertEqual(birthday_btn_alert_text, '選擇生日')
            print('進入選擇生日頁面正常')
            self.driver.find_element_by_id('android:id/button2').click()
            print('離開選擇生日頁面正常')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/ivBirthday'))
            birthday_btn.click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath("//*[@text='1982']").click()
            self.driver.find_element_by_xpath("//*[@text='2']").click()
            self.driver.find_element_by_xpath("//*[@text='31']").click()
            self.driver.find_element_by_id('android:id/button1').click()
            print('選擇生日功能正常')

            # 判斷Checkbox預設是否已勾選
            notification_checkbox = self.driver.find_element_by_class_name('android.widget.CheckBox')
            self.assertFalse(notification_checkbox.is_selected(), 'Checkbox預設為已勾選狀態!')
            print('Checkbox預設為未勾選')
            notification_checkbox.click()
            notification_checkbox_checked = bool(notification_checkbox.get_attribute("checked"))
            self.assertTrue(notification_checkbox_checked, 'Checkbox點擊後仍為未勾選狀態!')
            print('Checkbox點擊後可勾選')
            self.driver.implicitly_wait(3)

            # 判斷服務條款、隱私權政策功能
            self.driver.tap([(580, 800)])  # 服務條款
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS會員服務條款']"))
            self.driver.back()
            print('進入服務條款功能正常')
            self.driver.tap([(800, 800)])  # 隱私權政策
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS個資與隱私權聲明']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.widget.CheckBox'))
            print('進入隱私權政策功能正常')

            # 判斷下一步
            # 未勾選同意
            notification_checkbox.click()
            next_btn = self.driver.find_element_by_xpath("//*[@text='下一步']")  # 下一步btn
            next_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請同意 TVBS 會員中心的服務條款及隱私權政策。')
            print('未勾選同意點選下一步跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()

            # 已勾選同意
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.widget.CheckBox'))
            notification_checkbox.click()
            next_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tvWording1'))
            success_dialog_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tvWording1').text
            print('註冊成功，' + success_dialog_text)

            # 與我們聯絡
            self.driver.tap([(560, 680)])  # 我們聯絡btn
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/to_heading'))
            self.driver.find_element_by_id('com.google.android.gm:id/subject').send_keys('Automation_' + current_time)
            self.driver.implicitly_wait(3)
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/to_heading'))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btLogin'))
            print('進入與我們聯絡功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterRegisterTVBS_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_memberCenterRegisterFB(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath("//*[@text='我還沒有TVBS帳號，註冊去']").click()
            self.driver.implicitly_wait(3)

            # FB快速註冊
            fb_register_account_btn = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/ivFbRegister')
            fb_register_account_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rl_my_collection'))
            sleep(3)

            # 驗證FB會員名字
            fb_member_name = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_member_name')
            fb_member_name_text = fb_member_name.text
            self.assertEqual(fb_member_name_text, 'Jack Tsao')
            print('\nFB會員快速註冊成功，此次註冊用戶名稱為 : ' + fb_member_name_text)
            self.driver.swipe(900, 1500, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout'))
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Logout').click()
            print('FB會員快速註冊成功且順利登出')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterRegisterFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_hotSearch(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 熱搜
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_search').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_keyword'))
            search_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search')
            search_blank_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').text
            self.assertEqual(search_blank_text, '請搜尋你感興趣的內容')  # 判斷欄位placeholder
            print('\n=======元件判斷=======')
            print('搜尋欄位placeholder為 : ' + search_blank_text)

            # 判斷搜尋無結果
            search_blank.send_keys('qaz')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_searcherror'))
            no_result_text = self.driver.find_elements_by_class_name('android.widget.TextView')[4].text
            self.assertEqual(no_result_text, '查無相關內容，換個關鍵字試試吧！')
            print('搜尋無結果顯示wording為 :', no_result_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            search_cancel = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/search_cancel')
            search_cancel.click()

            # 自定義搜尋
            search_blank.send_keys('早午')
            search_cancel.click()
            search_blank.send_keys('早午')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            search_keyword = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.assertEqual(search_keyword, '早午')  # Title：顯示搜尋關鍵字名稱
            print('Title有顯示搜尋關鍵字名稱')

            # Tab bar驗證
            store_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
            item_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[3].text
            self.assertEqual(store_tab[0:3], '找店家')
            self.assertEqual(news_tab[0:3], '看報導')
            self.assertEqual(item_tab[0:3], '買東西')
            print('搜尋Tab文字為 : ' + store_tab[0:3] + '、' + news_tab[0:3] + '、' + item_tab[0:3])
            print('搜尋Tab文字正確')
            print('=======找店家=======')

            # 搜尋 - 判斷打電話btn
            phone_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_phone')
            if phone_btn.is_enabled() is True:
                phone_btn.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.asus.contacts:id/dialButton'))
                self.driver.back()
                print('該店家有電話且可撥打')
            else:
                print('該店家沒電話且按鈕反灰')

            # 搜尋 - 判斷看路線btn
            map_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_map')
            if map_btn.is_enabled() is True:
                map_btn.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.google.android.apps.maps:id/search_omnibox_menu_button'))
                self.driver.back()
                print('該店家有地址且可導航')
            else:
                print('該店家沒地址且按鈕反灰')

            # 自定義搜尋 - 收藏店家
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            self.driver.implicitly_wait(3)
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            click_collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            self.assertEqual(click_collection_btn.text, '已收藏')
            print('收藏店家後按鈕文字變為 : ' + collection_btn.text)
            collect_store_checked = bool(collection_btn.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('搜尋店家收藏功能正常')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 自定義搜尋 - 找店家跳轉
            article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            article_text = article.text
            print('自定義搜尋店家為 : ' + article_text)
            article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            direct_article = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            direct_article_text = direct_article.text
            print('自定義搜尋跳轉店家為 : ' + direct_article_text)
            self.assertEqual(article_text, direct_article_text)
            print('自定義搜尋店家功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))

            # 自定義搜尋 - 看報導
            print('=======看報導=======')
            search_news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            search_news_tab.click()
            # 顯示：主圖、標題、日期、收藏
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            print('看報導主圖、標題、日期、收藏有正常顯示')

            # 自定義搜尋 - 收藏報導
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            collect_store_checked = bool(collection_btn.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('搜尋報導收藏功能正常')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 自定義搜尋 - 看報導跳轉
            search_news_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            search_news_article_text = search_news_article.text
            print('自定義搜尋報導為 : ' + search_news_article_text)
            search_news_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.widget.TextView'))
            direct_search_news_article = self.driver.find_elements_by_class_name('android.widget.TextView')[1]
            direct_search_news_article_text = direct_search_news_article.text
            print('自定義搜尋跳轉報導為 : ' + direct_search_news_article_text)
            self.assertEqual(search_news_article_text, direct_search_news_article_text)
            print('自定義搜尋報導功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/navigation_search'))

            # 自定義搜尋 - 買東西跳轉
            print('=======買東西=======')
            search_blank.send_keys('芒果')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            search_item_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[3]
            search_item_tab.click()
            item_keyword = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            print('此次搜尋 : ' + item_keyword)
            search_item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            search_item_text = search_item.text
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_discount'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_price'))
            print('買東西主圖、標題、原價、特價有正常顯示')
            print('自定義搜尋商品為 : ' + search_item_text)
            search_item.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
            print('搜尋商品進入EC頁面成功')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/search_cancel').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_keyword'))
            # direct_search_item = self.driver.find_elements_by_id('store_title')[1]
            # direct_search_item_text = direct_search_item.text
            # print('自定義搜尋跳轉商品為 : ' + direct_search_item_text)
            # self.assertEqual(search_item_text, direct_search_item_text)
            # print('自定義搜尋商品功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/action_icon'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/navigation_search'))

            # # 推薦搜尋
            # search_autocomplete = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_list_autocom')
            # search_autocomplete.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/cbCollection'))
            # article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            # article_text = article.text
            # print('推薦搜尋文章標題為 : ' + article_text)
            # article.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # direct_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            # direct_article_text = direct_article.text
            # print('推薦搜尋跳轉文章標題為 : ' + article_text)
            # self.assertEqual(article_text, direct_article_text)
            # print('推薦搜尋功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/action_icon'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/navigation_search'))
            # search_cancel.click()

            # 熱門搜尋
            print('=======熱門搜尋=======')
            keyword_search = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_keyword')
            keyword_search_text = keyword_search.text[1:]
            print('熱門搜尋文章標籤為 : ' + keyword_search_text)
            keyword_search.click()
            keyword_search_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            print('跳轉搜尋文章標籤為 : ' + keyword_search_title)
            self.assertEqual(keyword_search_text, keyword_search_title)
            print('熱門搜尋引導正確')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/recyclerView_history'))

            # 歷史搜尋
            print('=======歷史搜尋=======')
            self.driver.find_element_by_xpath("//*[@text='#早午']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            article_text = article.text
            print('歷史搜尋文章標題為 : ' + article_text)
            article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            direct_article = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            direct_article_text = direct_article.text
            print('歷史搜尋跳轉標題為 : ' + article_text)
            self.assertEqual(article_text, direct_article_text)
            print('歷史搜尋功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/navigation_search'))

            # 刪除歷史紀錄
            delete_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_delete')
            delete_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/recyclerView_history'))  # 判斷歷史紀錄消失
            print('刪除歷史紀錄功能正常')

            # 自定義搜尋關閉網路
            print('=======網路狀態=======')
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            search_blank.send_keys('早午')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('自定義搜尋關閉網路功能正常')

            # 自定義搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('自定義搜尋開啟網路功能正常')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            search_cancel.click()

            # # 推薦搜尋關閉網路
            # search_blank.send_keys('早午')
            # self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            # search_autocomplete.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_retry'))
            # print('推薦搜尋關閉網路功能正常')
            #
            # # 推薦搜尋開啟網路
            # self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            # sleep(3)
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # print('推薦搜尋開啟網路功能正常')
            # self.driver.back()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/search_cancel'))
            # search_cancel.click()

            # 熱門搜尋關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            keyword_search.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('熱門搜尋關閉網路功能正常')

            # 熱門搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('熱門搜尋開啟網路功能正常')
            self.driver.back()

            # 歷史搜尋關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            self.driver.find_element_by_xpath("//*[@text='#早午']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('歷史搜尋關閉網路功能正常')

            # 歷史搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('歷史搜尋開啟網路功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/hotSearch_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_profileEdit(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 個人資料
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            profile = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member')
            profile.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))

            # 登入TVBS
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rl_modifyPhoto'))

            # 大頭貼
            # photo = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPhoto')
            # photo.click()

            # # 拍照
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/b_takePic').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.asus.camera:id/button_capture'))
            # self.driver.tap([(540, 1800)])
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.asus.camera:id/button_used'))
            # self.driver.find_element_by_id('com.asus.camera:id/button_used').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_confirm'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_confirm').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/rl_modifyPhoto'))
            #
            # # 相簿
            # photo.click()
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/b_choosePic').click()
            # 490 320
            # 修改基本資料
            modify_data = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyData')
            modify_data.click()
            nickname = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyData')
            nickname.click()
            random_nickname = random.choice('abcdefg') + str(random.randint(0, 9999))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPhoto').send_keys(random_nickname)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_save').click()
            # # 修改密碼
            # modify_password = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPassWord')
            # modify_password.click()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/profileEdit_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_myCollection(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 我的收藏
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_my_collection').click()
            self.driver.implicitly_wait(3)

            # 登入TVBS
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('mybooktest0604@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_Title'))

            # 收藏頁面
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_collection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))

            # 關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('\n=======網路狀態=======')
            print('我的收藏關閉網路功能正常')

            # 開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(4)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            # 判斷有無推薦店家
            if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is False:
                print('我的收藏開啟網路功能正常')
                print('=======找店家=======')
                print('當前無推薦店家')
                self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
                    'android.support.v7.app.ActionBar$Tab')[2])
            # 點選收藏
            else:
                print('我的收藏開啟網路功能正常')
                print('=======找店家=======')
                title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
                self.assertEqual(title_text, '更多店家推薦')
                store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
                self.assertEqual(collect_btn_text, "藏口袋")  # 判斷未收藏按鈕文字
                print('收藏店家為 : ' + store_text)
                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collected_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
                self.assertEqual(collected_btn_text, "已收藏")  # 判斷已收藏按鈕文字
                print('收藏按鈕文字變化正確 : ' + collect_btn_text + '->' + collected_btn_text)
                collect_people_count = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_count').text
                collect_people_desc = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_desc').text
                print(collect_people_count + collect_people_desc)

                # 判斷愛心有無填滿
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
                print('收藏後愛心有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article.click()  # 取消收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))

                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
                print('取消收藏後愛心沒有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article.click()  # 再次收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))

                # 返回收藏頁面
                collected_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                self.assertEqual(store_text.replace(" ", ""), collected_store_text.replace(" ", ""))
                print('已收藏的店家為 : ' + collected_store_text)
                print('確認為剛剛收藏的店家，收藏功能正常。')

                # # 更多文章收藏
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
                # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
                # more_article.click()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/action_icon'))
                # sleep(3)
                # for i in range(3):
                #     self.driver.swipe(900, 1500, 900, 300)
                #     sleep(1)
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/cbCollection'))
                # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article.click()  # 收藏推薦文章的第二篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                # sleep(3)
                # print('更多文章收藏功能正常')

                # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article[3].click()  # 收藏推薦文章的第四篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.back()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # print('更多文章收藏功能正常')

                # 收藏店家跳轉
                collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
                collect_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                print('要跳轉的店家為 : ' + collect_store_text)
                collect_store.click()

                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                      'com.tvbs.supertastemvppack:id/iv_img'))
                direct_store_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
                self.assertEqual(collect_store_text.replace(" ", ""), direct_store_text.replace(" ", ""))  # 去除空白
                print('跳轉後的店家為 : ' + direct_store_text)
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('收藏店家跳轉功能正常')

                # 判斷已收藏數量正不正確
                store_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
                self.assertEqual(store_amount, '找店家 1')
                print('店家收藏數量正確')

                # 刪除收藏
                action = TouchAction(self.driver)  # 創建TouchAction物件
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                dialog_text = self.driver.find_element_by_id('android:id/message').text
                self.assertEqual(dialog_text, '確認刪除?')
                print('長按收藏店家可跳出刪除訊息')

                # 取消刪除收藏
                self.driver.find_element_by_id('android:id/button2').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('取消刪除收藏店家功能正常')

                # 確定刪除收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                # 判斷刪除後數量是否有減少
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='找店家 0']"))
                print('確定刪除收藏功能正常')

                # 空收藏
                # action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                # action.perform()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                # self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/btn_more'))
                print('確定刪除所有收藏店家後會顯示"錯過那些必踩點?"按鈕')

            # 看報導
            print('=======看報導=======')
            self.driver.find_elements_by_class_name('android.widget.TextView')[2].click()
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/cl_main') is True:
                    action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                    action.perform()
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                    self.driver.find_element_by_id('android:id/button1').click()
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            self.assertEqual(title_text, '更多報導推薦')
            # 判斷有無推薦報導
            if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_date') is False:
                print('當前無推薦報導')
                self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
                    'android.support.v7.app.ActionBar$Tab')[2])
            else:
                date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
                datetime.datetime.strptime(date_time, '%Y/%m/%d')
                print('文章時間格式正確')
                article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
                print('收藏的報導標題為 : ' + article_text)

                # 點選收藏
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))

                # 判斷愛心有無填滿
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
                print('收藏後愛心有填滿')
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article.click()  # 取消收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/cbCollection'))

                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
                print('取消收藏後愛心沒有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article.click()  # 再次收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article2 = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[3]
                collect_article2.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                self.driver.back()

                # 返回收藏頁面
                collected_article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
                self.assertEqual(article_text, collected_article_text)
                print('已收藏的報導為 : ' + collected_article_text)
                print('確認為剛剛收藏的報導，收藏功能正常。')

                # # 更多文章收藏
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
                # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
                # more_article.click()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/action_icon'))
                # sleep(3)
                # for i in range(3):
                #     self.driver.swipe(900, 1500, 900, 300)
                #     sleep(1)
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/cbCollection'))
                # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article.click()  # 收藏推薦文章的第二篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                # sleep(3)
                # print('更多文章收藏功能正常')

                # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article[3].click()  # 收藏推薦文章的第四篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.back()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # print('更多文章收藏功能正常')

                # 收藏報導跳轉
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
                collect_article_text = collect_article.text
                print('要跳轉的報導為 : ' + collect_article_text)
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
                self.assertEqual(collect_article_text, direct_article_text)
                print('跳轉後的報導為 : ' + direct_article_text)
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('收藏報導跳轉功能正常')

                # 判斷已收藏數量正不正確
                article_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
                self.assertEqual(article_amount, '看報導 2')
                print('報導收藏數量正確')

                # 刪除收藏
                action = TouchAction(self.driver)  # 創建TouchAction物件
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cl_main')[0])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                dialog_text = self.driver.find_element_by_id('android:id/message').text
                self.assertEqual(dialog_text, '確認刪除?')
                print('長按收藏報導可跳出刪除訊息')

                # 取消刪除收藏
                self.driver.find_element_by_id('android:id/button2').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                print('取消刪除報導收藏功能正常')

                # 確定刪除收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_xpath("//*[@text='看報導 1']"))  # 判斷刪除後數量是否有減少

                # 空收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))  # 判斷刪除後數量是否有減少
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/btn_more'))
                print('確定刪除所有收藏店家後會顯示"大家在夯什麼?"按鈕')

            # 買東西
            print('=======買東西=======')
            self.driver.find_elements_by_class_name('android.widget.TextView')[3].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            self.assertEqual(title_text, '更多商品推薦')
            item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            print('收藏的商品為 :' + item.text)
            item.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
            print('進入EC商城')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/myCollection_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_myNotification(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 我的通知 - 文章
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_notifications').click()
            self.driver.implicitly_wait(3)
            notification = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            notification_text = notification.text

            # 判斷日期排序
            first_date = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_date')[0].text
            second_date = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_date')[1].text
            if first_date >= second_date:
                print('\n' + first_date + ' 大於等於 ' + second_date + ' : 文章日期排序正確')
            else:
                print(first_date + ' 小於 ' + second_date + ' : 文章日期排序錯誤')
                assert False

            # 關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            notification.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/button1'))
            print('\n我的通知關閉網路功能正常')

            # 開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(4)
            self.driver.find_element_by_id('android:id/button1').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('我的通知開啟網路功能正常')

            # 判斷通知文章標題
            print('我的通知文章標題為 : ' + notification_text)
            direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            self.assertEqual(notification_text, direct_article_text)
            print('跳轉通知文章標題為 : ' + direct_article_text)
            print('跳轉通知文章標題正確')
            print('我的通知功能正常')
            self.driver.back()
            self.driver.implicitly_wait(3)
            # 會員專屬

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/myNotification_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_officialAccount(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # FB官方帳號
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_FaceBook').click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_FaceBook'))
            print('\n可正確跳轉FB官方帳號')
            self.driver.back()

            # YouTube官方帳號
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_YouTube').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='食尚玩家']"))
            print('可正確跳轉YouTube官方帳號')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.google.android.youtube:id/subtitle'))
            self.driver.back()

            # LINE官方帳號
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Line').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='食尚玩家']"))
            print('可正確跳轉LINE官方帳號')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/OfficialAccount_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_otherSettings(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 推播通知
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rl_Setting').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='Pack 食尚玩家']"))
            print('\n可正確跳轉通知設定')
            self.driver.back()
            self.driver.implicitly_wait(3)

            # 分享APP
            
            # 評分APP

            # 新手教學
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Teching').click()
            self.driver.implicitly_wait(3)
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)
            print('新手教學功能正常')
            self.driver.swipe(900, 1500, 900, 200)
            self.driver.implicitly_wait(3)

            # 購物須知
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Buy_News').click()
            sleep(2)
            self.driver.swipe(900, 1600, 900, 700)
            sleep(2)
            self.driver.tap([(960, 1800)])  # ^按鈕
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('可正確跳轉購物須知')

            # 常見問題
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Question').click()
            sleep(2)
            self.driver.swipe(900, 1600, 900, 700)
            self.driver.implicitly_wait(3)
            self.driver.tap([(960, 1800)])  # ^按鈕
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('可正確跳轉常見問題')

            # 聯絡我們
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Contact_Us').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/subject'))
            self.driver.find_element_by_id('com.google.android.gm:id/subject').send_keys('Automation_' + current_time)
            self.driver.implicitly_wait(3)
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/subject'))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入聯絡我們功能正常')

            # 隱私權政策
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Privacy').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS個資與隱私權聲明']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入隱私權政策功能正常')

            # 會員服務條款
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Service').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS會員服務條款']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入服務條款功能正常')

            # 使用版本
            version = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Version')
            print('APP當前版本為 : ' + version.text)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/otherSettings_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../../report/supertasteAppReport/supertaste_App_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(SuperTaste('test_open'))  # 首頁底部Tab驗證
    # suite.addTest(SuperTaste('test_index'))  # 搖一搖、banner、節目即時看、上方Tab跳轉
    # suite.addTest(SuperTaste('test_hotRecommend'))  # 熱門推薦
    # suite.addTest(SuperTaste('test_relatedNews'))  # 相關報導
    # suite.addTest(SuperTaste('test_collectSearch'))  # 收藏後、取消收藏後搜尋
    # suite.addTest(SuperTaste('test_loginFeature'))  # 大頭貼、登入btn進入登入頁面
    suite.addTest(SuperTaste('test_memberCenterLoginPageCheck'))  # 登入頁面欄位、邏輯
    suite.addTest(SuperTaste('test_memberCenterLoginTVBS'))  # 登入TVBS會員
    suite.addTest(SuperTaste('test_memberCenterLoginFB'))  # 登入FB會員(APP登出狀態)
    suite.addTest(SuperTaste('test_memberCenterRegisterPageCheck'))  # 註冊頁面欄位、邏輯
    suite.addTest(SuperTaste('test_memberCenterRegisterTVBS'))  # 註冊TVBS會員
    suite.addTest(SuperTaste('test_memberCenterRegisterFB'))  # 註冊FB會員
    # suite.addTest(SuperTaste('test_hotSearch'))  # 熱搜
    # suite.addTest(SuperTaste('test_profileEdit'))  # 個人資料編輯(施工中)
    # suite.addTest(SuperTaste('test_myCollection'))  # 口袋
    # suite.addTest(SuperTaste('test_myNotification'))  # 我的通知
    # suite.addTest(SuperTaste('test_officialAccount'))  # 官方帳號
    # suite.addTest(SuperTaste('test_otherSettings'))  # 其他設定
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)
