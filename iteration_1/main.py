import pyautogui
from time import sleep

# Open Chrome
pyautogui.press("win")

pyautogui.write("Chrome", interval=0.1)
pyautogui.press("enter")

# Wait for Chrome to open
sleep(2)

# Navigate to website
pyautogui.write("yeezy.com", interval=0.1)
pyautogui.press("enter")

# Wait for page to load
sleep(5)

# Click the product
pyautogui.click(300, 300)

# Click add to cart button
pyautogui.click(1500, 800)

# ...

# print(pyautogui.position())
