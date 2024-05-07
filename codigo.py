# Passo a passo do sistema
#   Bibliotacas:
#       pyautogui, time
import pyautogui
import time

#   pyautogui.click -> Clicar com o mouse
#   pyautogui.write -> Escrever um texto
#   pyautogui.press -> Pressionar uma tecla do windows
#   pyautogui.hotkey -> apertar um conjundo de teclas (Ctrl C, Ctrl V, Alt tab)

#   1. Abrir o sistema da empresa

#       Abrir o navegardor (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=716, y=370)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

#pyautogui.press("tab")
#print(pyautogui.position())

#       Entrar no sistema da empresa
#       https://dlp.hashtagtreinamentos.com/python/intensivao/login     
#   2. Fazer login
#   3. Abrir/importar a base de dados de produtos para cadastrar
#   4. Cadastrar um produto
#   5. repetir isso tudo até acabar a lista de produtos

