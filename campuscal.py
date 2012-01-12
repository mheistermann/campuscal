#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <mh-git@sponc.de> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return - Martin Heistermann
# ----------------------------------------------------------------------------

import campusoffice
import bottle
from bottle import route, response, abort
import config

@route('/campuscal/<name>')
def get(name):
    try:
        username, password = config.users[name]
    except KeyError:
        abort(404, "no such user in config")

    # TODO: automatic start/end dates
    cal = campusoffice.fetchCalendar(
            config.start,
            config.end,
            username,
            password)
    ical_data = cal.read()

    response.content_type = 'text/calendar; charset=utf-8'
    response.set_header('Cache-Control', 'no-cache')

    return ical_data

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
