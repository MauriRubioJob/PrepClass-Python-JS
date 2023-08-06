import time


seconds = 0

while True:
    seconds += 1

    print(seconds // 3600, seconds // 60 % 60, seconds % 60, end="\r")
    time.sleep(0.001)
