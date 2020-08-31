import sqlite3

class Toukou:
    def __init__(self,tid,name,body,hi) -> None:
        self.tid = tid
        self.name = name
        self.body = body
        self.hi = hi

class ToukouDB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('bbs.db')
        self.cur = self.con.cursor()
    
    def close(self):
        self.con.close()

    def get_all(self) -> list:
        self.cur.execute('SELECT * FROM toukou ORDER BY hi DESC')
        rows = self.cur.fetchall()

        ret = []
        for row in rows:
            tid,name,body,hi = row
            toukou = Toukou(tid,name,body,hi)
            ret.append(toukou)
        
        return ret

    def insert(self,toukou):
        self.cur.execute('INSERT INTO toukou (name,body,hi) VALUES(?,?,datetime("NOW"))',[toukou.name,toukou.body])
        self.con.commit()

