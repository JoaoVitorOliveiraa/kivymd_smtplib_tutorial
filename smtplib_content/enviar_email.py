# O smtplib é um módulo que define um objeto de sessão de cliente SMTP que
# pode ser usado para enviar e-mail para qualquer máquina de internet.
# SMTP é um protocolo padrão de comunicação entre sistemas de email.
import smtplib

# Biblioteca para criar o email.
from email.message import EmailMessage

# Arquivo de mensagens prontas.
from mensagens_pre_prontas import *

from minha_senha_de_app import senha_de_app

#Função para enviar um email.
def enviar_email(remetente_email,
                 destinatario_email,
                 assunto_email,
                 corpo_email_html):

    mensagem = EmailMessage()                                       # Cria a mensagem.
    mensagem['Subject'] = assunto_email                             # Determina o assunto do email.
    mensagem['From'] = remetente_email                              # Determina o remetente do email.
    mensagem['To'] = destinatario_email                             # Determina o destinatário do email.
    senha = senha_de_app                                            # Senha de App da conta do Google.
    mensagem.set_content(corpo_email_html, subtype='html')    # Seta o conteúdo do email (do tipo html).

    envio_smtp = smtplib.SMTP('smtp.gmail.com: 587')     # Domínio SMTP do gmail.
    envio_smtp.starttls()                                # Coloca a conexão SMTP em modo TLS (Transport Layer Security). Assim, todos os comandos SMTP serão criptografados.
    envio_smtp.login(mensagem['From'], senha)            # Realiza o login do email do remetente.

    # Envia o email.
    envio_smtp.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    # OBS1: A função "as_string()" retorna a mensagem achatada como uma string.
    # OBS2: A função "encode()" codifica uma string em um formato específico, nesse caso "utf-8".

    print('Email enviado')


remetente = 'jvoliveira30@gmail.com'
destinatario = 'jvoliveira30@gmail.com'
assunto = avisos_de_segunda[0]
corpo = avisos_de_segunda[1]

enviar_email(remetente, destinatario, assunto, corpo)