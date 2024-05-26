import json
from datetime import datetime
from vlt_mod import Note, StorageExplorer, NoteWrapper
from vlt_mod import NoteWrapperError, NOTE_JSON_STRUCTURE, FileEntry, DirEntry
from enc_mod import EncAES as encryption


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

    def delete(self):
        st = StorageExplorer()
        st.delete(st.get_contents(self._note.path))




class User_files:
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
        