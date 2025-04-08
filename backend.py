import sqlite3 
import string 
import random 

BANCO = 'gerenciador.db'
conectar = sqlite3.connect(BANCO)
comandos = conectar.cursor()
foreign_key = None
email = None

class login: 

    def __init__(self) -> None:
        comandos.execute("""create table if not exists login(
                         id_login integer primary key autoincrement,
                         usuario text not null,
                         senha text not null,
                         Email text 
                         )""")
        
        comandos.execute("""create table if not exists conta(
                         plataformas text not null,
                         senhas text not null,
                         id_usuario integer,
                         foreign key(id_usuario) references login(id_login))""")
        conectar.commit()
    
    def criar_conta(self,usuario,senha,mail="null"):
        self.usuario = usuario 
        self.senha = senha
        email = mail
        comandos.execute("""insert into login(usuario,senha,Email)
                         values(:usuario,:senha,:Email)""",{'usuario':self.usuario,
                                                    'senha':self.senha, "Email":email})
        conectar.commit()
        
        
    
    def entrar(self,nome:str,key:str) -> bool:
        self.nome = nome 
        self.key = key 
        resultados:str

        comandos.execute("""select usuario,senha from login
                         where usuario =:usuario and senha = :senha""",{'usuario':self.nome,
                                                                        'senha':self.key})
        conectar.commit()
        resultados = comandos.fetchone()
        
        match resultados:
            case (inputuser, inputuser2):
                return True
            
            case _:
                return False
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
        indice = 0 
        nomes= 0 
        listas_usuarios:list= []

        comandos.execute("""select usuario from login""")
        valor = comandos.fetchall()
        conectar.commit()
        for c in range(len(valor)):
                listas_usuarios.append(
                valor[indice][nomes])
            
                indice+=1
        
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
    
    def buscar_senhas(self,usuario:str,todas:bool, especifica:str):

        comandos.execute("""select usuario, id_login from login
                         where usuario = :usuario """, {"usuario":usuario})
        id_conta= comandos.fetchmany()[0][1]
        conectar.commit()
        
        match todas:
            case True:
                comandos.execute("""select plataformas,senhas from conta
                             where id_usuario =:id_usuario""",{"id_usuario":id_conta})
                dados = comandos.fetchall()
                conectar.commit()
                for formatar in dados:
                    print(formatar)
            

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
        if(plataform !="" and password != ""):
            comandos.execute("""select id_login,usuario from login
                             where usuario = :usuario""", {"usuario":user})
            
            foreign_key = comandos.fetchone()[0]
            print(foreign_key)
            conectar.commit()

            comandos.execute("""insert into conta(plataformas,senhas,id_usuario)
                             values (:plataformas,:senhas,:id_usuario)""",{'senhas':password,
                             "id_usuario":foreign_key, "plataformas":plataform})
            conectar.commit()
        else:
            print("apenas dados válidos")
    
    def updating_user(self,account:str,choose,user) ->None:
        foreign_key = None
        
        comandos.execute("""select id_login from login
                                 where usuario =:usuario""",{'usuario':user})
        foreign_key= comandos.fetchone()[0]
        conectar.commit()

        match (choose):
            case '1':
                comandos.execute("""select Email from login
                where id_login =:id_login""",{'id_login':foreign_key})
                check_email = comandos.fetchone()[0]
                conectar.commit()

                if(account == check_email or account == ""):
                    return True
                
                else:
                    comandos.execute("""update login set Email =:Email
                                 where id_login =:id_login""",{"Email":account,"id_login":foreign_key})
                    conectar.commit()
            
            case '2':
                comandos.execute("""update login set senha = :senha
                                 where id_login = :id_login """,{'senha':account,'id_login':foreign_key})
                conectar.commit()

            case '3':
                comandos.execute("""update login set usuario =:usuario
                                 where id_login = :id_login""",{'usuario':account,'id_login':foreign_key})
                conectar.commit()
                
            

log =  login()
conta = contas()
#conta.apagar_conta('gabriel')
#print(bancos.entrar('gabriel','smail'))
#conectar.close()