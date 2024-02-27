import os,sqlite3

conn=sqlite3.connect('petshop.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS petshop (id INTEGER PRIMARY KEY AUTOINCREMENT, pet_type TEXT, pet_name TEXT, age INTEGER)''')
conn.commit()

def register_pet():
    print("----- REGISTER PET -----")
    pet_type=input("Enter the type of pet: ")
    pet_name=input("Enter the name of pet: ")
    age=int(input("Enter the age of pet: "))
    cursor.execute("INSERT INTO petshop (pet_type, pet_name, age) VALUES (?, ?, ?)", (pet_type, pet_name, age))
    conn.commit()
    print("##### Data saved #####")

def list_pets():
    print("----- LIST PETS -----")
    cursor.execute('SELECT * FROM petshop')
    data=cursor.fetchall()
    if not data: print("No pets registered!")
    else: [print(row) for row in data]

def modify_pet():
    print("----- MODIFY PET DATA -----")
    pet_id=int(input("Enter an ID: "))
    cursor.execute("SELECT * FROM petshop WHERE id = ?", (pet_id,))
    data=cursor.fetchone()
    if not data: print(f"No pet registered with ID = {pet_id}")
    else:
        new_pet_type=input("Enter a new pet type: ")
        new_pet_name=input("Enter a new pet name: ")
        new_age=int(input("Enter a new age: "))
        cursor.execute("UPDATE petshop SET pet_type=?, pet_name=?, age=? WHERE id=?", (new_pet_type, new_pet_name, new_age, pet_id))
        conn.commit()
        print("##### Data updated! #####")

def delete_pet():
    print("----- DELETE PET -----")
    pet_id=int(input("Enter an ID: "))
    cursor.execute("SELECT * FROM petshop WHERE id = ?", (pet_id,))
    data=cursor.fetchone()
    if not data: print(f"No pet registered with ID = {pet_id}")
    else:
        cursor.execute("DELETE FROM petshop WHERE id=?", (pet_id,))
        conn.commit()
        print("##### Pet deleted! #####")

def delete_all_pets():
    print("!!!!! DELETE ALL DATA FROM TABLE !!!!!")
    confirm=input("CONFIRM DELETION OF ALL PETS? [Y]es or [N]o?")
    if confirm.upper()=="Y":
        cursor.execute("DELETE FROM petshop")
        conn.commit()
        print("##### All records deleted! #####")
    else: print("Operation canceled by user!")

while True:
    print("------- CRUD - PETSHOP -------")
    print("""
    1 - Register Pet
    2 - List Pets
    3 - Modify Pet
    4 - Delete Pet
    5 - DELETE ALL PETS
    6 - EXIT
    """)
    choice=input("Choice -> ")
    if choice.isdigit(): choice=int(choice)
    else: choice=6; print("Enter a number. Restart the application!")
    if choice==1: register_pet()
    elif choice==2: list_pets()
    elif choice==3: modify_pet()
    elif choice==4: delete_pet()
    elif choice==5: delete_all_pets()
    elif choice==6: break
    else: input("Enter a number between 1 and 6.")

input("Press ENTER")
conn.close()
