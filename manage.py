#!/usr/bin/env python
import os
import sys
import socket  

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    if sys.argv[1] == 'start':
		localIP = socket.gethostbyname(socket.gethostname())
		port = '31500'
		sys.argv[1] = 'runserver'
		sys.argv.append( localIP+":"+port )
		# print sys.argv

    execute_from_command_line(sys.argv)
