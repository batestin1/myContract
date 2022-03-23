
#############################################################################################################################
#   filename:textoContrato.py                                                       
#  created: 2022-23-03                                                                
#   import your librarys below                                                    
#############################################################################################################################
from get_dados import Dados
# import our secrets
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
cep_empresa = secret[8]
cep_empresa = cep_empresa.replace("\n", "")
bairro_empresa = secret[7]
bairro_empresa = bairro_empresa.replace("\n", "")
estado_empresa = secret[9]
estado_empresa = estado_empresa.replace("\n", "")
cnpj = secret[10]
cnpj = cnpj.replace("\n", "")
email_empresa = secret[11]
email_empresa = email_empresa.replace("\n", "")
senha_empresa = secret[12]
senha_empresa = senha_empresa .replace("\n", "")


class Texto():
    def __init__(self) -> None:
        
        dados = Dados()

        titulo = "Contrato de Prestação de Serviço de Fotografia"
        subtitulo = f"{nome_empresa.upper()}"


        clausura12 = dados.textoValor

        #variaveis do contrato
        contratanteT = "Contratante"
        contratadoT = "Contratado"
        contratado = f"{nome_empresa.upper()}, com sede {end_empresa.upper()}, nº{num_empresa}, Bairro {bairro_empresa.upper()}, CEP {cep_empresa}, no Estado de {estado_empresa.upper()}  inscrita no CNPJ sob o nº {cnpj}."
        contratante = f"Eu {dados.nome} inscrita(o) no cpf {dados.cpf}, nascida(o) {dados.niver}, residente na {dados.endereco}, {dados.num}, complemento {dados.complemento}, localizado no bairro {dados.bairro}, na cidade {dados.cidade}, e no estado {dados.uf}."
        partes = f"""As partes identificadas acima têm, entre si, justo e acertado o presente Contrato de Prestação de Serviços para Foto {dados.tipo} 
        a ser realizado no(a) {dados.nomeEspaco} cujo endereco consta como {dados.enderecoEvento}, número {dados.bairroEvento}, complemento {dados.complementoEvento} localizado no bairro {dados.bairroEvento}, na cidade {dados.cidadeEvento} do estado {dados.ufEvento}.

        A data do evento será realizada no {dados.dataEvento} às {dados.horario} possuindo uma carga total de trabalho de {dados.totalHoras}.
        Explicitado tais informações, o contrato se regerá pelas cláusulas seguintes e pelas condições de preço, forma e termo de pagamento descritas no presente."""
        equipe = f"A equipe do CONTRATANTE prestará os serviços com 1 fotógrafos e 1 assistente de equipamentos."
        clausura2 = f"""Cláusula 2ª. O CONTRATANTE deverá fornecer ao CONTRATADO todas as informações necessárias à realização do serviço, devendo ser verídicas desde o momento pré-contrato à realização do orçamento, especificando os detalhes necessários à perfeita consecução do mesmo, e a forma de como ele deve ser entregue como: nome legível e identificação das pessoas de destaque; livre acesso da equipe ao local do evento; verificar a existência de pontos de energia (tomadas 110v) para os equipamentos, alimentação no buffet, taxa de estacionamento e qualquer eventualidade que por fim altere de alguma forma o valor do orçamento estabelecido. Paragrafo Único: O contratante reserva-se no direito de informar ao contratado o endereço e data de seu evento com uma tolerância de 05 meses após assinatura de contrato, caso ultrapasse esse período fica o contratante ciente de que o <nome do studio> poderá readequar uma outra equipe para o atendimento.
        """
        clausura3 = f"Cláusula 3ª.  É de responsabilidade do CONTRATANTE, eventuais danos físicos causados aos equipamentos ou membros da equipe por parte de seus convidados e por equipe de apoio do evento."
        clausura4 = f"Cláusula 4ª. O CONTRATANTE deverá fornecer a equipe CONTRATADA o direito a alimentação no local do evento."
        clausura5 = f"Cláusula 5ª. O período de pausa para alimentação da equipe será após a realização do ensaio externo a ser definido com a acessora e o contratante."
        clausura6 = f"Cláusula 6ª. O CONTRATANTE deve fornecer informações assertivas referente ao local do evento (exemplo, Making off, cerimônia.festa, surpresas, shows, etc...)."
        clausura7 = f"Cláusula 7ª. Em caso de alteração do local o cliente deve informar com até 25 dias de antecedência os novos endereços e o contratado irá avaliar se haverá alteração dos valores."
        clausura8 = f"Cláusula 8ª.  Caso o evento ultrapasse a tolerância do tempo estipulado será cobrado por adicional/hora R$ 80,00 para cada profissional."
        clausura9 = f"""Cláusula 9ª. O CONTRATADO deverá entregar ao CONTRATANTE os seguintes serviços:
        •	COBERTURA FOTOGRÁFICA COMPLETA DO EVENTO;
        •	PRÉVIA DAS FOTOS EM UM ARQUIVO VIRTUAL;
        •	ENTREGA DE TODAS AS FOTOS NO PENDRIVE;"""
        clausura10 = f"Cláusula 10ª. É dever do CONTRATADO oferecer ao contratante a cópia do presente instrumento, contendo todas as especificidades da prestação de serviço contratada."
        clausura11 = f"Cláusula 11ª. Caso haja alguma falha no equipamento do CONTRATADO alheio a sua vontade e só perceptível após a execução do serviço, que acarrete perda total ou parcial do serviço prestado, fica o CONTRATADO obrigado a devolver a quantia proporcional a perda ocorrida, até o limite do valor contratado, ou poderá compensar a CONTRATANTE de outra maneira, na concordância das partes."
        clausura13 = f"""Cláusula 13ª. Em caso de inadimplemento por parte do CONTRATANTE quanto ao pagamento do serviço prestado, deverá incidir sobre o valor do presente instrumento, multa pecuniária de 30 porcento de juros ao mês."""
        paragrafo13 = f"Parágrafo único. Em caso de cobrança judicial, devem ser acrescidas custas processuais e 20 porcento de honorários advocatícios."
        clausura14 = f"Cláusula 14ª. Poderá o presente instrumento ser rescindido por qualquer uma das partes em qualquer momento, sem que haja qualquer tipo de motivo relevante, não obstante a outra parte deverá ser avisada previamente por escrito, no prazo de 30 dias."
        clausura15 = f"Cláusula 15ª. Estando a parte CONTRATANTE cientes de que a rescisão do contrato por parte da mesma a obrigará ao pagamento do percentual de 25% (vinte e cinco por cento) do valor total acordado na Cláusula 13ª do presente instrumento."
        paragrafo15 = f"PARÁGRAFO PRIMEIRO – Rescindido o compromisso por inadimplemento dos CONTRATANTES, perderão estes em favor dos CONTRATADOS título de perdas e danos prefixadas, a totalidade dos valores que tiverem pago até a data do inadimplemento."
        clausura16 = f"Cláusula 16ª. O CONTRATADO assume o compromisso de realizar e entregar o serviço dentro do prazo de 240 dias , a contar da data do evento, de acordo com a forma estabelecida no presente contrato."
        clausura17 = f"Cláusula 17. O <nome do studio> não se responsabiliza por avarias futuras que possa ocorrer com o DVD/pendrive, devendo assim o cliente fazer suas cópias para manter seu material seguro."
        clausura18 = f"Cláusula 18ª. Após o prazo estabelecido na cláusula anterior, em casos de novas solicitações do material, o mesmo será cobrado pelo valor instituído pelo contratado (seja cópias, etc...). Mas a solicitação deverá ocorrer dentro do prazo de 60 dias a contar da data de entrega do material finalizado via plataformas da internet, pois após esse período todo material será descartado. Como cortesia o Studio colocará os materiais finais editados (não é o material bruto) virtualmente através de uma galeria web em plataformas utilizadas pela contratada. A forma como poderá ser feito o download é de responsabilidade do cliente."
        clausura19 = f"Cláusula 19ª. O material bruto só é entregue em caso de acordância no período contratual, pois o mesmo será cobrado o tempo de rendering, conversão e exportação e assim o material tornará usual pelo cliente."
        clausura20 = f"Cláusula 20ª. Fica compactuado entre as partes a total inexistência de vínculo trabalhista entre as partes contratantes, excluindo as obrigações previdenciárias e os encargos sociais, não havendo entre CONTRATADO e CONTRATANTE qualquer tipo de relação de subordinação."
        clausura21 = f"Cláusula 21ª. O CONTRATANTE autoriza o uso de imagens do evento, para divulgação em site, mostruários, portfólios e anúncios comerciais, respeitando-se a integridade e a moralidade do CONTRATANTE."
        clausura22 = f"Cláusula 22ª. Os negativos das fotos, fitas matrizes, cartões de memória etc. que serão utilizados serão de exclusiva propriedade do CONTRATADO, não estando incluídos no orçamento, não serão negociados e ficarão arquivados por um tempo determinado de 02 meses, para cópias e/ou ampliação eventualmente solicitadas pela CONTRATANTE, a preços atualizados e combinados no momento da solicitação. "
        clausura23 = f"Cláusula 23ª. Para dirimir quaisquer controvérsias oriundas do presente contrato, as partes elegem a descrição do serviço acima; Por estarem assim justos e contratados, firmam o presente instrumento, em duas vias de igual teor, concordados!"
        espaco = '\n'

        ###formatacao
        self.formatacao = f"""
        {titulo.center(110).upper()}
        {subtitulo.center(150)}
        {espaco}
        {contratanteT.center(150).upper()}
        {contratante}
        {espaco}
        {contratadoT.center(150).upper()}
        {contratado}
        {espaco}
        {partes}
        {espaco}
        {equipe}
        {espaco}
        {clausura2}
        {espaco}
        {clausura3}
        {espaco}
        {clausura4}
        {espaco}
        {clausura5}
        {espaco}
        {clausura6}
        {espaco}
        {clausura7}
        {espaco}
        {clausura8}
        {espaco}
        {clausura9}
        {espaco}
        {clausura10}
        {espaco}
        {clausura11}
        {espaco}
        {clausura12}
        {espaco}
        {clausura13}
        {espaco}
        {paragrafo13.center(80)}
        {espaco}
        {clausura14}
        {espaco}
        {clausura15}
        {espaco}
        {paragrafo15.center(80)}
        {espaco}
        {clausura16}
        {espaco}
        {clausura17}
        {espaco}
        {clausura18}
        {espaco}
        {clausura19}
        {espaco}
        {clausura20}
        {espaco}
        {clausura21}
        {espaco}
        {clausura22}
        {espaco}
        {clausura23}
        """



