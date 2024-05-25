import os.path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTreeWidgetItem

from data_base.data_bd import *
from ui_account_login_window import Ui_LoginWindow
from ui_account_sign_in_window import Ui_SigninWindow
from ui_dialog_dir_add import Ui_WinDirAdd
from ui_dialogwindow_note import Ui_Dialog
from ui_main_window_notes import Ui_MainWindow
from vault_module.vlt_mod import *

STORAGE = None
NOTE = None
PATH = None
USER = None


class NotesApp(QMainWindow):
    def __init__(self):

        super(NotesApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.myclose = False

        self.open_log_in_window()

        self.ui.btn_storage.clicked.connect(self.new_storage)

        # взаимодействие с кнопками
        self.ui.btn_add_note.clicked.connect(self.open_window_addNote)
        self.ui.btn_add_dir.clicked.connect(self.open_window_addDir)
        self.ui.btn_save.clicked.connect(self.saveNote)
        self.ui.btn_delete_note.clicked.connect(self.deleteItem)

        # взаимодействие со списком файлов
        self.ui.treeWidget.itemClicked.connect(self.openItem)

        # взаимодействие с textEdit

        self.flags_check()

    def closeEvent(self, event):
        global NOTE

        if NOTE:
            self.saveNote()

    def open_filemanager(self):

        file_dialog = QFileDialog()
        return file_dialog.getExistingDirectory(self, 'Создайте новую папку для заметок', 'Notes')

    def new_storage(self):
        global STORAGE, PATH, NOTE

        self.ui.treeWidget.clear()

        file_dialog = QFileDialog()
        PATH = file_dialog.getExistingDirectory(self, 'Создайте новую папку для заметок', 'Notes')

        STORAGE = Storage(PATH)
        STORAGE.load_structure()

        NOTE = None

        root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', f'{STORAGE.path}'])
        self.uploadTreeWidget(STORAGE.storage_entry, root_item)
        self.ui.treeWidget.addTopLevelItem(root_item)

    def flags_check(self):
        global NOTE, STORAGE

        if NOTE is None:
            self.ui.textEdit.setDisabled(True)
            self.ui.btn_delete_note.setText("Удалить папку")
            self.ui.textEdit.setText('-------- Заметка не выбрана или не создана --------')
            self.ui.btn_save.hide()
        else:
            self.ui.textEdit.setDisabled(False)
            self.ui.btn_save.show()
            self.ui.btn_delete_note.setText("Удалить заметку")
            self.ui.btn_delete_note.show()
        self.ui.label_save_or_del.setText("")

        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()

        if current_item and st.check_existance(current_item.text(3), path_tp='dir'):
            # self.ui.btn_delete_note.hide()
            self.ui.btn_delete_note.setText("Удалить папку")
            self.ui.btn_save.hide()

    # =================================================================================================
    # Функции отвечающие за логин и регистрацию пользователя
    # =================================================================================================
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

            # Создание структуры папок и файлов
            STORAGE = Storage(PATH)
            STORAGE.load_structure()
            STORAGE.user = USER.login

            root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', STORAGE.path])
            self.uploadTreeWidget(STORAGE.storage_entry, root_item)
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

        if not USER and not loginDuplicateChecker(login):

            PATH = self.open_filemanager()
            USER = registration(login, password, PATH)

            STORAGE = Storage(PATH)
            STORAGE.load_structure()

            root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', STORAGE.path])
            self.uploadTreeWidget(STORAGE.storage_entry, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

            self.show()
            self.reg_window.close()
        else:
            self.reg_dialog.label_error.setText('Введеный логин уже занят, пожалуйста'
                                                'введите новый логин')

    # =================================================================================================
    # Функции связанные с заметками и папками
    # =================================================================================================
    @staticmethod
    def uploadTreeWidget(directory, parent_item):
        global STORAGE

        if type(directory) is DirEntry and directory.path not in STORAGE.hierarchy.loaded:
            directory = STORAGE.hierarchy.load(directory.path)

        for element in directory.structure:
            if type(element) is DirEntry:
                # Если элемент является каталогом, создаем новый элемент дерева и добавляем его к родительскому элементу
                directory_item = QTreeWidgetItem([element.name, "DIR", '', element.path])
                parent_item.addChild(directory_item)
            else:
                # Если элемент является файлом, просто добавляем его к родительскому элементу
                file_item = QTreeWidgetItem([element.name.split('.')[0],
                                             element.name.split('.')[-1].upper(),
                                             '',
                                             element.path])
                parent_item.addChild(file_item)

    def saveNote(self):
        global NOTE, USER

        if NOTE:
            text = self.ui.textEdit.toPlainText()
            NOTE.user = USER.login
            NOTE.write(text)
            NOTE.save()
            self.ui.label_save_or_del.setText("Заметка была успешно сохранена!")

    def open_window_addNote(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.dialog.pushButton.clicked.connect(self.addNote)

    def open_window_addDir(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_WinDirAdd()
        self.dialog.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.dialog.btn_add_dir.clicked.connect(self.addDir)

    def addNote(self):
        global STORAGE, USER, NOTE
        self.saveNote()

        name = self.dialog.lineEdit.text()
        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()

        if st.check_existance(current_item.text(3), path_tp='dir'):
            path = current_item.text(3)
            storage = current_item
        else:
            path = current_item.parent().text(3)
            storage = current_item.parent()

        NOTE = STORAGE.create_note(path + f"/{name}.json")
        NOTE.change_header(name)
        NOTE._note.user = USER.login

        with open(f"{path}\\{name}" + ".json", 'w'):
            pass
        #     добавить выделение нового элемента в списке

        file_item = QTreeWidgetItem([name,
                                     "JSON",
                                     f"{NOTE._note.createtime}",
                                     path + f"/{name}.json"])
        storage.addChild(file_item)

        self.dialog_window.close()
        self.ui.textEdit.clear()

        self.flags_check()

    def addDir(self):
        name = self.dialog.lineEdit.text()
        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()

        if st.check_existance(current_item.text(3), path_tp='dir'):
            path = current_item.text(3)
            storage = current_item
        else:
            path = current_item.parent().text(3)
            storage = current_item.parent()

        os.mkdir(path + f"/{name}")
        dir_item = QTreeWidgetItem([name,
                                    "DIR",
                                    path + f"/{name}"])
        storage.addChild(dir_item)

        self.dialog_window.close()
        self.ui.textEdit.clear()

        self.flags_check()

    def deleteItem(self):
        import shutil

        global NOTE, STORAGE

        st = StorageExplorer()
        if not st.check_existance(self.ui.treeWidget.currentItem().text(3), path_tp='dir'):
            os.remove(f"{NOTE._note.path}")
            NOTE = None
            self.ui.treeWidget.currentItem().parent().removeChild(self.ui.treeWidget.currentItem())
        else:
            NOTE = None
            try:
                self.ui.treeWidget.currentItem().parent().removeChild(self.ui.treeWidget.currentItem())
            except AttributeError:
                self.ui.label_save_or_del.setText("Невозможно удалить корневую папку")
            else:
                shutil.rmtree(f"{self.ui.treeWidget.currentItem().text(3)}")

        self.flags_check()

    def openItem(self, element):
        global NOTE, STORAGE
        self.saveNote()

        st = StorageExplorer()
        path = element.text(3)
        if st.check_existance(path, path_tp='dir') and path not in STORAGE.hierarchy.loaded:
            file_object = DirEntry("", path, [])
            self.uploadTreeWidget(file_object, element)
            self.ui.treeWidget.addTopLevelItem(element)
            self.ui.treeWidget.expandItem(element)

        elif not st.check_existance(path, path_tp='dir'):
            file_object = FileEntry("", path)
            NOTE = STORAGE.get_note(file_object)
            self.ui.textEdit.setText(NOTE.read())
        else:
            pass
        self.flags_check()


if __name__ == "__main__":
    # ==Код не позволяющий включать приложению темную тему==
    sys.argv += ['-platform', 'windows:darkmode=0']
    # =======================================================
    app = QApplication(sys.argv)

    window = NotesApp()
    sys.exit(app.exec())
