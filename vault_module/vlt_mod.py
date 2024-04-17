import os
from base64 import b64encode, b64decode
import json
import enc_mod as encryption


class FEWrongArguments(Exception):
    "Wrong arguments ere given to FileExplorer method"


class FileFormatError(Exception):
    "File with wrong format (or wrong suffix) were given"


class ProtectionError(Exception):
    """Protection operation could not be procceed without further errors\
 and data loses"""


class NoteParametersError(Exception):
    "Some of notes parameters are empty or incorrectly presented"


class FileEntry:
    """Basic (file) entry class for file hierarchy search
    """
    def __init__(self, name: str,  path: str):
        self.name = name
        self.path = path


class DirEntry(FileEntry):
    """Directory entry class for file hierarchy search
    """
    def __init__(self, name: str, path: str, contents: list):
        super().__init__(name, path)
        self.contents = contents
        self.structure = []


class _FileExplorer():
    """works with paths, files and dirs
    """
    def __init__(self):
        self.curr_path = None
        self.dest_path = None

    @staticmethod
    def fix_path(path: str):
        """returns proper absolute path

        Args:
            path (str): path than need to be processed

        Returns:
            str: proper path
        """
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
        """sets current path with proper path

        Args:
            path (str): path that we want to set as current
        """
        path = self.fix_path(path)
        if not self.check_existance(path, "dir"):
            self.curr_path = None
        else:
            self.curr_path = path

    @staticmethod
    def type_check(path: str) -> int:
        """checks if path leads to file, dir or neither

        Args:
            path (str): path that need to be checked

        Returns:
            int: 1 for dir, 2 for file, 0 for neither of those
        """
        if os.path.isdir(path):
            return 1
        if os.path.isfile(path):
            return 2
        return 0

    def get_contents(self, path):
        """Creates Entry object for entered path

        Args:
            path (str): path that defines Entry object

        Returns:
            DirEntry: if path leads to dir
            FileEntry: if path leads to file
            None: if path is incorrect or leads to neither dir nor file
        """
        contents = []
        f_type = self.type_check(path)
        if f_type == 1:
            entries = os.listdir(path)
            for name in entries:
                contents.append(path + '/' + name)
            return DirEntry(path.split("/")[-1], path, contents)
        if f_type == 2:
            return FileEntry(path.split("/")[-1], path)
        return None

    def get_structure(self, path: str) -> DirEntry:
        """generates hierarchy of Entries

        Args:
            path (str): path that lead to root dir for structure build

        Returns:
            DirEntry: root of structure
        """
        root = self.get_contents(path)
        for entry in root.contents:
            if self.type_check(entry) == 1:
                root.structure.append(self.get_structure(entry))
            elif self.type_check(entry) == 2:
                root.structure.append(self.get_contents(entry))
        return root


