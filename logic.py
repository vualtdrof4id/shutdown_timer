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
