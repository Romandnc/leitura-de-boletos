from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='priv.env')

login = os.getenv("EMAIL_LOGIN")
senha = os.getenv("EMAIL_SENHA")

remitentes = [
    'sp.tatuape@parceiro-kroton.com.br',
    'faturaporemailsp@brasil.enel.com',
    'noreply.atendimentoenel@brasil.enel.com'
]

assuntos_boletos = [
    'Universidade Anhanguera - Boleto Mensalidade',
    'Imóvel 894225111 - Fatura com vencimento em '
]