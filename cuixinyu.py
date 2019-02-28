import sqlite3

def UserData():
    conn = sqlite3.connect('gameformat.db')

    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS GAME
           (ID INT PRIMARY KEY     NOT NULL,
           SCORE          INT,
           WINCOUNT       INT,
           LOSECOUNT      INT);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def addRecord(id, score, wincount, losecount):
    #if want to add something, just put (id, score, wincount, losecount)
    conn = sqlite3.connect('gameformat.db')
    c = conn.cursor()
    print("Opened database successfully")

    c.execute('INSERT INTO GAME VALUES(?, ?, ?, ?)',(id, score, wincount, losecount))
    conn.commit()
    print("Records created successfully")
    conn.close()

def delete(id):
    conn = sqlite3.connect('gameformat.db')
    c = conn.cursor()
    print("Opened database successfully")
    c.execute('DELETE FROM GAME WHERE id=?',(id,))
    conn.commit()
    print("Records deleted successfully")
    conn.close()

def searchData(id=''):
    conn = sqlite3.connect('gameformat.db')
    c = conn.cursor()
    c.execute('SELECT * FROM GAME WHERE id= ?', (id,))
    row = c.fetchall()
    print(row)
    conn.close()

def dataUpdate(id, score='', wincount='', losecount=''):
    conn = sqlite3.connect('gameformat.db')
    c = conn.cursor()
    c.execute('UPDATE GAME SET score=?,wincount=?, losecount=? WHERE id=?',\
              (score, wincount, losecount, id))
    conn.commit()
    print("Records updated successfully")
    conn.close()

def view():
    conn = sqlite3.connect('gameformat.db')
    c = conn.cursor()
    print("Opened database successfully")

    cursor = c.execute("SELECT id, score, wincount, losecount from GAME")
    for row in cursor:
        print("ID = ", row[0])
        print("Score = ", row[1])
        print("Win_Count = ", row[2])
        print("Lose_Count = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()



UserData()
dataUpdate(1234)
view()