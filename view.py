import text


class View:
    
    def main_menu(self):
        print(text.menu[0])
        for i, item in enumerate(text.menu[1:], 1):
            print(f'{i:>5} {item}')
        select = input(text.menu_select)
        if select.isdigit() and 0 < int(select) < len(text.menu):
            return int(select)  
        print(text.input_menu_error(text.menu))
        
    def create_note(self):
        return tuple([input(txt) for txt in text.input_note])
    
    def find_note(self):
        return int(input(text.find_note))

    def print_note(self, founded_note):
        print('=========================')
        print("Выбранная заметка:\n")
        print(founded_note)
        print('=========================\n')

    def action_with_note(self, founded_note):
        if founded_note:
            self.print_note(founded_note)
        else:
            print(text.unfounded_note)

    def note_menu(self):
        print(text.menu_note_action[0])
        for i, item in enumerate(text.menu_note_action[1:], 1):
            print(f'{i:>5} {item}')
        select = input(text.menu_select)
        if select.isdigit() and 0 < int(select) < len(text.menu_note_action):
            return int(select)
        print(text.input_menu_error(text.menu_note_action))

    def message_delete_note(self):
        print(text.note_delete)

    def update_note(self):
        return self.create_note()

    def show_all_notes(self, notes):
        for note in notes:
            print('==================================')
            print(note)
            print('==================================')