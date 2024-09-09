import urllib
from IPython.display import display
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.keys import Keys
# pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os


contatos = pd.read_excel('DOMUS_1.xlsx')
display(contatos)

midia = "C:/Users/mathe/DOMUS2.jpeg"


navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
navegador.get("https://web.whatsapp.com/")

# while len(navegador.find_elements_by_id('side')) < 1:
# -> lista for vazia -> que o elemento não existe ainda
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
time.sleep(2)


def enviar_midiaa(midiaa):

    navegador.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
    attach = navegador.find_element(
        By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._3HQNh._1un-p > div._2jitM > div > span > div > div > ul > li:nth-child(1) > button > input[type=file]")

    attach.send_keys(midiaa)
    # attach.send_keys(Keys.ENTER)
    time.sleep(2)
    send = navegador.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
    escrever = navegador.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p').send_keys("")

    time.sleep(2)
    send.click()


for i, mensagem in enumerate(contatos['Mensagem']):

    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Número"]
    texto = urllib.parse.quote(f" {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    # while len(navegador.find_elements_by_id("side")) < 1:
    # -> lista for vazia -> que o elemento não existe ainda
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(5)  # só uma garantia
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        navegador.find_element("xpath",
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(3)

        enviar_midiaa(midia)
        time.sleep(4)
        
        
        
