from config import login, senha
from mail_client import conectar_email, buscar_emails
from downloader import salvar_boletos

def main():
    objCon = conectar_email(login, senha)
    ids = buscar_emails(objCon)

    dados = []
    for num in ids:
        resultado, dado = objCon.fetch(num, '(RFC822)')
        dados.append((num, dado))

    salvar_boletos(dados)

if __name__ == "__main__":
    main()