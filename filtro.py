def email_valido(email_msg, remitentes, assuntos_boletos):
    remetente = email_msg['From'].lower()
    assunto = email_msg['Subject'].lower()
    return any(r in remetente for r in remitentes) and any(a.lower() in assunto for a in assuntos_boletos)