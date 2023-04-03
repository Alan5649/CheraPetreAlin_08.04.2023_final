import sqlite3




class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def save_to_database(self):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", (self.name, self.description, self.price))
        conn.commit()

    @staticmethod
    def list_all_products():
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        rows = c.fetchall()
        for row in rows:
            print(row)

    @staticmethod
    def delete_product(id):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE id=?", (id,))
        conn.commit()


