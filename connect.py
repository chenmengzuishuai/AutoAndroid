import uiautomator2 as u2
import os

if os.name == 'nt':
    d = u2.connect()
    print(d.info)
else:
    d = u2.connect("0.0.0.0")
