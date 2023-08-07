import datetime
from operator import itemgetter

from file_operation import File_operation
from note import Note


def get_time():
    return datetime.datetime.now()


class Notebook:

    def __init__(self, file_operation):
        self.notes = list()
        self.file_operation = file_operation

    def read_notes(self):
        return self.file_operation.read_json()

    def save_notes(self):
        self.file_operation.save_json(self.notes)

    def create_note(self, new_note):
        time = get_time()
        self.notes = self.read_notes()
        max_uid = 0
        for note in self.notes:
            if int(note.uid) > max_uid:
                max_uid = int(note.uid)
        self.notes.append(Note(str(max_uid + 1), time, *new_note))
        self.save_notes()

    def find_note(self, id):
        self.notes = self.read_notes()
        for note in self.notes:
            if int(note.uid) == id:
                return self.note_to_dict(note)
        return None

    def note_to_dict(self, note):
        return f'id: {note.uid}\ntime: {note.time}\ntitle: {note.title}\nmessage: {note.message}'

    def delete_note(self, id):
        deleted_note = None
        self.notes = self.read_notes()
        for index, note in enumerate(self.notes):
            if int(note.uid) == id:
                deleted_note = self.notes.pop(index)
        self.save_notes()
        return deleted_note

    def update_note(self, id:int, updated_note: tuple):
        self.notes = self.read_notes()
        for note in self.notes:
            if int(note.uid) == id:
                note.time = get_time()
                note.title = updated_note[0]
                note.message = updated_note[1]
        self.save_notes()

    def get_notes(self):
        self.notes = self.read_notes()
        return self.notes

    def sort_notes(self):
        notes = self.read_notes()
        return notes