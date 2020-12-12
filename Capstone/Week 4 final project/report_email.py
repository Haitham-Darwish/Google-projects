#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 05:18:49 2020

@author: Haitham Essam
"""

from datetime import date
import os
import reports
import emails


table_data = []

path='supplier-data/descriptions/'
pdf=""
list_of_files = os.listdir(path)
for file in list_of_files:
        with open(path+file) as file:
            #table_data.append(["name",file.readline().strip()])
            #table_data.append([ "weight",file.readline().strip()])
            #table_data.append([""])
            pdf+="name: "+file.readline().strip()+"<br/>weight: "+file.readline().strip()+"<br/><br/>"
            


if __name__ == "__main__":
    attachment ="/tmp/processed.pdf"
    reports.generate_report(attachment,"Processed Update on "+date.today().strftime("%B %d, %Y"), 
                            pdf)
    
    message = emails.generate_email("automation@example.com", 
                          '{}@example.com'.format(os.environ.get("USER")),
                          'Upload Completed - Online Fruit Store',
                          'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
                          attachment)
    
    emails.send_email(message)