import backend
import getpass
banco = backend.log
conta = backend.conta

inicio= ['criar conta','entrar','recuperar conta','atualizar a senha gmail.com']
entrada = ['armazenar senhas','apagar conta','atualizar',"visualizar senhas"]

class interfaces:
    def __init__(self) ->None:
        self.verificacao = None
        self.auth = None
        self.armazenar = True
        self.apagar = False
        self.ambiguidade = None
        self.isequal = False
        self.deleted = False
        self.toupdate = True
        self.choose = True
        self.user =None

        self.salvar_dados= {
        "user":str,
        "password":str
        }
    
    def user_input(self):
        while True:
            for a, c in enumerate(inicio):
                print(f'\n {a}-{c}')
            
            self.options = input("\n escolha uma das opções ou q para sair:")
        
            match str(self.options):
                case '0':
                    self.creating()
                case '1':
                    self.user_interface()
            
                case '2':
                    self.recovered()
                
                case '3':

                    self.user = input("insira o seu usuário:")
                    password = input("insira a sua senha:")
                    isauth=conta.saving_gmail_pass(self.user,password)

                    if(isauth):
                        print("alterado com sucesso")
                    
                    else:
                        print("\n senha ou usuário incorreto")
                case 'q':
                    break

                case _:
                    print("\n insira uma das opções válidas")
    
    def creating(self):
        while True:
            self.user = input("\n crie um usuário:")
            account_password = input("\n insira uma senha ou g para gerar uma:")
            iscreated = conta.busca(self.user)
            self.creating_email()
            
            match iscreated:
                case True:
                    print(f"\n usuário existente para {self.user}")
                
                case False:

                    if(self.user == '' or account_password == ''):
                        print("insira usuários válidos")
                        continue
                    
                    if(account_password == 'g'):
                        generated_password = conta.gerar_senha()
                        conta.criar_conta(self.user,generated_password,
                                          self.email)
                        break
                    
                    else:
                        conta.criar_conta(self.user,account_password,self.email)
                        break
                
    def authentication(self) -> bool:

        while (not self.auth):
            self.user = input("\n insira o seu usuário:")
            self.senha = input("\n insira sua senha:")

            self.auth = banco.entrar(self.user,self.senha)

            match self.auth:

                case True:
                    return True
                
                case False:
                    return False
    
    def user_interface(self):
        self.response = self.authentication()

        if(self.response):
            print(f"bem vindo {self.user}")
            while(self.choose):
                for a,c in enumerate(entrada):
                    print(f"\n {a}-{c}")
                
                options = input("\n insira a sua opção ou q para sair:")
                
                match options:

                    case 'q':
                        self.choose = False
                    
                    case '0':
                        self.storage_password()
                    
                    case '1':
                        self.deleting()
                        self.choose = False
                    
                    case '2':
                        self.updating()
                    
                    case '3':
                        self.see()
                    case _:
                        print("\n nenhuma opção foi selecionada")
        else:
            print("\n senha ou usuário incorreto")

    def storage_password(self):
        self.armazenar = True
        while(self.armazenar):
            self.plataforma = input("\n insira a plataforma ou q para sair:")
            password = None
            self.isequal = conta.ambiguity(self.user,self.plataforma)

            match self.plataforma:

                case 'q':
                    self.armazenar = False
                
                case self.plataforma if self.plataforma !='':
                    password = input("\n insira uma senha ou g para gerar uma:")

                    if(password == 'g' and not self.isequal):
                        generated = conta.gerar_senha()
                        conta.addpasswords(self.plataforma,generated,self.user)
                    
                    elif(self.isequal):
                        print("\n senha já existe")

                    else:
                        conta.addpasswords(self.plataforma, password,self.user)
                case _:
                    print("\n valor não válido")
    
    def deleting(self):
            conta.todelete(self.user,self.deleted)
    
    def creating_email(self):
        while True:
            create_email = input("\n criar um email s ou n:")
            if(create_email == 's'):
                self.email = input("\n insira um email válido:")
                self.isemail = conta.cheking_emails(self.email)

                match self.isemail:
                    case True:
                        print("\n email já existe :(")
                    
                    case False:
                        print("\n email criado com sucesso!!")
                        break
                    
                    case None:
                        print("\n email criado com sucesso!!")
                        break
            
            if(create_email == 'n'):
                self.email = None
                break
            
            else:
                print("\n insira um valor válido")
    
    def updating(self):
            self.toupdate= True
            while(self.toupdate):
                updt= input("1:email \n 2:senha \n 3:nome \n q to quit :")

                match updt:

                    case '1':
                        self.creating_email()

                        if (conta.updating_user(self.email,updt,self.user) 
                            or self.email ==""):
                            print("\n possível erro:\n 1: dados existentes \n 2:dados foram deixados em branco")
                        
                        else:
                            conta.updating_user(self.email,updt,self.user)
                    
                    case '2' if updt :
                        password= input("\n insira a nova senha:")

                        if(password!= ""):
                            conta.updating_user(password,updt,self.user)
                        
                        else:
                            print("\n insira dados válidos")
                    
                    case '3':
                        new_name = input("\n insira o novo nome:")
                        notunique = conta.busca(new_name)

                        if notunique:
                            print("\n nome existente, crie outro nome")
                        
                        elif new_name == "":
                            print("\n valor vázio, coloque um valor")
                        else:
                            conta.updating_user(new_name,updt,self.user)
                    case 'q':
                        self.toupdate = False
                    
                    case _:
                        print("\n por favor, insira uma das opções")
    
    def recovered(self):
            users = input("\n insira o seu usuário:")
            #password = input("insira a sua senha:")
            conta.recovering(users)
    
    def see(self):
        choose = input("\n procurar senha aperte p ou t para ver todas as senhas:")

        match choose:

            case "t":
                conta.buscar_senhas(self.user,True,None)
            
            case 'p':
                senha = input("\n nome da plataforma que deseja buscar:")
                
                conta.buscar_senhas(self.user,False,senha)
            
            case _:
                print("\n opção inválida, escolha pelo menos umas das opções")
        

    def main(self):
        self.user_input()

main = interfaces()
main.main()