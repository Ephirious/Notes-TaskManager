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


def serch_user(Login, Password):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('users.db')
    c = db.cursor()

    c.execute(f"SELECT * FROM users WHERE login={Login}")
    value = c.fetchall()
    close_table(db, c)
    if value != [] and value[0][1] == Password:
        return True
    else:
        return False


def registration(Login, Password):
    # Подключение к базе, создание курсора
    db = sqlite3.connect('user.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE Login={login}")
    value = c.fetchall()
    # если таких значений не найдено value = [], приравнивается к false
    if value:
        # Дописать ссылку на файлик
        c.execute("INSERT INTO users Login={login}, Password={password}, 'hcddhe.txt')")
    else:
        return "Такой пользователь уже есть!"
    close_table(db, c)
    return
