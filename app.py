import pyautogui as pag
import time as t
import os

os.system("xdg-open http://200.133.203.133/home")
t.sleep(1)

pag.press("tab")
pag.press("tab")
pag.press("tab")

pag.write("PT304775X")
pag.press("tab")
pag.press("enter")
