# from threading import Thread,Timer
import time
import keyboard
# import mouse
from mouse._mouse_event import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE


#放大镜
mag_key=58#58=caps lock,57=space
mag_triggrt_key=74#74=Num-键
x_key='x'
c_key='c'
z_key='z'
#小地图
smap_key='m'
#大地图    
lmap_key='tab'
#标志位
if_smap_key_pressed=False
if_lmap_key_pressed=False
if_mag_key_pressed=False
if_x_key_pressed=False
if_magnified=False

keyboard.block_key(91)#禁用win键，防止跳出游戏



while True:
    time.sleep(0.001)
#放大镜
    if (not if_mag_key_pressed) and keyboard.is_pressed(mag_key):
        if_mag_key_pressed=True
        if not if_magnified:
            keyboard.send(mag_triggrt_key)
            if_magnified=True
    elif if_mag_key_pressed and (not keyboard.is_pressed(mag_key)):
        if_mag_key_pressed=False
        if if_magnified:
            keyboard.send(mag_triggrt_key)
            if_magnified=False
    # elif if_magnified:
    #     if keyboard.is_pressed('='):      
    #         keyboard.send('*')
    if if_magnified:
        if (not if_x_key_pressed) and (keyboard.is_pressed(z_key) or keyboard.is_pressed(x_key) or keyboard.is_pressed(c_key)):
            if_x_key_pressed=True
            keyboard.send(mag_triggrt_key)
        elif if_x_key_pressed and (not (keyboard.is_pressed(z_key) or keyboard.is_pressed(x_key) or keyboard.is_pressed(c_key))):
            if_x_key_pressed=False
            keyboard.send(mag_triggrt_key)
#限制鼠标活动范围
    # if mouse.get_position()[1]<350:
    #     mouse.move(1269, 769, absolute=True, duration=0)
#小地图
    if (not if_smap_key_pressed) and keyboard.is_pressed(smap_key):
        if_smap_key_pressed=True
        smap_pr_time=time.time()
    elif if_smap_key_pressed and (not keyboard.is_pressed(smap_key)):
        if_smap_key_pressed=False
        keyboard.send(smap_key)
#大地图
    if (not if_lmap_key_pressed) and keyboard.is_pressed(lmap_key):
        if_lmap_key_pressed=True
    elif if_lmap_key_pressed and (not keyboard.is_pressed(lmap_key)):
        if_lmap_key_pressed=False
        keyboard.send(lmap_key)