class StorageExplorer(_FileExplorer):
    """File system explorer with Storage creating functionality
    """
    def check_for_storage(self) -> bool:
        """checks if current path leads to storage

        Returns:
            bool: True if path contains not empty storage's json else False
        """
        if self.curr_path is None:
            return False
        self.dest_path = self.curr_path + "/.storage/storage.json"
        if (self.check_existance(self.dest_path, "file") and
           os.path.getsize(self.dest_path) > 0):
            return True
        return False

    def read_storage(self, path: str):
        """Creates new Storage object

        Args:
            path (str): path to storage dir

        Returns:
            Storage: new storage object
        """
        self.curr_path = path
        if self.check_for_storage():
            with open(self.curr_path + "/.storage/storage.json", "r",
                      encoding="utf-8") as file:
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
    def __init__(self, path: str) -> None:
        self.header = str()
        self.user = str()
        self.note_id = int()
        self.path = path
        self.enc_flag = int()
        self.enc_parameters = list()
        self.data = str()

    def open(self):
        """opens note's .json file and loads note's data

        Raises:
            FileFormatError: were given wrong path to note
        """
        if self.path is not None:
            if self.path.split(".")[-1] != "json" or \
               not os.path.isfile(self.path):
                raise FileFormatError
            with open(self.path, 'rb') as file:
                records = json.load(file)
            self.header = records["header"]
            self.user = records["user"]
            self.note_id = records["id"]
            self.enc_flag = records["encryption"][0]
            if self.enc_flag != 0:
                self.enc_parameters = records["encryption"][1]
            self.data = records["data"]

    def save(self):
        """writes note's contents into .json file

        Raises:
            FileFormatError: were given frong filename format
        """
        if self.path is not None:
            if self.path.split(".")[-1] != "json":
                raise FileFormatError
            records = {}
            records["header"] = self.header
            records["user"] = self.user
            records["id"] = self.note_id
            records["encryption"] = [0, 0]
            records["encryption"][0] = self.enc_flag
            if self.enc_flag != 0:
                records["encryption"][1] = self.enc_parameters
            records["data"] = self.data
            dmp = json.dumps(records, ensure_ascii=False)
            with open(self.path, 'w', encoding="utf-8") as file:
                file.write(dmp)

    def protect(self, password):
        """protects data of note with encryption
            also adds encryption parameters to notes

        Args:
            password (bytes/string): new password for data encryption

        Raises:
            ProtectionError: can't protect data that is already protected
        """
        if self.enc_flag != 0:
            raise ProtectionError
        alg = encryption.EncChaCha()
        salt = encryption.get_random_bytes(16)
        e_data, tag, nonce, _ = alg.encrypt(
                                            self.data.encode("utf-8"),
                                            encryption.bcrypt(
                                                password,
                                                cost=12,
                                                salt=salt))
        self.enc_flag = 1
        self.data = b64encode(e_data).decode("utf-8")
        self.enc_parameters = list(map(
                                       lambda x: b64encode(x).decode("utf-8"),
                                       [tag,
                                        nonce,
                                        salt]))

    def unprotect(self, password):
        """decrypt note's data

        Args:
            password (bytes/string): password for data decryption

        Raises:
            ProtectionError: can't unprotect data that is not protected
            encryption.EncAuthError: can't authenticate data
        """
        if self.enc_flag != 1:
            raise ProtectionError
        alg = encryption.EncChaCha()
        self.data = b64decode(self.data.encode("utf-8"))
        self.enc_parameters = list(map(
                                       lambda x: b64decode(x).encode("utf-8"),
                                       self.enc_parameters))
        self.data, auth = alg.decrypt(self.data,
                                      self.enc_parameters[0],
                                      self.enc_parameters[1],
                                      alg.pass_to_hash(password,
                                                       self.enc_parameters[2]))
        if not auth:
            raise encryption.EncAuthError
        self.data = self.data.decode("utf-8")
        self.enc_flag = 0
        self.enc_parameters = []

    @staticmethod
    def load_from_entry(note_entry: FileEntry):
        """creates Note from search entry

        Args:
            note_entry (FileEntry): Entry of note

        Returns:
            Note: new note with loaded data
        """
        new_note = Note(note_entry.path)
        new_note.open()
        return new_note


class Storage():
    """ represent storage of notes
    """
    def __init__(self, path: str):
        self.name = str()
        self.user = str()
        self.path = path
        self.storage_entry = list()

    def json_load(self, storage_data: dict):
        """loads storage data from read json (dict)

        Args:
            storage_data (dict): data that needs to be loaded
        """
        self.name = storage_data["name"]
        self.user = storage_data["user"]

    def load_structure(self):
        """creates DirEntry of storage
        """
        if self.path is not None:
            st_expl = StorageExplorer()
            self.storage_entry = st_expl.get_structure(self.path)


fl = StorageExplorer()
st = fl.read_storage("./test/st")
nt = Note.load_from_entry(st.storage_entry.structure[1].structure[0])
nt.protect("13")
nt.unprotect("13")
nt.save()
