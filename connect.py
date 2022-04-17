import uiautomator2 as u2
import os

'''
Connect with device
return d as device
'''



if os.name == 'nt':
    d = u2.connect()
    print(d.info)
else:
    d = u2.connect("192.168.2.2")
