import sqlite3

conn = sqlite3.connect('petshop.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS petshop (id INTEGER PRIMARY KEY AUTOINCREMENT, pet_type TEXT, pet_name TEXT, age INTEGER)''')
conn.commit()

def register_pet():
    pet_type = input("pet type: ")
    pet_name = input("pet name: ")
    age = int(input("pet age: "))
    cursor.execute("INSERT INTO petshop (pet_type, pet_name, age) VALUES (?, ?, ?)", (pet_type, pet_name, age))
    conn.commit()
    print("data saved")

def list_pets():
    cursor.execute('SELECT * FROM petshop')
    data = cursor.fetchall()
    if not data:
        print("no pets")
    else:
        for row in data:
            print(f"id: {row[0]}, type: {row[1]}, name: {row[2]}, age: {row[3]}")

def modify_pet():
    pet_id = int(input("id: "))
    cursor.execute("SELECT * FROM petshop WHERE id = ?", (pet_id,))
    data = cursor.fetchone()
    if not data:
        print("no pet found")
        return
    new_pet_type = input("new type: ")
    new_pet_name = input("new name: ")
    new_age = int(input("new age: "))
    cursor.execute("UPDATE petshop SET pet_type=?, pet_name=?, age=? WHERE id=?", (new_pet_type, new_pet_name, new_age, pet_id))
    conn.commit()
    print("data updated")

def delete_pet():
    pet_id = int(input("id: "))
    cursor.execute("SELECT * FROM petshop WHERE id = ?", (pet_id,))
    data = cursor.fetchone()
    if not data:
        print("no pet found")
        return
    cursor.execute("DELETE FROM petshop WHERE id=?", (pet_id,))
    conn.commit()
    print("pet deleted")

def delete_all_pets():
    confirm = input("confirm delete all? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM petshop")
        conn.commit()
        print("all deleted")
    else:
        print("cancelled")

def main_menu():
    while True:
        choice = input("1-register 2-list 3-modify 4-delete 5-delete all 6-exit: ")
        if choice == '1':
            register_pet()
        elif choice == '2':
            list_pets()
        elif choice == '3':
            modify_pet()
        elif choice == '4':
            delete_pet()
        elif choice == '5':
            delete_all_pets()
        elif choice == '6':
            break
        else:
            print("invalid")

main_menu()
conn.close()
