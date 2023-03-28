# O projeto consiste em pedir para o usuario login e senha, e com o selenium entrar em um site e colocar as variaveis no campo.

# 1) Importações
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
# 2) Função responsavel por iniciar o selenium

def iniciar_driver():

    # Cria uma variavel para armezanar a função Options
    chrome_options = Options()


    # cria uma lista com os parametros da options, no final do programa temos uma lista
    arguments = ['--lang=pt-BR']

    # Add os argumentos da lista arguments na variavel chrome_options
    for argument in arguments:
        chrome_options.add_argument(argument)


    # Configurações experimentais, sempre carrega-las
    chrome_options.add_experimental_option('prefs',{
    # alterar o local padrao de download de arquivos
    # 'download.default_directory' : 'local',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade' : True,
    # desabilita a confirmação de dowload
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications' :2,
    # Permite multiplos downloads
    'profile.default_content_setting_values.automatic_downloads' : 1
    })

    


    # Inicializa o webdriver e carrega o chrome_optons
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

    # Inicializa o Wait
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
        NoSuchElementException, # não encontro elemento
        ElementNotVisibleException, # não visivel
        ElementNotSelectableException # não esta disponivel para clicar
        ]

    )

    return driver, wait
driver,wait  = iniciar_driver()
driver.maximize_window()

#driver.implicitly_wait(10) #- Para cada requisição após essa linha, irá esperar 10 segundos

# 3) Inicia a janela com os dados a serem inseridos pelo usuario
login = pag.prompt(text= 'Digite o seu login: ', title= 'APP - VICTOR')
senha = pag.password(text='Digite a sua senha',title= 'APP - VICTOR',mask= '*')

# 4) Acessar o site do email:
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1680007443&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dabed54ef-bd6c-0bd6-23cc-9ba130aa56c3&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
sleep(2)

# 5) Digita a informação de email

# Estou utilizando o wait para deixar mais profissional, com ele dou um intervalo de 10s, porem ele tentara clicar durante esse intervalo
email_login = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//*[@id="i0116"]'))) 
email_login.click()
email_login.send_keys(login)


# 6)Clica no campo de busca
botao1_busca = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]')))
botao1_busca.click()


#7) Digita a informação de senha
email_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//*[@id="i0118"]')))
email_senha.click
email_senha.send_keys(senha)


# 8) clica no campo de busca
botao2_busca = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]')))
botao2_busca.click()

input('')





