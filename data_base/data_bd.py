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


def search_user(login, password):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE login=?", (login,))
    value = c.fetchall()
    close_table(db, c)
    if value and (value[0][0] == login and value[0][1] == password):
        return True
    else:
        return False


def registration(login, password):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('data_base/user.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE login=?", (login,))
    value = c.fetchall()
    # если таких значений не найдено value = [], приравнивается к false
    if not value:
        c.execute("INSERT INTO users  (login, password) VALUES (?, ?)", (login, password))
        close_table(db, c)
        return True
    else:
        close_table(db, c)
        return False
