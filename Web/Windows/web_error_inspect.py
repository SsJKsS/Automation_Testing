# ERROR判斷
def error_inspect(self):
    # PHP Error
    if 'PHP Error' in self.driver.page_source:
        error_flag = True
        self.assertFalse(error_flag, '網頁出現 ERROR')
    # 特殊字元搜尋Error
    elif 'An Error Was Encountered' in self.driver.page_source:
        error_flag = True
        self.assertFalse(error_flag, '網頁出現 ERROR')

