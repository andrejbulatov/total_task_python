menu = ['Главное меню', 'Создать заметку', 'Найти заметку', 'Удалить заметку', 'Вывести все записки', 'Выйти из программы']
menu_select = 'выберите пункт меню: \n'
menu_note_action = ['Действия с заметкой', 'Удалить заметку', 'Изменить заметку', 'Вернуться в главное меню']
input_note = ['Введите заголовок ', 'Введите сообщение ']
find_note = 'Введите порядковый номер заметки\n'
unfounded_note = 'Заметка с таким номером не найдена!\n'
def input_menu_error(array):
    return f'ошибка ввода! выберите пункт от 1 до {len(array) - 1}'
note_delete = '\nЗаметка успешно удалена\n'