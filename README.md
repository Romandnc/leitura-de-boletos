Este projeto utiliza variáveis de ambiente para proteger dados sensíveis, como login de e-mail e senha.
Para rodar corretamente, você deve criar um arquivo chamado priv.env na raiz do projeto com o seguinte conteúdo:
EMAIL_LOGIN=seuemail@exemplo.com
EMAIL_SENHA=suaSenhaSegura123
Substitua os dados pelos seus dados reais.
O arquivo config.py está configurado para buscar essas variáveis usando os.getenv().
Os remetentes e assuntos de boletos também estão definidos com exemplos genéricos — você pode personalizar conforme sua necessidade:)
