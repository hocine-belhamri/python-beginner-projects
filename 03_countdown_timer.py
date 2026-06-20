import time
ur = int(input("enter the time in seconds: "))
for x in range(ur,0,-1):
    seconds = x % 60
    hours = int(x/3600) 
    minutes = int((x-(hours*3600))/60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME IS OUT!")
     