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
                         usuario text,
                         senha text
                         )""")
        
        comandos.execute("""create table if not exists conta(
                         plataformas text,
                         senhas text,
                         id_usuario integer,
                         foreign key(id_usuario) references login(id_login))""")
        conectar.commit()
    
    def criar_conta(self,usuario,senha):
        self.usuario = usuario 
        self.senha = senha
        comandos.execute("""insert into login(usuario,senha)
                         values(:usuario,:senha)""",{'usuario':self.usuario,
                                                    'senha':self.senha})
        #conectar.commit()
        
        #comandos.execute("select * from login")
        #print(comandos.fetchall())
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

        #conectar.commit()

        try:
            
            if(self.nome == resultados[0]
            and self.key == resultados[1]):
                return True
        
        except TypeError:
            return False
        
        #conectar.commit()

        """possivel vulnerabilidade do codigo fonte, o usuário pode 
        alterar o código e tentar puxar senhas ou login de outros usuários
        possível solução: criptografar senhas dos usuários ao deslogar do sistema."""

    
    def busca(self,usuario:str,senhas:str) ->bool:
        self.usuario = usuario 
        indice = 0 
        nomes= 0 
        listas_usuarios:list= []
        if(senhas):
            comandos.execute("""select id_login from login
                             where usuario = :usuario""",{'usuario':self.usuario})
            valor = comandos.fetchone()[0]
            print(valor)

            comandos.execute("""select  plataformas from conta
                             where id_usuario = :id_usuario""",{'id_usuario':valor})
            valor = comandos.fetchall()
            for c in range(len(valor)):
                listas_usuarios.append(
                    valor[indice][0]
                )
                indice+=1
            #print(valor[1][0])
        
        else:
            comandos.execute("""select usuario from login""")
            valor = comandos.fetchall()
            for c in range(len(valor)):
                listas_usuarios.append(
                valor[indice][nomes])
            
                indice+=1
        inicio = 0 
        final = len(valor)-1 

        while inicio <= final:
            metade = (inicio+final)//2 
            chute = listas_usuarios[metade]

            if chute == self.usuario:
                return True
            if chute < self.usuario:
                inicio = metade+1 
            
            else:
                final = metade-1
    
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
            comandos.execute("""insert into conta(plataformas,senhas,id_usuario)
                         values (:plataformas,:senhas,:id_usuario)""",{
                             'senhas':armazenar, 'id_usuario':self.foreign_key,
                             'plataformas':plat
                         } )
        conectar.commit()


log =  login()
conta = contas()
#conta.apagar_conta('gabriel')
#print(bancos.entrar('gabriel','smail'))
#conectar.close()