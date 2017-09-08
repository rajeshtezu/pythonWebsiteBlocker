#! /usr/bin/python3

import time
from datetime import datetime as dt

#hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.linkedin.com", "linkedin.com"]

startTime = 16  # start blocking website_list
endTime = 18    # end blocking website_list


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endTime):
        '''Inserting ip address and webstie url. ie; webstie url which needs to be blocked'''
        print("Working time...")
        with open(hosts_path, "r+") as fp:
            content = fp.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    fp.write(redirect + " " + website + "\n")
    else:
        '''Removing ip address and blocked webstie url'''
        print("Fun time...")
        with open(hosts_path, "r+") as fp:
            content = fp.readlines()
            fp.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    fp.write(line)
            fp.truncate()  # Removes content of file after the file pointer location

    time.sleep(5)
