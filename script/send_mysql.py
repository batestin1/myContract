
#############################################################################################################################
#   filename:send_mysql.py                                                       
#   created: 2022-03-14                                                              
#   import your librarys below                                                    
#############################################################################################################################

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
secret = open("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/secrets/secrets.txt", 'r')
secret = list(secret)
#variaveis

path = secret[0]
path = path.replace("\n", "")
nome_empresa = secret[4]
nomecurto = nome_empresa.replace(" ","")





#configs

#connection
banco = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = ""
)

cursor = banco.cursor()

cursor = banco.cursor()
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {nomecurto}')
my_conn = create_engine(f'mysql+mysqldb://root:@localhost/{nomecurto}')

### read jsons ### 

data = pd.read_csv(f"{path}download/dados_contrato.csv", header='infer', index_col= False) 
data.to_sql(con=my_conn, name='clients', if_exists='append', index=False)
print("Carregado com sucesso!")

