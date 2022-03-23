
#############################################################################################################################
#   filename:send_pdf.py                                                       
#   created: 2022-23-14                                                              
#   import your librarys below                                                    
#############################################################################################################################
from fpdf import FPDF
from time import sleep
from textoContrato import Texto
from get_dados import Dados
from datetime import date
secret = open("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/secrets/secrets.txt", 'r')
secret = list(secret)
#variaveis

path = secret[0]
path = path.replace("\n", "")


dados = Dados()
texto = Texto()

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 10)
data_atual = date.today()
data = data_atual.strftime('%Y%m%d')

#transformações
#reformatando o nome do contratante
nome = dados.nome
nome = nome.replace(" ", "_").lower()


pdf.multi_cell(180, 10,  txt = texto.formatacao, align = 'J')
pdf.output(f"{path}pdf/contract_{nome}_{data}.pdf").encode('cp1252')




