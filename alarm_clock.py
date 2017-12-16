# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
#
# https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


import time
import os
import sys


def create_alarm():
    print("How would you like to set your alarm?\n (1) Local clock time\n (2) Seconds\n (3) Minutes\n (4) Hours\n (5) Combination of seconds, minutes, & hours")
    user_input = int(input("Choose one of the options (1-5): "))
    set_alarm(user_input)
    return


def set_alarm(user_input):
    if user_input == 1:
        year = int(input("Enter year: "))
        day = int(input("Enter day: "))
        hour = int(input("Enter hour: "))
        minute = int(input("Enter minute: "))
        second = int(input("Enter second: "))
        pass
    elif user_input == 2:
        wait_time = int(input("Enter wait time in seconds: "))
        # time.sleep(wait_time)
        sound_alarm(wait_time)
    elif user_input == 3:
        wait_time = int(input("Enter wait time in minutes: ")) * 60
        # time.sleep(wait_time)
        sound_alarm(wait_time)
    elif user_input == 4:
        wait_time = int(input("Enter wait time in hours: ")) * 3600
        # time.sleep(wait_time)
        sound_alarm(wait_time)
    elif user_input == 5:
        seconds = int(input("Enter seconds: "))
        minutes = int(input("Enter minutes: "))
        hours = int(input("Enter hours: "))
        wait_time = (hours * 3600) + (minutes * 60) + seconds
        # time.sleep(wait_time)
        sound_alarm(wait_time)
    else:
        try:
            os.system("cls") # If OS is Windows
            main()
        except:
            os.system("clear") # If OS is Linux or Mac
            main()


def sound_alarm(wait_time):
    time.sleep(wait_time)
    os.system('say "This is your alarm."')
    for ring in range(5):
        sys.stdout.write("\a")
        # print("\a")
        # print("lol")
        # sys.stdout.flush()
    #     time.sleep(2)
    sys.stdout.flush()