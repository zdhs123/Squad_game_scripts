import keyboard
import time

target_key='caps lock'
if_target_key_pressed=False

while True:
    time.sleep(0.1)
    if (not if_target_key_pressed) and keyboard.is_pressed(target_key):
        if_target_key_pressed=True
        keyboard.send('-')
        #print('1')
    elif if_target_key_pressed and (not keyboard.is_pressed(target_key)):
        if_target_key_pressed=False
        #print('2')
        keyboard.send('-')