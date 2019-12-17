import sqlite3

creation_table_str = """
    CREATE TABLE IF NOT EXISTS EDUCATION (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sigun TEXT,
        emd TEXT,
        types TEXT,
        named TEXT,
        daepyo TEXT,
        telno TEXT,
        address TEXT,
        lat TEXT,
        loat TEXT
    );
"""

check_if_table = """
    SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?;
"""

insertion_sample_data = """
    INSERT INTO EDUCATION VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

if __name__ == "__main__":
    conn = sqlite3.connect('soa2.db')
    cur = conn.cursor()
    cur.execute(check_if_table, ("EDUCATION",))
    if cur.fetchone()[0] == 1:
        print('EDUCATION table already exists.')
    else:
        cur.execute(creation_table_str)
        conn.commit()
        print("EDUCATION table created successfully.")

    conn.commit()
    conn.close()