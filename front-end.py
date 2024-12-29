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

inicio= ['criar conta','entrar']
entrada = ['armazenar senhas','apagar conta']

for a, c in enumerate(inicio):
    print(f'{a} -{c}')


escolher = input('insira uma opção:')
if escolher == '0':
    while True:

        usuario = input('crie um usuário:')
        #senha = input('crie uma senha forte ou g para gerar uma:')
        verificacao = banco.busca(usuario,False)

        if verificacao:
            print(f'usuario existente para {usuario}')
            continue
        
        else:
            senha = input('crie uma senha forte ou g para gerar uma:')
            if(senha == 'g'):
                senha = banco.gerar_senha()
                print(senha)

            banco.criar_conta(usuario,senha)
            print('conta criada com suscesso!!')
            break

elif escolher == '1':
    while not auth:
        usuario = input('insira seu usuario:')
        senha = getpass.getpass('insira sua senha:')

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
            ambiguidade = banco.busca(usuario,plataforma)
            if plataforma == 'q':
                break
            if(ambiguidade):
                print('senha já armazenada')
            else:
                senha = input("insira sua senha ou g para gerar uma:")
            
                if senha == 'g':
                    senha = banco.gerar_senha()
            
                conta.id_(plataforma,usuario,senha,None)
    
    elif escolher == '1':
        apagar = True
        conta.id_(None,usuario,None,apagar)
        #conta.apagar_conta(usuario)
    

