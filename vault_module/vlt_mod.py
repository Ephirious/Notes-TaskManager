import datetime
import os
from base64 import b64encode, b64decode
import json
from random import randint
import enc_module.enc_mod as encryption

NOTE_JSON_STRUCTURE = {"user", "header", "id", "encryption", "data"}


class FEWrongArguments(Exception):
    "Wrong arguments are given to FileExplorer method"


class FileFormatError(Exception):
    "File with wrong format (or wrong suffix) were given"


class ProtectionError(Exception):
    """Protection operation could not be procceed without further errors\
 and data loses"""


class NoteParametersError(Exception):
    "Some of notes parameters are empty or incorrectly presented"


class NoteWrapperError(Exception):
    "Wrong protection argument were given to NoteWrapper"


class FileEntry:
    """Basic (file) entry class for file hierarchy search
    """

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def __repr__(self) -> str:
        return "File: " + self.path

    def set_new_path(self, new: str):
        """changes path to entry

        Args:
            new (str): updated path
        """
        self.path = new
        self.name = self.path.split('/')[-1]


class DirEntry(FileEntry):
    """Directory entry class for file hierarchy search
    """

    def __init__(self, name: str, path: str, contents: list):
        super().__init__(name, path)
        self.contents = contents
        self.structure = []

    def __repr__(self) -> str:
        return f"Dir: {self.path}\nContents: " \
            + " ".join((i for i in self.contents))


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

    def get_entry(self, path):
        f_type = self.type_check(path)
        if f_type == 1:
            return DirEntry(path.split("/")[-1], path, [])
        if f_type == 2:
            return FileEntry(path.split("/")[-1], path)
        return None

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
        structure = []
        x = self.get_entry(path)
        if isinstance(x, DirEntry):
            entries = os.listdir(path)
            for name in entries:
                contents.append(path + '/' + name)
                structure.append(self.get_entry(path + '/' + name))
            x.structure = structure
            x.contents = contents
            return x
        if isinstance(x, FileEntry):
            return x
        return None

    def cmp(self, entry: FileEntry):
        return isinstance(entry, FileEntry)

    def get_structure(self, path: str) -> DirEntry:
        """generates hierarchy of Entries

        Args:
            path (str): path that lead to root dir for structure build

        Returns:
            DirEntry: root of structure
        """
        root = self.get_contents(path)

        return root

    def delete(self, entry):
        """recursively deletes substructure

        Args:
            entry (FileEntry|DirEntry): entry that needs to be deleted

        Raises:
            FEWrongArguments: if entry was ot given

        Returns:
            int: 0 if deletion is succesfull, 1 if entry already does not exist
        """
        if isinstance(entry, FileEntry):
            if self.check_existance(entry.path, "file"):
                os.remove(self.fix_path(entry.path))
                return 0
            return 1
        if isinstance(entry, DirEntry):
            if self.check_existance(entry.path, "dir"):
                entry = self.get_structure(entry.path)
                for elem in entry.contents:
                    self.delete(elem)
                os.rmdir(self.fix_path(entry.path))
                return 0
            return 1
        raise FEWrongArguments


class Hierarchy:
    """Represent file system hierarchy
    """

    def __init__(self, root: str):
        f_e = _FileExplorer()
        self.root = f_e.get_contents(root)
        self.loaded = {}
        self._f_e = _FileExplorer()

    def load(self, path: str) -> DirEntry:
        """Loads structure of DirEntry

        Args:
            dr_e (DirEntry): DirEntry that needs to be loaded

        Returns:
            DirEntry: Loaded DirEntry
        """

        root = self._f_e.get_contents(path)
        root.structure = []
        for entry in root.contents:
            if self._f_e.type_check(entry) in {1, 2}:
                root.structure.append(self._f_e.get_contents(entry))
        if self._f_e.check_existance(path, "dir"):
            self.loaded[path] = root
        return root

    def update(self, path: str):
        """Updates(reloads) structure of DirEntry

        Args:
            path (str): path of DirEntry that needs to be updated.
        """
        if path in self.loaded:
            self.loaded[path] = self.load(self.loaded[path])

    def delete(self, path: str):
        """deletes entry from disk and hierarchy

        Args:
            path (str): path to entry for deletion.
        """
        if path in self.loaded:
            self._f_e.delete(self.loaded[path])
            stc = [self.loaded[path]]
            while (len(stc)):
                x = stc.pop()
                for i in x.contents:
                    if i in self.loaded:
                        stc.append(self.loaded[i])
                self.loaded.pop(x)
        else:
            self._f_e.delete(self._f_e.get_contents(path))
        self.update("/".join(path.split("/")[-1]))


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
        self.createtime = str(datetime.datetime.now())

    def dict_fix(self):
        records = {"header": self.header,
                   "user": self.user,
                   "id": self.note_id,
                   "encryption": [0, 0],
                   "data": self.data,
                   "createtime": self.createtime}

        records["encryption"][0] = self.enc_flag
        if self.enc_flag != 0:
            records["encryption"][1] = self.enc_parameters

        return records

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
            self.createtime = records["createtime"]

    def save(self):
        """writes note's contents into .json file

        Raises:
            FileFormatError: were given frong filename format
        """
        if self.path is not None:
            if self.path.split(".")[-1] != "json":
                raise FileFormatError
            dmp = json.dumps(self.dict_fix(), ensure_ascii=False, indent=2)
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
        e_data, tag, nonce, _ = alg.encrypt(self.data.encode("utf-8"),
                                            password)
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
            lambda x: b64decode(x.encode("utf-8")),
            self.enc_parameters))
        self.data, auth = alg.decrypt(self.data,
                                      self.enc_parameters[0],
                                      self.enc_parameters[1],
                                      password)
        if not auth:
            raise encryption.EncAuthError
        self.data = self.data.decode("utf-8")
        self.enc_flag = 0
        self.enc_parameters = []

    @staticmethod
    def new_note(path=None):
        """creates new note with random id

        Returns:
            Note: new empty note
        """
        new = Note(path)
        new.note_id = randint(1, 10 ** 10 - 1)
        return new

    @staticmethod
    def load_from_entry(note_entry: FileEntry):
        """creates Note from search entry

        Args:
            note_entry (FileEntry): Entry of note

        Returns:
            Note: new note with loaded data
        """
        read_note = Note(note_entry.path)
        read_note.open()
        return read_note

    def copy(self):
        """creates note object that copies original note (except for id)

        Returns:
            Note: note's copy
        """
        new = Note.new_note()
        new.header = self.header
        new.data = self.data
        new.enc_flag = self.enc_flag
        new.enc_parameters = self.enc_parameters
        new.user = self.user
        new.createtime = datetime.datetime.now()
        return new


