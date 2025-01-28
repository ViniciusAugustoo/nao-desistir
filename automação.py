import pyautogui as pa
import time
import continuação

x, y = pa.position()
time.sleep(3)

print(f"a posicao do mouse {x}, {y}")

pa.press(832, 64)
