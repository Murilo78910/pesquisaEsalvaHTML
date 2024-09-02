import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# Solicitar ao usuário que insira seu nome
nome = input("Por favor, insira o que deseja pesquisar: ")

# site desejado
url = "https://www.google.com.br"

# id da caixa de pesquisa
id_input = "APjFqb"

# id para pesquisar
id_pesquisar = "gNO89b"

# id do link
id_link = '//*[@id="tads"]/div/div/div/div/div[1]/a'

# navegador desejado
nav = webdriver.Chrome()

# entra no site
nav.get(url)

# encontra os elementos necessários
input = nav.find_element(By.ID, id_input)

# clica dentro da barra de pesquisa
input.click()

# qual a sua pesquisa?
print(input.send_keys(nome))

# escreve o que vovê digitou
pesquisar = nav.find_element(By.CLASS_NAME, id_pesquisar)

# clica para pesquisar
pesquisar.click()

# esperar carregar
sleep(5)

input2 = nav.find_element(By.XPATH, id_link)
input2.click()

sleep(30)

