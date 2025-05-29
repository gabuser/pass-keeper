import bcrypt
import hashlib
import base64


msg = b'hidden data'
saltt = bcrypt.gensalt()

password = base64.b64encode(hashlib.sha256(msg).digest())

storage = bcrypt.hashpw(password,saltt)
inputed = b'hidden data'

a = base64.b64encode(hashlib.sha256(inputed).digest())

if(bcrypt.checkpw(a,storage)):
    print('senha correta')

else:
    print('senha errada')