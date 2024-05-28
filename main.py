import os.path
import sys

from PySide6 import QtGui
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QFileDialog, QTreeWidgetItem, QGroupBox, QCheckBox, QTextBrowser, QLabel,
                               QHBoxLayout)

from data_base.data_bd import *
from tasks_and_shared.user_tasks_and_sharred import *
from ui_account_login_window import Ui_LoginWindow
from ui_account_sign_in_window import Ui_SigninWindow
from ui_add_new_task import Ui_AddNewTask
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

        self.open_log_in_window()

        self.ui.btn_storage.clicked.connect(self.new_storage)

        # взаимодействие с кнопками
        self.ui.btn_add_note.clicked.connect(self.open_window_addNote)
        self.ui.btn_add_dir.clicked.connect(self.open_window_addDir)
        self.ui.btn_save.clicked.connect(self.save_note)
        self.ui.btn_delete_note.clicked.connect(self.delete_item)

        # взаимодействие со списком файлов
        self.ui.treeWidget.itemClicked.connect(self.open_item)

        # взаимодействие с ComboBox
        self.ui.fontSizeBox.addItems(str(x) for x in range(6, 52))

        # взаимодействие с textEdit
        self.ui.btn_formatBold.clicked.connect(self.do_bold_text)
        self.ui.btn_formatUnderline.clicked.connect(self.do_underline_text)
        self.ui.btn_formatItalic.clicked.connect(self.do_italic_text)
        self.ui.fontSizeBox.currentIndexChanged.connect(self.change_text_size)
        self.ui.fontComboBox.currentIndexChanged.connect(self.change_font_Text)

        # взаимодействие с Таск-менджером
        self.ui.btn_add_task.clicked.connect(self.open_window_addTask)
        self.ui.btn_delete_task.clicked.connect(self.remove_tasks)

        self.tasks = []
        self.listTasksToRemove = []

        self.userTasks = []
        self.tasksTags = ['Дом', 'Работа', 'Хобби']

        self.ui.comboBoxTags.addItems(self.tasksTags)
        self.ui.btn_filterByTags.clicked.connect(self.filtered_task_by_tags)

        self.flags_check()

    def close_event(self, event):
        global NOTE

        if NOTE:
            self.save_note()

    def flags_check(self):
        global NOTE, STORAGE

        if NOTE is None:
            self.ui.textEdit.setDisabled(True)
            self.ui.btn_delete_note.setText('Удалить папку')
            self.ui.textEdit.setText('-------- Заметка не выбрана или не создана --------')
            self.ui.btn_save.hide()
        else:
            self.ui.textEdit.setDisabled(False)
            self.ui.btn_save.show()
            self.ui.btn_delete_note.setText('Удалить заметку')
            self.ui.btn_delete_note.show()
        self.ui.label_save_or_del.setText('')

        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()

        if current_item and st.check_existance(current_item.text(3), path_tp='dir'):
            # self.ui.btn_delete_note.hide()
            self.ui.btn_delete_note.setText('Удалить папку')
            self.ui.btn_save.hide()

    def open_filemanager(self):

        file_dialog = QFileDialog()
        return file_dialog.getExistingDirectory(self, 'Создайте новую папку для заметок', '')

    def new_storage(self):
        global STORAGE, PATH, NOTE
        file_dialog = QFileDialog()
        PATH = file_dialog.getExistingDirectory(self, 'Создайте новую папку для заметок', '')
        if PATH:
            STORAGE = Storage(PATH)
            STORAGE.load_structure()

            NOTE = None

            self.ui.treeWidget.clear()
            root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', f'{STORAGE.path}'])
            self.upload_tree_widget(STORAGE.storage_entry, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

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

        user_password = get_password(self.login_dialog.lineEdit_name.text())
        password_is_ok = EncRSA.check_pass(self.login_dialog.lineEdit_password.text(), user_password.encode())

        if password_is_ok:
            USER = search_user(self.login_dialog.lineEdit_name.text(), user_password)
            if USER.data:
                PATH = USER.data
            else:
                PATH = self.open_filemanager()
                add_link_to_data(USER.login, PATH)

            # Создание структуры папок и файлов
            STORAGE = Storage(PATH + '/notes')
            STORAGE.load_structure()
            STORAGE.user = USER.login

            root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', STORAGE.path])
            self.upload_tree_widget(STORAGE.storage_entry, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

            self.update_tasks()

            self.show()
            self.ui.label_account.setText(f'Аккаунт: {USER.login}')

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
            USER = registration(login, EncRSA.pass_to_hash(password).decode(), PATH)

            USER_FILES = UserFiles(USER.login, USER.password, 0, PATH, [])
            USER_FILES.generate_dirs()

            STORAGE = Storage(PATH + '/notes')
            STORAGE.load_structure()

            root_item = QTreeWidgetItem([f'{STORAGE.name}', 'DIR', '', STORAGE.path])
            self.upload_tree_widget(STORAGE.storage_entry, root_item)
            self.ui.treeWidget.addTopLevelItem(root_item)

            self.update_tasks()

            self.show()
            self.ui.label_account.setText(f'Аккаунт: {USER.login}')

            self.reg_window.close()
        else:
            self.reg_dialog.label_error.setText('Введеный логин уже занят, пожалуйста'
                                                'введите новый логин')

    # =================================================================================================
    # Функции связанные с заметками и папками
    # =================================================================================================
    @staticmethod
    def upload_tree_widget(directory, parent_item):
        global STORAGE

        if type(directory) is DirEntry and directory.path not in STORAGE.hierarchy.loaded:
            directory = STORAGE.hierarchy.load(directory.path)

        for element in directory.structure:
            if type(element) is DirEntry:
                # Если элемент является каталогом, создаем новый элемент дерева и добавляем его к родительскому элементу
                directory_item = QTreeWidgetItem([element.name, 'DIR', element.createtime, element.path])
                parent_item.addChild(directory_item)
            else:
                # Если элемент является файлом, просто добавляем его к родительскому элементу
                file_item = QTreeWidgetItem([element.name.split('.')[0],
                                             element.name.split('.')[-1].upper(),
                                             str(element.createtime).replace('T', ''),
                                             element.path])
                parent_item.addChild(file_item)

    def save_note(self):
        global NOTE, USER

        if NOTE:
            text = self.ui.textEdit.toHtml()
            NOTE.user = USER.login
            NOTE.write(text)
            NOTE.save()
            self.ui.label_save_or_del.setText('Заметка была успешно сохранена!')

    def open_window_addNote(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.dialog.pushButton.clicked.connect(self.add_note)

    def open_window_addDir(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_WinDirAdd()
        self.dialog.setupUi(self.dialog_window)
        self.dialog_window.show()
        self.dialog.btn_add_dir.clicked.connect(self.add_dir)

    def add_note(self):
        global STORAGE, USER, NOTE
        self.save_note()

        name = self.dialog.lineEdit.text()
        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()
        if current_item:
            if st.check_existance(current_item.text(3), path_tp='dir'):
                path = current_item.text(3)
                storage = current_item
            else:
                path = current_item.parent().text(3)
                storage = current_item.parent()
        else:
            path = PATH
            storage = self.ui.treeWidget.topLevelItem(0)

        NOTE = STORAGE.create_note(path + f'/{name}.json')
        NOTE.change_header(name)
        NOTE._note.user = USER.login

        with open(f'{path}\\{name}' + '.json', 'w'):
            pass
        #     добавить выделение нового элемента в списке

        file_item = QTreeWidgetItem([name,
                                     'JSON',
                                     f'{NOTE._note.createtime}',
                                     path + f'/{name}.json'])
        storage.addChild(file_item)
        self.ui.treeWidget.expandItem(file_item)
        self.ui.treeWidget.setCurrentItem(file_item)


        self.dialog_window.close()
        self.ui.textEdit.clear()

        self.flags_check()

    def add_dir(self):
        name = self.dialog.lineEdit.text()
        st = StorageExplorer()
        current_item = self.ui.treeWidget.currentItem()

        if current_item:
            if st.check_existance(current_item.text(3), path_tp='dir'):
                path = current_item.text(3)
                storage = current_item
            else:
                path = current_item.parent().text(3)
                storage = current_item.parent()
        else:
            path = PATH
            storage = self.ui.treeWidget.topLevelItem(0)

        os.mkdir(path + f'/{name}')
        dir_item = QTreeWidgetItem([name,
                                    'DIR',
                                    str(datetime.datetime.now()),
                                    path + f'/{name}'])
        storage.addChild(dir_item)

        self.dialog_window.close()
        self.ui.textEdit.clear()

        self.flags_check()

    def delete_item(self):
        import shutil

        global NOTE, STORAGE

        st = StorageExplorer()
        if not st.check_existance(self.ui.treeWidget.currentItem().text(3), path_tp='dir'):
            os.remove(f"{NOTE.get_path()}")
            NOTE = None
            self.ui.treeWidget.currentItem().parent().removeChild(self.ui.treeWidget.currentItem())
        else:
            NOTE = None
            try:
                self.ui.treeWidget.currentItem().parent().removeChild(self.ui.treeWidget.currentItem())
            except AttributeError:
                self.ui.label_save_or_del.setText('Невозможно удалить корневую папку')
            else:
                shutil.rmtree(f'{self.ui.treeWidget.currentItem().text(3)}')

        self.flags_check()

    def open_item(self, element):
        global NOTE, STORAGE
        self.save_note()

        st = StorageExplorer()
        path = element.text(3)
        if st.check_existance(path, path_tp='dir') and path not in STORAGE.hierarchy.loaded:
            file_object = DirEntry('', path, [], '')
            self.upload_tree_widget(file_object, element)
            self.ui.treeWidget.addTopLevelItem(element)
            self.ui.treeWidget.expandItem(element)

        elif st.check_existance(path, path_tp='file') and path.split('.')[-1] == 'json':
            file_object = FileEntry('', path, '')
            NOTE = STORAGE.get_note(file_object)
            self.ui.textEdit.setText(NOTE.read())
        self.flags_check()

    # =================================================================================================
    # Функции отвечающие за разметку
    # =================================================================================================
    def change_text_size(self):
        charFormatFontSize = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())
        charFormatNorm = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())

        charFormatFontSize.setFontPointSize(float(self.ui.fontSizeBox.currentText()))
        charFormatNorm.setFontPointSize(float(self.ui.textEdit.currentCharFormat().fontPointSize()))
        if self.ui.textEdit.textCursor().charFormat().fontPointSize() == float(self.ui.fontSizeBox.currentText()):
            self.ui.textEdit.setCurrentCharFormat(charFormatNorm)
        else:
            self.ui.textEdit.setCurrentCharFormat(charFormatFontSize)

    def do_bold_text(self):
        charFormatBold = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())
        charFormatNorm = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())
        charFormatBold.setFontWeight(900)
        charFormatNorm.setFontWeight(400)
        if self.ui.textEdit.textCursor().charFormat().fontWeight() == 400:
            self.ui.textEdit.setCurrentCharFormat(charFormatBold)
        else:
            self.ui.textEdit.setCurrentCharFormat(charFormatNorm)

    def do_underline_text(self):
        charFormatUnderline = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())
        charFormatNorm = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())

        charFormatUnderline.setFontUnderline(True)
        charFormatNorm.setFontUnderline(False)
        if self.ui.textEdit.textCursor().charFormat().fontUnderline():
            self.ui.textEdit.setCurrentCharFormat(charFormatNorm)
        else:
            self.ui.textEdit.setCurrentCharFormat(charFormatUnderline)

    def do_italic_text(self):
        charFormatItalic = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())
        charFormatNorm = QtGui.QTextCharFormat(self.ui.textEdit.currentCharFormat())

        charFormatItalic.setFontItalic(True)
        charFormatNorm.setFontItalic(False)
        if self.ui.textEdit.textCursor().charFormat().fontItalic():
            self.ui.textEdit.setCurrentCharFormat(charFormatNorm)
        else:
            self.ui.textEdit.setCurrentCharFormat(charFormatItalic)

    def change_font_Text(self):
        if self.ui.textEdit.currentCharFormat().fontUnderline():
            self.ui.textEdit.setCurrentFont(QFont(self.ui.fontComboBox.currentText(),
                                                  self.ui.textEdit.currentCharFormat().fontPointSize(),
                                                  self.ui.textEdit.currentCharFormat().fontWeight(),
                                                  self.ui.textEdit.currentCharFormat().fontItalic()))

            self.ui.textEdit.setFontUnderline(True)
        else:
            self.ui.textEdit.setCurrentFont(QFont(self.ui.fontComboBox.currentText(),
                                                  self.ui.textEdit.currentCharFormat().fontPointSize(),
                                                  self.ui.textEdit.currentCharFormat().fontWeight(),
                                                  self.ui.textEdit.currentCharFormat().fontItalic()))

    # =================================================================================================
    # Функции отвечающие за Таск-менджер
    # =================================================================================================

    def open_window_addTask(self):
        self.dialog_window = QDialog()
        self.dialog = Ui_AddNewTask()
        self.dialog.setupUi(self.dialog_window)

        self.dialog.dateTimeEdit_start.setDateTime(datetime.datetime.now())
        self.dialog.dateTimeEdit_end.setDateTime(datetime.datetime.now())

        self.dialog.comboBoxTags.addItems(self.tasksTags)

        self.dialog_window.show()
        self.dialog.pushButton.clicked.connect(self.add_task)

    def create_new_task(self, task_data, time_days, filename, flag=False, ):
        groupBoxTask = QGroupBox()
        groupBoxTask.setMaximumSize(999999, 100)
        boxTaskLayout = QHBoxLayout()

        checkBox = QCheckBox()
        checkBox.stateChanged.connect(self.add_task_to_remove)
        boxTaskLayout.addWidget(checkBox)

        textBrowser = QTextBrowser()
        textBrowser.setText(task_data)
        textBrowser.setMaximumSize(999999, 90)
        boxTaskLayout.addWidget(textBrowser)

        label = QLabel()
        label.setText(time_days)
        label.setMinimumSize(150, 50)
        label.setMaximumSize(150, 50)

        if flag:
            label.setStyleSheet("QLabel { color: red; }")
        boxTaskLayout.addWidget(label)

        groupBoxTask.setLayout(boxTaskLayout)

        checkBox.setProperty('task_id', self.ui.verticalLayout_4.count())
        checkBox.setProperty('filename', filename)
        # Добавляем задание в компоновку
        self.ui.verticalLayout_4.addWidget(groupBoxTask)
        return groupBoxTask

    def add_task(self):
        global USER
        data = self.dialog.lineEdit_task.text()
        time_date_start = datetime.datetime.strptime(self.dialog.dateTimeEdit_start.text(), '%d.%m.%Y %H:%M')
        time_date_end = datetime.datetime.strptime(self.dialog.dateTimeEdit_end.text(), '%d.%m.%Y %H:%M')

        if not self.dialog.lineEdit_category.text():
            task_tag = self.dialog.comboBoxTags.currentText()
            self.ui.comboBoxTags.setCurrentIndex(self.tasksTags.index(self.dialog.comboBoxTags.currentText()))
        else:
            task_tag = self.dialog.lineEdit_category.text()
            self.tasksTags.append(task_tag)
            self.ui.comboBoxTags.clear()
            self.ui.comboBoxTags.addItems(self.tasksTags)
            self.ui.comboBoxTags.setCurrentIndex(self.tasksTags.index(task_tag))

        # Сохранение таски в виде файла
        USER_FILES = UserFiles(USER.login, USER.password, 0, PATH, [])

        filename = str(uuid4())
        newFileTask = Note(PATH + '/tasks/' + filename + '.json')
        new_header = json.dumps(
            {"st_time": time_date_start.isoformat(), "end_time": time_date_end.isoformat(), "tags": []})
        newFileTask.header = new_header
        newFileTask.protect(USER.password)
        task = Task(newFileTask, USER.password)
        task.write(data)
        task.include_tag(task_tag)

        tags = USER_FILES.get_tasks()
        if task_tag not in tags and \
                task_tag not in ['Дом', 'Работа', 'Хобби']:
            tags.append(task_tag)
            USER_FILES.save_tags(tags)

        task.save(USER.password)

        self.filtered_task_by_tags()

        mounth_start, day_start = time_date_start.strftime('%B %d').split()
        mounth_end, day_end = time_date_end.strftime('%B %d').split()

        flag_time_is_up = False
        if time_date_end <= datetime.datetime.now():
            flag_time_is_up = True

        time = f"{' '.join((mounth_start[:3], day_start))} - {' '.join((mounth_end[:3], day_end))}"

        self.tasks.append([task_tag,
                           self.create_new_task(data, time, filename, flag_time_is_up),
                           [data, time, filename, flag_time_is_up, ]])
        self.dialog_window.close()

    def add_task_to_remove(self, state):
        checkbox = self.sender()
        task_id = checkbox.property('task_id')
        filename = checkbox.property('filename')

        task_tag, task_widget, _, = self.tasks[task_id]
        if state == 2:
            self.listTasksToRemove.append([task_id, task_widget, filename])
        elif state == 0:
            self.listTasksToRemove.remove([task_id, task_widget, filename])

    def remove_tasks(self):
        if self.listTasksToRemove != [] and self.ui.verticalLayout_4:
            for task_id, task_widget, filename in self.listTasksToRemove:
                child = self.ui.verticalLayout_4.takeAt(task_id)
                if child.widget():
                    child.widget().deleteLater()
                self.tasks.pop(task_id)
                os.remove(PATH + '/tasks/' + filename + '.json')

            self.listTasksToRemove.clear()

    def filtered_task_by_tags(self):
        # Удаляем все виджеты из компоновки
        while self.ui.verticalLayout_4.count():
            child = self.ui.verticalLayout_4.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Получаем текущий выбранный тег
        current_tag = self.ui.comboBoxTags.currentText()

        # Добавляем виджеты, соответствующие текущему тегу
        for task_tag, task_widget, components in self.tasks.copy():
            if task_tag == current_tag:
                self.ui.verticalLayout_4.addWidget(
                    self.create_new_task(components[0], components[1], components[2], components[3]))

        # Обновляем компоновку
        self.ui.verticalLayout_4.update()

    def update_tasks(self):
        self.tasks.clear()

        USER_FILES = UserFiles(USER.login, USER.password, 0, PATH, [])
        tasks = USER_FILES.get_tasks()

        self.tasksTags = ['Дом', 'Работа', 'Хобби'] + USER_FILES.get_tags()
        self.ui.comboBoxTags.clear()
        self.ui.comboBoxTags.addItems(self.tasksTags)

        for i in tasks:
            data = i.read()
            time_date_start = i.start_time
            time_date_end = i.end_time
            task_tag = list(i.tags)[0]

            mounth_start, day_start = time_date_start.strftime('%B %d').split()
            mounth_end, day_end = time_date_end.strftime('%B %d').split()

            time = f"{' '.join((mounth_start[:3], day_start))} - {' '.join((mounth_end[:3], day_end))}"

            flag_F = False
            if time_date_end <= datetime.datetime.now():
                flag_F = True

            self.tasks.append([task_tag,
                               self.create_new_task(data, time, flag_F),
                               [data, time, flag_F]])

        self.filtered_task_by_tags()


if __name__ == "__main__":
    # ==Код не позволяющий включать приложению темную тему==
    sys.argv += ['-platform', 'windows:darkmode=0']
    # =======================================================
    app = QApplication(sys.argv)

    window = NotesApp()
    sys.exit(app.exec())
