import backend
import getpass
banco = backend.log
conta = backend.conta
verificacao = None
auth = None
armazenar = True
plataforma = None
apagar = False
ambiguidade = None

salvar_dados= {
    "user":str,
    "password":str
}

inicio= ['criar conta','entrar']
entrada = ['armazenar senhas','apagar conta','atualizar',"visualizar senhas"]

for a, c in enumerate(inicio):
    print(f'{a} -{c}')


escolher = input('insira uma opção:')
if escolher == '0':
    while True:

        usuario = input('crie um usuário:')
        senha = input('crie uma senha forte ou g para gerar uma:')
        recover = input("insert a email or space to skip:")

        salvar_dados['user']= usuario

        verificacao = banco.busca(salvar_dados['user'])
        salvar_dados['user'] =verificacao if verificacao else usuario
        salvar_dados['password'] = senha

        match (salvar_dados):
            case {"user":data} | {"password":data} if salvar_dados['user'] != "" and salvar_dados['password'] != "" and salvar_dados['user'] !=True:
                
                banco.criar_conta(salvar_dados['user'], salvar_dados['password'],recover)
                print("conta criada com sucesso")
                break
            
            case {"passoword":"g"}:
                senha = banco.gerar_senha()
                banco.criar_conta(salvar_dados['user'],senha,
                                  recover)
                print("conta criada com sucesso!")
                break

            case {"user": True}:
                print(f"usuário existente para {usuario}")
            
            case _:
                print("crie uma conta válida!")

elif escolher == '1':
    while not auth:
        usuario = input('insira seu usuario:')
        senha = input('insira sua senha:')

        auth = banco.entrar(usuario,senha)

        if auth:
            print(f'bem vindo {usuario}')
            
            #conta.id_(usuario)
        else:
            print('ops, senha ou usuario incorreto.')
        #continue
    
    for c, a in enumerate(entrada):
        print(f'{c}- {a}')

    escolher = input('escolha sua opção:')
    if escolher == '0':

        while(armazenar):
            plataforma = input('insira a plataforma ou q para sair:')
            isequal= backend.conta.ambiguity(usuario, plataforma)
            if plataforma == 'q':
                break

            elif(isequal):
                print("senha já existe")
            else:
                senha = input("insira sua senha ou g para gerar uma:")

                if senha == 'g':
                    senha = banco.gerar_senha()
                
                conta.addpasswords(plataforma,senha,usuario)
                #conta.id_(plataforma,usuario,senha,None)

    
    elif escolher == '1':
        apagar = True
        print(usuario)
        conta.todelete(usuario,apagar)
        #conta.id_(None,usuario,None,apagar)
        #conta.apagar_conta(usuario)
    
    elif escolher == '2':
        banco.buscar_senhas(usuario,True,False)
    
    elif escolher == '3':
        updt= input("1:email \n 2:senha \n 3:nome :")
        
        if(updt == '1'):
            email = input("insira o novo email:")
            
            if(conta.updating_user(email,updt,usuario)):
                print("email existente, atualize outro email")
            
            else:
                conta.updating_user(email,updt,usuario)
        
        elif(updt == '2'):
            senha = input("insira a senha:")
            conta.updating_user(senha,updt,usuario)
            print("senha alterada com sucesso")
        
        elif(updt == '3'):
            new_name = input("insira o novo nome:")

            notunique = conta.busca(new_name)
            if(notunique):
                print("nome existente.")
            
            else:
                conta.updating_user(new_name,updt,usuario)
                print("nome alterado com sucesso!")