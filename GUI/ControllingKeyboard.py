#! /usr/bin/env python3
import pyautogui

pyautogui.typerwrite("Types the best words", interval=0.2) #sens virtual keypresses => check which field is in focus through .click method; interval adds time between chars

pyautogui.typerwrite(['a', 'b', 'left', 'left', 'X', "y"], interval=0.1) #type a series of chars

pyautogui.KEYBOARD_KEYS() #returns a list of all aavilable keys to press

pyautogui.press('f1') #to press task key

pyautogui.hotkey(['ctrl', 'o']) #to multipress keys
