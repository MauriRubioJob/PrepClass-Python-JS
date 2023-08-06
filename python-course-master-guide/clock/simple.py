import time

seconds = 0
minutes = 0
hours = 0

while True:
    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1

    print(hours, minutes, seconds, end="\r")
    time.sleep(0.01)
