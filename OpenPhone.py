# -*- coding:utf-8 -*-
from appium import webdriver
import os
import logging
import logger
class Open():
    try:
        def Phone(self ,appPackage,appActivity,deviceid,port):
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 设备系统
            desired_caps['automationName'] = 'UiAutomator2'
            desired_caps['platformVersion'] = os.popen('adb -s %s shell getprop ro.build.version.release' % deviceid).readlines()[0].strip('\r\n')  # 设备系统版本
            desired_caps['deviceName'] = deviceid # 设备名称
            desired_caps['appPackage'] = appPackage
            desired_caps['appActivity'] = appActivity
            desired_caps['udid'] = deviceid
            #desired_caps['unicodeKeyboard'] = "True"
            #desired_caps['resetKeyboard'] = "True"
            try:
                driver = webdriver.Remote('http://localhost:'+port+'/wd/hub',desired_caps)
                return driver
            except:
                logging.info('%s-appium服务端未开启,请检查'%deviceid)
    except :
        pass

if __name__ == '__main__':
    decice='127.0.0.1:62001'
    #if decice in a:
    driver = Open().Phone('com.tencent.mm', '.ui.LauncherUI', decice, '4723')
    driver.implicitly_wait(50)
    driver.find_element_by_name('注册').click()
    #print driver.find_elements_by_id('com.tencent.mm:id/hz')[0].is_displayed()

    #driver.find_element_by_id('com.dobe.sandbox:id/appIcon').click()
    #driver.find_element_by_name('微信').click()














