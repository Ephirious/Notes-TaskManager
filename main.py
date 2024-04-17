import os.path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from ui_account_login_window import Ui_LoginWindow
from ui_dialogwindow_note import Ui_Dialog
from ui_main_window_notes import Ui_MainWindow


class NotesApp(QMainWindow):
    def __init__(self):
        global NAME_NOTE
        super(NotesApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.open_accountWindow()

        NAME_NOTE = None
        DirectoryPath = None

        # взаимодействие с кнопками
        self.ui.btn_add_note.clicked.connect(self.open_window_addNote)
        self.ui.btn_save.clicked.connect(self.saveNote)
        self.ui.btn_delete_note.clicked.connect(self.delete_note)
        # взаимодействие с списком файлов
        self.ui.listWidget.itemClicked.connect(self.open_note)
        # взаимодействие с textEdit

        # заполнение listWidget
        self.research_notes()

        self.flags_check()

    def flags_check(self):
        global NAME_NOTE

        if NAME_NOTE is None:
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

    def open_accountWindow(self):
        self.account_window = QDialog()
        self.account_dialog = Ui_LoginWindow()
        self.account_dialog.setupUi(self.account_window)

        self.account_window.show()
        self.account_dialog.btn_login.clicked.connect(self.login_in_account)

    def login_in_account(self):
        name = '123'
        password = name[::-1]
        if self.account_dialog.lineEdit_name.text() == name and \
                self.account_dialog.lineEdit_password.text() == password:
            self.show()
            self.account_window.close()
        else:
            self.account_dialog.label_error.setText('Вы кто такие!? Я вас не звал!\n'
                                                    'Проверьте верность введеного логина или пароля. ')

    def research_notes(self):
        if self.ui.listWidget.count():
            self.ui.listWidget.clear()

        name_storage = "Notes"
        if os.path.exists(name_storage):
            self.ui.listWidget.addItem(f"===={name_storage}====")
            for file_name in os.listdir(name_storage):
                self.ui.listWidget.addItem(file_name)

    def saveNote(self):
        global NAME_NOTE

        if NAME_NOTE:
            text = self.ui.textEdit.toPlainText()
            with open(f'Notes\\{NAME_NOTE}', 'w') as file:
                file.write(text)
                file.close()
                self.ui.label_save_or_del.setText("Заметка была успешно сохранена!")

    def addNote(self):
        global NAME_NOTE
        self.saveNote()

        NAME_NOTE = self.dialog.lineEdit.text() + '.txt'

        if len(NAME_NOTE) > 15:
            name_n = NAME_NOTE[:10] + '...'
            self.ui.listWidget.addItem(name_n)
        elif len(NAME_NOTE) == 0:
            pass
        else:
            self.ui.listWidget.addItem(NAME_NOTE)
        #     добавить выделение нового элемента в списке

        if not os.path.exists(f"Notes\\{NAME_NOTE}"):
            with open(f"Notes\\{NAME_NOTE}", 'w'):
                pass

        self.dialog_window.close()
        self.ui.textEdit.clear()

        self.flags_check()

    def delete_note(self):
        global NAME_NOTE

        if os.path.exists(f"Notes\\{NAME_NOTE}"):
            os.remove(f"Notes\\{NAME_NOTE}")
            self.research_notes()
            NAME_NOTE = None

            self.flags_check()

    def open_note(self, name):
        global NAME_NOTE

        self.saveNote()
        if os.path.exists(f"Notes\\{name.text()}"):
            NAME_NOTE = name.text()
            with open(f"Notes\\{NAME_NOTE}", 'r') as file:
                self.ui.textEdit.setText(file.read())

        self.flags_check()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    sys.exit(app.exec())
