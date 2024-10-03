from models.__init__ import CURSOR, CONN

class Product:
    
    all = {}

    def __init__(self, model:str, price:float, description: str, id:int = None):
        self.id = id
        self.model = model
        self.price = price
        self.description = description
        
    def __repr__(self):
        return f"<Product {self.id}: {self.model}, price:${self.price} description: {self.description}>"
    
    @classmethod
    def instance_from_db(cls, row):
        product = cls.all.get(row[0])
        if product:
            product.model = row[1]
            product.price = row[2]
            product.description = row[3]
        else:
            product = cls(row[1], row[2], row[3])
            product.id = row[0]
            cls.all[product.id] = product
        return product
    @classmethod
    def find_by_id(cls,id):
        sql = """SELECT * FROM products WHERE id = ?"""
        rows = CURSOR.execute(sql, (id,)).fetchall()
        return[cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_model(cls, model):
        sql = """SELECT * FROM products WHERE model = ?"""
        row = CURSOR.execute(sql, (model,)).fetchall()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        sql= """SELECT * FROM products"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def create(cls, model:str, price: float, description: str):
        sql= """ INSERT INTO products (model, price, description) VALUES ( ? , ? , ? )"""
        CURSOR.execute(sql, (model, price, description))
        CONN.commit()

    @classmethod
    def update(cls, id:int, model: str, price:float, description: str):
        sql= """ UPDATE products SET model = ?, price = ?, description = ? WHERE id = ?"""
        CURSOR.execute(sql, (model, price, description, id))
        CONN.commit()

    @classmethod
    def delete(cls, id:int):
        sql= """DELETE FROM products WHERE id = ? """
        CURSOR.execute(sql, (id,))
        CONN.commit()

    

