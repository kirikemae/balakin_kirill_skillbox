import sqlite3

update_query = """
UPDATE table_effective_manager
SET salary = 
    CASE 
        WHEN (salary * 1.10) > 100000 THEN NULL
        ELSE salary * 1.10
    END
WHERE name = ?
"""

delete_query = """
DELETE FROM table_effective_manager
WHERE name = ? AND (SELECT COUNT(*) FROM table_effective_manager WHERE name = ?) = 0
"""

def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str):
    cursor.execute(update_query, (name,))
    cursor.execute(delete_query, (name, name))

if __name__ == "__main__":
    with sqlite3.connect("hw4.db") as conn:
        c = conn.cursor()
        name = input('Введите фамилию: ')
        ivan_sovin_the_most_effective(c, name)
