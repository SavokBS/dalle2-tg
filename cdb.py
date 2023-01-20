import sqlite3
import json
import traceback

class CDB():
    def __init__(self):
        self.conn = sqlite3.connect("cdb.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (ID int, name text, Data json)""")
        except sqlite3.OperationalError:
            pass
        except Exception as e:
            print(traceback.format_exc())

    def new(self, data):
        try:
            self.cursor.execute("INSERT INTO main (ID, name, Data) VALUES (?,?,?)", (data["ID"], data["name"], json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())
    def load(self, id):
        try:
            self.cursor.execute("SELECT * FROM main WHERE ID=?", (id,))
            return json.loads(self.cursor.fetchall()[0][2])
        except Exception as e:
            pass
    def loadall(self):
        try:
            a = []
            self.cursor.execute("SELECT * FROM main")
            a = self.cursor.fetchall()
           # for db in this:
                #data = json.loads(db[2])
                #append(data)
            
            return a
        except Exception as e:
            print(traceback.format_exc())

    def loadsort(self):
        try:
            a = []
            self.cursor.execute("SELECT * FROM main ORDER BY money DESC")
            this = self.cursor.fetchall()
            for db in this:
                data = json.loads(db[2])
                a.append(data)
            
            return a
        except Exception as e:
            print(traceback.format_exc())

    def update(self, id, data):
        try:
            self.cursor.execute(f"UPDATE main SET Data=? WHERE ID=?", (json.dumps(data, ensure_ascii=0), id))
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())
    def delete(self, id):
        try:
            self.cursor.execute(f"DELETE FROM main WHERE ID={id}")
            self.conn.commit()
        except:
            	pass
            	
            