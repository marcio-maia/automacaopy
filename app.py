#   4 - Clicar em entrar
#   5 - Clicar em cada campo e preencher com as informações extraidas da planilhas
#   6 - Clicar em cadastrar
#   7 - Repito os passos 5 e 6

# Bibliotecas:
from selenium import webdriver # Navegador
from selenium.webdriver.common.by import By # Permite selecionar campos e interagir com eles
from time import sleep # Para usar pausas entre taréfas
import openpyxl # para automação de planilhas

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


#   1 - Navegar até o site https://contabilidade-devaprender.netlify.app/
options = webdriver.ChromeOptions()
#drive = webdriver.Chrome()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=options)


drive.get("https://platform.senior.com.br/login/?redirectTo=https%3A%2F%2Fplatform.senior.com.br%2Fsenior-x%2F&tenant=plansulsc.com.br")
sleep(3)


#   2 - Digitar e-mail e a senha
usuario = drive.find_element(By.XPATH,"//input[@id='username-input-field']")
usuario.send_keys('162761')

senha= drive.find_element(By.XPATH,"//input[@id='password-input-field']")
sleep(1)
senha.send_keys('07472')

botao_entrar = drive.find_element(By.XPATH,"//button[@id='loginbtn']")
sleep(1)
botao_entrar.click()
sleep(3)

#clickable = drive.find_elements(By.XPATH, "//app-menu-item[@id='menu-item-3']")
clickable = drive.find_element(By.XPATH, "//app-menu-item[@id='menu-item-3']")
ActionChains(drive)\
        .click(clickable)\
        .perform()   

sleep(1)
menu2 = drive.find_element(By.XPATH,"//em[@id='apps-menu-item-icon-Marcação-de-ponto-2.0']")
ActionChains(drive)\
        .click(menu2)\
        .perform()  

sleep(1)  
menu3 = drive.find_element(By.XPATH,"//a[@id='apps-menu-item-0']")
ActionChains(drive)\
        .click(menu3)\
        .perform() 
