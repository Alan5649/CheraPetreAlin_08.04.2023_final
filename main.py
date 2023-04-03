import sqlite3

from User import User
from order import Order
from product import Product


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


while True:
    print("1. Adauga utilizator")
    print("2. Lista utilizatori")
    print("3. Sterge utilizator\n")
    print("4. Adauga produs")
    print("5. Lista produse")
    print("6. Sterge produs\n")
    print("7. Adauga comanda")
    print("8. Lista comenzi")
    print("9. Actualizeaza comanda")
    print("10. Sterge comanda\n")

    # alte optiuni...

    optiune = input("Selectati o optiune: ")
    if optiune == "1":
        name = input("Nume utilizator: ")
        email = input("Email utilizator: ")
        password = input("Parola utilizator: ")
        new_user = User(name, email, password)
        new_user.save_to_database()
    elif optiune == "2":
        User.list_all_users()
    elif optiune == "3":
        id = input("Introduceti id-ul utilizatorului pe care doriti sa il stergeti: ")
        User.delete_user(id)
    elif optiune == "4":
        name = input("Nume produs: ")
        description = input("Descriere produs: ")
        price = float(input("Pret produs: "))
        new_product = Product(name, description, price)
        new_product.save_to_database()
    elif optiune == "5":
        Product.list_all_products()
    elif optiune == "6":
        id = input("Introduceti id-ul produsului pe care doriti sa il stergeti: ")
        Product.delete_product(id)
    elif optiune == "7":
        user_id = input("Id utilizator: ")
        product_id = input("Id produs: ")
        quantity = input("Cantitate: ")
        new_order = Order(user_id, product_id, quantity)
        new_order.save_to_database()
    elif optiune == "8":
        Order.list_all_orders()
    elif optiune == "9":
        id = input("Introduceti id-ul comenzii pe care doriti sa o actualizati: ")
        user_id = input("Noul id utilizator: ")
        product_id = input("Noul id produs: ")
        quantity = input("Noua cantitate: ")
        updated_order = Order(user_id, product_id, quantity)
        updated_order.update_order(id)
    elif optiune == "10":
        id = input("Introduceti id-ul comenzii pe care doriti sa o stergeti: ")
        Order.delete_order(id)

    else:
        print("Optiune invalida")

    raspuns = input("Doriti sa continuati? (da/nu) ")
    if raspuns.lower() != "da":
        break

