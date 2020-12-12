#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 04:12:28 2020

@author: Haitham Essam
"""

import os
from PIL import Image
from concurrent import futures

executor = futures.ProcessPoolExecutor()
path = "supplier-data/images/"
def run(infile):
   '''
	Change image to  resize it, jpeg, convert
    it to RGB and save it at the same file
	
	Args:
		infile the image name we want to change
   '''

   with Image.open(path+infile) as image:
       # Resize the image to 600x400 
       # Change it to RGB (3 channel)  instead of RGBA (4 channel) which has 
       # Opacity also, save file as jpeg at the same file directory
       
       infile = infile.split(".")[0]+".jpeg"
       image.resize((600,400)).convert('RGB').save(path+infile, 'jpeg')

if __name__ == "__main__":
    
  # Walk throgh all images that are in this folder
  for infile in os.listdir(path):#os.walk(path):
    try:
          # run many image at same time to save tome (Multiprocessing)
          executor.submit(run, infile)
    except OSError as e:
      print(e)


  executor.shutdown()
 
