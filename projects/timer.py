print("Welcome to custom countdown and step down timer! ")
import time
start = int(input("Enter starting time in seconds:"))
stop = int(input("Enter a stopping time in seconds:"))
step = int(input("Enter a time to step/skip:"))
step = -step
for x in range(start, stop - 1, step):
     if x == 13:
      continue
     print(x)
     time.sleep(1)
