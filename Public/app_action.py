# coding=utf-8
from appium import webdriver
from time import sleep
import sys
import os
sys.path.append('./Public')
from public_tools import app_tool

class action():
    def __init__(self):
        self.desired_caps = {}
        #设备名，设备操作系统，版本，包，Activity，键盘动作，重置键盘
        #自动获取当前设备名
        self.desired_caps['deviceName']=app_tool().get_devicename()
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.1'
        self.desired_caps['appPackage'] = 'com.blm.minidaiapp'
        self.desired_caps['appActivity'] = 'com.blm.minidaiapp.activity.StartActivity'
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] =True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        sleep(3)
    def scrolldown(self,precent=0.5):
        '''页面下啦，输入百分比可控制下拉程度'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y, x * 0.5,y * precent)
    def scrolltop(self,precent=0.5):
        '''页面上拉，输入百分比可控制下拉程度'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5,y * precent, x * 0.5, y )
    def scrollleft(self,precent=0.5):
        '''页面左拉，输入百分比可控制下拉程度'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*precent, y * 0.5,x, y * 0.5)
    def scrollright(self,precent=0.5):
        '''页面右拉，输入百分比可控制下拉程度'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x, y * 0.5,x * precent, y * 0.5)

if __name__=="__main__":
    pass



















