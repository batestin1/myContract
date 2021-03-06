
#############################################################################################################################
#   filename: sendEmail.py                                                       
#   created: 2022-23-03                                                            
#   import your librarys below                                                    
#############################################################################################################################

import mimetypes
import os
import smtplib
from get_dados import Dados
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
data_atual = date.today()
data = data_atual.strftime('%Y%m%d')
secret = open("C:/Users/Bates/Documents/Repositorios/LIBS/myContract/secrets/secrets.txt", 'r')
secret = list(secret)
#variaveis

path = secret[0]
path = path.replace("\n", "")
pix = secret[1]
banco = secret[2]
favorecido = secret[3]
nome_empresa = secret[4]
end_empresa = secret[5]
num_empresa = secret[6]
cep_empresa = secret[7]
bairro_empresa = secret[8]
estado_empresa = secret[9]
cnpj = secret[10]
email_empresa = secret[11]
senha_empresa = secret[12]


dados = Dados()
nomeFull = dados.nome.split()
primeiroNome = nomeFull[0].capitalize()
nome = dados.nome
nome = nome.replace(" ", "_").lower()


def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return

    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    elif maintype == 'image':
        with open(filename, 'rb') as out:
            mime = MIMEImage(f.read(), _subtype=subtype)
    elif maintype == 'audio':
        with open(filename, 'rb') as f:
            mime = MIMEAudio(f.read(), _subtype=subtype)
    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())

        encoders.encode_base64(mime)

    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)

de = f'{email_empresa}'
para = [f'{dados.email}']

msg = MIMEMultipart()
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = f"CONTRATO - {dados.nome} - {data} "

# Corpo da mensagem
msg.attach(MIMEText(f"""
<h3> <strong> <center> CONTRATO </center> </strong> </h3>

<p> Caro {primeiroNome}, </p>
    
<p> Em anexo voc?? esta recebendo uma c??pia do <b> contrato </b> previamente acordado entre as partes </p>
    
<p> Estando de acordo, por favor, assine-o e reenvie para n??s! </p>




<p> <i> Att, </i> </p>
<p> <i> <b> {nome_empresa} </i> </b> </p>""", 'html', 'utf-8'))

# Arquivos anexos.
adiciona_anexo(msg, f'{path}pdf/contract_{nome}_{data}.pdf')


raw = msg.as_string()

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login(f'{email_empresa}', f'{senha_empresa}')
smtp.sendmail(de, para, raw)
smtp.quit()

print('Email Enviado!')
