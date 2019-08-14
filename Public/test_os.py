# coding=utf-8
import os
import re

def get_devicename():
    '''获取设备ID'''
    r = os.popen('adb devices')
    info = r.readlines()
    for i in info:
        comp = re.compile('device$')
        if len(re.findall(comp, i)) > 0:
            list=i.split('\t')
            return list[0]
def get_apkname():
    for files in os.walk('./../package'):
        appPackage=files[-1][-1]
    return appPackage

def get_app_package():
    os.chdir('./../package')
    r=os.popen('aapt dump badging {}'.format(get_apkname()))
    info = r.readlines()
    for i in info:
        print i


