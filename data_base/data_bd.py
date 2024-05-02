import sqlite3


# db = sqlite3.connect('user.db')
# Создание крусора
# c = db.cursor()
# закомитить таблицу чтобы при каждом запуске она еще раз не крафтилась
# link_to_data -- ссылка на заметку
# c.execute("""CREATE TABLE users (
#   login text,
#   password text,
#  link_to_data text
# )""")
# db.commit()
# db.close()

def close_table(db, c):
    db.commit()
    c.close()
    db.close()


class User:
    def __init__(self, login, password, data):
        self.login = login
        self.password = password
        self.data = data


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
