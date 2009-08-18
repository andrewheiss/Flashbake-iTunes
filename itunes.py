#
#	itunes.py
#
#	Author: Andrew Heiss - http://www.andrewheiss.com
#	Project site: http://github.com/andrewheiss/Flashbake-iTunes/
#	Date: August 18, 2009
#
#	Description: 
#	Frankenscript plugin that takes track information from iTunes via Applescript and adds it to a git commit message with Flashbake
#
#	Version 1.0

import os
import string
from flashbake.plugins import AbstractMessagePlugin

class iTunes(AbstractMessagePlugin):
    def init(self, config):
        """ Nothing needed. """

    def addcontext(self, message_file, config):
        """ Get the track info and write it to the commit message """

        info = trackinfo()

        if info == None:
            message_file.write('Couldn\'t get current track.\n')
        else:
            message_file.write('%s\n' % info)

        return True

def trackinfo():
	"""Call the Applescript file"""
	
	cmd = """osascript ~/.flashbake/plugins/current_track.scpt"""
	
	stdout_handle = os.popen(cmd, "r")
	text = stdout_handle.read()
	
	return text
	