# -*- coding:utf-8 -*-

def launchApp(device, packagename):
    return device.app_start(packagename)

import uiautomator2 as u2
