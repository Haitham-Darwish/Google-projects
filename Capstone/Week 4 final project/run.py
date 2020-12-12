#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 04:57:52 2020

@author: Haitham Essam
"""
import os
import requests

path='supplier-data/descriptions/'
list_of_files = os.listdir(path)
for file in list_of_files:
        with open(path+file) as f:
            name=f.readline().strip()
            d = {
                    "name":name, 
                    "weight":int(f.readline().strip().strip(" lbs")),
                    "description":f.read().strip(), 
                    "image_name":f.split('.')[0]+".jpeg"}
        response = requests.post('http://localhost/fruits/', data=d)
        print(response.status_code)
