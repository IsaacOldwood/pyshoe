import pyautogui
from time import sleep

pyautogui.press("win")

pyautogui.write("Chrome", interval=0.1)
pyautogui.press("enter")

sleep(2)

pyautogui.write("yeezy.com", interval=0.1)
pyautogui.press("enter")

sleep(5)

pyautogui.click(300, 300)

pyautogui.click(1500, 800)

# ...

# print(pyautogui.position())
