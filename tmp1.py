


from datetime import datetime

import time
# chrome --remote-debugging-port=9222 --user-data-dir="F:\Anaconda_Play\selenium" 

# get current time
print(time.time())

print(time.ctime())

print(datetime.now())

a = 1

while True:
    if datetime.now() > datetime.strptime("2022-11-01 23:48:12", "%Y-%m-%d %H:%M:%S"):
        print("Time is up!")
        break

time.sleep(0.001)
