
#############################################################################################################################
#   filename:get_dados.py                                                       
#   created: 2022-23-03                                                              
#   import your librarys below                                                    
#############################################################################################################################

import requests
import pandas as pd

secret = open("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/secrets/secrets.txt", 'r')
secret = list(secret)
#variaveis

path = secret[0]
path = path.replace("\n", "")
pix = secret[1]
pix = pix.replace("\n", "")
banco = secret[2]
banco = banco.replace("\n", "")
favorecido = secret[3]
favorecido = favorecido.replace("\n", "")
nome_empresa = secret[4]
nome_empresa = nome_empresa.replace("\n", "")
end_empresa = secret[5]
end_empresa = end_empresa.replace("\n", "")
num_empresa = secret[6]
num_empresa = num_empresa.replace("\n", "")
cep_empresa = secret[7]
cep_empresa = cep_empresa.replace("\n", "")
bairro_empresa = secret[8]
bairro_empresa = bairro_empresa.replace("\n", "")
estado_empresa = secret[9]
estado_empresa = estado_empresa.replace("\n", "")
cnpj = secret[10]
cnpj = cnpj.replace("\n", "")
email_empresa = secret[11]
email_empresa = email_empresa.replace("\n", "")
senha_empresa = secret[12]
senha_empresa = senha_empresa .replace("\n", "")

data = pd.read_csv(f"{path}download/dados_contrato.csv", header='infer', index_col= False)

class Dados():
    def __init__(self) -> None:
        for i in range(data.shape[0]):
            self.nome = data['NOME DO CONTRATANTE'][i].upper()
            self.email = data['EMAIL DO CONTRATANTE'][i].lower()
            self.tel = data['TELEFONE DO CONTRATANTE'][i]
            self.cpf = data['CPF DO CONTRANTANTE'][i]
            self.cpf = str(self.cpf)
            self.cpf = self.cpf.zfill(11)
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
                self.textoValor = f"""O presente serviço será remunerado pela quantia de R$:{self.valorAcordo}, referente aos serviços efetivamente prestados, devendo ser pago na seguinte condição: {self.formaPagamento}. O pagamento só poderá ser aceito por transferência, e PIX para o seguinte endereço eletrônico: PIX: {pix} banco {banco} favorecido: {favorecido}."""
            else:
                self.textoValor = f"""O presente serviço será remunerado pela quantia de R$:{self.valorAcordo}, referente aos serviços efetivamente prestados, devendo ser pago na seguinte condição: {self.formaPagamento}. Acertado esta condição, segue demais critérios: o valor total de parcelas R$:{self.valorParcela} com total de {self.totalParcelas} parcelas, sendo da qual, uma quitação de entrada no valor de R$:{self.valorEntrada}. O pagamento será efetuado  por transferência, e PIX para o seguinte endereço eletrônico: PIX: {pix} banco {banco} favorecido: {favorecido} a partir do dia 15 de cada mes subjacente."""

