#Создание соединения
import sqlite3
from sqlite3 import Error
import datetime

con = sqlite3.connect('mydatabase.db')

#Создание базы данных
def sql_connection():
    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

#Создание таблицы
def sql_table(con):
    #курсор SQLit3
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()


con = sql_connection()
sql_table(con)

#Вставка данных в таблицу
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)',
                  entities)
    con.commit()

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

sql_insert(con, entities)



#Обновление таблицы
def sql_update(con):
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    con.commit()


sql_update(con)

#Оператор SELECCT
#Выборка всех данных
#Счетчик
def sql_fetch(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()
    #Выводит кол-во строк
    print(len(rows))

    for row in rows:
        #Выводит все строки из таблицы
      print(row)
    #Выводит -1
    print(cursorObj.execute('SELECT * FROM employees').rowcount)
    #Выводит кол-во удаленных строк
    print(cursorObj.execute('DELETE FROM employees').rowcount)

sql_fetch(con)

#Выборка с условием
def sql_fetch1(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()


    for row in rows:
        print(row)

sql_fetch1(con)

#Список таблиц
def sql_fetch2(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())


sql_fetch2(con)

#Проверка существования таблицы
def sql_fetch3(con):
    cursorObj = con.cursor()

    #Создание табдицы, если существует
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    #Удаление таблицы, если сущетствует
    cursorObj.execute('drop table if exists projects')
    #проверим, существует ли таблица, к которой нужно получить доступ, выполнив следующий запрос
    #Возвращает пустой массив, так как таблицы не существует
    cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "projects"')

    print(cursorObj.fetchall())

    con.commit()

sql_fetch3(con)

#Удаление таблицы
def sql_fetch4(con):
    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()


sql_fetch4(con)

#Массовая вставка строк
cursorObj = con.cursor()

cursorObj.execute('create table if not exists projects(id integer, name text)')

data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]

cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)


#SQLite3 datetime
cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()

#Закрытие соединения
con.close()

