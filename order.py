import sqlite3




class Order:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def save_to_database(self):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)", (self.user_id, self.product_id, self.quantity))
        conn.commit()

    @staticmethod
    def list_all_orders():
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("SELECT * FROM orders")
        rows = c.fetchall()
        for row in rows:
            print(row)

    def update_order(self, id):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("UPDATE orders SET user_id=?, product_id=?, quantity=? WHERE id=?", (self.user_id, self.product_id, self.quantity, id))
        conn.commit()

    @staticmethod
    def delete_order(id):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("DELETE FROM orders WHERE id=?", (id,))
        conn.commit()
