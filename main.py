import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  website TEXT,
  username TEXT,
  password TEXT)
""")

conn.commit()

from tkinter import*

root= Tk()

root.title("Password Manager")
root.geometry("500x400")
root.resizable(False,False)

Label(root,text="Password Manager",
      font=("Arial",18,"bold")).pack(pady=20)

Label(root,text="Website").pack()
website_entry= Entry(root,width=40)
website_entry.pack()


Label(root,text="Username/Email").pack()
username_entry=Entry(root,width=40)
username_entry.pack()

Label(root,text="Password").pack()
password_entry= Entry(root,width=40,show="*")
password_entry.pack()

def save_password():
  website= website_entry.get()
  username= username_entry.get()
  password= password_entry.get()

  cursor.execute(
    "INSERT INTO passwords (website,username,password)VALUES(?,?,?)",
    (website,username,password)
  )

  conn.commit()

  website_entry.delete(0,END)
  username_entry.delete(0,END)
  password_entry.delete(0,END)

  print("Password Saved Successfully!")

Button(
  root,
  text= "Save Password",
  command= save_password,
  bg="green",
  fg="white",
  width=20
).pack(pady=10)


root.mainloop()






























