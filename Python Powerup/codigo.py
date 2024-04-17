#passo a passo do projeto da Greice
# Passo 1: Entrar no sistema da empresa 
   #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
from sqlite3 import Time
import time
import pyautogui

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# pyautogui.hotkey ("ctrl", "v")

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# abrir o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
#dar uma pausa um pouco maior que (3 segundos)

#Passo 2: Fazer logingreiceboliveira@gmail.com  senha
# selecione o campo do e-mail
pyautogui.click(x=682, y=372)
pyautogui.write("greiceboliveira@gmail.com") #escrever seu e-mail
pyautogui.press("tab") #passando para o proximo campo
pyautogui.write("senha")
pyautogui.click(x=970, y=531) #clique no botão
time.sleep(3)

#Passo 3:Importar a base de produtos greiceboliveira@gmail.com sua senha cadastrar
import pandas as pd

tabela = pd.read_csv("Python Powerup/produtos.csv")

print(tabela)

#Passo 4:Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=661, y=258) #clique no campo de código
    codigo = tabela.loc[linha, "codigo"] #pegar da tabela o campo que queremos preencher
    pyautogui.write(str(codigo)) #preencher o campo
    pyautogui.press("tab") #passar para o proximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) #preencher o campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
       pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") #cadastra o produto (botao enviar)
    #dar scroll de tudo pra cima senha
    pyautogui.scroll(5000)
#Passo 5:Repetir o processo de cadastro até acabar
