import pyautogui as gui
import time
import pyperclip as ppc

gui.PAUSE = 1
gui.press('win')
gui.write('chrome')
gui.press('enter')
time.sleep(2)

for i in [713,714,889]:
    gui.hotkey('ctrl','t')
    ppc.copy('http://dataimesc.imesc.ma.gov.br/series/'+str(i)+'/show')
    gui.hotkey('ctrl', 'v')
    gui.press('enter')

gui.alert('End')
