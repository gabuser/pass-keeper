import base64 
import os 
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string 
import random

class Object_bytes:

    def key_password(self):
        letters = ''.join(string.ascii_letters+string.digits+
                          string.punctuation)
        
        self.password = ''.join(random.choices(letters,k=50))
        
    def salting(self):
        self.salt = os.urandom(16)
        return self.salt

    def generating(self,password,salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length= 32,
            salt=salt,
            iterations=1_200_000)
        
        self.hashed = base64.urlsafe_b64encode(kdf.derive(password.encode()))

class processing(Object_bytes):
    def setting(self):
        pass

    def locking(self,data,salt):
        self.encripted=[]
        self.plataforms = []
        #print("senha única, guarde em algum lugar, não guarde nesse banco. \n")

        #self.password =self.key_password()
        #print(self.password)
        self.generating(self.password,salt)
        self.key = Fernet(self.hashed)

        for _ in data:
            #print(a)

            #print(a)
            self.token = self.key.encrypt(_[0].encode())
            self.encripted.append(self.token)
            self.plataforms.append(_[1])
        
            
            #temp.append(self.token)
        
        #return temp
        #print(self.token)
        
    def unlocking(self,data,salt):
        self.decript = []
        self.plataforms = []

        self.password =input("insira sua senha para descriptografar:")

        try:
            self.generating(self.password,salt)
            self.key = Fernet(self.hashed)

            for _ in data:
                
                self.tobedecrypt= self.key.decrypt(_[0])
                self.decript.append(self.tobedecrypt.decode())
                self.plataforms.append(_[1])
            #print(self.decript)
            #print(type(self.decript[0]))
            return True
        
        except:
            print("\n token inválido, verifique a senha. se voce perdeu ou não tem mais acesso, será necessário" 
            "por segurança deletar todos os seus dados e criar as senhas novamente.")
            
            return False

saving = processing()