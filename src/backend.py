import sqlite3 
import string 
import random 
import smtplib,ssl
import safe
import hash

BANCO = 'gerenciador.db'
conectar = sqlite3.connect(BANCO)
comandos = conectar.cursor()
foreign_key = None
email = None
saf = safe.saving
hashh = hash.hashing()

class login: 

    def __init__(self) -> None:
        comandos.execute("""create table if not exists login(
                         id_login integer primary key autoincrement,
                         usuario text not null,
                         senha text not null,
                         Email text,
                         gmail password text,
                         salt text
                         )""")
        
        comandos.execute("""create table if not exists conta(
                         plataformas text,
                         senhas text,
                         id_usuario integer,
                         foreign key(id_usuario) references login(id_login))""")
        conectar.commit()
    
    def criar_conta(self,usuario,senha,mail="null"):
        self.usuario = usuario 
        self.senha = senha
        email = mail
        salt = saf.salting()
        
        hashh.generating_hash(self.senha.encode())
        salt_hash = hashh.creating_salt()
        final_hash = hashh.adding_salt(salt_hash)

        comandos.execute("""insert into login(usuario,senha,Email,salt)
                         values(:usuario,:senha,:Email,:salt)""",{'usuario':self.usuario,
                                                    'senha':final_hash, "Email":email, "salt":salt})
        conectar.commit()
        #saf.key_password()
        #self.returned = saf.password
    
    def entrar(self,nome:str,input_password:str) -> bool:
        self.nome = nome 
        self.input_password= input_password 
        resultados:str

        """comandos.execute(select usuario,senha from login
                         where usuario =:usuario and senha = :senha,{'usuario':self.nome,
                                                                                      'senha':self.key})"""
        comandos.execute("""select id_login from login
                         where usuario in(:usuario)""",{'usuario':self.nome})
        foreign_key = comandos.fetchone()

        if(foreign_key):

            comandos.execute("""select senha from login
                         where id_login in (:id_login)""",{
                             'id_login':foreign_key[0]
                         })
        #conectar.commit()
            password= comandos.fetchone()[0]
            result= hashh.authentication_hash(self.input_password.encode(),password)

        else:
            result = False
        
        match result:
            
            case result if result:
                return True
            
            case _:
                return False
        """"match resultados:
            case (input1,input2) if resultados != None or resultados !='':
                print(input1)
            
            case _:
                return False"""
        """we can use a simple parttern matching to fix this code, the code works as we want to, however,
        the bahavior might bring out vulnabilities due to be an error treatment. 
        Once we are checking if values exists in the database, instead of checking that way, it's possible 
        to match for patterns. 
        
        for instance: if values dosen't return a string literal, the second case could handle this error by 
        matching the status of the returned value."""

        """updated: tested and working without the error handler""" 
    
    def ambiguity(self, saved_user,password) -> bool:
        saved_user= saved_user
        comandos.execute("""select id_login from login
                         where  usuario= :usuario""",{"usuario":saved_user})
        
        check= comandos.fetchone()[0]
        #conectar.commit()

        comandos.execute("""select plataformas from conta
                         inner join login on id_usuario = :id_login
                         where plataformas = :plataformas""",
                         {"id_login":check, "plataformas":password})
        getting= comandos.fetchone()
        
        match getting:
            case [(password)]:
                return True
            
            case _:
                return False
        conectar.commit()

    def busca(self,usuario:str) ->bool:
        self.usuario = usuario 
        listas_usuarios:list= []

        comandos.execute("""select usuario from login""")
        valor = comandos.fetchall()

        for _ in  range(len(valor)):
            listas_usuarios.append(
                valor[_][0])
        
        listas_usuarios= sorted(listas_usuarios)
        inicio = 0 
        final = len(listas_usuarios)-1 

        while inicio <= final:
            metade = (inicio+final)//2 
            chute = listas_usuarios[metade]

            if chute == self.usuario :
                return True
            
            if chute < self.usuario:
                inicio = metade+1 
            
            else:
                final = metade-1
        return False
    
    def buscar_senhas(self,usuario:str,busca:str,senha:str):
        foreign_key = None
        
        comandos.execute("""select id_login from login
                         where usuario = :usuario""", {"usuario":usuario})
        foreign_key= comandos.fetchone()[0]
        conectar.commit()
        
        match busca:
            case True:
                comandos.execute("""select distinct plataformas, senhas from conta
                                 inner join login on id_usuario= :id_login
                                """, {"id_login":foreign_key})
                #print(comandos.fetchall())
                datas = comandos.fetchall()
                conectar.commit()

                for b,a in datas:
                    print(f"\n {b}: {a}")
            
            case False:
                datas = None
                #foreign_key = None
                comandos.execute("""select distinct senhas from conta
                                 inner join login on id_usuario = :id_login
                                 where plataformas in (:plataformas)""",
                                {"id_login":foreign_key, "plataformas":senha})
                
                try:
                    datas = comandos.fetchone()[0]
                    conectar.commit()

                    print(f"{senha}:{datas}")
                
                except TypeError:
                    print("\n nenhuma senha encontrada")

    def cheking_emails(self,service):

        comandos.execute("""select Email from login
                         where Email in (:Email)""",{"Email":service})
        
        try:
            Emails_returned = comandos.fetchone()[0]
            print(Emails_returned)
            conectar.commit()

            if service in Emails_returned:
                return True
            else:
                return False
        except TypeError:
            return None
        
    def gerar_senha(self):
        self.resultado = ''.join(
            random.choices(string.ascii_letters+string.digits+
                           string.punctuation,k=30)
        )
        
        return self.resultado

