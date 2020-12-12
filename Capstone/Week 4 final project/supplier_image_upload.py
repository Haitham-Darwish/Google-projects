#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 04:47:10 2020

@author: Haitham Essam
"""
import requests
import os
from concurrent import futures

executor = futures.ThreadPoolExecutor()
url = "http://localhost/upload/"

for infile in os.listdir("supplier-data/images"):#os.walk('.'):
    try:
        if "jpeg" in infile:
            print(infile)

            # send the image to the server
            with open("supplier-data/images/"+infile,  'rb') as opened:
                r = executor.submit(requests.post,url, files={'file' : opened})                
                print(r.result().request.body)
                print(r.result().status_code)
           
    except OSError as e:
      print(e)

