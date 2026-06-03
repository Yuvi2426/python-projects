import time
my_time = int(input("enter time for which you would like to rest for:"))
for x in range(my_time, 0, -1):
    seconds = x%60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
while my_time == 0:
    print("you should have some rest")
    my_time = int(input("enter time for which you would like to rest for:"))
else:
    time.sleep(my_time)
    print("times up")