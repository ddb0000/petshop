import sqlite3

def main():
    with sqlite3.connect('petshop.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS petshop (id INTEGER PRIMARY KEY AUTOINCREMENT, pet_type TEXT, pet_name TEXT, age INTEGER)''')
        ops = {
            '1': lambda: c.execute("INSERT INTO petshop (pet_type, pet_name, age) VALUES (?, ?, ?)", (input("pet type: "), input("pet name: "), int(input("pet age: ")))).lastrowid and print("data saved"),
            '2': lambda: print("\n".join(f"id: {row[0]}, type: {row[1]}, name: {row[2]}, age: {row[3]}" for row in c.execute('SELECT * FROM petshop').fetchall()) or "no pets"),
            '3': lambda: (lambda pid=input("id: "): c.execute("UPDATE petshop SET pet_type=?, pet_name=?, age=? WHERE id=?", (input("new type: "), input("new name: "), int(input("new age: ")), pid)).rowcount and print("data updated") if c.execute("SELECT * FROM petshop WHERE id = ?", (pid,)).fetchone() else print("no pet found"))(),
            '4': lambda: (lambda pid=input("id: "): c.execute("DELETE FROM petshop WHERE id=?", (pid,)).rowcount and print("pet deleted") if c.execute("SELECT * FROM petshop WHERE id = ?", (pid,)).fetchone() else print("no pet found"))(),
            '5': lambda: c.execute("DELETE FROM petshop").rowcount and print("all deleted") if input("confirm delete all? (y/n): ").lower() == "y" else print("cancelled")
        }
        while (ch := input("1-register 2-list 3-modify 4-delete 5-delete all 6-exit: ")) != '6':
            ops.get(ch, lambda: print("invalid"))()

if __name__ == "__main__":
    main()
