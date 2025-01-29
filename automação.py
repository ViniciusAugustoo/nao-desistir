import pyautogui as pa
import time

time.sleep(2)

x, y = pa.position()

print(f"a posicao do mouse {x}, {y}")

pa.press('win')
time.sleep(1)
pa.write('whatsapp')
time.sleep(1)
pa.press('enter')
time.sleep(4)
pa.click(x=301, y=196)
time.sleep(1)
pa.click(x=578, y=696)
pa.write('fedida mais eu amo')
pa.press('enter')
