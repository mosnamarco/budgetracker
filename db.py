import sqlite3

def create_table(table_name, columns):
  con = sqlite3.connect("budget.db")
  cur = con.cursor()

  query = f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join(columns)})"
  cur.execute(query)

def insert_data(table_name, data):
  con = sqlite3.connect("budget.db")
  cur = con.cursor()

  query = f"INSERT INTO {table_name} VALUES(?, ?, ?)"
  cur.execute(query, data)
  
  con.commit()

def get_data(table_name):
  con = sqlite3.connect("budget.db")
  cur = con.cursor()
  
  query = f"SELECT * FROM {table_name}"
  
  res = cur.execute(query).fetchall()
  print(res)

  return res 