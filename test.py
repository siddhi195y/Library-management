from tkinter import *
from tkinter import messagebox
from tkcalendar import  DateEntry
import sqlite3

con = sqlite3.Connection("database")
cur = con.cursor()
global abcd
abcd = []
cur.execute("create table if not exists database(title varchar2(30))")
cur.execute("insert into database values('Database System Concepts (Abraham Silberschatz,Henry Korth)')")
cur.execute("insert into database values('Fundamentals of database systems(elmasri and S.Navathe)')")

cur.execute("create table if not exists mathematics (title varchar2(30))")

cur.execute("create table  if not exists python(title varchar2(30))")

cur.execute("create table  if not exists digital(title varchar2(30))")

cur.execute("create table  if not exists novel (title varchar2(30))")

rt1 = Tk()
rt1.title("GPA's LIBRARY MANAGEMENT SYSTEM")
rt1.configure(background='light green')
Label(rt1, text="GPA LIBRARY MANAGEMENT SYSTEMS", font="times 20 bold", bd=3, bg="light yellow").grid(row=0, column=0)
Label(rt1, text="Siddhi More", font="times 15 bold").grid(row=1, column=0)
Label(rt1, text="Enrollment Number=187020", font="times 15 bold").grid(row=2, column=0)
Label(rt1, text="BATCH=A", font="times 15 bold").grid(row=3, column=0)
rt1.after(1000, rt1.destroy)
rt1.mainloop()