class contas(login):
    def todelete(self,user:str,deleted:bool):
        self.deleted = deleted

        self.names = user
        comandos.execute("""select id_login
                         from login where usuario = :usuario""",
                         {'usuario':self.names})
        foreign_key = comandos.fetchone()[0]
        conectar.commit()
        
        comandos.execute("""delete from conta 
                         where id_usuario = :id_usuario""",
                         {'id_usuario':foreign_key})
        
        comandos.execute("""delete from login
                         where usuario = :usuario """,{'usuario':self.names})
        conectar.commit()
    
    def addpasswords(self,plataform:str,password:str,
                     user:str):
               
        foreign_key = None

        comandos.execute("""select id_login,usuario from login
                             where usuario = :usuario""", {"usuario":user})
        foreign_key = comandos.fetchone()[0]

        """comandos.execute(select senhas from conta 
                             where id_usuario in (:id_usuario),{"id_usuario":foreign_key})
        
        data = comandos.fetchall()"""
        if(plataform !="" and password !=""):
            comandos.execute("""insert into conta(plataformas,senhas,id_usuario)
                             values (:plataformas,:senhas,:id_usuario)""",{'senhas':password,
                                'id_usuario':foreign_key,'plataformas':plataform})
            conectar.commit()
        
        """if(plataform !="" and password != ""):
            comandos.execute(select salt from login
                             where id_login in (:id_login),{
                                 'id_login':foreign_key
                             })
            salt = comandos.fetchone()[0]"""
        
        """try:
                match data:
                    case data if type(data[0][0]) == bytes:
                        unlocking = saf.unlocking(data,salt)

                        if(unlocking):
                            comandos.execute(insert into conta(plataformas,senhas,id_usuario)
                                values (:plataformas,:senhas,:id_usuario),{'senhas':password,
                                "id_usuario":foreign_key, "plataformas":plataform})
                        
                            conectar.commit()
                            return True
                
                    case data if type(data[0][0]) == str:
                    
                        comandos.execute(insert into conta(plataformas,senhas,id_usuario)
                             values (:plataformas,:senhas,:id_usuario),{'senhas':password,
                             "id_usuario":foreign_key, "plataformas":plataform})
                    
                        conectar.commit()
                        return True
                    
            except IndexError:
                comandos.execute(insert into conta(plataformas, senhas,id_usuario)
                                 values (:plataformas,:senhas,:id_usuario),{"senhas":password,
                                "id_usuario":foreign_key,"plataformas":plataform})
                conectar.commit()
        else:
            print("apenas dados válidos")

        
        #except KeyboardInterrupt:"""
            
    def updating_user(self,account:str,choose,user) ->None:
        foreign_key = None
        comandos.execute("""select id_login from login
                                 where usuario =:usuario""",{'usuario':user})
        foreign_key= comandos.fetchone()[0]
        #conectar.commit()

        match (choose):
            case '1':
                comandos.execute("""select Email from login
                where id_login =:id_login""",{'id_login':foreign_key})
                self.check_email = comandos.fetchone()[0]
                #conectar.commit()

                if(account == self.check_email):
                    return True
                
                else:
                    comandos.execute("""update login set Email =:Email
                                 where id_login =:id_login""",{"Email":account,"id_login":foreign_key})
                    conectar.commit()
            
            case '2':
                hashh.generating_hash(account.encode())
                updating_salt = hashh.creating_salt()
                new_hash = hashh.adding_salt(updating_salt)

                comandos.execute("""update login set senha = :senha
                                 where id_login = :id_login """,{'senha':new_hash,'id_login':foreign_key})
                conectar.commit()

            case '3':
                comandos.execute("""update login set usuario =:usuario
                                 where id_login = :id_login""",{'usuario':account,'id_login':foreign_key})
                conectar.commit()
            
            case '4':
                comandos.execute("""select plataformas from conta
                                 inner join login on id_usuario =:id_login
                                 and plataformas in(:plataformas)""",{
                                     'id_login':foreign_key,'plataformas':account
                                 })
                
                try:
                    plataform= comandos.fetchone()[0]
                    new_plataform= input("insira a nova plataforma:")

                    if(plataform != new_plataform
                       and new_plataform !=''):
                        
                        comandos.execute("""select senhas from conta 
                                         where plataformas in(:plataformas)
                                         and id_usuario in(:id_usuario)""",
                                         {'plataformas':plataform,'id_usuario':foreign_key})
                        unique_password = comandos.fetchone()[0]
                        conectar.commit()

                        comandos.execute("""update conta set plataformas =:plataformas
                                         where senhas in(:senhas)""",{
                                            'plataformas':new_plataform,'senhas':unique_password})
                        conectar.commit()

                        return True
                    
                    else:
                        return False
                
                except TypeError:
                    return False
            
            case '5':#problem to be solved. when the user insert an wrong value, for some reason it's jut stay as wrong without any change
                comandos.execute("""select plataformas from conta
                                 inner join login on id_usuario =:id_login
                                 where plataformas in (:plataformas)""",
                                 {'id_login':foreign_key,'plataformas':account})
                
                oldpass=comandos.fetchone()
                
                if(oldpass):
                    new_password = input("insira a sua nova senha:")

                    if(new_password != ''):
                        comandos.execute("""select senhas,plataformas from conta
                                         inner join login on id_usuario=:id_login
                                         where plataformas in (:plataformas)""",
                                         {'id_login':foreign_key, 'plataformas':oldpass[0]})
                        pattern = comandos.fetchall()

                        
                        match pattern:
                            #print(True)
                            case pattern if type(pattern[0][0]) == bytes:
                                comandos.execute("""select salt from login
                                                 where id_login in (:id_login)""",{'id_login':foreign_key})
                                salt= comandos.fetchone()[0]

                                if(saf.unlocking(pattern,salt)):
                                    #updatedpass = new_password
                                    plataforms = pattern[0][1]
                                    #datas = [(updatedpass,plataforms)]
                                    
                                    comandos.execute("""update conta set senhas=:senhas
                                                     where id_usuario in (:id_usuario)
                                                     and plataformas in (:plataformas)""",{"senhas":new_password,
                                                                                           "plataformas":plataforms,"id_usuario":foreign_key})
                                    conectar.commit()
                            
                            case pattern if type(pattern[0][0]) == str:
                                    plataforms = pattern[0][1]

                                    comandos.execute("""update conta set senhas =:senhas
                                                     where id_usuario in (:id_usuario)
                                                     and plataformas in (:plataformas)""",{"senhas":new_password,
                                                                                           "plataformas":plataforms,"id_usuario":foreign_key})
                                    conectar.commit()

                                    """saf.locking(datas,salt)
                                    newencription = saf.encripted[0]

                                    comandos.execute(update conta set senhas =:senhas
                                                 where id_usuario in (:id_usuario)
                                                 and plataformas in (:plataformas),{
                                                     'senhas':newencription,'id_usuario':foreign_key,'plataformas':plataforms
                                                 })
                                    conectar.commit()"""
                                #print(salt)
                    #passord = self.isencripted(user)
                    else:
                        print('\n insira um senha válida')
                else:
                    print('\n não há nenhuma senha com esse nome')
                    
    def recovering(self,user:str):
            port = 465
            security = ssl.create_default_context()
            send = True

            comandos.execute("""select Email, gmail from login
                         where usuario in (:usuario)""",{"usuario":user})
            datas= comandos.fetchall()
            conectar.commit()

            if(datas):
                email = datas[0][0]
                gmail_pass = datas[0][1]

                try:
                    try:
                        with smtplib.SMTP_SSL("smtp.gmail.com", port,context=security) as mini_server:
                            mini_server.login(email,gmail_pass)
                            CODE = self.gerar_senha()
                            mini_server.sendmail("random@gmail.com",email,f"{CODE}")
                            print("email enviado com sucesso!!")
                            send = True

                    except smtplib.SMTPResponseException:
                        print("erro, a conexão foi fechada isso ocorre pois: \n1 não foi encontrado nenhum email ou senha\n 2 email incorreto \n 3 senha incorreta")
                        send = False
                    
                    while send:
                        insert_code = input("insira o código enviado em seu email:")

                        if(insert_code == "q"):
                            break

                        elif(insert_code == CODE):
                            new_password = input("insira a sua nova senha:")
                            self.updating_user(new_password,'2',user)
                            print("senha alterada com sucesso!!")
                            break

                        else:
                            print("Código incorreto, olhe o seu email")
                except smtplib.SMTPAuthenticationError:
                    print("API do google recusou essa conexão, verifique a senha da API e email")

    def saving_gmail_pass(self,user,password):
        print("\n essa senha é usada para permitir que este programa possa se comunicar " \
        "com a API do gmail google e possa enviar emails")
        foreign_key = None 

        try:
            comandos.execute("""select id_login from login
                             where usuario in (:usuario)""",{'usuario':user})
            foreign_key = comandos.fetchone()[0]

            comandos.execute("""select senha from login
                where id_login in(:id_login)""",{'id_login':foreign_key})
            
            original_password = comandos.fetchone()[0]
            result = hashh.authentication_hash(password.encode(),original_password)

            if result:
                self.gmail_password = input("insira a nova senha do app password:")
                
                comandos.execute("""update login set gmail = :gmail
                             where id_login = :id_login""",{"gmail":self.gmail_password,"id_login":foreign_key[0]}) 
                
                conectar.commit()
                return True
            
            else:
                return False
        
        except:
            return False
        
    def isstorage(self,user):
        self.parsing= []

        foreign_key = None
        try:
            comandos.execute("""select id_login from login
                         where usuario in (:usuario)""",{'usuario':user})
        
            foreign_key = comandos.fetchone()[0]# new problem found 

        #conectar.commit()

            comandos.execute("""select senhas,plataformas from conta
                        inner join login on id_usuario = :id_login""",{"id_login":foreign_key})
        
            self.password= comandos.fetchall()

            comandos.execute("""select salt from login
                         where id_login in(:id_login)""",{'id_login':foreign_key})
        
            self.salt = comandos.fetchone()[0]
        #conectar.commit()

            if self.password:

                return True
        
            else:
                saf.key_password()
                self.new_keypass =saf.password 
                return False
        except TypeError:
            return True
        """função para verificar se há dados armazenados no gerenciador, se os dados
        estiverem armazenados, significa que o usuário já tem a chave criptográfica, caso 
        contrário é necessário criar um. a função retornará false ou true"""
    
    def isencripted(self,user):
        foreign_key = None
        count_function = 0

        #valid = self.isstorage(user)
        """if(valid):

            comandos.execute(select id_login from login
                             where usuario in (:usuario),{'usuario':user})
            
            foreign_key = comandos.fetchone()[0]

            match self.password:

                case self.password if type(self.password[0][0]) == bytes :
                    
                    unlocked=saf.unlocking(self.password,self.salt)

                    for _ in range(len(saf.decript)):
                        converted= saf.decript[_]
                        plataforms = saf.plataforms[_]

                        comandos.execute(update conta set senhas = :senhas
                                         where id_usuario in (:id_usuario)
                                         and plataformas in (:plataformas), {'plataformas':plataforms,
                                                                                'id_usuario':foreign_key,
                                                                                'senhas':converted})
                        conectar.commit()
                    
                    if(unlocked):
                        return True
                    
                    else:
                        return False"""
                    
                #case self.password if type(self.password[0][0]) == str:
        comandos.execute("""select id_login from login
                         where usuario in (:usuario)""",{
                             "usuario":user
                         })
        foreign_key = comandos.fetchone()[0]

        try:
            comandos.execute("""select senhas, plataformas from conta
                         where id_usuario in (:id_usuario)""",{
                             "id_usuario":foreign_key
                         })
            datas = comandos.fetchall()
            
            comandos.execute("""select salt from login
                              where id_login in (:id_login)""",{
                             "id_login":foreign_key
                            })
        
            salt = comandos.fetchone()[0]

            #count_function+=1
            match datas:
                case datas if type(datas[0][0]) == bytes:
                    result = saf.unlocking(datas,salt)

                    if(result !=False):
                        for _ in range(len(saf.decript)):
                            binary = saf.decript[_]
                            plataforms = saf.plataforms[_]

                            comandos.execute("""update conta set senhas=:senhas
                                         where id_usuario in(:id_usuario)
                                         and plataformas in (:plataformas)""",{'plataformas':plataforms,
                                                                               'id_usuario':foreign_key,
                                                                               'senhas':binary})
                        conectar.commit()
                        return True
                
                case _:
                    return True
                
        except IndexError:
            return True
    
    def encrypt(self,user):
        comandos.execute("""select id_login from login
                         where usuario in (:usuario)""",{
                             "usuario":user
                         })
        foreign_key = comandos.fetchone()[0]

        comandos.execute("""select senhas, plataformas from conta
                         where id_usuario in (:id_usuario)""",{
                             "id_usuario":foreign_key
                         })
        datas = comandos.fetchall()
            
        comandos.execute("""select salt from login
                              where id_login in (:id_login)""",{
                             "id_login":foreign_key
                            })
        
        salt = comandos.fetchone()[0]

        try:
            match datas:
                case datas if type(datas[0][0]) == str:
                    saf.locking(datas,salt)

                    for _ in range(len(saf.encripted)):
                        binary = saf.encripted[_]
                        plataforms = saf.plataforms[_]

                        comandos.execute("""update conta set senhas = :senhas
                        where id_usuario in (:id_usuario) 
                        and plataformas in (:plataformas)""",
                        {'plataformas':plataforms, 'id_usuario':foreign_key,
                        'senhas':binary})
                    
                        conectar.commit()
                    return True
        
        except IndexError:
            print("dados salvos")
        
                
    def deleting_passwords(self,user):
        confirmation = True
        lenght_password = 0

        comandos.execute("""select id_login from login
                         where usuario in (:usuario)""",{
                             'usuario':user
                         })
        foreign_key = comandos.fetchone()[0]

        while confirmation:
            removing_passwords= input("insira o nome da plataforma(netflix, amazon,hbo,google...):")
            
            if(removing_passwords=='q'):
                confirmation = False

            else:
                comandos.execute("""delete from conta
                                     where id_usuario in(:id_usuario)
                                     and plataformas in(:plataformas)""",
                                     {
                                        "id_usuario":foreign_key, "plataformas":removing_passwords
                                     })
                conectar.commit()
                    
log =  login()
conta = contas()
#conta.apagar_conta('gabriel')
#print(bancos.entrar('gabriel','smail'))
#conectar.close()