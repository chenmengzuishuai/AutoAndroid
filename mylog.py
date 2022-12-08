# -*- coding:utf-8 -*-
#  NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
import logging
import time

logger = logging.getLogger("simplelog")
logger.setLevel(logging.DEBUG)


def getdate():
    current = time.localtime()
    date = "{0}{1}{2}{3}{4}{5}".format(current.tm_year,
                                       str(current.tm_mon+100)[-2:],
                                       str(current.tm_mday+100)[-2:],
                                       str(current.tm_hour+100)[-2:],
                                       str(current.tm_min+100)[-2:],
                                       str(current.tm_sec+100)[-2:])
    return date

currentdate = getdate()

fh = logging.FileHandler("%s.log" % currentdate)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")