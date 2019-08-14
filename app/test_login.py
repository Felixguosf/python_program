# coding=utf-8
from appium import webdriver
from time import sleep
import unittest
import HtmlTestRunnerCN
class minidai(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'dc8d442',
            'platformVersion': '6.0',
            'appPackage': 'com.blm.minidaiapp',
            'appActivity': 'com.blm.minidaiapp.activity.StartActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(30)
        sleep(3)
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

    def tearDown(self):
        sleep(5)
        self.driver.quit()

if __name__=='__main__':
    suite=unittest.TestSuite()
    for i in range(1,2):
        suite.addTest(minidai('test%d'%i))
    filename='d:\\app.html'
    fp=open(filename,'wb')
    yy=HtmlTestRunnerCN.HTMLTestRunner(stream=fp,title='report',description='info')
    yy.run(suite)
    fp.close()