class NoteWrapper():
    """Class that provides wrapper for Note object
    """

    def __init__(self, note: Note, protection):
        self._note = note
        self.protection_flag = protection

    def change_header(self, header: str):
        """changes header of note to provided one

        Args:
            header (str): new header of note
        """
        self._note.header = header

    def change_path(self, path):
        """changes path to note's file to provided one

        Args:
            path (str): new path
        """
        self._note.path = path

    def get_header(self) -> str:
        """get header of note

        Returns:
            str: header of note
        """
        return self._note.header

    def get_path(self) -> str:
        """get path to note

        Returns:
            str: path to note
        """
        return self._note.path

    def write(self, new_data: str):
        """change note's contents

        Args:
            new_data (str): new contents of note
        """
        self._note.data = new_data

    def read(self) -> str:
        """read note's contents

        Returns:
            str: note's data
        """
        return self._note.data

    def save(self, key=None):
        """saves note to file

        Args:
            key (str, optional): key used for encryption. Defaults to None.

        Raises:
            NoteWrapperError: raised if wrong set of args were given
        """
        if self.protection_flag and key is None:
            raise NoteWrapperError
        if self.protection_flag:
            self._note.protect(key)
        self._note.save()
        if self.protection_flag:
            self._note.unprotect(key)

    def copy(self):
        """creates copy of note (only id differs)

        Returns:
            NoteWrapper: Wrapper of note's copy
        """
        return NoteWrapper(self._note.copy(), self.protection_flag)


class Storage():
    """ represent storage of notes
    """

    def __init__(self, path: str):
        self.name = path.split('/')[-1]
        self.user = str()
        self.path = path
        self.protection = bool()
        self.storage_entry = None
        self.hierarchy = None

    def json_load(self, storage_data: dict):
        """loads storage data from read json (dict)

        Args:
            storage_data (dict): data that needs to be loaded
        """
        self.name = storage_data["name"]
        self.user = storage_data["user"]
        self.protection = storage_data["protection"]

    def load_structure(self):
        """creates DirEntry of storage
        """
        if self.path is not None:
            self.hierarchy = Hierarchy(self.path)
            self.storage_entry = self.hierarchy.root

    @staticmethod
    def new_storage(name: str, path: str, protection: bool):
        """creates new storage object (not a dir)

        Args:
            name (str): name of storage
            path (str): path to storage
            protection (bool): tells if stoarge should be protected

        Returns:
            Storage: new storage object
        """

        new = Storage(path)
        new.protection = protection
        new.name = name
        new.load_structure()
        return new

    def get_note(self, file: FileEntry) -> NoteWrapper:
        """creates Notewrapper from note's FileEntry

        Args:
            file (FileEntry): _description_

        Returns:
            NoteWrapper: _description_
        """
        return NoteWrapper(Note.load_from_entry(file), self.protection)

    def create_note(self, path) -> NoteWrapper:
        """creates new notewrapper object (not a file)

        Returns:
            NoteWrapper: _description_
        """
        new = Note.new_note(path)
        new.user = self.user
        return NoteWrapper(new, self.protection)

    def save_as(self, note: NoteWrapper, path: str, key=None):
        """writes note as file to a proveded path

        Args:
            note (NoteWrapper): note that will be written
            path (str): path of new file
            key (str, optional): encryption key. Defaults to None.
        """
        new = note.copy()
        new.change_path(path)
        new.save(key)

    def remove(self, entry):
        """deletes entry from hierarchy and file system

        Args:
            entry (FileEntry|DirEntry): Entry that needs to be deleted.
        """
        self.hierarchy.delete(entry.path)