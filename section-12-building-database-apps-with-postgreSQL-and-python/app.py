from tkinter import *
import tkinter as tk
import psycopg2
root = Tk()

def get_data(name,age,phone):
    conn =psycopg2.connect(
        host='localhost',
        database='management',
        user='postgres',
        password='1234'
    )

    cur = conn.cursor()
    query= '''INSERT INTO student (NAME,AGE,PHONE) VALUES (%s,%s,%s);'''
    cur.execute(query,(name,age,phone))
    print('Insert Successfully')
    conn.commit()
    conn.close()
def search(name):
    conn =psycopg2.connect(
        host='localhost',
        database='management',
        user='postgres',
        password='1234'
    )
    cur = conn.cursor()
    query= f'''SELECT * FROM student WHERE NAME = '{name}' ;'''
    cur.execute(query,(name))
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()
    display_all()

def display_search(row):
    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=9,column=0)
    listbox.insert(END,row)

def display_all():
    conn =psycopg2.connect(
        host='localhost',
        database='management',
        user='postgres',
        password='1234'
    )
    cur = conn.cursor()
    query= '''SELECT * FROM student  ;'''
    cur.execute(query)
    row = cur.fetchall()

    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=10,column=1)
    for x in row:
        listbox.insert(END,x)
canvas = Canvas(root,height = 280,width = 500)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Add Data")
label.grid(row = 0,column=1)

label = Label(frame,text="Name")
label.grid(row = 1,column=0)

label = Label(frame,text="Age")
label.grid(row = 2,column=0)

label = Label(frame,text="Numberphone")
label.grid(row = 3,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

entry_phone = Entry(frame)
entry_phone.grid(row=3,column=1)

button = Button(
    frame,text="Add Data",
    command= lambda:  get_data(
        entry_name.get(),
        entry_age.get(),
        entry_phone.get()
    )
)
button.grid(row=4,column=1)

label = Label(frame,text="Search Data")
label.grid(row = 5,column=1)

label = Label(frame,text="Search by Name")
label.grid(row = 6,column=0)

entry_data = Entry(frame)
entry_data.grid(row=6,column=1)

button = Button(
    frame,text="Search Data", command= lambda:search(entry_data.get())
)
button.grid(row=6,column=2)
display_all()


root.mainloop()