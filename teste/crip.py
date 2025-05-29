from cryptography.fernet import Fernet

key= Fernet.generate_key() #gerando uma chave para criptografar e realizar oposto 

cripto = Fernet(key) #instanciando objeto fenet para realizar operações de criptografia e decriptografia

# estamos instanciando e passando esse objeto para a variável cripto, passando métodos e atributos 

data = input("mensagem que deseja criptografada:")

if data != "":
    token = cripto.encrypt(bytes(data.encode()))
    print(f"mensagem:'{token}")

    desc = input("deseja descriptografar:")

    if desc == 's':
        d = cripto.decrypt(token)
        print(d)
    