#!/usr/bin/env python
# coding: utf-8

import smtplib
import email.message
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email_com_anexo(nome_arquivo):  
    corpo_email = """
    <p>Esse e um email pra idosa da minha mae te amo.</p>
    <p>Segue em anexo o arquivo solicitado.</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = "Arquivo de Folgas"
    msg['From'] = 'guuiisantiago2018@gmail.com'
    msg['To'] = 'santiagokelly201@gmail.com'
    password = 'fwjnjchqbakimfef'

    # Adicionar o corpo do e-mail
    msg.attach(MIMEText(corpo_email, 'html'))

    # Anexar o arquivo
    with open(nome_arquivo, 'rb') as arquivo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(arquivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename="{nome_arquivo}"')
        msg.attach(parte)

    # Enviar o e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(msg['From'], password)
        servidor.sendmail(msg['From'], [msg['To']], msg.as_string())
        print('E-mail enviado com anexo!')

def calcular_dias_da_semana(dia_inicio, dias_no_mes):
    dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    dias_semana = []

    for dia in range(1, dias_no_mes + 1):
        dia_semana_atual = (dia_inicio + (dia - 1)) % 7
        dias_semana.append(dias_da_semana[dia_semana_atual])

    return dias_semana

def criar_excel(nome_colaborador, dias_no_mes, dia_inicio, primeira_folga):
    dias_semana = calcular_dias_da_semana(dia_inicio, dias_no_mes)

    # Criar o cabeçalho
    cabecalho = ['Dias do mês'] + [str(dia) for dia in range(1, dias_no_mes + 1)]
    df = pd.DataFrame(columns=cabecalho)

    # Adicionar a linha com os dias do mês
    df.loc[0] = [''] + [str(dia) for dia in range(1, dias_no_mes + 1)]

    # Adicionar a linha com os dias da semana
    df.loc[1] = ['Dias da semana'] + dias_semana

    # Calcular as folgas a cada 5 dias
    dias_folga = [primeira_folga + i * 6 for i in range((dias_no_mes - primeira_folga) // 6 + 1) if (primeira_folga + i * 6) <= dias_no_mes]

    # Adicionar a linha com as folgas
    linha_colaborador = [nome_colaborador] + ['F' if dia in dias_folga else '' for dia in range(1, dias_no_mes + 1)]
    df.loc[2] = linha_colaborador

    nome_arquivo = 'folgas.xlsx'
    df.to_excel(nome_arquivo, index=False, header=False)

    print(f'Arquivo "{nome_arquivo}" criado com sucesso!')
    return nome_arquivo

# Exemplo de uso
nome_colaborador = input("Digite o nome do colaborador: ")
dias_no_mes = int(input("Digite o número de dias no mês: "))  
dia_inicio = int(input("Digite o dia da semana em que o mês começa (0=segunda, 6=domingo): "))  
primeira_folga = int(input("Digite a data da primeira folga do mes  (apenas o dia): "))  

# Criar o arquivo Excel e enviar por e-mail
nome_arquivo_gerado = criar_excel(nome_colaborador, dias_no_mes, dia_inicio, primeira_folga)
enviar_email_com_anexo(nome_arquivo_gerado)
