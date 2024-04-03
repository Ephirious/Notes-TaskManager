import sys
import json
sys.path.append('..')
from enc_module import enc_mod as encryption


class FileFormatError(Exception):
    "Were given file with wrong format (or wrong suffix)"

class ProtectionError(Exception):
    "Protection operation could not be procceed without further errors and data loses"

class NoteParametersError(Exception):
    "Some of notes parameters are empty or incorrectly presented"


class Note:
    """represents notes in program
    """
    def __init__(self, path) -> None:
        self.header = None
        self.user = None
        self.enc_flag = None
        self.enc_parameters = None
        self.data = None
        if path is not None:
            if path.split(".")[1] != "json":
                raise FileFormatError
            with open(path, 'rb') as file:
                records = json.loads(file)
            self.header = records["header"]
            self.user = records["user"]
            self.enc_flag = records["encryption"][0]
            if self.enc_flag is not None:
                self.enc_parameters = records["encryption"][1]
            self.data = records["data"]


    def protect(self, password):
        """protects data of note with encryption
            also adds encryption parameters to notes

        Args:
            password (bytes/string): new password for data encryption

        Raises:
            ProtectionError: can't protect data that is already protected
        """
        if self.enc_flag is not None:
            raise ProtectionError
        alg = encryption.EncChaCha()
        salt = encryption.get_random_bytes
        self.data, tag, nonce, _ = alg.encrypt(password, salt)
        self.enc_flag = True
        self.enc_parameters = [tag, nonce, salt]

    def unprotect(self, password):
        """decrypt note's data

        Args:
            password (bytes/string): password for data decryption

        Raises:
            ProtectionError: can't unprotect data that is not protected
            encryption.EncAuthError: can't authenticate data
        """
        if self.enc_flag is not None:
            raise ProtectionError
        alg = encryption.EncChaCha()
        self.data, auth = alg.decrypt(self.data, self.enc_parameters[0], self.enc_parameters[1],
                                      pass_hash=alg.pass_to_hash(password, self.enc_parameters[3]))
        if not auth:
            raise encryption.EncAuthError
