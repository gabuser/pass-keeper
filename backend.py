import sqlite3 
import string 
import random 

BANCO = 'gerenciador.db'
conectar = sqlite3.connect(BANCO)
comandos = conectar.cursor()

class login: 

    def __init__(self) -> None:
        comandos.execute("""create table if not exists login(
                         id_login integer primary key autoincrement,
                         usuario text not null,
                         senha text not null
                         )""")
        
        comandos.execute("""create table if not exists conta(
                         plataformas text not null,
                         senhas text not null,
                         id_usuario integer,
                         foreign key(id_usuario) references login(id_login))""")
        conectar.commit()
    
    def criar_conta(self,usuario,senha):
        self.usuario = usuario 
        self.senha = senha
        comandos.execute("""insert into login(usuario,senha)
                         values(:usuario,:senha)""",{'usuario':self.usuario,
                                                    'senha':self.senha})
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
        confirm = 0
        comandos.execute("""select id_login from login
                         where  usuario= :usuario""",{"usuario":saved_user})
        
        check= comandos.fetchone()[0]
        #conectar.commit()

        comandos.execute("""select plataformas from conta
                         where id_usuario = :id_usuario and plataformas = :plataformas
                         """,{"id_usuario":check,"plataformas":password})
        valor = comandos.fetchone()

        match valor:
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
        """if(senhas): #preciso trabalhar nisso aqui, esqueci de apagar ksksksks
            comandos.execute(select id_login from login
                             where usuario = :usuario,{'usuario':self.usuario})
            valor = comandos.fetchone()[0]
            
            comandos.execute(select  plataformas from conta
                             where id_usuario = :id_usuario,{'id_usuario':valor})
            valor = comandos.fetchall()
            for c in range(len(valor)):
                listas_usuarios.append(
                    valor[indice][0]
                )
                indice+=1
            #print(valor[1][0])"""
        
        
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
        
        if(todas):
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
    def id_(self,plat,nomes:str,armazenar:str,
            excluir:bool):
        self.excluir = excluir

        self.nomes = nomes
        comandos.execute("""select id_login, usuario
                         from login where usuario = :usuario""",
                         {'usuario':self.nomes})
        #conectar.commit()

        self.foreign_key = comandos.fetchone()[0]

        if(self.excluir):
            comandos.execute("""delete from conta 
                         where id_usuario = :id_usuario""",
                         {'id_usuario':self.foreign_key})
        
            comandos.execute("""delete from login
                         where usuario = :usuario """,{'usuario':self.nomes})
        
        else:
            if(plat !="" and armazenar !=""):
                comandos.execute("""insert into conta(plataformas,senhas,id_usuario)
                         values (:plataformas,:senhas,:id_usuario)""",{
                             'senhas':armazenar, 'id_usuario':self.foreign_key,
                             'plataformas':plat
                         } )
                conectar.commit()
            else:
                print("insira dados válidos")
            
            """Note: this code needs to be simplify, it's current unreadeble and confuse. 
            this might lead to futher problems in the future case not updated. a better 
            function name and a better condition more organized."""


log =  login()
conta = contas()
#conta.apagar_conta('gabriel')
#print(bancos.entrar('gabriel','smail'))
#conectar.close()