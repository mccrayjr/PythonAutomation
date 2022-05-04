#! /usr/bin/env python3
import pyautogui #pyautogui.readthedocs.org

#x and y originates in the the upper left-hand corner of the screen
# x increases right, y increases down

pyautogui.size() #return a tuple of (width, height) so alternatively

width, height = pyautogui.size()

pyautogui.position() #returns current position of the cursor

pyautogui.moveTo(10, 10) #(x, y, duration=1.5) duration is number of seconds it should take
pyautogui.moveRel(200, 0) #move 200 pixles to the right, you can also add duration

pyautogui.click() #self-explanatory lots of keywords availbable in docs can also pass (x, y) coords
pyautogui.rightClick()
pyautogui.doubleClick()

#WARNING: this will hijack your mouse. there is a brief .1 sec delay after each call. If you can slam the mouse to the top left corner pyautogui will raise an exception

#you can use the collowing func in the terminal/CLI to find current mouse position live
pyautogui.displayMousePosition()
