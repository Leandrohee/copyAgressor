import pyautogui as pa

procura = pa.locateOnScreen('./imgs/comprado.png',confidence=0.9,region=(100,200,300,300))
print(procura)