# coding=utf-8
import os
import re

class app_tool():
    def __init__(self):
        pass

    def get_devicename(self):
        '''通过adb指令获取当前连接PC的设备名'''
        r = os.popen('adb devices')
        info = r.readlines()
        for i in info:
            comp = re.compile('device$')
            if len(re.findall(comp, i)) > 0:
                list = i.split('\t')
                return list[0]

    def get_apkname(self):
        '''获取当前的apkname'''
        for files in os.walk('./../package'):
            appPackage = files[-1][-1]
        return appPackage









