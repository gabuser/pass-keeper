import backend
banco = backend.log
conta = backend.conta

inicio= ['criar conta','entrar','recuperar conta','app passwords']
entrada = ['armazenar senhas','apagar conta','atualizar',"visualizar senhas","apagar senhas"]
erro_atualizacao = ['verifique se os dados foram digitados corretamente','verifique se o valor já existe',
                    'verifique se você não deixou os valores em branco']

#class called interface to represent the interface or the front-end of the program
class interfaces:
    #init function to initialize a reserved space that will be used in the memory
    def __init__(self) ->None:
        self.verificacao = None
        self.auth = None
        self.armazenar = True
        self.apagar = False
        self.ambiguidade = None
        self.isequal = False
        self.deleted = False
        self.toupdate = True
        #self.choose = True
        self.user =None

        """obs: it's possible to reduce most of the reserved space to optimize the program
        since all those variables are just being used temporarily and 
        take up space in memory to hold values."""
    
    #function that will handle with the user's input and manage the output
    def user_input(self):
        while True:
            for a, c in enumerate(inicio):
                print(f'{a}-{c}')
            
            self.options = input("\n escolha uma das opções ou q para sair:")
        
            match str(self.options):
                case '0':
                    self.creating()

                    """print("#"*50)
                    print("\n SENHA PARA CRIPTOGRAFAR E DESCRIPTOGRAFAR OS SEUS DADOS QUE SÃO ARMAZENADOS!")
                    print("\n ATENÇÃO: caso você perder essa senha, não será mais possível recuperar as senhas \n")
                    print(f"\n senha: {conta.returned}\n")
                    print("#"*50)"""

                case '1':
                    self.user_interface()
            
                case '2':
                    self.recovered()
                
                case '3':

                    self.user = input("insira o seu usuário ou ctrl+c para sair:")
                    password = input("insira a sua senha ou ctrl+c para sair:")
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
            self.user = input("\n crie um usuário ou ctrl+c para sair:")
            self.account_password = input("\n insira uma senha ou aperte enter para gerar uma ou ctrl+c para sair:")
            
            iscreated = conta.busca(self.user)
            self.creating_email()

            blank_lines= self.user.split(" ")
            last_word= len(blank_lines)-1

            blank_lines_password = self.account_password.split(" ")
            
            last_word_pass = len(blank_lines_password)-1

            if(blank_lines[0]=='' and blank_lines[last_word]
               =='' or blank_lines !=''
               and blank_lines_password[0] == ''
               and blank_lines_password[last_word_pass] == ''
               or blank_lines_password!=''):
                
                self.user=[_  for _ in blank_lines if _ !='']
                self.user = ' '.join(self.user)

                self.account_password=[_ for _ in blank_lines_password if _ != ""]
                self.account_password = ' '.join(self.account_password)
            #if(len(self.user)>1):
            #tam = len(self.user)
            #teste = ' '.join(self.user[0:tam]) 
            #print(self.user)
            #print(len(self.user)*'' == '')
            #print(len(self.user)*'' == '')
            #print(len(self.user)*""=="") should not be used
                #print(self.user)
            
            match iscreated:
                case True:
                    print(f"\n usuário existente para {self.user}")
                
                case False:
                    
                    if(self.user == ''):
                        print("\n ERROR:verifique se o usuário foi deixado em branco")
                        #continue
                    
                    elif(len(self.account_password)<6 or self.account_password ==""):#precisa ser arrumado, contém vulnerabilidade.
                        self.generated_password = conta.gerar_senha()

                        conta.criar_conta(self.user,self.generated_password,
                                          self.create_email)
                        
                        print("\n ATENÇÃO: SENHA QUE FOI GERADO AUTOMATICAMENTE, ELA É USADA PARA VOCÊ LOGAR:")
                        print("#"*50,)
                        print(f'\n sua senha é: {self.generated_password}')
                        print("\n caso sua senha for menor que 6 caracteres, uma senha automática também será gerada")
                        print("#"*50)
                        #print("\n ATENÇÃO, SENHA QUE FOI GERADO AUTOMATICAMENTE, ELA É USADA PARA VOCÊ LOGAR\n")
                        break

                    else:
                        conta.criar_conta(self.user,self.account_password,self.create_email)
                        break
            
    def authentication(self) -> bool:
        self.auth = False
        while (not self.auth):
            self.user = input("\n insira o seu usuário ou ctrl+c para sair:")
            self.senha = input("\n insira sua senha ou ctrl+c para sair:")

            self.auth = banco.entrar(self.user,self.senha)

            match self.auth:

                case True:
                    return True
                
                case False:
                    print("\n senha ou usuário incorreto, por favor verifique os seus dados!\n")
                    continue
    
    def user_interface(self):
        self.response = self.authentication()
        datas_saved = conta.isstorage(self.user)

        if(not datas_saved):
            print("\n aparentimente você não tem uma chave criptográfica")
            print(f"\nsua chave é {conta.new_keypass} ")

        if(self.response):
            try:
                print(f"\n bem vindo {self.user}")
            
                while(True):
                    for a,c in enumerate(entrada):
                        print(f"\n {a}-{c}")
                
                    options = input("\n insira a sua opção ou q para sair ou ctrl+c para sair:")
                
                    match options:

                        case 'q':
                            #conta.isencripted(self.user)
                            conta.encrypt(self.user)
                            break
                    
                        case '0':
                            self.storage_password()
                    
                        case '1':
                            self.deleting()
                            break
                    
                        case '2':
                            self.updating()
                    
                        case '3':
                            self.see()
                    
                        case '4':
                            self.delete_password(self.user)
                    #case '4':
                        #u = self.user
                        #conta.isencripted(self.user)
                        case _:
                            print("\n nenhuma opção foi selecionada")

            except KeyboardInterrupt:
                conta.encrypt(self.user)

    def storage_password(self):
        self.armazenar = True
        #isdecript = conta.isencripted(self.user)

        try:
            if(conta.isencripted(self.user)):
                while(self.armazenar):
                    self.plataforma = input("\n insira a plataforma ou q para sair ou ctrl+c para sair:")
                    password = None
                    self.isequal = conta.ambiguity(self.user,self.plataforma)

                    match self.plataforma:

                        case 'q':
                            self.armazenar = False
                            print("\n dados salvos!")
                            #conta.isencripted(self.user)
                
                        case self.plataforma if self.plataforma !='':
                            password = input("\n insira uma senha ou g para gerar uma ou ctrl+c para sair:")

                            if(password == 'g' and not self.isequal):
                                generated = conta.gerar_senha()
                                conta.addpasswords(self.plataforma,generated,self.user)
                    
                            elif(self.isequal):
                                print("\n senha já existe")

                            else:
                                conta.addpasswords(self.plataforma, password,self.user)
                    
                        case _:
                            print("\n valor não válido")
                        
        except KeyboardInterrupt:
            print("\n dados salvo!")

    def deleting(self):
            conta.todelete(self.user,self.deleted)
    
    def creating_email(self):
        while True:
            self.create_email = input("\n criar um email ou enter para continuar ou ctrl+c para sair:")
            #if(create_email == 's'):
            #self.email = input("\n insira um email válido:")
            create_email = self.create_email.split(" ")
            lenght_email = len(create_email)-1

            if(create_email[0]=="" and create_email[lenght_email]==""
               or create_email[0] != "" ):
                
                deleting_blank = [_ for _ in create_email if _ !="" ]
                self.create_email = ''.join(deleting_blank)
                #print('essa condição foi satisfeita')
            
            #else:
             #   self.create_email
            
            self.isemail = conta.cheking_emails(self.create_email)

            match self.isemail:
                    case True:
                        print("\n email já existe :(")
                    
                    case False:
                        print("\n email criado com sucesso!!")
                        break
                    
                    case None:
                        if(self.create_email ==''):
                            self.create_email = None
                        break
                
    def updating(self):
            self.toupdate= True
            while(self.toupdate):
                updt= input("\n 1:email \n 2:senha de login \n 3:usuario " \
                "\n 4:plataforma \n 5:senha da plataforma \n \n q to quit ou ctrl+c para sair :")

                match updt:

                    case '1':
                        self.creating_email()

                        if (conta.updating_user(self.create_email,updt,self.user)):
                            #print(conta.updating_user(self.create_email,updt,self.user))
                            #print(self.create_email)
                            print("\n possível erro:\n 1: dados existentes \n 2:dados foram deixados em branco")
                        
                        else:
                            conta.updating_user(self.create_email,updt,self.user)
                            print("\n email atualizado com sucesso!")
                    
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
                            #print(self.user)
                            conta.updating_user(new_name,updt,self.user)
                            self.user = new_name# ponto a ser observado(futuros erros)
                    
                    case '4':
                        self.plataforma = input("\n insira o nome da plataforma(netflix,amazon...):")
                        
                        confirmation = conta.updating_user(self.plataforma,updt,self.user)

                        if(confirmation):
                            print("\n atualizado com sucesso")
                        
                        else:
                            print("#"*50)
                            for a,b in enumerate(erro_atualizacao):
                                print(f'{a+1}:{b}\n')
                            
                            print("ERROR")
                            print('# \n'*50)
                    
                    case '5':
                        result = conta.isencripted(self.user)
                        
                        if(result):
                            new_password = input("insira o nome da plataforma:")
                            conta.updating_user(new_password,updt,self.user)

                    case 'q':
                        self.toupdate = False
                    
                    case _:
                        print("\n por favor, insira uma das opções")
    
    def recovered(self):
            users = input("\n insira o seu usuário ou ctrl+c para sair:")
            #password = input("insira a sua senha:")
            conta.recovering(users)
    
    def see(self):
            isdecript = conta.isencripted(self.user)
            #print(isdecript)
            if(isdecript):
                choose = input("\n procurar senha aperte p ou t para ver todas as senhas ou ctrl+c para sair:")

                match choose:

                    case "t":
                        conta.buscar_senhas(self.user,True,None)
                        conta.isencripted(self.user)
            
                    case 'p':
                        senha = input("\n nome da plataforma que deseja buscar ou ctrl+c para sair:")
                
                        conta.buscar_senhas(self.user,False,senha)
                        conta.isencripted(self.user)
            
                    case _:
                        print("\n opção inválida, escolha pelo menos umas das opções")
            """else:
                self.response = True
                self.user_interface()"""
    
    def delete_password(self,user):
        
        conta.deleting_passwords(user)

    def main(self):
        self.user_input()

#manager= interfaces()
#manager.main()