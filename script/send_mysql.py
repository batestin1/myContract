
#############################################################################################################################
#   filename:send_mysql.py                                                       
#   created: 2022-03-14                                                              
#   import your librarys below                                                    
#############################################################################################################################

import mysql.connector
from sqlalchemy import create_engine
import json
import pandas as pd
import random


#configs

#connection
banco = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = ""
)

cursor = banco.cursor()

cursor = banco.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS <nomedasuaempresa>')
my_conn = create_engine('mysql+mysqldb://root:@localhost/<nomedasuaempresa>')

### read jsons ### 

data = pd.read_csv("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/download/<nomedasuaempresa> - Formulario.csv", header='infer', index_col= False) 
data.to_sql(con=my_conn, name='clients', if_exists='append', index=False)
print("Carregado com sucesso!")

