import sqlite3


def close_table(db, c):
    db.commit()
    c.close()
    db.close()


class User:
    def __init__(self, login, password, data):
        self.login = login
        self.password = password
        self.data = data


#def add_link_to_note(login, path):
   # db = sqlite3.connect('data_base/user.db')
   #  c = db.cursor()

    # c.execute("INSERT INTO links  (login, path) VALUES (?, ?)",
    #           (login, path))


# def list_of_users_links(login):
#     db = sqlite3.connect('data_base/user.db')
#     c = db.cursor()

    # c.execute("SELECT path FROM  links  WHERE login=?", (login,))
    # list_of_links = c.fetchall()
    # return list_of_links


# def delete_link_to_data(path):
#     db = sqlite3.connect('data_base/user.db')
#     c = db.cursor()

    # c.execute("DELETE FROM links WHERE path=?", (path,))



def search_user(login, password):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute(f"SELECT * FROM users WHERE login={login}")
    value = c.fetchall()
    close_table(db, c)
    if value and (value[0][0] == login and value[0][1] == password):
        return User(*value[0])
    else:
        return False


def loginDuplicateChecker(login):
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE login=?", (login,))
    value = c.fetchall()
    if value:
        close_table(db, c)
        return True
    else:
        close_table(db, c)
        return False


def add_link_to_data(login, data):
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute("UPDATE users  SET link_to_data=? WHERE login=?",
              (data, login,))
    close_table(db, c)


def registration(login, password, data=None):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE login=?", (login,))
    value = c.fetchall()
    # если таких значений не найдено value = [], приравнивается к false
    c.execute("INSERT INTO users  (login, password, link_to_data) VALUES (?, ?, ?)",
              (login, password, data,))
    close_table(db, c)
    return User(login, password, data)

def add_task_to_bd(id, task_name, time_start, time_stop, teg):
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()
    c.execute("INSERT INTO tasks  (id, task_name, time_start, time_stop, teg) VALUES (?, ?, ?, ?, ?)",
              (id, task_name, time_start, time_stop, teg))
    close_table(db, c)


def delete_task_bd(task_id):
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    close_table(db, c)


db = sqlite3.connect('user.db')
# Создание крусора
c = db.cursor()
# закомитить таблицу чтобы при каждом запуске она еще раз не крафтилась
#link_to_data -- ссылка на заметку
c.execute("""CREATE TABLE IF NOT EXISTS users (
   login text,
   password text,
   link_to_data text, 
   key text
 )""")

db = sqlite3.connect('user.db')
# Создание крусора
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
   id integer,
   task_name text,
   time_start text,
   time_stop text,
   teg text
 )""")
close_table(db, c)

#Таблица для хранения данных о заметке
#db = sqlite3.connect('user.db')
# Создание крусора
#c = db.cursor()
# закомитить таблицу чтобы при каждом запуске она еще раз не крафтилась

#c.execute("""CREATE TABLE notes (
#   user_name text,
#   artical text,
#   text_artical text,
#   last_save text
# )""")
#db.commit()
#db.close()
