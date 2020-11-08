# initial setting
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# initial setting
def setUp(self):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0',
        'deviceName': 'ce031713bc2694670d',  # S8+(8.0) : ce031713bc2694670d, HTC(9.0) NE9CF1S01374
        'appPackage': 'com.tvbs.supertastemvppack',
        'appActivity': 'com.tvbs.supertaste.ui.activity.SplashActivity',
        'autoGrantPermissions': True
    }

    self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 連接Appium
    self.driver.implicitly_wait(8)
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def init(self):
    # 新手教學
    for i in range(3):
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        self.driver.implicitly_wait(3)

    # 立即逛逛btn
    self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
    self.driver.implicitly_wait(3)


def login_email(self):
    # 執行Email登入
    WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_xpath("//*[@text='登入']"))  # 等待【會員登入】頁出現
    self.driver.implicitly_wait(1)
    account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')  # 定位帳號欄位
    self.driver.implicitly_wait(1)
    password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')  # 定位密碼欄位
    account_blank.send_keys('freyjachen0008@gmail.com')  # 帳號欄位傳值
    self.driver.implicitly_wait(1)
    password_blank.send_keys('a123456')  # 密碼欄位傳值
    self.driver.implicitly_wait(6)
    self.driver.find_element_by_xpath("//*[@text='登入']").click()  # Click「登入」button
    # sleep(10)  # 登入動作較久，必須強制等待

    print('已登入Email')


def find_specific_str(self, className, specificStr):
    # tab1 = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[0]  # 找店家 %d
    content_desc = className.get_attribute('content-desc')
    # 【找關鍵字】【方法一】
    print('\t要搜尋的字串為：『' + content_desc + '』')  # 96 找店家 0
    if specificStr in content_desc:  # 使用in運算子檢查
        print('\t字串中有\'' + specificStr + '\'')
    else:
        print('\t字串中沒有\'' + specificStr + '\'')
        self.assertFalse(specificStr, '找不到指定字串')
    # 【找關鍵字】【方法二】
    # pos = content_desc.find(specificStr)
    # if pos >= 0:  # 有找到
    #     print('字串中有\'' + specificStr + '\'')
    # else:  # 沒有找到
    #     print('字串中沒有\'' + specificStr + '\'')
    #     self.assertFalse(specificStr, '找不到指定字串')

    print(len(content_desc))  # 5
    print(content_desc[4:len(content_desc)])  # 0
    print(int(content_desc[4:len(content_desc)]))  # 0

    print('\t找到字串 : ' + specificStr)


def pocket_list(self):
    flag = True
    # noinspection PyBroadException
    try:
        self.driver.implicitly_wait(6)

        # 關掉【新手教學頁】
        init(self)

        self.driver.implicitly_wait(1)
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            'com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
        self.driver.implicitly_wait(1)
        pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
        self.driver.implicitly_wait(2)
        pocket_tab.click()  # Click「口袋」button

        # 執行Email登入
        login_email(self)
        print('Test Case Pass : 825')

        #
        sleep(6)
        WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id(
            'com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
        pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
        pocket_tab.click()  # Click「口袋」button
        sleep(6)
        # WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/tv_title'))
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='口袋清單']"))  # 等待【口袋清單】頁出現
        print('\t開【口袋清單頁】')
        print('Test Case Pass : 826')

        back = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon')  # ＜返回鍵
        title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')  # title
        self.driver.implicitly_wait(1)
        self.assertEqual(title.text, '口袋清單')
        print('\t左：＜返回鍵')
        print('\tTitle：顯示『口袋清單』')
        print('Test Case Pass : 827')

        tab1 = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[0]  # 找店家 %d
        tab2 = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]  # 看報導 %d
        tab3 = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2]  # 買東西 %d
        # 尋找指定字串『找店家』、『看報導』、『看報導』是否存在
        find_specific_str(self, tab1, '找店家')
        find_specific_str(self, tab2, '看報導')
        find_specific_str(self, tab3, '買東西')
        print('Test Case Pass : 828')

        tab1_is_selected = bool(tab1.is_selected())
        self.assertTrue(tab1_is_selected, "畫面沒有預設在「找店家」Tab")
        print('\t畫面預設在「找店家」Tab')
        print('Test Case Pass : 829')

    except:
        flag = False
        if flag is False or Exception:
            self.driver.save_screenshot(
                '../../screenshot/supertasteAppFail/otherSettings_Fail_{}.png'.format(current_time))
            self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()

