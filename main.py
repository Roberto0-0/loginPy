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
  print("\033[32mDatebase create with success.\033[m")  
except sqlite3.OperationalError:
  os.system("clear") 
  print("\033[32mConnected with database.\033[m")

print(" "*5,"Bem-vindo(a)!!")
while True:
  print("""[1] Registra-se
[2] Entrar""")
  Opcao_client = input(": ")
  if Opcao_client == '1':
    name = input("Nome: ")
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
    password = getpass.getpass("Senha: ")
    while True:
     	if len(password) <= 4:
     		password = getpass.getpass("\033[31mSenha muito curta\033[m: ")
     	elif len(password) > 4:
     		break
    Cpassword = getpass.getpass("Confirmar senha: ")
    while True:
        if Cpassword != password:
        	Cpassword = getpass.getpass("\033[31mAs senha não se batem\033[m: ")
        elif Cpassword == password:
        	password = hashlib.sha224(password.encode()).hexdigest()
        	break
    Cursor.execute("""INSERT INTO clients(name, email, password )VALUES(?,?,?)""",(name, email, password))
    data.commit()
    print("\033[32mAccount create with success! %s/%s/%s\033[m"%(datetime.date.today().day, datetime.date.today().month,datetime.date.today().year))
  elif Opcao_client == '2':
    c_email = input("E-mail: ")
    while True:
      if not "@""gmail"".com" in c_email:
        c_email = input("\033[031mE-mail invalido\033[m: ")
        for values in Cursor.execute("SELECT * FROM clients"):
          if c_email == values[2]:
            email_id = values[0]
            continue
          elif c_email != values[2]:
            c_email = input("\033[31mE-mail errado\033[m: ")
            while True:
              if not "@""gmail"".com" in c_email:
                c_email = input("\033[31mEmail invalido\033[m: ")
              elif "@""gmail"".com" in ec_mail:
                break
        break
      elif "@""gmail"".com" in c_email:
        for values in  Cursor.execute("SELECT * FROM clients"):
          if c_email == values[2]:
            email_id = values[0]
            break
          elif c_email != values[2]:
            c_email = input("\033[31mE-mail errado\033[m: ")
            while True:
              if not "@""gmail"".com" in c_email:
                c_email = input("\033[31mEmail invalido\033[m: ")
              elif "@""gmail"".com" in c_email:
                break
        break
    c_password = getpass.getpass("Senha: ")
    for values in Cursor.execute("SELECT * FROM clients"):
      if c_password == values[3]:
        password_id = values[0]
        if email_id == password_id:
          print(f"\033[32mBem vindo(a)\033[m \033[35m{values[1]}\033[m")
          exit()
      elif c_password != values[3]:
        c_password = getpass.getpass("\033[31mSenha errada\033[m: ")
        if c_password == values[3]:
          password_id = values[0]
          if password_id == email_id:
            print(f"\033[32mBem vindo(a)\033[m \033[35m{values[1]}\033[m")
            exit()
        elif c_password != values[3]:
          c_password = getpass.getpass("\033[31mSenha errada\033[m: ")
          if c_password == values[3]:
            password_id = values[0]
            if password_id == email_id:
              print(f"\033[32mBem vindo(a)\033[m \033[35m{values[1]}\033[m")
              exit()
          elif c_password != values[3]:
            pass
  elif Opcao_client == '-h':
     	for values in Cursor.execute("SELECT * FROM clients"):
     		print(values)
  elif Opcao_client == "exit":
      print("Volte sempre")
      exit()
