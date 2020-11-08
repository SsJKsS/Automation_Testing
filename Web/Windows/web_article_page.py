from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


def article_line_direct(self):
    # 文章內頁 LINE 官方帳號
    print('\n=======LINE 官方帳號=======')
    self.driver.find_element_by_class_name('extended1').find_elements_by_tag_name('a')[0].click()
    self.driver.implicitly_wait(5)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('mdQrCode'))
    print('LINE官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])


def article_youtube_direct(self):
    # 文章內頁 YouTube 官方帳號
    print('\n=======YouTube 官方帳號=======')
    self.driver.find_element_by_class_name('extended1').find_elements_by_tag_name('a')[1].click()
    sleep(1)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    fb_check = False
    if '食尚玩家' in self.driver.page_source:
        fb_check = True
    self.assertTrue(fb_check, '未跳轉到YouTube官方帳號')
    print('YouTube官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])


def article_fb_direct(self):
    # 文章內頁 FB 官方帳號
    print('\n=======FB 官方帳號=======')
    self.driver.find_element_by_class_name('extended1').find_elements_by_tag_name('a')[2].click()
    self.driver.implicitly_wait(5)

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    fb_check = False
    if '食尚玩家' in self.driver.page_source:
        fb_check = True
    self.assertTrue(fb_check, '未跳轉到FB官方帳號')
    print('FB官方帳號跳轉正常 : ' + self.driver.title)
    self.driver.close()
    self.driver.switch_to.window(handles[0])


def article_fb_share(self):
    # 分享文章至 FB
    print('\n=======分享文章至 FB =======')
    self.driver.find_element_by_class_name('community_bar').find_elements_by_tag_name('a')[0].click()

    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[1])
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('email'))
    self.driver.find_element_by_id('email').send_keys('tvbstest0727@gmail.com')  # add your account here
    self.driver.find_element_by_id('pass').send_keys('Tvbs2020')  # add your password here
    self.driver.find_element_by_id('loginbutton').click()
    self.driver.find_element_by_name('__CONFIRM__').click()
    sleep(5)
    # 獲取當前視窗控制代碼集合（列表型別）
    handles = self.driver.window_handles
    self.driver.switch_to.window(handles[-1])
    self.driver.get('https://www.facebook.com/jack.tvbs.5')
    self.driver.implicitly_wait(10)


def article_pre_next(self):
    # 跳轉上一則、下一則文章
    print('\n=======跳轉上一則、下一則文章=======')
    # 上一篇
    pre_article = self.driver.find_element_by_id('bottom_next_href2').text
    self.driver.find_element_by_id('bottom_next_href2').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('margin_b10')[2])
    direct_article_title = self.driver.find_elements_by_class_name('margin_b10')[2].text
    self.assertEqual(pre_article, direct_article_title)

    # 下一篇
    next_article = self.driver.find_element_by_id('bottom_prev_href2').text
    self.driver.find_element_by_id('bottom_prev_href2').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('margin_b10')[2])
    direct_article_title = self.driver.find_elements_by_class_name('margin_b10')[2].text
    self.assertEqual(next_article, direct_article_title)
    print('上下篇文章跳轉正常')


