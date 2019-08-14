# coding=utf-8
from appium import webdriver
from time import sleep
import unittest
import HtmlTestRunnerCN
class minidai(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:21503',
            'platformVersion': '8.1',
            'appPackage': 'com.blm.minidaiapp',
            'appActivity': 'com.blm.minidaiapp.activity.StartActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(30)
        sleep(3)
    def scrolldown(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.9, x * 0.5,y * 0.1)
    def scrolltop(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5,y * 0.1, x * 0.5, y * 0.9)
    def scrollleft(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.1, y * 0.5,x * 0.9, y * 0.5)
    def scrollright(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.9, y * 0.5,x*0.1, y * 0.5)
    def test1(self):
        '''验证普通用户退出后登录成功'''
        self.driver.find_element_by_name('我的').click()
        sleep(1)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        self.driver.find_element_by_id('iv_my_fragment_user_face').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('安全退出').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('rb_main_my').click()
        sleep(2)
        self.driver.find_element_by_id('btn_my_fragment_login').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('et_login_user_name').clear()
        self.driver.find_element_by_id('et_login_user_name').send_keys('13252320705')
        self.driver.find_element_by_id('et_login_password').send_keys('gsf13252320705')
        self.driver.find_element_by_xpath('//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.implicitly_wait(30)
    def test2(self):
        '''验证自助标投资成功'''
        self.driver.find_element_by_name('出借').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('tv_bid_btn').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('et_money').send_keys('5000')
        self.driver.find_element_by_name('立即出借').click()
    def test3(self):
        '''验证投资散标查看详情页面成功'''
        self.driver.find_element_by_name('出借').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('散标').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('车商贷-沃尔沃S60 #10025530').click()
        self.driver.implicitly_wait(20)
        sleep(2)
        self.scrolldown()
        sleep(2)
        self.driver.find_element_by_name('出借记录').click()
        sleep(2)
        self.driver.find_element_by_name('债权信息').click()
        sleep(3)
        self.driver.find_element_by_name('转让记录').click()
    def test4(self):
        '''验证投资债权转让成功'''
        self.driver.find_element_by_name('出借').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('债权转让').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('tv_finance_transfer').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('btn_finance_adapter_bid').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('et_investment_creditor_money').send_keys('5000')
        self.driver.find_element_by_name('确认出借').click()
    def test5(self):
        '''验证新手指南进入成功'''
        self.driver.find_element_by_id('ll_home_fragment_new_hand').click()
        self.driver.implicitly_wait(20)

    def test6(self):
        '''验证充值金额成功'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        self.driver.find_element_by_name('充值').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('快捷充值').click()
    def test7(self):
        '''验证提现功能正常'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        self.driver.find_element_by_name('提现').click()
        self.driver.implicitly_wait(10)
    def test8(self):
        '''验证出借记录功能正常'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        self.driver.find_element_by_name('出借记录').click()
        self.driver.tap([(54,121),(431,150)])
    def test9(self):
        '''验证回款明细功能正常'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        sleep(1)
        self.driver.find_element_by_name('回款明细').click()
    def test10(self):
        '''验证债权装让功能正常'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        sleep(1)
        self.driver.find_element_by_name('债权装让').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('转让中').click()
        sleep(2)
        self.driver.find_element_by_name('已转让').click()
    def test11(self):
        '''验证债权转让说明进入成功'''
        self.driver.find_element_by_name('我的').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_cunguan_tips_dialog_close').click()
        sleep(1)
        self.driver.find_element_by_name('债权装让').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iv_title_question').click()
    def test12(self):
        '''验证首页下拉进入到推荐页上啦回到首页'''
        self.scrolltop()
        sleep(3)
        self.scrolldown()


    def tearDown(self):
        sleep(5)
        self.driver.quit()

if __name__=='__main__':
    pass
    # suite=unittest.TestSuite()
    # for i in range(1,12):
    #     suite.addTest(minidai('test%d'%i))
    # file='d:\\app.html'
    # f=open(file,"wb")
    # runner=unittest.TextTestRunner()
    # runner=HTMLTestRunnerCN.HTMLTestRunner(stream=f,title='report',description='info')
    # runner.run(suite)
    # f.close()
