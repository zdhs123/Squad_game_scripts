#import _thread
import keyboard
import mouse
#from mouse._mouse_event import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
import time


#放大镜
mag_key='caps lock'
mag_triggrt_key=74#Num-键
if_mag_key_pressed=False
#小地图
smap_key='m'
if_smap_key_pressed=False
#大地图    
lmap_key='tab'
if_lmap_key_pressed=False



#mouse.on_button(lambda:keyboard.send(mag_triggrt_key),(),RIGHT,UP)#右键开镜放大
#keyboard.remap_key('shift', mag_key)#Win键放大
#keyboard.hook(lambda event:(print(event.name+":("+str(event.scan_code)+'):'+event.event_type )))#调试用显示按键码
keyboard.block_key(91)#禁用win键，防止跳出游戏



while True:
    time.sleep(0.001)
#放大镜
    if (not if_mag_key_pressed) and keyboard.is_pressed(mag_key):
        if_mag_key_pressed=True
        keyboard.send(mag_triggrt_key)
        #keyboard.send('shift')
    elif if_mag_key_pressed and (not keyboard.is_pressed(mag_key)):
        if_mag_key_pressed=False
        keyboard.send(mag_triggrt_key)
        #keyboard.release('shift')
#小地图
    if (not if_smap_key_pressed) and keyboard.is_pressed(smap_key):
        if_smap_key_pressed=True
    elif if_smap_key_pressed and (not keyboard.is_pressed(smap_key)):
        if_smap_key_pressed=False
        keyboard.send(smap_key)
#大地图
    if (not if_lmap_key_pressed) and keyboard.is_pressed(lmap_key):
        if_lmap_key_pressed=True
    elif if_lmap_key_pressed and (not keyboard.is_pressed(lmap_key)):
        if_lmap_key_pressed=False
        keyboard.send(lmap_key)
