import sqlite3




class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_to_database(self):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (self.name, self.email, self.password))
        conn.commit()

    @staticmethod
    def list_all_users():
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        for row in rows:
            print(row)

    @staticmethod
    def delete_user(id):
        conn = sqlite3.connect('marketplace.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id=?", (id,))
        conn.commit()
