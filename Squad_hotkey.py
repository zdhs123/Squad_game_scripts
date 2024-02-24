from threading import Thread,Timer
import time
import keyboard
import mouse
from mouse._mouse_event import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE


#放大镜 
mag_key=58#58=caps lock,57=space
mag_triggrt_key=74#Num-键

#小地图
smap_key='m'
#大地图
lmap_key='tab'
#标志位
if_mag_key_pressed=False
# if_mouse_R_pressed=False
# if_mouse_R_pressed_and_maged=False
if_smap_key_pressed=False
if_lmap_key_pressed=False

# def event_mouse_double_click():
#     keyboard.send(74)

def event_mouse_down():
    def mouse_down_thread():
        if mouse.is_pressed(RIGHT):
            keyboard.send(74)
    Timer(0.25,mouse_down_thread).start()

# def event_mouse_up():
#     Thread(target=lambda:()).start()

mouse.on_button(event_mouse_down,(),RIGHT,DOWN)#右键按下0.15秒开镜放大
# mouse.on_button(event_mouse_double_click,(),RIGHT,DOUBLE)#右键双击开镜+放大
# mouse.on_button(event_mouse_up,(),RIGHT,UP)#右键抬起终止线程
# keyboard.remap_key('shift', mag_key)#Win键放大
# keyboard.hook(lambda event:(print(event.name+":("+str(event.scan_code)+'):'+event.event_type )))#调试用显示按键码
keyboard.block_key(91)#禁用win键，防止跳出游戏



while True:
    time.sleep(0.001)
#放大镜
    if (not if_mag_key_pressed) and (keyboard.is_pressed(mag_key)):
        if_mag_key_pressed=True
        keyboard.send(mag_triggrt_key)
        pr_time=time.time()
        #keyboard.send('shift')
    elif if_mag_key_pressed and (not (keyboard.is_pressed(mag_key))):
        if_mag_key_pressed=False
        if time.time()-pr_time>0.25:
            keyboard.send(mag_triggrt_key)               
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
