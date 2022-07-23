import time
bottles = 99
while bottles != 0:
    print(str(bottles) + " bottles of beer on the wall")
    print("Take 1 down, pass it around")
    bottles = bottles - 1 
    time.sleep(1)
print("No bottles left")