#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 05:54:07 2020

@author: pc
"""

import shutil
import psutil
import emails
import os
import socket

disk=shutil.disk_usage('.')
available_disk = disk.free/disk.total
subject_line=""
if available_disk <0.2:
    subject_line += "Error - Available disk space is less than 20% "
    
if psutil.cpu_percent() > 80:
    subject_line += "Error - CPU usage is over 80% "
    
if (psutil.virtual_memory().available>>20) < 500:
    subject_line += "Error - Available memory is less than 500MB "
    
if socket.gethostbyname('localhost') == "127.0.0.1":
    subject_line += "Error - localhost cannot be resolved to 127.0.0.1 "

    
message = emails.generate_email("automation@example.com", 
                          '{}@example.com'.format(os.environ.get("USER")),
                          subject_line,
                          'Please check your system and resolve the issue as soon as possible.')
    
emails.send_email(message)