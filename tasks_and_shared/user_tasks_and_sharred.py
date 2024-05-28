import json
from datetime import datetime
import os
from Cryptodome.Random import get_random_bytes
from uuid import uuid4
from vault_module.vlt_mod import Note, StorageExplorer, NoteWrapper
from vault_module.vlt_mod import NOTE_JSON_STRUCTURE, FileEntry
from enc_module.enc_mod import EncRSA


class Task(NoteWrapper):
    def __init__(self, note: Note, key: str):
        super().__init__(note, 1, key)
        task_data = json.loads(note.header)
        self.start_time = datetime.fromisoformat(task_data["st_time"])
        self.end_time = datetime.fromisoformat(task_data["end_time"])
        self.tags = set(task_data["tags"])
    
    def exclude_tag(self, tag: str):
        self.tags.discard(tag)

    def include_tag(self, tag: str):
        self.tags.add(tag)
    
    def change_start_time(self, st_time: datetime):
        if self.end_time < st_time:
            return 1
        self.start_time = st_time
        return 0
    
    def change_end_time(self, en_time: datetime):
        if self.start_time > en_time:
            return 1
        self.end_time = en_time
        return 0
    
    def save(self, key: str):
        self._note.header = json.dumps({"st_time": self.start_time.isoformat(),
                                        "end_time": self.end_time.isoformat(),
                                        "tags": list(self.tags)})
        super().save(key)


class UserFiles:
    def __init__(self, username, key, code, path, add):
        self.username = username
        self.key = key
        self.code = code
        self.path = StorageExplorer.fix_path(path)
        self.additional = add
    
    def dict_fix(self) -> dict:
        return {"username": self.username,
                "code": self.code,
                "additional": self.additional}
    
    def get_tasks(self) -> list:
        task_list = []
        st = StorageExplorer()
        path = self.path + '/tasks'
        task_dir = st.get_contents(path)
        for i in task_dir.structure:
            if isinstance(i, FileEntry):
                with open(i.path, "r", encoding="UTF-8") as file:
                    task = json.load(file)
                if i.name.split('.')[-1] == "json" and \
                   task.keys() == NOTE_JSON_STRUCTURE:
                    task_list.append(Task(Note.load_from_entry(i), self.key))
        return task_list
    
    def create_task(self, start_time, end_time, tags, path):
        n_task = Note.new_note(path)
        h = json.dumps({"st_time": start_time,
                        "en_time": end_time,
                        "tags": tags})
        n_task.header = h
        n_task.protect(self.key)
        n_task.save()
        task = Task(n_task, self.key)
        return task
    
    def generate_dirs(self):
        st = StorageExplorer()
        dir_list = [self.path + i for i in ["", "/notes",  "/tasks", "/shared",
                                            "/shared/keys"]]
        for i in dir_list:
            if not os.path.isdir(i):
                os.mkdir(i)
        if len(os.listdir(dir_list[-1])) < 2:
            pr_key, pb_key = EncRSA.generate_keys()
            with open(
                     self.path +  "/shared/keys/public.pem", "wb") as file:
                file.write(EncRSA.export_public(pb_key))
            with open(self.path + "/shared/keys/private.bin", 'wb') as file:
                file.write(EncRSA.export_private(pr_key, self.key))
        if not os.path.isfile(self.path + '/tags.json'):
            tags = json.dumps([])
            with open(self.path + "/tags.json", 'w', encoding='UTF-8') as file:
                file.write(tags)
    
    def get_tags(self):
        with open(self.path + "/tags.json", 'r', encoding='UTF-8') as file:
            tags = file.read()
        return json.loads(tags)
    
    def save_tags(self, tags_list: list):
        tags = json.dumps(tags_list)
        with open(self.path + "/tags.json", 'w', encoding='UTF-8') as file:
            file.write(tags)
    
    def get_keys(self):
        with open(self.path + "/shared/keys/public.pem", 'rb') as file:
            pb_key = EncRSA.import_public(file.read())
        with open(self.path + "/shared/keys/private.bin", 'rb') as file:
            pr_key = EncRSA.import_private(file.read(), self.key)
        return pr_key, pb_key

    def get_shared(self) -> list:
        shared_list = []
        st = StorageExplorer()
        dr = st.get_contents(self.path + '/shared')
        pr_key, _ = self.get_keys()
        names_list = [i.path[:-4] for i in dr.structure
                      if isinstance(i, FileEntry) and
                      i.name.split('.')[-1] == 'key' and
                      st.check_existance(i.path[:-3] + 'json', "file")]
        for i in names_list:
            with open(i + '.key', 'rb') as file:
                session_key = EncRSA().decrypt_session_key(pr_key, file.read())
            new = Note.load_from_entry(FileEntry(i.split('/')[-1] + '.json',
                                                 i + '.json'))
            shared_list.append(NoteWrapper(new, 1, session_key))
        return shared_list


def share_a_note(share_path: str, note: NoteWrapper):
    new_name = str(uuid4())
    new_note = note.copy()
    new_note.change_path(share_path + f'/shared/{new_name}.json')
    session_key = b'\0'
    while b'\0' in session_key:
        session_key = get_random_bytes(32)
    new_note.protection_flag = 1
    new_note.save(session_key)
    with open(share_path + '/shared/keys/public.pem', 'rb') as file:
        pb_key = EncRSA.import_public(file.read())
    enc_key = EncRSA().encrypt_session_key(pb_key, session_key)
    del session_key
    with open(share_path + f'/shared/{new_name}.key', 'wb') as file:
        file.write(enc_key)
        
