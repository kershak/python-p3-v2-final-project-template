from models.__init__ import CURSOR, CONN
class Rma:

    all = {}

    def __init__(self, rma_number, received_on, id= None):
        self.id = id
        self.rma_number = rma_number
        self.received_on = received_on
        #self.products = products

    def __repr__(self):
        return f"<RMA {self.id}: {self.rma_number}, recevied_on: {self.received_on}>"
    
    
    @classmethod
    def instance_from_db(cls, row):
        rma = cls.all.get(row[0])
        if rma:
            rma.rma_number = row[1]
            rma.received_on = row[2]
            #rma.products = row[3]
        else:
            rma = cls(row[1], row[2])
            rma.id = row[0]
            cls.all[rma.id] = rma
        return rma

    @classmethod
    def find_by_id(cls,id):
        sql= """SELECT * FROM rmas WHERE id = ? """
        rows = CURSOR.execute(sql,(id,)).fetchall()
        return[cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_number(cls, rma_number):
        sql = """ SELECT * FROM rmas WHERE rma = ? """
        rows = CURSOR.execute(sql,(rma_number,)).fetchall()
        return[cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_all(cls):
        sql = """ SELECT * FROM rmas"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def create(cls, rma_number: str, received_on:str):
        sql= """ INSERT INTO rmas (rma, date_received) VALUES ( ? , ? )"""
        CURSOR.execute(sql, (rma_number, received_on))
        CONN.commit()

    @classmethod
    def update(self, id:int,rma: str, received_on:str):
        sql= """ UPDATE rmas SET rma = ?, date_received = ? WHERE id = ?"""
        CURSOR.execute(sql, (rma, received_on, id))
        CONN.commit()

    @classmethod
    def delete(cls, id:int):
        sql= """DELETE FROM rmas WHERE id = ? """
        CURSOR.execute(sql, (id,))
        CONN.commit()