#!/usr/bin/env python3

import os
import sys
from PIL import Image
from concurrent import futures
from multiprocessing import Pool

dir = "/opt/icons/"
if not os.path.exists(dir):
  os.mkdir(dir)
  #os.makedirs(dir)
#t=[]
executor = futures.ProcessPoolExecutor()

def run(infile):
   '''
	Change image to jpeg
	
	Args:
		infile the image name we want to change
   '''

   with Image.open('images/'+infile) as image:
       print(dir+infile)
       image.rotate(90).resize((128,128)).convert('RGB').save(dir+infile, 'jpeg')

if __name__ == "__main__":

  for infile in os.listdir(sys.argv[1]): # os.walk('.'):
    print(infile)
    try:
          #t.append(infile)
          executor.submit(run, infile)
    except OSError as e:
      print(e)


  executor.shutdown()
  # p = Pool(len(t))
  # p.map(run,t)
