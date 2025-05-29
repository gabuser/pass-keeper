import smtplib,ssl
password = "ezai gndd yqpg mdse"
sender = "random@gmail.com"

recived = "trabalhoinvest100@gmail.com"
security = ssl.create_default_context()
port = 465
#gerar_senha = backend.contas()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=security) as server:
    server.login("trabalhoinvest100@gmail.com", password)
    server.sendmail(sender,recived,"ola mundo")


#password = "ezai gndd yqpg mdse"
#port = 465
