# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
#
# https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


import os
import sys
import time
import datetime
import pygame


def create_alarm():
    print("Do you want the alarm to go off at a particular time or after a certain amount of time has passed?\n (1) At a particular time\n (2) After a certain amount of time has passed\n")
    option = input("Select one of the two options (1/2): ")
    set_alarm(option)


def set_alarm(option):
    if option == "1":
        print("\n\n\nAt what time do you want the alarm to go off?\nGive the year (y), month (m), day (d), hour (h), minute (n), and second (s) of the time for the alarm, and input each as its numeric value (a positive integer) followed by whitespace (except for the second unit), in that order. The year must be four digits long and everything else must be two digits long.\n\nSample input: 2017 07 12 23 53 00\n")
        set_clock()
    elif option == "2":
        print("\n\n\nHow long from now do you want the alarm to go off?\nUse days, hours, minutes, and seconds to set the alarm, and input each as a positive integer or float (0 if none).\n")
        set_timer()
    else:
        try:
            os.system("clear")
        except:
            os.system("cls")
        finally:
            create_alarm()


def set_clock():
    while True:
        user_input = input("Enter yyyy mm dd hh nn ss: ")
        time_list = user_input.split(" ")
        try:
            time_list = [int(time_unit) for time_unit in time_list if int(time_unit) >= 0 and "." not in time_unit]
            clock = datetime.datetime(time_list[0], time_list[1], time_list[2], hour=time_list[3], minute=time_list[4], second=time_list[5])
        except:
            print("INVALID INPUT\n")
            continue
        if clock < datetime.datetime.now():
            print("INVALID INPUT: DATETIME HAS ALREADY PASSED\n")
            continue
        else:
            while True:
                wait_time = 0
                if clock == datetime.datetime.now():
                    time.sleep(wait_time)
                    break
        break
    sound_alarm()


def set_timer():
    # Combine prompts and values into a dictionary
    prompts = ["Enter days: ", "Enter hours: ", "Enter minutes: ", "Enter seconds: "]
    values = [86400, 3600, 60, 1]
    wait_time = 0
    index = 0
    for prompt in prompts:
        value = values[index]
        index += 1
        while True:
            prompt_input = 0
            user_input = input(prompt)
            try:
                prompt_input += float(user_input)
            except:
                print("INVALID INPUT: MUST BE INTEGER OR FLOAT\n")
                continue
            if prompt_input < 0:
                print("INVALID INPUT: CANNOT BE NEGATIVE\n")
                continue
            else:
                wait_time += prompt_input * value
                break
    time.sleep(wait_time)
    sound_alarm()


def sound_alarm():
    os.system('say "This is your alarm."')
    print("\nAlarm is going off...\n")
    song = "ready_for_it.ogg"
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(song)
    sound.play(loops=-1)
    while True:
        input("Press enter to turn off alarm: ")
        break
    sound.stop()
    pygame.mixer.quit()
    print("\nAlarm has been turned off.")