def issue():
    issuue1 = Tk()
    issuue1.geometry('850x450')
    issuue1.config(bg="black")
    Label(issuue1, text="Kindly Fill Details For Issuing of book", bg="powder blue", fg="black", relief="raised", bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)

    def issuedatabase():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS issuedatabase1(id INTEGER PRIMARY KEY,roll text,bookname text, author text,number text,date text)")
        cur.execute("INSERT INTO issuedatabase1 Values(Null,?,?,?,?,?)",
                    (e1.get(), e2.get(), e3.get(), e4.get(), cal.get()))


        label1 = Label(issuue1, text="Book Successfully Issued  ", font="times 20")
        label1.grid(row=10, column=2)

        conn.commit()
        conn.close()



    l1 = Label(issuue1, text="Enroll no.", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    roll_text = StringVar()
    e1 = Entry(issuue1, textvariable=roll_text)
    e1.grid(row=3, column=2)
    l2 = Label(issuue1, text="Book Name", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    book_text = StringVar()
    e2 = Entry(issuue1, textvariable=book_text)
    e2.grid(row=4, column=2)
    l3 = Label(issuue1, text="Book Author", font="times 20", bg="black", fg="white")
    l3.grid(row=5, column=1)
    author_text = StringVar()
    e3 = Entry(issuue1, textvariable=author_text)
    e3.grid(row=5, column=2)
    l4 = Label(issuue1, text="Book Number", font="times 20", bg="black", fg="white")
    l4.grid(row=6, column=1)
    number_text = StringVar()
    e4 = Entry(issuue1, textvariable=number_text)
    e4.grid(row=6, column=2)
    Label(issuue1, text='Choose date', font="times 20", bg="black", fg="white").grid(row=7, column=1)
    cal = DateEntry(issuue1, width=12, borderwidth=2)
    cal.grid(row=7,column=2)





    b1 = Button(issuue1, text="SUBMIT", width=20, command=issuedatabase, bg="red", fg="white", font="times 0 bold")
    b1.grid(row=8, column=2)
    def reset():
        e1.delete(0, END)
        e1.insert(0, "")
        e2.delete(0, END)
        e2.insert(0, "")
        e3.delete(0, END)
        e3.insert(0, "")
        e4.delete(0, END)
        e4.insert(0, "")
        cal.delete(0,END)
        cal.insert(0,"")
    b2 = Button(issuue1, text="RESET", width=20,command=reset, bg="red", fg="white", font="times 0 bold")
    b2.grid(row=8, column=1)

    issuue1.mainloop()
def return1():
    issuue1 = Tk()
    issuue1.geometry('850x450')
    issuue1.config(bg="black")
    Label(issuue1, text="Kindly Fill Details For Returning of book", bg="powder blue", fg="black", relief="raised", bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)

    def returndatabase():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM issuedatabase1 WHERE roll=? AND bookname=?", (e1.get() , e2.get()))
        row = cur.fetchall()

        print(row)
        if row != []:
            user_name = row[0][1]

            Label(issuue1,text="Book Returned Successfully...!",font="times 20").grid(row=10,column=2)
            Button(login_window, text="next page", command=nextpage).grid(row=11, column=2)
            sql_delete_query = """DELETE from issuedatabase1 where roll= """+user_name
            cur.execute(sql_delete_query)
            conn.commit()
        else:

            Label(issuue1,text="Roll Number Not Found..!",font="times 20").grid(row=10, column=2)

        conn.close()


    l1 = Label(issuue1, text="Enroll no.", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    roll_text = StringVar()
    e1 = Entry(issuue1, textvariable=roll_text)
    e1.grid(row=3, column=2)
    l2 = Label(issuue1, text="Book Name", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    book_text = StringVar()
    e2 = Entry(issuue1, textvariable=book_text)
    e2.grid(row=4, column=2)
    l3 = Label(issuue1, text="Book Author", font="times 20", bg="black", fg="white")
    l3.grid(row=5, column=1)
    author_text = StringVar()
    e3 = Entry(issuue1, textvariable=author_text)
    e3.grid(row=5, column=2)
    l4 = Label(issuue1, text="Book Number", font="times 20", bg="black", fg="white")
    l4.grid(row=6, column=1)
    number_text = StringVar()
    e4 = Entry(issuue1, textvariable=number_text)
    e4.grid(row=6, column=2)
    Label(issuue1, text='Choose date', font="times 20", bg="black", fg="white").grid(row=7, column=1)
    cal = DateEntry(issuue1, width=12, borderwidth=2)
    cal.grid(row=7, column=2)

    b1 = Button(issuue1, text="SUBMIT", width=20, command=returndatabase, bg="red", fg="white", font="times 0 bold")
    b1.grid(row=8, column=2)
    def reset():
        e1.delete(0, END)
        e1.insert(0, "")
        e2.delete(0, END)
        e2.insert(0, "")
        e3.delete(0, END)
        e3.insert(0, "")
        e4.delete(0, END)
        e4.insert(0, "")
        cal.delete(0,END)
        cal.insert(0,"")
    b2 = Button(issuue1, text="RESET", width=20,command=reset, bg="red", fg="white", font="times 0 bold")
    b2.grid(row=8, column=1)
    issuue1.mainloop()



def newstudent():
    issuue1 = Tk()
    issuue1.geometry('850x450')
    issuue1.config(bg="black")
    Label(issuue1, text="Kindly Fill Details For Adding New Student", bg="powder blue", fg="black", relief="raised",
          bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)
    def newstudentdatabase():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS newstudentdatabase1(id INTEGER PRIMARY KEY,name text,roll text, department text,mobnumber text)")
        cur.execute("INSERT INTO newstudentdatabase1 Values(Null,?,?,?,?)",
                    (e1.get(), e2.get(), e3.get(), e4.get()))
        label1 = Label(issuue1, text="New Student Added Successfully....!", font="times 20")
        label1.grid(row=10, column=2)

        conn.commit()
        conn.close()
    l1 = Label(issuue1, text="Name :", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    roll_text = StringVar()
    e1 = Entry(issuue1, textvariable=roll_text)
    e1.grid(row=3, column=2)
    l2 = Label(issuue1, text="Enroll :", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    book_text = StringVar()
    e2 = Entry(issuue1, textvariable=book_text)
    e2.grid(row=4, column=2)
    l3 = Label(issuue1, text="Department :", font="times 20", bg="black", fg="white")
    l3.grid(row=5, column=1)
    author_text = StringVar()
    e3 = Entry(issuue1, textvariable=author_text)
    e3.grid(row=5, column=2)
    l4 = Label(issuue1, text="Mobile no. :", font="times 20", bg="black", fg="white")
    l4.grid(row=6, column=1)
    number_text = StringVar()
    e4 = Entry(issuue1, textvariable=number_text)
    e4.grid(row=6, column=2)


    b1 = Button(issuue1, text="SUBMIT", width=20, command=newstudentdatabase, bg="red", fg="white", font="times 0 bold")
    b1.grid(row=7, column=2)
    def reset():
        e1.delete(0, END)
        e1.insert(0, "")
        e2.delete(0, END)
        e2.insert(0, "")
        e3.delete(0, END)
        e3.insert(0, "")
        e4.delete(0, END)
        e4.insert(0, "")
    b2 = Button(issuue1, text="RESET", width=20,command=reset, bg="red", fg="white", font="times 0 bold")
    b2.grid(row=7, column=1)
    issuue1.mainloop()


def newbook():
    issuue1 = Tk()
    issuue1.geometry('850x450')
    issuue1.config(bg="black")
    Label(issuue1, text="Kindly Fill Details For Adding New Book", bg="powder blue", fg="black", relief="raised",
          bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)

    def newbookdatabase():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS newbookdatabase1(id INTEGER PRIMARY KEY,bname text,author text, bknumber text)")
        cur.execute("INSERT INTO newbookdatabase1 Values(Null,?,?,?)",
                    (e1.get(), e2.get(), e3.get()))
        label1 = Label(issuue1, text="New Book Added Successfully....!", font="times 20")
        label1.grid(row=10, column=2)

        conn.commit()
        conn.close()
    l1 = Label(issuue1, text="Bookname :", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    roll_text = StringVar()
    e1 = Entry(issuue1, textvariable=roll_text)
    e1.grid(row=3, column=2)
    l2 = Label(issuue1, text="Author :", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    book_text = StringVar()
    e2 = Entry(issuue1, textvariable=book_text)
    e2.grid(row=4, column=2)
    l3 = Label(issuue1, text="Book no. :", font="times 20", bg="black", fg="white")
    l3.grid(row=5, column=1)
    author_text = StringVar()
    e3 = Entry(issuue1, textvariable=author_text)
    e3.grid(row=5, column=2)

    b1 = Button(issuue1, text="ADD", width=20, command=newbookdatabase, bg="red", fg="white", font="times 0 bold")
    b1.grid(row=6, column=2)
    def reset():
        e1.delete(0, END)
        e1.insert(0, "")
        e2.delete(0, END)
        e2.insert(0, "")
        e3.delete(0, END)
        e3.insert(0, "")
    b2 = Button(issuue1, text="RESET", width=20,command=reset, bg="red", fg="white", font="times 0 bold")
    b2.grid(row=6, column=1)
    issuue1.mainloop()




def searchbook():
    issuue1 = Tk()
    issuue1.geometry('850x450')
    issuue1.config(bg="black")
    Label(issuue1, text="Kindly Fill Details For Adding New Book", bg="powder blue", fg="black", relief="raised",
          bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)

    def searchdatabase():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM newbookdatabase1 WHERE bname=? AND bknumber=?", (e1.get(), e2.get()))
        row = cur.fetchall()
        conn.close()
        print(row)
        if row != []:
            user_name = row[0][1]
            if e1.get() == user_name:
                Label(issuue1,text="Book Founded With Name: " + user_name,font="times 20").grid(row=7,column=2)
        else:
            Label(issuue1,text="Book Not Found",font="times 20").grid(row=7,column=2)



    l1 = Label(issuue1, text="Bookname :", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    roll_text = StringVar()
    e1 = Entry(issuue1, textvariable=roll_text)
    e1.grid(row=3, column=2)
    l2 = Label(issuue1, text="Book no. :", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    book_text = StringVar()
    e2 = Entry(issuue1, textvariable=book_text)
    e2.grid(row=4, column=2)

    b1 = Button(issuue1, text="SEARCH", width=20, command=searchdatabase, bg="red", fg="white", font="times 0 bold")
    b1.grid(row=5, column=2)
    def reset():
        e1.delete(0, END)
        e1.insert(0, "")
        e2.delete(0, END)
        e2.insert(0, "")
    b2 = Button(issuue1, text="RESET", width=20,command=reset, bg="red", fg="white", font="times 0 bold")
    b2.grid(row=5, column=1)
    issuue1.mainloop()




def nextpage():
    root1 = Tk()
    root1.geometry("750x200")
    Label(root1, text="WELCOME TO GPA LIBRARY", bg="powder blue", fg="black", relief="raised", bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)
    def exit1():
        root1.destroy()
    Button(root1, text="ISSUE", height=2, width='20', bd=10, bg='turquoise', fg='black',
           font='times 10 bold',command=issue).grid(row=2, column=0)
    Button(root1, text="RETURN",command=return1, height=2, width=20, bd=10, bg='turquoise', fg='black', font='times 10 bold'
           ).grid(row=2, column=1)
    Button(root1, text="ADD NEW STUDENT",command=newstudent, height=2, width='20', bd=10, bg='turquoise', fg='black', font='times 10 bold'
           ).grid(row=2, column=2)
    Button(root1, text="ADD NEW BOOK",command=newbook, height=2, width='20', bd=10, bg='turquoise', fg='black', font='times 10 bold'
           ).grid(row=3, column=0)
    Button(root1, text="SEARCH BOOK",command=searchbook, height=2, width='20', bd=10, bg='turquoise', fg='black', font='times 10 bold'
           ).grid(row=3, column=1)
    Button(root1, text="EXIT",command=exit1, height=2, width='20', bd=10, bg='turquoise', fg='black', font='times 10 bold'
           ).grid(row=3, column=2)
    root1.mainloop()

'''def enter():

    Label(root, text="Access granted", font="times 15 bold").grid(row=10, column=2)
    Button(root, text="next page", command=nextpage, bd=5, bg='yellow').grid(row=11, column=2)'''





def login_database():
    conn=sqlite3.connect("1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM test1 WHERE name=? AND password=?",(e1.get(),e2.get()))
    row=cur.fetchall()
    conn.close()
    print(row)
    if row!=[]:
        user_name=row[0][1]
        l3.config(text="user name found with name: "+user_name)
        Button(login_window,text="next page",command=nextpage,bd=5,bg="green",fg="black").grid(row=8,column=2)
    else:
        l3.config(text="user not found ")




def loginsign():
    def login_database():
        conn=sqlite3.connect("1.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM test1 WHERE name=? AND password=?",(e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        print(row)
        if row!=[]:
            user_name=row[0][1]
            if e1.get()==user_name:
                l3.config(text="user name found with name: "+user_name)
                Button(login_window,text="next page", command=nextpage).grid(row=11, column=2)
        else:
            l3.config(text="user not found ")

    login_window = Tk()
    login_window.geometry("850x500")
    login_window.title("Library Form")
    login_window.config(bg="black")
    '''C = Canvas(signup_window, bg="blue", height=500, width=850)
    filename = PhotoImage(file = "C:\\Users\\Yash\\Documents\\pythonproject\\venv\\library.gif")
    background_label = Label(signup_window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.grid(row=0,column=0)'''
    'Label(signup_window, text="Gpa Library Form", font="times 20 bold", bd=3, bg="light yellow").grid(row=0,column=1)'
    Label(login_window, text="Kindly Login Into The System", bg="powder blue", fg="black", relief="raised", bd=7,
          font="forte 20 bold",
          width='50').grid(row=0, column=0, columnspan=4)
    l1 = Label(login_window, text="Username", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    l2 = Label(login_window, text="Password", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)

    name_text = StringVar()
    e1 = Entry(login_window, textvariable=name_text)
    e1.grid(row=3, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text,show = "*")
    e2.grid(row=4, column=2)

    button1 = Button(login_window, text="Login", command=login_database, width=20, bg="green", fg="white",
                     font="times 0 bold")
    button1.grid(row=12, column=2)
    login_window.mainloop()

def signup():

    def signup_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS test1(id INTEGER PRIMARY KEY,name text,email text, password text,phone text,address text,deparment text)")
        cur.execute("INSERT INTO test1 Values(Null,?,?,?,?,?,?)",
                        (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
        label1 = Label(signup_window, text="Sign Up successfull please do login now !", font="times 20")
        label1.grid(row=13, column=2)

        conn.commit()
        conn.close()

    signup_window = Tk()
    signup_window.geometry("850x500")
    signup_window.title("Library Form")
    signup_window.config(bg="black")
    '''C = Canvas(signup_window, bg="blue", height=500, width=850)
    filename = PhotoImage(file = "C:\\Users\\Yash\\Documents\\pythonproject\\venv\\library.gif")
    background_label = Label(signup_window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.grid(row=0,column=0)'''
    'Label(signup_window, text="Gpa Library Form", font="times 20 bold", bd=3, bg="light yellow").grid(row=0,column=1)'
    Label(signup_window, text="GPA LIBRARY FORM", bg="powder blue", fg="black", relief="raised", bd=7,
              font="forte 20 bold",
              width='50').grid(row=0, column=0, columnspan=4)
    l1 = Label(signup_window, text="user name", font="times 20", bg="black", fg="white")
    l1.grid(row=3, column=1)
    l2 = Label(signup_window, text="user email", font="times 20", bg="black", fg="white")
    l2.grid(row=4, column=1)
    l3 = Label(signup_window, text="user password", font="times 20", bg="black", fg="white")
    l3.grid(row=5, column=1)
    l4 = Label(signup_window, text="phone number", font="times 20", bg="black", fg="white")
    l4.grid(row=6, column=1)
    l5 = Label(signup_window, text="Address", font="times 20", bg="black", fg="white")
    l5.grid(row=7, column=1)
    l6 = Label(signup_window, text="Department", font="times 20", bg="black", fg="white")
    l6.grid(row=8, column=1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=3, column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=4, column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=5, column=2)
    phone_text = StringVar()
    e4 = Entry(signup_window, textvariable=phone_text)
    e4.grid(row=6, column=2)
    addr_text = StringVar()
    e5 = Entry(signup_window, textvariable=addr_text)
    e5.grid(row=7, column=2)
    department_text = StringVar()
    e6 = Entry(signup_window, textvariable=department_text)
    e6.grid(row=8, column=2)
    b1 = Button(signup_window, text="Signup", width=20, command=signup_database, bg="red", fg="white",
                    font="times 0 bold")
    b1.grid(row=12, column=2)
    button1 = Button(signup_window, text="Login", command=loginsign, width=20, bg="green", fg="white",
                         font="times 0 bold")
    button1.grid(row=12, column=1)





login_window = Tk()
login_window.geometry("850x500")
login_window.title("Library Form")
login_window.config(bg="black")
'''C = Canvas(signup_window, bg="blue", height=500, width=850)
filename = PhotoImage(file = "C:\\Users\\Yash\\Documents\\pythonproject\\venv\\library.gif")
background_label = Label(signup_window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.grid(row=0,column=0)'''
'Label(signup_window, text="Gpa Library Form", font="times 20 bold", bd=3, bg="light yellow").grid(row=0,column=1)'
Label(login_window, text="Kindly Login Into The System", bg="powder blue", fg="black", relief="raised", bd=7, font="forte 20 bold",
      width='50').grid(row=0, column=0, columnspan=4)
l1 = Label(login_window, text="Username", font="times 20", bg="black", fg="white")
l1.grid(row=3, column=1)
l2 = Label(login_window, text="Password", font="times 20", bg="black", fg="white")
l2.grid(row=4, column=1)
l3=Label(login_window,font="times 20",bg="black",fg="white")
l3.grid(row=7,column=2)

name_text = StringVar()
e1 = Entry(login_window, textvariable=name_text)
e1.grid(row=3, column=2)
password_text = StringVar()
e2 = Entry(login_window, textvariable=password_text,show = "*")
e2.grid(row=4, column=2)


b1 = Button(login_window, text="Signup", width=20, command=signup, bg="red", fg="white", font="times 0 bold")
b1.grid(row=6, column=1)
button1 = Button(login_window, text="Login", command=login_database, width=20, bg="green", fg="white", font="times 0 bold")
button1.grid(row=6, column=2)




login_window.mainloop()