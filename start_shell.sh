#bin/bash

#rm -r download
#mkdir download
cd pip
pip install -r requisitos.txt
cd ../download
#
wget https://docs.google.com/forms/u/0/d/1GsnncbrNR91zyfih1W77NJETgQJGk5KPCxFhYHbtdGk/downloadresponses?tz_offset=-10800000&sort_by_timestamp=true
unzip *.zip
cd ../script
clear
echo "#########################################################################################################################################################################################################"
echo "                                                                              LEIA O CONTRATO                                            "
echo "######################################################################################################################################################################################################"
python show_contract.py
echo "#################################################################################################################################################################################################"
echo """ DESEJA SALVAR ESTE CONTRATO
[1] - SIM
[2] - NÃO """
read escolha

if [ $escolha == 1 ]
then
    clear
    python send_pdf.py
    clear
   echo "Arquivo salvo em pdf! "
else
    clear
    echo "Ok!"
fi
echo "#################################################################################################################################################################################################"

echo """ DESEJA ENVIÁ-LO POR E-MAIL
[1] - SIM
[2] - NÃO """
read escolha2
if [ $escolha == 1 ]
then
    clear
    python sendEmail.py
    clear
    echo "Arquivo enviado por email! "
else
    clear
    echo "Ok!"
fi

echo "#################################################################################################################################################################################################"

echo """ DESEJA SALVA-LO EM UM BANCO DE DADOS
[1] - SIM
[2] - NÃO """
read escolha2
if [ $escolha == 1 ]
then
    clear
    python send_mysql.py
    clear
    echo "Arquivo salvo em MYSQL! "
else
    clear
    echo "Ok!"
fi
echo "#################################################################################################################################################################################################"
clear

echo "Programa Finalizado!"