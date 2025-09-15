import imaplib
from datetime import datetime, timedelta

def conectar_email(login, senha):
    objCon = imaplib.IMAP4_SSL('imap.gmail.com')
    objCon.login(login, senha)
    objCon.select(mailbox='inbox', readonly=True)
    return objCon

def buscar_emails(objCon):
    data_limite = datetime.today() - timedelta(days=40)
    data_formatada = data_limite.strftime('%d-%b-%Y')
    resposta, IdEmails = objCon.search(None, f'SINCE {data_formatada}')
    return IdEmails[0].split()
