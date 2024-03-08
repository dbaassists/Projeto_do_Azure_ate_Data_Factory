# %%

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import base64


def envia_arquivo_unidades(fromaddr, toaddr, nome, forma_pagamento):
    forma_pagamento = forma_pagamento
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "{0} - Link para Pagamento - Workshop Bi com Azure".format(nome)
    body = "Olá Meu Jovem {0}!!\n\nEspero que esteja tudo bem contigo! \n\Desde já gostaria de agradecer por acreditar no Workshop que está prestes a participar. \n\nSegue o link para pagamento e confirmação da sua inscrição. Em breve estarei enviando outro e-mail com maiores informações.\n\nGrande Abraço, \n\nGabriel Quintella".format(
        nome
    )
    msg.attach(MIMEText(body, "htmml"))

    if forma_pagamento == "PIX":
        arquivo = rf"../Python/img_pix.png"
        with open(arquivo, "rb") as imagem_anexo:
            imagem_base64 = base64.b64encode(imagem_anexo.read()).decode()

        mensagem_imagem = MIMEImage(base64.b64decode(imagem_base64), name="img_pix.png")
        mensagem_imagem.add_header("Content-ID", "<qrcode>")
        msg.attach(mensagem_imagem)

        corpo_email = f"""
        <html>
        <body>
        <p>Olá {nome},</p>
        <p>Espero que esteja tudo bem contigo!</p>
        <p>Quero expressar minha gratidão por seu interesse em nosso Workshop. Sua participação é muito valorizada!</p>
        <p>Segue o link para pagamento e confirmação da sua inscrição.</p>
        <p>Estarei em contato em breve com mais detalhes sobre o evento.</p>
        <p>Grande Abraço, 
        <p>Gabriel Quintella</p>
        <img src="cid:qrcode" alt="QR Code">
        </body>
        </html>
        """

    elif forma_pagamento == "Cartão de Crédito":
        arquivo = rf"../Python/img_cartao.png"
        with open(arquivo, "rb") as imagem_anexo:
            imagem_base64 = base64.b64encode(imagem_anexo.read()).decode()

        mensagem_imagem = MIMEImage(
            base64.b64decode(imagem_base64), name="img_cartao.png"
        )
        mensagem_imagem.add_header("Content-ID", "<cartao>")
        msg.attach(mensagem_imagem)

        corpo_email = f"""
        <html>
        <body>
        <p>Olá {nome},</p>
        <p>Espero que esteja tudo bem contigo!</p>
        <p>Quero expressar minha gratidão por seu interesse em nosso Workshop. Sua participação é muito valorizada!</p>
        <p>Segue o link para pagamento e confirmação da sua inscrição.</p>
        <p>Estarei em contato em breve com mais detalhes sobre o evento.</p>
        <p>Grande Abraço, 
        <p>Gabriel Quintella</p>
        <img src="cid:cartao" alt="Cartão Crédito">
        </body>
        </html>
        """

    else:
        print("FORA DO PADRÃO")

    msg.attach(MIMEText(corpo_email, "html"))

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, "qiwb hnqt ucvn ehfx")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


# %%

fromaddr = "dbaassists@gmail.com"
toaddr = "dbaassists@gmail.com"
nome = "Gabriel Quintella"
forma_pagamento = "Cartão de Crédito"

envia_arquivo_unidades(fromaddr, toaddr, nome, forma_pagamento)

# %%


arq_dados = rf"C:\Temp\Python_YT\Git\Projeto_do_Azure_ate_Data_Factory\03_MATERIAL_APOIO\Python\DADOS\Inscrição Workshop BI com Azure.csv"

df = pd.read_csv(
    arq_dados,
    sep=",",
    usecols=[1, 3, 10],
    names=["nome", "email", "forma_pagamento"],
    dtype={"nome": "str", "email": "str", "forma_pagamento": "str"},
    header=0,
)

for i, coluna in df.iterrows():
    print(coluna["nome"])
    print(coluna["email"])
    print(coluna["forma_pagamento"])

    fromaddr = "dbaassists@gmail.com"
    toaddr = coluna["email"]
    nome = coluna["nome"]
    forma_pagamento = coluna["forma_pagamento"]

    envia_arquivo_unidades(fromaddr, toaddr, nome, forma_pagamento)
