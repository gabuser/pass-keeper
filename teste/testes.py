import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b"password" #senha usada para criar o hash necessário para chave
salt = os.urandom(16) # salt contendo 16 bytes de tamanho na memoria para diferenciar a chave
kdf = PBKDF2HMAC( #função usada para criar uma chave derivativa
    algorithm=hashes.SHA256(),#algoritmo usado para criar a chave
    length=32, #tamanho dessa chave
    salt=salt,
    iterations=1_200_000, # tempo ou quantidade de vezes para criar a chave, criando 1200000 
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
token = f.encrypt(b"Secret message!")
print(salt)
b'...'
print(f.decrypt(token))
b'Secret message!'