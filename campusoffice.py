# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <mh-git@sponc.de> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return - Martin Heistermann
# ----------------------------------------------------------------------------

import urllib2
import cookielib
from urllib import urlencode

def fetchCalendar(start, end, username, password):
    loginParameters = {
            'size':1024,
            'regwaygguid':'',
            'evgguid':'',
            'u': username,
            'p': password,
            }
    loginUrl="https://www.campus.rwth-aachen.de/office/views/campus/redirect.asp"
    icalUrl="https://www.campus.rwth-aachen.de/office/views/calendar/iCalExport.asp"

    icalParameters = {
            'startdt': start,
            'enddt': end,
            }

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
    opener.open(loginUrl, urlencode(loginParameters))
    # TODO: check login success

    return opener.open(icalUrl, urlencode(icalParameters))
