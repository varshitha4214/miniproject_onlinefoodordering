import sqlite3

def connect():
    conn=sqlite3.connect("fooddata.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS food1(itemid INTEGER PRIMARY KEY,itemname text,hotelname text,price integer,quantity integer,phoneno integer,address text)")
    conn.commit()
    conn.close()

def insert(itemid, itemname, hotelname, price, quantity, phoneno, address):
    conn = sqlite3.connect("fooddata.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO food1 VALUES(?,?,?,?,?,?,?)",(itemid, itemname, hotelname, price, quantity, phoneno, address))
    conn.commit()
    conn.close()

def update(itemid, itemname, hotelname, price, quantity,phoneno,address):
    conn = sqlite3.connect("fooddata.db")
    cur = conn.cursor()
    cur.execute("UPDATE food1 SET itemname=?,hotelname=?,price=?,quantity=?,phoneno=?,address=? WHERE itemid=?",(itemname, hotelname, price, quantity,phoneno,address,itemid))
    conn.commit()
    conn.close()

def delete(itemid):
    conn = sqlite3.connect("fooddata.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM food1 WHERE itemid=?", (itemid,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("fooddata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM food1")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(itemid="", price=""):
    conn = sqlite3.connect("fooddata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM food1 WHERE itemid=? OR price=?", (itemid, price))
    rows = cur.fetchall()
    conn.close()
    return rows
connect()

