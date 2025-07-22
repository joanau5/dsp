# NaClProfile.py
# An encrypted version of the Profile class provided by the Profile.py module
# 
# for ICS 32
# by Mark S. Baldwin

#Lucas Murray
#lomurray@uci.edu
# 25608000
#Joana Ugarte
#joanau@uci.edu
#44875730

# TODO: Install the pynacl library so that the following modules are available
# to your program.
import json, time, os
from pathlib import Path
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from NaClDSEncoder import NaClDSEncoder
from Profile import Profile, Post, DsuFileError, DsuProfileError

# TODO: Import the Profile and Post classes
# TODO: Import the NaClDSEncoder module
    
# TODO: Subclass the Profile class
class NaClProfile(Profile):
    def __init__(self):
        """
        TODO: Complete the initializer method. Your initializer should create the follow three 
        public data attributes:

        public_key:str
        private_key:str
        keypair:str

        Whether you include them in your parameter list is up to you. Your decision will frame 
        how you expect your class to be used though, so think it through.
        """
        self.public_key = ''
        self.private_key = ''
        self.keypair = ''
        self._posts = []

    def generate_keypair(self) -> str:
        """
        Generates a new public encryption key using NaClDSEncoder.

        TODO: Complete the generate_keypair method.

        This method should use the NaClDSEncoder module to generate a new keypair and populate
        the public data attributes created in the initializer.

        :return: str    
        """
        nacl_enc = NaClDSEncoder()
        nacl_enc.generate()
        self.public_key = nacl_enc.public_key
        self.private_key = nacl_enc.private_key
        self.keypair = nacl_enc.keypair
        

    def import_keypair(self, keypair: str):
        """
        Imports an existing keypair. Useful when keeping encryption keys in a location other than the
        dsu file created by this class.

        TODO: Complete the import_keypair method.

        This method should use the keypair parameter to populate the public data attributes created by
        the initializer. 
        
        NOTE: you can determine how to split a keypair by comparing the associated data attributes generated
        by the NaClDSEncoder
        """
        self.keypair = keypair
        for i in range(len(keypair)-1):
            if keypair[i] == '=':
                num = i
                self.public_key = keypair[:i + 1]
                self.private_key = keypair[i + 1:]
            
        

    """
    TODO: Override the add_post method to encrypt post entries.

    Before a post is added to the profile, it should be encrypted. Remember to take advantage of the
    code that is already written in the parent class.

    NOTE: To call the method you are overriding as it exists in the parent class, you can use the built-in super keyword:
    
    super().add_post(...)
    """
    def add_post(self, post: Post) -> None:
        newpost = post
        newpost.set_entry
        nacl_enc = NaClDSEncoder()
        enkey = nacl_enc.encode_public_key(self.public_key)
        privkey = nacl_enc.encode_private_key(self.private_key)
        box = nacl_enc.create_box(privkey, enkey)
        newmessage = nacl_enc.encrypt_message(box, newpost.entry)
        newpost.set_entry(newmessage)
        super().add_post(newpost)


    """
    TODO: Override the get_posts method to decrypt post entries.

    Since posts will be encrypted when the add_post method is used, you will need to ensure they are 
    decrypted before returning them to the calling code.

    :return: Post
    
    NOTE: To call the method you are overriding as it exists in the parent class you can use the built-in super keyword:
    super().get_posts()
    """
    
    def get_posts(self) -> list[Post]:
        nacl_enc = NaClDSEncoder()
        enkey = nacl_enc.encode_public_key(self.public_key)
        privkey = nacl_enc.encode_private_key(self.private_key)
        box = nacl_enc.create_box(privkey, enkey)
        listy2 = []
        listy = super().get_posts()
        for x in listy:
            greg = Post()
            greg.set_entry(x.entry)
            greg.set_time(x._timestamp)
            msg = greg.entry
            depost = nacl_enc.decrypt_message(box, msg) 
            greg.set_entry(depost)
            listy2.append(greg)

        return listy2
            
            
        
        

    """
    TODO: Override the load_profile method to add support for storing a keypair.

    Since the DS Server is now making use of encryption keys rather than username/password attributes, you will 
    need to add support for storing a keypair in a dsu file. The best way to do this is to override the 
    load_profile module and add any new attributes you wish to support.

    NOTE: The Profile class implementation of load_profile contains everything you need to complete this TODO.
     Just copy the code here and add support for your new attributes.
    """
    def load_profile(self, path: str) -> None:
        p = Path(path)

        if os.path.exists(p) and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.public_key = obj['public_key']
                self.private_key = obj['private_key']
                self.keypair = obj['keypair']
                for post_obj in obj['_posts']:
                    post = Post(post_obj['entry'], post_obj['timestamp'])
                    self._posts.append(post)
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()




    def encrypt_entry(self, entry:str, public_key:str) -> bytes:
        """
        Used to encrypt messages using a 3rd party public key, such as the one that
        the DS server provides.
        
        TODO: Complete the encrypt_entry method.

        NOTE: A good design approach might be to create private encrypt and decrypt methods that your add_post, 
        get_posts and this method can call.
        
        :return: bytes 
        """
        nacl_enc = NaClDSEncoder()

        enkey = nacl_enc.encode_public_key(public_key)
        privkey = nacl_enc.encode_private_key(self.private_key)
        box = nacl_enc.create_box(privkey, enkey)
        newmessage = nacl_enc.encrypt_message(box, entry)
        return newmessage
        
        
        
