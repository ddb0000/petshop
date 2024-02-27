import sqlite3

def main():
    with sqlite3.connect('petshop.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS petshop (id INTEGER PRIMARY KEY, pet_type TEXT, pet_name TEXT, age REAL)''')

        def input_val(prompt, type_=str, error_msg="Invalid input, try again."):
            while True:
                try:
                    value = type_(input(prompt))
                    if type_ is float and value < 0: raise ValueError("Negative value not allowed.")
                    if type_ is str and not value.isalpha(): raise ValueError("Only letters allowed.")
                    return value
                except ValueError:
                    print(error_msg)

        ops = {
            '1': lambda: c.execute("INSERT INTO petshop (pet_type, pet_name, age) VALUES (?, ?, ?)", (input_val("pet type: "), input_val("pet name: "), input_val("pet age: ", float))) and print("data saved"),
            '2': lambda: print("\n".join(f"id: {row[0]}, type: {row[1]}, name: {row[2]}, age: {row[3]}" for row in c.execute("SELECT * FROM petshop").fetchall()) or "no pets"),
            '3': lambda: (lambda pid: (lambda t, n, a: c.execute("UPDATE petshop SET pet_type=?, pet_name=?, age=? WHERE id=?", (t, n, a, pid)) and print("data updated"))(*[input_val(f"new {x}: ", float if x == 'age' else str) for x in ["type", "name", "age"]]) if c.execute("SELECT * FROM petshop WHERE id = ?", (pid,)).fetchone() else print("no pet found"))(input("id: ")),
            '4': lambda: (lambda pid: c.execute("DELETE FROM petshop WHERE id=?", (pid,)) and print("pet deleted") if c.execute("SELECT * FROM petshop WHERE id = ?", (pid,)).fetchone() else print("no pet found"))(input("id: ")),
            '5': lambda: c.execute("DELETE FROM petshop") and print("all deleted") if input("confirm delete all? (y/n): ").lower() == 'y' else print("cancelled"),
        }

        while (ch := input("1-register 2-list 3-modify 4-delete 5-delete all 6-exit: ")) != '6':
            ops.get(ch, lambda: print("invalid"))()

if __name__ == "__main__":
    main()
