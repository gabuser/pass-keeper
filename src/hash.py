import bcrypt
import hashlib
import base64

class hashing:

    def generating_hash(self,data):
        self.data = data
        
        self.computation= base64.b64encode(hashlib.sha256(self.data).digest())
    
    def creating_salt(self):
        self.salt_hash=bcrypt.gensalt()

        return self.salt_hash
    
    def adding_salt(self,salt):
        self.output = bcrypt.hashpw(self.computation,salt)

        return self.output
    
    def authentication_hash(self,input_hash,saved_hash):
        self.input_hash = input_hash
        self.cheking = base64.b64encode(hashlib.sha256(self.input_hash).digest())

        if(bcrypt.checkpw(self.cheking,saved_hash)):
            return True
        
        else:
            return False