from controller import Controller
from file_operation import File_operation
from notebook import Notebook
from view import View

if __name__ == '__main__':
    file_operation = File_operation('data.json')
    controller = Controller(Notebook(file_operation), View())
    controller.start()