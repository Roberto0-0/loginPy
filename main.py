#!/usr/bin/python3
import sqlite3
import getpass
import hashlib
import datetime
import os

data = sqlite3.connect("database/data.db")
Cursor = data.cursor()

try:
  data.execute("""
  CREATE TABLE clients (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
  )""")
  print("\033[32mDatebase created successfully.\033[m")  
except sqlite3.OperationalError:
  os.system("clear") 
  print("\033[32mConnected with database.\033[m")

print(" "*5,"Welcome!!")
while True:
  print("""[1] Sing up\n[2] Log in""")
  Opcao_client = input(": ")
  if Opcao_client == '1':
    name = input("Name: ")
    while True:
      if len(name) <= 5:
        name = input("\033[31mNome muito curto\033[m: ")
      if len(name) > 5:
        break
    email = input("E-mail: ")
    while True:
      if not "@""gmail"".com" in email:
        email = input("\033[31mEmail invalido\033[m: ")
        for values in  Cursor.execute("SELECT * FROM clients"):
          if email == values[2]:
            email = input("\033[31mE-mail já existe\033[m: ")
            while True:
              if not "@""gmail"".com"  in email:
                email = input("\033[31mEmail invalido\033[m: ")
              elif "@""gmail"".com" in email:
                break
          elif email != values[2]:
            pass
        break
      elif "@""gmail"".com" in email:
        for values in  Cursor.execute("SELECT * FROM clients"):
          if email == values[2]:
            email = input("\033[31mE-mail já existe\033[m: ")
            while True:
              if not "@""gmail"".com" in email:
                email = input("\033[31mEmail invalido\033[m: ")
              elif "@""gmail"".com" in email:
                break
          elif email != values[2]:
            pass
        break
    password = getpass.getpass("Password: ")
    while True:
        if len(password) <= 4:
            password = getpass.getpass("\033[31mSenha muito curta\033[m: ")
        elif len(password) > 4:
            break
    confirmPassword = getpass.getpass("Confirmar senha: ")
    while True:
        if confirmPassword != password:
            confirmPassword = getpass.getpass("\033[31mAs senha não se batem\033[m: ")
        elif confirmPassword == password:
            password = hashlib.sha224(password.encode()).hexdigest()
            break
    Cursor.execute("""INSERT INTO clients(name, email, password )VALUES(?,?,?)""",(name, email, password))
    data.commit()
    print("\033[32mAccount create with success! %s/%s/%s\033[m"%(datetime.date.today().day, datetime.date.today().month,datetime.date.today().year))
  
  elif Opcao_client == '-h':
    for values in Cursor.execute("SELECT * FROM clients"):
        print(values)
  elif Opcao_client == "exit":
    print("Have a good day!!")
    exit()
