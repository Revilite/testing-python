import pyautogui as pai
import time
import random

# X 2380 Y 1039


pai.click(2380, 1039)

for x in range(200):
  pai.typewrite("")
  pai.press("Enter")
  randomInteger = random.randint(2, 60)
  print(randomInteger)
  time.sleep(randomInteger)