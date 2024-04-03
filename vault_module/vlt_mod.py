import sys
sys.path.append('..')
import os
import json
from enc_module import enc_mod as encryption


class FEWrongArguments(Exception):
    "Wrong arguments ere given to FileExplorer method"


class FileFormatError(Exception):
    "File with wrong format (or wrong suffix) were given"


class ProtectionError(Exception):
    """Protection operation could not be procceed without further errors\
 and data loses"""


class NoteParametersError(Exception):
    "Some of notes parameters are empty or incorrectly presented"


class FileExplorer():
    """works with paths, files and dirs
    """
    def __init__(self):
        self.curr_path = None
        self.dest_path = None

    @staticmethod
    def check_existance(path: str, path_tp: str) -> bool:
        """checks if path is existing

        Args:
            path (str): path to file/dir
            path_tp (str): specify what we are looking for "dir/file"

        Raises:
            FEWrongArguments: path_tp have a wrong string

        Returns:
            bool: True if exists else False
        """
        if os.path.exists(path):
            if path_tp == "dir" and os.path.isdir(path):
                return True
            if path_tp == "file" and os.path.isfile(path):
                return True
            raise FEWrongArguments
        return False

    def set_curr_path(self, path):
        if not self.check_existance(path, "dir"):
            self.curr_path = None
    

class StorageExplorer(FileExplorer):

    def check_for_storage(self) -> bool:
        if self.curr_path is None:
            return False
        self.dest_path = self.curr_path + "/.storage/storage.json"
        if (self.check_existance(self.dest_path, "file") and 
           os.path.getsize(self.dest_path) > 0):
            return True
        return False
    
    def read_storage(self, path):
        self.curr_path = path
        if self.check_for_storage():
            with open(self.curr_path + "/.storage/storage.json", "r",
                      encoding="Unicode") as file:
                storage_data = json.load(file)
                return storage_data
        else:
            self.curr_path = None
            return None


class Storage():
    """ represent storage of notes
    """
    def __init__(self, path):
        self.name = None
        self.user = None
        self.path = path
        self.notes = []
        self.storage_structure = []
    
    def update_storage(self):
        pass

    def load_storage(self):
        pass


class Note:
    """represents notes in program
    """
    def __init__(self, path) -> None:
        self.header = None
        self.user = None
        self.id = None
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
        self.data, auth = alg.decrypt(self.data, self.enc_parameters[0],
                                      self.enc_parameters[1],
                                      pass_hash=alg.pass_to_hash(password,
                                      self.enc_parameters[3]))
        if not auth:
            raise encryption.EncAuthError
