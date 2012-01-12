# rwth-campuscal

## Description

CampusOffice is the university course management system used
at RWTH Aachen University.

This script is intended to provide CampusOffice ical data via HTTP without
requiring a HTTP POST login, so campusoffice calendars can easily be added
as external calendars to calendar software.

(I wish CampusOffice would provide easily accessible URL itself, e.g. secured
by a private token)

You will need to run this on a webserver somewhere (maybe even on localhost
for a local calendar client).

*campuscal* also supports multiple user accounts.

**Warning**: be be careful not to leak your config.py, as we cannot avoid
storing the very sensitive CampusOffice passwords.


* Homepage: <https://github.com/mheistermann/rwth-campuscal>
* Author: Martin Heistermann, <mh-git@sponc.de>

## Dependencies

You need to install [bottle.py](http://bottlepy.org/).

## License
    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    <mh-git@sponc.de> wrote this file. As long as you retain this notice you
    can do whatever you want with this stuff. If we meet some day, and you think
    this stuff is worth it, you can buy me a beer in return - Martin Heistermann
    ----------------------------------------------------------------------------
