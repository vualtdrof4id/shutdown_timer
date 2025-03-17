import os
import platform
import time

def schedule_shutdown(minutes):
    seconds = minutes * 60
    system = platform.system()
    if system == 'Windows':
        os.system(f'shutdown /s /t {seconds}')
    elif system == 'Linux' or system == 'Darwin':
        os.system(f'shutdown -h +{minutes}')
    print(f'Shutting down in {minutes} minutes')
    return seconds

def cancel_shutdown():
    system = platform.system()
    if system == 'Windows':
        os.system('shutdown /a')
    elif system == 'Linux' or system == 'Darwin':
        os.system('shutdown -c')
    print('Shutdown cancelled')

def countdown_timer(minutes):
    seconds_left = minutes * 60
    while seconds_left > 0:
        minutes_left, seconds = divmod(seconds_left, 60)
        print(f'Time left: {minutes_left:02}:{seconds:02}', end='\r')
        time.sleep(1)
        seconds_left -= 1
    schedule_shutdown(0)