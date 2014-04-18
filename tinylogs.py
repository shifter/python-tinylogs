'''
TinyLogs: Logging colored messages to a shell.
Author:  takeshix <takeshix@adversec.com
Color reference: http://misc.flogisoft.com/bash/tip_colors_and_formatting
'''
from __future__ import print_function
from time import strftime
from sys import exit

class TinyLogs:
    def __init__(self,debug=False):
        self.c_info = '\033[1;37m'
        self.c_success = '\033[1;32m'
        self.c_warning = '\033[1;33m'
        self.c_error = '\033[1;31m'
        self.c_debug = '\033[0;37m' 
        self.c_escape = '\033[0m'
        self.c_delimiter = '\033[1;1m'
        self.DEBUG = debug

    def timestamp(self):
        return strftime('%H:%M:%S')

    def info(self,msg): 
        print('{D}[{E}{C}INFO{E}{D}]{E} {D}[{E}{C}{T}{E}{D}]{E} {S}'.format(
                E=self.c_escape,D=self.c_delimiter,C=self.c_info,T=self.timestamp(),S=str(msg)))

    def success(self,msg): 
        print('{D}[{E}{C}SUCCESS{E}{D}]{E} {D}[{E}{C}{T}{E}{D}]{E} {S}'.format(
                E=self.c_escape,D=self.c_delimiter,C=self.c_success,T=self.timestamp(),S=str(msg)))

    def warning(self,msg):
        print('{D}[{E}{C}WARNING{E}{D}]{E} {D}[{E}{C}{T}{E}{D}]{E} {S}'.format(
                E=self.c_escape,D=self.c_delimiter,C=self.c_warning,T=self.timestamp(),S=str(msg)))

    def error(self,msg):
        print('{D}[{E}{C}ERROR{E}{D}]{E} {D}[{E}{C}{T}{E}{D}]{E} {S}'.format(
                E=self.c_escape,D=self.c_delimiter,C=self.c_error,T=self.timestamp(),S=str(msg)))
        exit()

    def debug(self,msg):
        if self.DEBUG:
            print('{D}[{E}{C}DEBUG{E}{D}]{E} {D}[{E}{C}{T}{E}{D}]{E} {S}'.format(
                E=self.c_escape,D=self.c_delimiter,C=self.c_debug,T=self.timestamp(),S=str(msg)))
