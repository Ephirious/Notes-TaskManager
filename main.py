import os.path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTreeWidgetItem

from data_base.data_bd import *
from ui_account_login_window import Ui_LoginWindow
from ui_account_sign_in_window import Ui_SigninWindow
from ui_dialogwindow_note import Ui_Dialog
from ui_main_window_notes import Ui_MainWindow
from vault_module.vlt_mod import *


class NotesApp(QMainWindow):
    def __init__(self):
        global STORAGE, USER, PATH, NOTE

        super(NotesApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        STORAGE = StorageExplorer()
        NOTE = None
        PATH = None
        USER = None

        self.open_log_in_window()

        self.ui.btn_storage.clicked.connect(self.open_filemanager)

        # взаимодействие с кнопками
        self.ui.btn_add_note.clicked.connect(self.open_window_addNote)
        self.ui.btn_save.clicked.connect(self.saveNote)
        self.ui.btn_delete_note.clicked.connect(self.delete_note)

        # взаимодействие с списком файлов
        self.ui.treeWidget.itemClicked.connect(self.open_note)
        self.ui.treeWidget.whatsThis()

        # взаимодействие с textEdit

        self.flags_check()

    def ebe(self, e):
        print(e)

    def open_filemanager(self):
        global PATH

        if PATH is None:
            file_dialog = QFileDialog()
            return file_dialog.getExistingDirectory(self, 'Создайте новую папку для заметок', 'Notes')
        else:
            pass

    def flags_check(self):
        global NOTE

        if NOTE is None:
            self.ui.textEdit.setDisabled(True)
            self.ui.textEdit.setText('-----Заметка не выбрана или не создана-----')
            self.ui.btn_save.hide()
            self.ui.btn_delete_note.hide()
        else:
            self.ui.textEdit.setDisabled(False)
            self.ui.btn_save.show()
            self.ui.btn_delete_note.show()
        self.ui.label_save_or_del.setText("")

    def open_window_addNote(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.dialog.pushButton.clicked.connect(self.addNote)

    def open_log_in_window(self):
        self.login_window = QDialog()
        self.login_dialog = Ui_LoginWindow()
        self.login_dialog.setupUi(self.login_window)

        self.login_window.show()
        self.login_dialog.btn_login.clicked.connect(self.log_in_account)
        self.login_dialog.btn_reg.clicked.connect(self.open_sign_in_window)

    def log_in_account(self):
        global USER, PATH, STORAGE

        USER = search_user(self.login_dialog.lineEdit_name.text(),
                           self.login_dialog.lineEdit_password.text())
        if USER:
            if USER.data:
                PATH = USER.data
            else:
                PATH = self.open_filemanager()
                add_link_to_data(USER.login, PATH)

            STORAGE = Storage(PATH)
            STORAGE.name = PATH.split('/')[-1]
            STORAGE.user = USER.login

            root_item = QTreeWidgetItem([f'{STORAGE.name}'])
            self.research_notes(PATH, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

            self.show()
            self.login_window.close()
        else:
            self.login_dialog.label_error.setText('Проверьте верность введеного логина или пароля. ')

    def open_sign_in_window(self):

        # если открыто окно логина
        self.login_window.close()

        self.reg_window = QDialog()
        self.reg_dialog = Ui_SigninWindow()
        self.reg_dialog.setupUi(self.reg_window)

        self.reg_window.show()
        self.reg_dialog.btn_signup.clicked.connect(self.sign_in_account)

    def sign_in_account(self):
        global USER, PATH, STORAGE

        login = self.reg_dialog.lineEdit_login.text()
        password = self.reg_dialog.lineEdit_password.text()

        USER = search_user(login, password)

        if not USER and loginDuplicateChecker(login):

            PATH = self.open_filemanager()
            USER = registration(login, password, PATH)
            STORAGE = Storage(PATH)
            STORAGE.name = PATH.split('/')[-1]
            STORAGE.user = login

            root_item = QTreeWidgetItem([f'{STORAGE.name}'])
            self.research_notes(PATH, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

            self.show()
            self.reg_window.close()
        else:
            self.reg_dialog.label_error.setText('Введеный логин уже занят, пожалуйста'
                                                'введите новый логин')

    """ ФУНКЦИЯ ЗАПЛАТКА НА ТОТ МОМЕНТ,
     ПОКА НЕ БУДЕТ ГОТОВА load_structure().structure
     """

    def research_notes(self, directory, parent_item):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                # Если элемент является каталогом, создаем новый элемент дерева и добавляем его к родительскому элементу
                directory_item = QTreeWidgetItem([item])
                parent_item.addChild(directory_item)
                # Рекурсивно вызываем функцию для обработки подкаталога
                self.research_notes(item_path, directory_item)
            else:
                # Если элемент является файлом, просто добавляем его к родительскому элементу
                file_item = QTreeWidgetItem([item])
                parent_item.addChild(file_item)

    def saveNote(self):
        global NOTE

        if NOTE:
            text = self.ui.textEdit.toPlainText()
            NOTE.write(text)
            NOTE.save()
            self.ui.label_save_or_del.setText("Заметка была успешно сохранена!")

    def addNote(self):
        global STORAGE, USER, PATH, NOTE

        self.saveNote()

        NOTE = STORAGE.create_note()
        NOTE.change_header(self.dialog.lineEdit.text())

        if len(NOTE._note.header) > 15:
            name_n = NOTE._note.header[:10] + '...'
            self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem([name_n]))
        elif len(NOTE._note.header) == 0:
            pass
        else:
            self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem([NOTE._note.header]))
        #     добавить выделение нового элемента в списке

        self.dialog_window.close()
        self.ui.textEdit.clear()
        self.flags_check()

    def delete_note(self):
        global NOTE

        if os.path.exists(f"Notes\\{NOTE}"):
            os.remove(f"Notes\\{NOTE}")
            self.research_notes()
            NOTE = None

            self.flags_check()

    def open_note(self, name):
        global NOTE, STORAGE

        self.saveNote()
        NOTE = STORAGE.get_note(name.text(0))

        self.ui.textEdit.setText(NOTE.read())

        self.flags_check()


if __name__ == "__main__":
    # ==Код не позволяющий включать приложению темную тему==
    sys.argv += ['-platform', 'windows:darkmode=0']
    # =======================================================
    app = QApplication(sys.argv)

    window = NotesApp()
    sys.exit(app.exec())
