from notebook import Notebook
from view import View


class Controller:
    def __init__(self, notebook: Notebook, view: View):
        self.notebook = notebook
        self.view = view

    def start(self):
        while True:
            select = self.view.main_menu()
            if select == 1:
                self.notebook.create_note(self.view.create_note())
            elif select == 2:
                id = self.view.find_note()
                founded_note = self.notebook.find_note(id)
                self.view.action_with_note(founded_note)
                while True:
                    note_select = self.view.note_menu()
                    if note_select == 1:
                        self.notebook.delete_note(id)
                        self.view.message_delete_note()
                    if note_select == 2:
                        updated_note = self.view.update_note()
                        self.notebook.update_note(id, updated_note)
                    if note_select == 3:
                        break
            elif select == 3:
                self.notebook.delete_note(self.view.find_note())
                self.view.message_delete_note()
            elif select == 4:
                notes = self.notebook.sort_notes()
                self.view.show_all_notes(notes)
            elif select == 5:
                break