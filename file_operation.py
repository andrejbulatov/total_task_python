import json

from note import Note


class File_operation:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        notes_list = list()
        with open(self.file_path, 'r', encoding='utf-8') as note_file:
            notes_json = note_file.read()
            notes = json.loads(notes_json)
            new_notes = sorted(notes, key=lambda k: k["time"])
            for item in new_notes:
                notes_list.append(Note(item['id'], item['time'], item['title'], item['message']))
        return notes_list

    def save_json(self, notes):
        notes_list = list()
        for note in notes:
            notes_list.append({'id': note.uid,
                               'time': note.time,
                               'title': note.title,
                               'message': note.message
                               })
        note_json = json.dumps(notes_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)
        with open(self.file_path, 'w', encoding='utf-8') as note_file:
            note_file.write(note_json)