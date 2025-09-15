from datetime import datetime
import os
from email import message_from_bytes
from pathlib import Path
from filtro import email_valido
from config import remitentes, assuntos_boletos

def salvar_boletos(lista_emails):
    caminho_downloads = str(Path.home() / "Downloads")
    pasta_boletos = os.path.join(caminho_downloads, "Boletos")
    os.makedirs(pasta_boletos, exist_ok=True)

    for id_email, dados_email in lista_emails:
        conteudo_bruto = dados_email[0][1]
        mensagem = message_from_bytes(conteudo_bruto)

        if email_valido(mensagem, remitentes, assuntos_boletos):
            for parte in mensagem.walk():
                if parte.get_content_maintype() == 'multipart':
                    continue
                if parte.get('Content-Disposition') is None:
                    continue

                nome_arquivo = parte.get_filename()

                if not nome_arquivo or "boleto" in nome_arquivo.lower():
                    remetente = mensagem['From'].split('<')[-1].replace('>', '').replace('@', '_').replace('.', '_')
                    assunto = mensagem['Subject'] or "sem_assunto"
                    assunto_formatado = assunto.replace(' ', '_')[:30]
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    nome_arquivo = f"{remetente}_{assunto_formatado}_{timestamp}.pdf"

                if nome_arquivo.lower().endswith('.pdf'):
                    caminho_arquivo = os.path.join(pasta_boletos, nome_arquivo)
                    with open(caminho_arquivo, 'wb') as arquivo:
                        arquivo.write(parte.get_payload(decode=True))
                    print(f"Boleto salvo: {caminho_arquivo}")