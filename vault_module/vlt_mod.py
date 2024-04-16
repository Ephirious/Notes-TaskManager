import enc_mod as encryption
import os
import json


class FEWrongArguments(Exception):
    "Wrong arguments ere given to FileExplorer method"


class FileFormatError(Exception):
    "File with wrong format (or wrong suffix) were given"


class ProtectionError(Exception):
    """Protection operation could not be procceed without further errors\
 and data loses"""


class NoteParametersError(Exception):
    "Some of notes parameters are empty or incorrectly presented"

class _EntryContents:
    def __init__(self, name: str,  path: str, contents: list):
        self.name = name
        self.path = path
        self.contents = contents

class FileEntry(_EntryContents):
    def __init__(self, name: str, path: str, contents: list):
        super().__init__(name, path, contents)

class DirEntry(_EntryContents):
    def __init__(self, name: str, path: str, contents: list):
        super().__init__(name, path, contents)
        self.structure = []


class FileExplorer():
    """works with paths, files and dirs
    """
    def __init__(self):
        self.curr_path = None
        self.dest_path = None

    @staticmethod
    def fix_path(path):
        path = os.path.abspath(os.path.expanduser(path))
        return path

    def check_existance(self, path: str, path_tp: str) -> bool:
        """checks if path is existing

        Args:
            path (str): path to file/dir
            path_tp (str): specify what we are looking for "dir/file"

        Raises:
            FEWrongArguments: path_tp contains a wrong string

        Returns:
            bool: True if exists else False
        """
        path = self.fix_path(path)
        if path_tp == "dir" and os.path.isdir(path):
            return True
        if path_tp == "file" and os.path.isfile(path):
            return True
        if os.path.exists(path):
            return False
        raise FEWrongArguments

    def set_curr_path(self, path: str):
        path = self.fix_path(path)
        if not self.check_existance(path, "dir"):
            self.curr_path = None
        else:
            self.curr_path = path
    
    @staticmethod
    def type_check(path: str) -> int:
        if os.path.isdir(path):
            return 1
        if os.path.isfile(path):
            return 2
        return 0
    
    def get_contents(self, path="") -> _EntryContents:
        contents = []
        f_type = self.type_check(path)
        if f_type == 1:
            entries = os.listdir(path)
            for name in entries:
                contents.append(path + "/" + name)
            return DirEntry(path.split("/"[-1]), path, contents)
        if f_type == 2:
            return FileEntry(path.split("/"[-1]), path, contents)
        return None
    
    def get_structure(self, path="") -> DirEntry:
        root = self.get_contents(path)
        for entry in root.contents:
            if self.type_check(entry) == 1:
                root.structure.append(self.get_structure(entry))
            elif self.type_check(entry) == 2:
                root.structure.append(self.get_contents(entry))
        return root


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
                new_storage = Storage(path)
                new_storage.json_load(storage_data)
                new_storage.load_structure()
                return new_storage
        else:
            return None
        

class Note:
    """represents notes in program
    """
    def __init__(self, path) -> None:
        self.header = None
        self.user = None
        self.note_id = None
        self.path = path
        self.enc_flag = None
        self.enc_parameters = None
        self.data = None

    def open(self):
        """opens note's .json file and loads note's data

        Raises:
            FileFormatError: were given wrong path to note
        """
        if self.path is not None:
            if self.path.split(".")[1] != "json" or \
               not os.path.isfile(self.path):
                raise FileFormatError
            with open(self.path, 'rb') as file:
                records = json.loads(file)
            self.header = records["header"]
            self.user = records["user"]
            self.note_id = records["id"]
            self.enc_flag = records["encryption"][0]
            if self.enc_flag is not None:
                self.enc_parameters = records["encryption"][1]
            self.data = records["data"]

    def save(self):
        """writes note's contents into .json fiel

        Raises:
            FileFormatError: were given frong filename format
        """
        if self.path is not None:
            if self.path.split(".")[1] != "json":
                raise FileFormatError
            records = {}
            records["header"] = self.header
            records["user"] = self.user
            records["id"] = self.note_id
            records["encryption"] = [None, None]
            records["encryption"][0] = self.enc_flag
            if self.enc_flag is not None:
                records["encryption"][1] = self.enc_parameters
            records["data"] = self.data
            with open(self.path, 'wb') as file:
                json.dump(file, records, ensure_ascii=False)

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


class Storage():
    """ represent storage of notes
    """
    def __init__(self, path):
        self.name = None
        self.user = None
        self.path = path
        self.storage_entry = None

    def json_load(self, storage_data):
        self.name = storage_data["name"]
        self.user = storage_data["user"]

    def load_structure(self):
        st_expl = StorageExplorer()
        self.storage_entry = st_expl.get_structure(self.path)

    def get_note(self, note_entry: FileEntry) -> Note:
        return Note(note_entry.path).open()


if __name__ == "__main__":
    fl = FileExplorer()
    fl.set_curr_path('.')
    if fl.check_existance(fl.curr_path + "/test/f.txt", "file"):
        print(fl.type_check(fl.curr_path + "/test/f.txt"))
        fl.get_structure(fl.curr_path)

