import _thread
import keyboard
import mouse
from mouse._mouse_event import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
import time


#放大镜
mag_key='-'
#   if_mag_key_pressed=False
#小地图
smap_key='m'
if_smap_key_pressed=False
#大地图    
lmap_key='tab'
if_lmap_key_pressed=False
#右键开镜放大
#if_mouse_right_down=False
#def mouse_down_callback():
#    keyboard.send(mag_key)
def mouse_up_callback():
    keyboard.send(mag_key)

#mouse.on_button(mouse_down_callback,(),RIGHT,DOWN)
mouse.on_button(mouse_up_callback,(),RIGHT,UP)


while True:
    time.sleep(0.001)
#放大镜
#    if (not if_mag_key_pressed) and keyboard.is_pressed(mag_key):
#        if_mag_key_pressed=True
#        keyboard.send('-')
#    elif if_mag_key_pressed and (not keyboard.is_pressed(mag_key)):
#        if_mag_key_pressed=False
#        keyboard.send('-')
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
