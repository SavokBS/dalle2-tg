import sqlite3
import json
import traceback

class DB():
    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (id int, data json)""")
        except sqlite3.OperationalError:
            pass
        except Exception as e:
            print(traceback.format_exc())

    def new(self, id, data):
        try:
            self.cursor.execute("INSERT INTO main (id, data) VALUES (?,?)", (id, json.dumps(data, ensure_ascii=False)))
            self.conn.commit()
            print('Commited new group!')
        except Exception as e:
            print(traceback.format_exc())
    def load(self, id):
        try:
            self.cursor.execute("SELECT * FROM main WHERE id=?", (id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(traceback.format_exc())
    def loadall(self):
        try:
            a = []
            self.cursor.execute("SELECT * FROM main")
            return self.cursor.fetchall()
        except Exception as e:
            print(traceback.format_exc())
    
    def loadSort(self, value):
        self.cursor.execute(f"SELECT * FROM main ORDER BY {value} DESC")
        return self.cursor.fetchall()

    def update(self, id, value, new_value):
        try:
            self.cursor.execute(f"UPDATE main SET {value}=? WHERE id=?", (new_value, id))
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())
    def custom(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())
            
            

          

            