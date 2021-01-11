import pyautogui
import win32api,win32con
import time
import keyboard
import cv2
import numpy as np
import random
import PIL as pillow
import threading
# version 2: Changed getpixel to array to speedup search,Added random for use on later days once you buy the temple


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def lmd(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
def lmu(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

b1=(1446,257,1993,653)


im1 = cv2.imread('DayOver.PNG')
a1=np.array(im1)

im2 = cv2.imread('BuyMenu.png')
a2 = np.array(im2)

#Game box Cords
x1 = 1446
y1 = 460
x2 = 260
y2 = 179
#enemy RGB = (204,204,204)
time.sleep(1)
game ={
    'day': 0
}


def day():
    while keyboard.is_pressed('q') == False: 
        if pyautogui.locateOnScreen(a1,region=((b1)),confidence=.70) == None and  pyautogui.locateOnScreen(a2,region=((b1)),confidence=.70) == None :#Getting past day end 
            box = pyautogui.screenshot(region=(x1, y1, x2, y2))#Region where the game is played
            width, hight = box.size #getting the size of the game area use
            for x in range(0,width,1): #search every 5th pixel on x axis
                for y in range(0,hight,1):# search every 5th pixel on y axis
                    rgb= np.array(box.getpixel((x,y)))#RGB
                    if rgb[2] == 204: #Looking for blue color code 204
                        lmd(x+1446, y + 460)
                        #time.sleep(.001)
                        lmu(90+1445, 25 + 259)





def end_screen_one():
  while keyboard.is_pressed('q') == False:  
        if pyautogui.locateOnScreen(a1,region=((b1)),confidence=.70) != None:#Getting past day end
            time.sleep(1)
            click(1808,622)
            time.sleep(2)            
def end_screen_two():
    while keyboard.is_pressed('q') == False:    
        if pyautogui.locateOnScreen(a2,region=((b1)),confidence=.70) != None and game['day'] <3: #getting past buy menu need to expand on this later
            time.sleep(1)
            click(1940, 631)                       
            game['day'] += 1
            print(game['day'])#for debugging seems to not cound right?
            time.sleep(1) 
        if pyautogui.locateOnScreen(a2,region=((b1)),confidence=.70) != None and game['day'] >=3: #getting past buy menu need to expand on this later
            time.sleep(1)
            click(1797, 360)
            time.sleep(1)
            click(1940, 631)
            game['day'] += 1
            print(game['day'])#for debugging seems to not counting right?
t1 = threading.Thread(target=day)
t2 = threading.Thread(target=end_screen_one)
t3 = threading.Thread(target=end_screen_two)

def main():
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    main()
