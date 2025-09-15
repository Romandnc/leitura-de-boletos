from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='priv.env')

login = os.getenv("EMAIL_LOGIN")
senha = os.getenv("EMAIL_SENHA")

remitentes = [
    'exemplodo@gmail.com',
    'seuremitente@gmail.com'
]

assuntos_boletos = [
    'o assunto do seu boleto',
    'assunto do seu outro boleto'
    ]