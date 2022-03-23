
#############################################################################################################################
#   filename:dadosContrante.py                                                       
#   created: 2022-03-14                                                              
#   import your librarys below                                                    
#############################################################################################################################

import requests
import pandas as pd
import json
data = pd.read_csv("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/download/<nomedasuaempresa> - Formulario.csv", header='infer', index_col= False)

class Dados():
    def __init__(self) -> None:
        for i in range(data.shape[0]):
            self.nome = data['NOME DO CONTRATANTE'][i].upper()
            self.email = data['EMAIL DO CONTRATANTE'][i].lower()
            self.tel = data['TELEFONE DO CONTRATANTE'][i]
            self.cpf = data['CPF DO CONTRANTANTE'][i]
            self.niver = data['DATA DE NASCIMENTO'][i]
            cep = data['CEP DO CONTRATANTE'][i]
            cep = str(cep)
            if len(cep) < 8:
                self.cep = cep.zfill(8)
            else:
                self.cep = cep
            url = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
            self.endereco = url["logradouro"].upper()
            self.bairro = url['bairro'].upper()
            self.cidade = url['localidade'].upper()
            self.uf = url['uf'].upper()
            complemento = url['complemento'].upper()
            if complemento == '':
                self.complemento = "NENHUM"
            else:
                self.complemento = complemento.upper()
            self.nomeEspaco = data['NOME DO ESPAÇO(BUFFET, OU SEMELHANTES)'][i].upper()
            self.num = data['NÚMERO DA RESIDÊNCIA'][i]
            self.tipo = data['TIPO DE EVENTO A SER REALIZADO'][i].upper()
            cep_espaco = data['CEP DO ESPAÇO'][i]
            cep_espaco = str(cep_espaco)
            if len(cep_espaco) < 8:
                self.cep_espaco = cep_espaco.zfill(8)
            else:
                self.cep_espaco = cep_espaco
            url = requests.get(f"https://viacep.com.br/ws/{self.cep_espaco}/json/").json()
            self.enderecoEvento = url["logradouro"].upper()
            self.bairroEvento = url['bairro'].upper()
            self.cidadeEvento = url['localidade'].upper()
            self.ufEvento = url['uf'].upper()
            complementoEvento = url['complemento'].upper()
            if complementoEvento == '':
                self.complementoEvento = "NENHUM"
            else:
                self.complementoEvento = complementoEvento.upper()
            self.dataEvento = data['DATA DO EVENTO'][i]
            self.horario = data['HORARIO DO EVENTO'][i]
            self.totalHoras = data['TOTAL DE HORAS ACORDADO COM A EQUIPE'][i]
            self.formaPagamento = data['FORMA DE PAGAMENTO'][i]
            valorAcordo = data['VALOR TOTAL ACORDADO ENTRE AS PARTES'][i]
            self.valorAcordo = float(valorAcordo)
            self.totalParcelas = data['TOTAL DE PARCELAS'][i]
            valorParcela = data['VALOR DE CADA PARCELA'][i]
            self.valorParcela = float(valorParcela)
            valorEntrada = data['VALOR ENTRADA'][i]
            self.valorEntrada = float(valorEntrada)
            if self.formaPagamento == "À VISTA":
                self.textoValor = f"""O presente serviço será remunerado pela quantia de R$:{self.valorAcordo}, referente aos serviços efetivamente prestados, devendo ser pago na seguinte condição: {self.formaPagamento}. O pagamento só poderá ser aceito por transferência, e PIX para o seguinte endereço eletrônico: PIX: <pix> banco <banco> favorecido: <favorecido>."""
            else:
                self.textoValor = f"""O presente serviço será remunerado pela quantia de R$:{self.valorAcordo}, referente aos serviços efetivamente prestados, devendo ser pago na seguinte condição: {self.formaPagamento}. Acertado esta condição, segue demais critérios: o valor total de parcelas R$:{self.valorParcela} com total de {self.totalParcelas} parcelas, sendo da qual, uma quitação de entrada no valor de R$:{self.valorEntrada}."""