# def test_myCollection(self):
#
#         # 我的收藏
#         self.driver.find_element_by_xpath("//*[@text='我的']").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/iv_my_collection').click()
#         self.driver.implicitly_wait(3)
#
#         # 登入TVBS
#         # 定位帳號欄位
#         account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
#         # 定位密碼欄位
#         password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
#         # 帳號欄位傳值
#         account_blank.send_keys('mybooktest0604@gmail.com')
#         # 密碼欄位傳值
#         password_blank.send_keys('s23321286')
#         self.driver.find_element_by_xpath("//*[@text='登入']").click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/tv_Title'))
#
#         # 收藏頁面
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_collection').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more'))
#
#         # 關閉網路
#         self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
#         self.driver.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_retry'))
#         print('\n=======網路狀態=======')
#         print('我的收藏關閉網路功能正常')
#
#         # 開啟網路
#         self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
#         sleep(4)
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
#         # 判斷有無推薦店家
#         if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is False:
#             print('我的收藏開啟網路功能正常')
#             print('=======找店家=======')
#             print('當前無推薦店家')
#             self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
#                 'android.support.v7.app.ActionBar$Tab')[2])
#         # 點選收藏
#         else:
#             print('我的收藏開啟網路功能正常')
#             print('=======找店家=======')
#             title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
#             self.assertEqual(title_text, '更多店家推薦')
#             store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
#             collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
#             self.assertEqual(collect_btn_text, "藏口袋")  # 判斷未收藏按鈕文字
#             print('收藏店家為 : ' + store_text)
#             collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             collect_article.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collected_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
#             self.assertEqual(collected_btn_text, "已收藏")  # 判斷已收藏按鈕文字
#             print('收藏按鈕文字變化正確 : ' + collect_btn_text + '->' + collected_btn_text)
#             collect_people_count = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_count').text
#             collect_people_desc = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_desc').text
#             print(collect_people_count + collect_people_desc)
#
#             # 判斷愛心有無填滿
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
#             print('收藏後愛心有填滿')
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             collect_article.click()  # 取消收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#
#             collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
#             print('取消收藏後愛心沒有填滿')
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article.click()  # 再次收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             self.driver.back()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#
#             # 返回收藏頁面
#             collected_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
#             self.assertEqual(store_text.replace(" ", ""), collected_store_text.replace(" ", ""))
#             print('已收藏的店家為 : ' + collected_store_text)
#             print('確認為剛剛收藏的店家，收藏功能正常。')
#
#             # # 更多文章收藏
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
#             # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
#             # more_article.click()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/action_icon'))
#             # sleep(3)
#             # for i in range(3):
#             #     self.driver.swipe(900, 1500, 900, 300)
#             #     sleep(1)
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/cbCollection'))
#             # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article.click()  # 收藏推薦文章的第二篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             # sleep(3)
#             # print('更多文章收藏功能正常')
#
#             # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article[3].click()  # 收藏推薦文章的第四篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.back()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # print('更多文章收藏功能正常')
#
#             # 收藏店家跳轉
#             collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
#             collect_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
#             print('要跳轉的店家為 : ' + collect_store_text)
#             collect_store.click()
#
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_img'))
#             direct_store_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
#             self.assertEqual(collect_store_text.replace(" ", ""), direct_store_text.replace(" ", ""))  # 去除空白
#             print('跳轉後的店家為 : ' + direct_store_text)
#             self.driver.back()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#             print('收藏店家跳轉功能正常')
#
#             # 判斷已收藏數量正不正確
#             store_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
#             self.assertEqual(store_amount, '找店家 1')
#             print('店家收藏數量正確')
#
#             # 刪除收藏
#             action = TouchAction(self.driver)  # 創建TouchAction物件
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             dialog_text = self.driver.find_element_by_id('android:id/message').text
#             self.assertEqual(dialog_text, '確認刪除?')
#             print('長按收藏店家可跳出刪除訊息')
#
#             # 取消刪除收藏
#             self.driver.find_element_by_id('android:id/button2').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#             print('取消刪除收藏店家功能正常')
#
#             # 確定刪除收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             # 判斷刪除後數量是否有減少
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='找店家 0']"))
#             print('確定刪除收藏功能正常')
#
#             # 空收藏
#             # action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             # action.perform()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             # self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/btn_more'))
#             print('確定刪除所有收藏店家後會顯示"錯過那些必踩點?"按鈕')
#
#         # 看報導
#         print('=======看報導=======')
#         self.driver.find_elements_by_class_name('android.widget.TextView')[2].click()
#         while True:
#             if self.is_element_exist('com.tvbs.supertastemvppack:id/cl_main') is True:
#                 action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#                 action.perform()
#                 WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#                 self.driver.find_element_by_id('android:id/button1').click()
#             else:
#                 break
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more'))
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/action_icon'))
#         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
#         self.assertEqual(title_text, '更多報導推薦')
#         # 判斷有無推薦報導
#         if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_date') is False:
#             print('當前無推薦報導')
#             self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
#                 'android.support.v7.app.ActionBar$Tab')[2])
#         else:
#             date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
#             datetime.datetime.strptime(date_time, '%Y/%m/%d')
#             print('文章時間格式正確')
#             article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
#             print('收藏的報導標題為 : ' + article_text)
#
#             # 點選收藏
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#
#             # 判斷愛心有無填滿
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
#             print('收藏後愛心有填滿')
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article.click()  # 取消收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/cbCollection'))
#
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
#             print('取消收藏後愛心沒有填滿')
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article.click()  # 再次收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article2 = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[3]
#             collect_article2.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             self.driver.back()
#
#             # 返回收藏頁面
#             collected_article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
#             self.assertEqual(article_text, collected_article_text)
#             print('已收藏的報導為 : ' + collected_article_text)
#             print('確認為剛剛收藏的報導，收藏功能正常。')
#
#             # # 更多文章收藏
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
#             # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
#             # more_article.click()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/action_icon'))
#             # sleep(3)
#             # for i in range(3):
#             #     self.driver.swipe(900, 1500, 900, 300)
#             #     sleep(1)
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/cbCollection'))
#             # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article.click()  # 收藏推薦文章的第二篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             # sleep(3)
#             # print('更多文章收藏功能正常')
#
#             # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article[3].click()  # 收藏推薦文章的第四篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.back()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # print('更多文章收藏功能正常')
#
#             # 收藏報導跳轉
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
#             collect_article_text = collect_article.text
#             print('要跳轉的報導為 : ' + collect_article_text)
#             collect_article.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
#             self.assertEqual(collect_article_text, direct_article_text)
#             print('跳轉後的報導為 : ' + direct_article_text)
#             self.driver.back()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#             print('收藏報導跳轉功能正常')
#
#             # 判斷已收藏數量正不正確
#             article_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
#             self.assertEqual(article_amount, '看報導 2')
#             print('報導收藏數量正確')
#
#             # 刪除收藏
#             action = TouchAction(self.driver)  # 創建TouchAction物件
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cl_main')[0])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             dialog_text = self.driver.find_element_by_id('android:id/message').text
#             self.assertEqual(dialog_text, '確認刪除?')
#             print('長按收藏報導可跳出刪除訊息')
#
#             # 取消刪除收藏
#             self.driver.find_element_by_id('android:id/button2').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             print('取消刪除報導收藏功能正常')
#
#             # 確定刪除收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(
#                 lambda x: x.find_element_by_xpath("//*[@text='看報導 1']"))  # 判斷刪除後數量是否有減少
#
#             # 空收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(
#                 lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))  # 判斷刪除後數量是否有減少
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/btn_more'))
#             print('確定刪除所有收藏店家後會顯示"大家在夯什麼?"按鈕')
#
#         # 買東西
#         print('=======買東西=======')
#         self.driver.find_elements_by_class_name('android.widget.TextView')[3].click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more'))
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/iv_channel'))
#         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
#         self.assertEqual(title_text, '更多商品推薦')
#         item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
#         print('收藏的商品為 :' + item.text)
#         item.click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
#         print('進入EC商城')
#
#     except:
#         flag = False
#         if flag is False or Exception:
#             self.driver.save_screenshot(
#                 '../../screenshot/supertasteAppFail/myCollection_Fail_{}.png'.format(current_time))
#             self.assertTrue(flag, 'Execute Fail.')