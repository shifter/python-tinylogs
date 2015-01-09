# TinyLogs:   Logging colored messages to a shell.
# Author:     takeshix <takeshix@adversec.com
# Colors:     http://misc.flogisoft.com/bash/tip_colors_and_formatting
# License:    MIT License
from __future__ import print_function
import sys
import time


class TinyLogs:
    c_info = '\033[1;37m'
    c_success = '\033[1;32m'
    c_warning = '\033[1;33m'
    c_error = '\033[1;31m'
    c_debug = '\033[0;37m'
    c_escape = '\033[0m'
    c_delimiter = '\033[1;1m'
    t_info = 'INFO'
    t_success = 'SUCCESS'
    t_warn = 'WARNING'
    t_error = 'ERROR'
    t_debug = 'DEBUG'

    def __init__(self, debug=False, file=False, multi=False):
        self.DEBUG = debug
        self.file = file
        self.multi = multi

    def _timestamp(self):
        return time.strftime('%H:%M:%S')

    def info(self, msg):
        if self.file:
            log = open(self.file, 'a')
            log.write('[{title}] [{timestamp}] {message}\n'.format(
                title=self.t_info,
                timestamp=self._timestamp(),
                message=str(msg)
            ))
            log.close()

        if (self.file and self.multi) or not self.file:
            print('{D}[{E}{C}{title}{E}{D}]{E} {D}[{E}{C}{timestamp}{E}{D}]{E} {message}'.format(
                title=self.t_info,
                E=self.c_escape,
                D=self.c_delimiter,
                C=self.c_info,
                timestamp=self._timestamp(),
                message=str(msg)
            ))

    def success(self, msg):
        if self.file:
            log = open(self.file, 'a')
            log.write('[{title}] [{timestamp}] {message}\n'.format(
                title=self.t_success,
                timestamp=self._timestamp(),
                message=str(msg)
            ))
            log.close()

        if (self.file and self.multi) or not self.file:
            print('{D}[{E}{C}{title}{E}{D}]{E} {D}[{E}{C}{timestamp}{E}{D}]{E} {message}'.format(
                title=self.t_success,
                E=self.c_escape,
                D=self.c_delimiter,
                C=self.c_success,
                timestamp=self._timestamp(),
                message=str(msg)
            ))

    def warn(self, msg):
        if self.file:
            log = open(self.file, 'a')
            log.write('[{title}] [{timestamp}] {message}\n'.format(
                title=self.t_warn,
                timestamp=self._timestamp(),
                message=str(msg)
            ))
            log.close()

        if (self.file and self.multi) or not self.file:
            print('{D}[{E}{C}{title}{E}{D}]{E} {D}[{E}{C}{timestamp}{E}{D}]{E} {message}'.format(
                title=self.t_warn,
                E=self.c_escape,
                D=self.c_delimiter,
                C=self.c_warning,
                timestamp=self._timestamp(),
                message=str(msg)))

    def error(self, msg):
        if self.file:
            log = open(self.file, 'a')
            log.write('[{title}] [{timestamp}] {message}\n'.format(
                title=self.t_error,
                timestamp=self._timestamp(),
                message=str(msg)
            ))
            log.close()

        if (self.file and self.multi) or not self.file:
            print('{D}[{E}{C}{title}{E}{D}]{E} {D}[{E}{C}{timestamp}{E}{D}]{E} {message}'.format(
                title=self.t_error,
                E=self.c_escape,
                D=self.c_delimiter,
                C=self.c_error,
                timestamp=self._timestamp(),
                message=str(msg)
            ))
        sys.exit()

    def debug(self, msg):
        if self.DEBUG:
            if self.file:
                log = open(self.file, 'a')
                log.write('[{title}] [{timestamp}] {message}\n'.format(
                    title=self.t_error,
                    timestamp=self._timestamp(),
                    message=str(msg)
                ))
                log.close()

            if (self.file and self.multi) or not self.file:
                print('{D}[{E}{C}{title}{E}{D}]{E} {D}[{E}{C}{timestamp}{E}{D}]{E} {message}'.format(
                    title=self.t_debug,
                    E=self.c_escape,
                    D=self.c_delimiter,
                    C=self.c_debug,
                    timestamp=self._timestamp(),
                    message=str(msg)))