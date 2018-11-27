#!/usr/bin/python
#-*- coding:utf-8 -*-
import win32con
import win32api
import win32gui
resultId = '1.jpg'
bmpFile='C:/Users/Marketin/Desktop/100.jpg'
print(u'正在设置图片:%s为桌面壁纸...' % resultId)
key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
#2拉伸适应桌面,0桌面居中
win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmpFile, 1+2)
print(u'成功应用图片:%s为桌面壁纸'  % resultId)
