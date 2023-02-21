import sqlite3

# Conectarea la baza de date
conn = sqlite3.connect('marketplace.db')
c = conn.cursor()

# Crearea tabelelor
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT)''')


c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS orders
             (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, quantity INTEGER)''')

# Functii pentru a adauga, lista si sterge utilizatori
def adauga_utilizator(name, email, password):
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()

def lista_utilizatori():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)

def sterge_utilizator(id):
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()

# Functii pentru a adauga, lista si sterge un produs
def adauga_produs(name, description, price):
    c.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", (name, description, price))
    conn.commit()

def lista_produse():
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    for row in rows:
        print(row)

def sterge_produs(id):
    c.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()

# Functii pentru a adauga, lista, modifica si sterge o comanda
def adauga_comanda(user_id, product_id, quantity):
    c.execute("INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
    conn.commit()

def lista_comenzi():
    c.execute("SELECT * FROM orders")
    rows = c.fetchall()
    for row in rows:
        print(row)

def modifica_comanda(id, user_id, product_id, quantity):
    c.execute("UPDATE orders SET user_id=?, product_id=?, quantity=? WHERE id=?", (user_id, product_id, quantity, id))
    conn.commit()

def sterge_comanda(id):
    c.execute("DELETE FROM orders WHERE id=?", (id,))
    conn.commit()

# Exemplu de utilizare a functiilor
adauga_utilizator("Ioana Popescu", "ioana.popescu@example.com", "password")
adauga_utilizator("Alexandru Ionescu", "alexandru.ionescu@example.com", "password")
lista_utilizatori()
sterge_utilizator(1)
lista_utilizatori()

adauga_produs("Product 1", "Description 1", 9.99)
adauga_produs("Product 2", "Description 2", 19.99)
adauga_produs("Product 3", "Description 3", 39.99)
adauga_produs("Product 4", "Description 4", 29.99)
lista_produse()
sterge_produs(1)
lista_produse()

adauga_comanda(1, 1, 2)
lista_comenzi()
modifica_comanda(1, 2, 2, 3)
lista_comenzi()
sterge_comanda(1)
lista_comenzi()

c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS products")
c.execute("DROP TABLE IF EXISTS orders")
