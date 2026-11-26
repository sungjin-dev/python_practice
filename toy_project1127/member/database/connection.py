import sqlite3

def insert_customer(name, phone):    
    with sqlite3.connect("data/member.db") as conn:        
        conn.execute(            
            "INSERT INTO customers (name, phone) VALUES (?, ?)",            
            (name, phone)        )