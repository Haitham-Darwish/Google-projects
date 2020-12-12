# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:08:24 2020

@author: pc
"""

#!/usr/bin/env python3
import re
import operator
import csv

per_user = dict()
error = dict()
per_user_dict = dict()
with open("syslog.log") as f:
  for line in f.readlines():
    search  = re.search(r"ERROR [\w' ]* ", line)
    user = re.search(r'\([\w.]+\)', line).group()[1:-1]
    #print(line)
   # print(user)
    if search:
        print(line)
        print(search.group())
        error[search.group()[6:]] = error.get(search.group()[6:], 0) + 1
        per_user[user] = per_user.get(user, {"Error":0, "INFO":0})
        per_user[user]["Error"] =(
                per_user[user]["Error"] + 1)
    else:
        per_user[user] = per_user.get(user, {"Error":0, "INFO":0})
        #print(per_user[user]["INFO"])
        per_user[user]["INFO"] =(
                per_user[user]["INFO"] + 1)
per_user = sorted(per_user.items(), key=operator.itemgetter(0))
per_user_list = []
for user in per_user:
    per_user_list.append({"Username":user[0], "INFO":user[1]["INFO"], "Error":user[1]["Error"]})
    #print({"Username":user[0], "Error":user[1]["Error"], "INFO":user[1]["INFO"]})

error_list = []
error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
#print(error)

for er in error:
   # print(er)
    error_list.append({"Error":er[0], "Count":er[1]})
    
# print(error)

keys=["Error","Count"]
with open("error_message.csv", "w") as error_csv:
     writer = csv.DictWriter(error_csv, fieldnames=keys)
     writer.writeheader()
     writer.writerows(error_list)

keys=["Username", "INFO", "Error"]
with open("user_statistics.csv", "w") as error_csv:
     writer = csv.DictWriter(error_csv, fieldnames=keys)
     #writer = csv.writer(error_csv)
     writer.writeheader()
     writer.writerows(per_user_list)     
    