import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harman94000",
    database="Harman",
)


Harman = tkinter.Tk()
Harman.geometry("250x250+575+240")
Harman.title("Panel")


def Admin_login():
    Harman.withdraw()

    def check():
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Username,Adminpassword FROM Harmanadmin")
            myresult = mycursor.fetchall()
            username = user.get()
            password = passw.get()
            for db_username, db_pass in myresult:
                if username == db_username and password == db_pass:
                    messagebox.showinfo(
                        "Login Success", "Username and password are correct!"
                    )
                    admin()
                    top1.destroy()
                    return
            messagebox.showerror(
                "Login Error",
                "Incorrect username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            top1.destroy()

    top1 = tkinter.Toplevel()
    top1.geometry("200x120+600+250")
    top1.title("Login")
    user_label = Label(top1, text="Username:")
    user_label.place(x=10, y=10)
    pass_label = Label(top1, text="Password:")
    pass_label.place(x=10, y=50)
    user = tkinter.Entry(top1, width=15)
    user.place(x=80, y=10)
    passw = tkinter.Entry(top1, width=15, show="*")
    passw.place(x=80, y=50)
    login = Button(top1, text="Login", command=check, width=5, height=1)
    login.place(x=60, y=80)


def admin():
    top1 = tkinter.Toplevel()
    top1.geometry("350x480")
    top1.title("Admin Panel")

    i = 0
    buttons = [
        ("CHECK BOOKS STOCK", stock_check),
        ("LIST OF STAFF", staff_list),
        ("LIST OF STUDENTS", student_list),
        ("APPROVE STUDENT", approve_student_acc),
        ("RECRUIT STAFF", recruit_staff),
        ("SEARCH BOOK", Book_search),
        ("APPROVE STOCK", Stock_app),
    ]

    for text, cmd in buttons:
        Button(
            top1,
            text=text,
            command=cmd,
            width=20,
            height=2).place(
            x=100,
            y=15 + i)
        i += 70


def approve_student_acc():
    top2 = tkinter.Toplevel()
    top2.geometry("1500x500")

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Student_reg")
        myresult = mycursor.fetchall()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        top2.destroy()
        return

    columns = [
        ("Studentname", 10),
        ("Age", 25),
        ("Address", 15),
        ("Stream", 10),
        ("Class", 25),
        ("Mobile", 20),
        ("Email", 10),
        ("Username", 15),
        ("UserPassword", 15),
    ]

    x_positions = []
    current_x = 9
    for _, width in columns:
        x_positions.append(current_x)
        current_x += width * 8

    for o, (header, _) in enumerate(columns):
        label = tkinter.Label(top2, text=header, width=columns[o][1])
        label.place(x=x_positions[o], y=10)

    for i, x in enumerate(myresult):
        Entry_stored = []
        name = x[0]
        Buttons = []

        try:
            mycursor.execute(f"SELECT * FROM Student_reg")
            myresult1 = mycursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            top2.destroy()
            return

        list_data = []

        for z in myresult1:
            list_data = list(z)

        for o in range(min(len(x), len(columns))):
            y = x[o]
            text = tkinter.Entry(top2, width=columns[o][1])
            text.place(x=x_positions[o], y=40 + i * 30)
            text.insert(END, str(y))
            text.config(state=DISABLED)
            Entry_stored.append(text)

        def Approve(a, b, c):
            try:
                mycursor.execute(
                    f"INSERT INTO Users(Studentname, Age, Address, Stream_Enrolled, Class, Mobile, Email, Username, UserPassword) VALUES('{
                        list_data[0]}', '{
                        list_data[1]}', '{
                        list_data[2]}', '{
                        list_data[3]}', '{
                        list_data[4]}', '{
                            list_data[5]}', '{
                                list_data[6]}', '{
                                    list_data[7]}', '{
                                        list_data[8]}')")
                mycursor.execute(
                    f"DELETE FROM Student_reg WHERE Studentname='{c}'")
                mydb.commit()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                mydb.rollback()
            finally:
                for y in a:
                    y.destroy()
                for button in b:
                    button.destroy()

        def Reject(a, b, c):
            try:
                for y in a:
                    mycursor.execute(
                        f"DELETE FROM Student_reg WHERE Studentname='{c}'")
                    mydb.commit()
                    y.destroy()
                for button in b:
                    button.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                mydb.rollback()

        b1 = Button(
            top2,
            text="Approve",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Approve(e, b, n),
        )
        b1.place(x=x_positions[o] + 80, y=40 + i * 30)
        Buttons.append(b1)
        b2 = Button(
            top2,
            text="Reject",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Reject(e, b, n),
        )
        b2.place(x=x_positions[o] + 220, y=40 + i * 30)
        Buttons.append(b2)


def recruit_staff():
    top2 = tkinter.Toplevel()
    top2.geometry("1500x500")

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Staff_reg")
        myresult = mycursor.fetchall()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        top2.destroy()
        return

    columns = [
        ("Username", 10),
        ("Mobile", 25),
        ("Email", 15),
        ("UserPassword", 10),
        ("Designation", 25),
        ("Address", 20),
    ]

    x_positions = []
    current_x = 6
    for _, width in columns:
        x_positions.append(current_x)
        current_x += width * 8

    for o, (header, _) in enumerate(columns):
        label = tkinter.Label(top2, text=header, width=columns[o][1])
        label.place(x=x_positions[o], y=10)

    for i, x in enumerate(myresult):
        Entry_stored = []
        name = x[0]
        Buttons = []

        try:
            mycursor.execute(f"SELECT * FROM Staff_reg")
            myresult1 = mycursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            top2.destroy()
            return

        list_data = []

        for z in myresult1:
            list_data = list(z)

        for o in range(min(len(x), len(columns))):
            y = x[o]
            text = tkinter.Entry(top2, width=columns[o][1])
            text.place(x=x_positions[o], y=40 + i * 30)
            text.insert(END, str(y))
            text.config(state=DISABLED)
            Entry_stored.append(text)

        def Approve(a, b, c):
            try:
                mycursor.execute(
                    f"INSERT INTO Employees(Username, Mobile, Email, UserPassword, Designation, Address) VALUES('{
                        list_data[0]}', '{
                        list_data[1]}', '{
                        list_data[2]}', '{
                        list_data[3]}', '{
                        list_data[4]}', '{
                            list_data[5]}')")
                mycursor.execute(f"DELETE FROM Staff_reg WHERE Username='{c}'")
                mydb.commit()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                mydb.rollback()
            finally:
                for y in a:
                    y.destroy()
                for button in b:
                    button.destroy()

        def Reject(a, b, c):
            try:
                for y in a:
                    mycursor.execute(
                        f"DELETE FROM Staff_reg WHERE Username='{c}'")
                    mydb.commit()
                    y.destroy()
                for button in b:
                    button.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                mydb.rollback()

        b1 = Button(
            top2,
            text="Approve",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Approve(e, b, n),
        )
        b1.place(x=x_positions[o] + 80, y=40 + i * 30)
        Buttons.append(b1)
        b2 = Button(
            top2,
            text="Reject",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Reject(e, b, n),
        )
        b2.place(x=x_positions[o] + 220, y=40 + i * 30)
        Buttons.append(b2)


def Stock_app():
    top2 = tkinter.Toplevel()
    top2.geometry("1500x500")

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Stock_update_req")
        myresult = mycursor.fetchall()
    except BaseException:
        messagebox.showerror(
            "Database Error",
            "Error fetching data from database.")
        return

    columns = [
        ("BOOKNAME", 10),
        ("AUTHORNAME", 25),
        ("PAGES", 15),
        ("PUBLISHER", 10),
        ("PURCHASE DATE", 25),
        ("PRICE", 20),
        ("COPIES", 20),
        ("SUBJECT", 15),
        ("CATEGORY", 20),
    ]

    x_positions = []
    current_x = 9
    for _, width in columns:
        x_positions.append(current_x)
        current_x += width * 8

    for o, (header, _) in enumerate(columns):
        label = tkinter.Label(top2, text=header, width=columns[o][1])
        label.place(x=x_positions[o], y=10)

    for i, x in enumerate(myresult):
        Entry_stored = []
        name = x[0]
        Buttons = []

        try:
            mycursor.execute(f"SELECT * FROM Stock_update_req")
            myresult1 = mycursor.fetchall()
        except BaseException:
            messagebox.showerror("Data Not Found")
            top2.destroy()
            return

        list_data = []

        for z in myresult1:
            list_data = list(z)

        for o in range(min(len(x), len(columns))):
            y = x[o]
            text = tkinter.Entry(top2, width=columns[o][1])
            text.place(x=x_positions[o], y=40 + i * 30)
            text.insert(END, str(y))
            text.config(state=DISABLED)
            Entry_stored.append(text)

        def Approve(a, b, c):
            try:
                mycursor.execute(
                    f"INSERT INTO Inventory_stock(BOOKNAME, Authorname, Pages, Publications, Date_of_purchase, Price, Copies, Sub, Category) VALUES('{
                        list_data[0]}', '{
                        list_data[1]}', '{
                        list_data[2]}', '{
                        list_data[3]}', '{
                        list_data[4]}', '{
                            list_data[5]}', '{
                                list_data[6]}', '{
                                    list_data[7]}', '{
                                        list_data[8]}')")
                mycursor.execute(
                    f"DELETE FROM Stock_update_req WHERE BOOKNAME='{c}'")
                mydb.commit()
            except BaseException:
                messagebox.showerror(
                    "Database Error", "Error processing approval.")
            finally:
                for y in a:
                    y.destroy()
                for button in b:
                    button.destroy()

        def Reject(a, b, c):
            try:
                for y in a:
                    mycursor.execute(
                        f"DELETE FROM Stock_update_req WHERE BOOKNAME='{c}'"
                    )
                    mydb.commit()
                    y.destroy()
                for button in b:
                    button.destroy()
            except BaseException:
                messagebox.showerror(
                    "Database Error", "Error processing rejection.")

        b1 = Button(
            top2,
            text="Approve",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Approve(e, b, n),
        )
        b1.place(x=x_positions[o] + 80, y=40 + i * 30)
        Buttons.append(b1)
        b2 = Button(
            top2,
            text="Reject",
            width=20,
            height=1,
            command=lambda e=Entry_stored, b=Buttons, n=name: Reject(e, b, n),
        )
        b2.place(x=x_positions[o] + 220, y=40 + i * 30)
        Buttons.append(b2)


def staff_select():
    top1 = tkinter.Toplevel()
    Harman.withdraw()
    top1.geometry("200x120+600+250")
    top1.title("Select an option")

    def login_process():
        Staff_login()
        top1.destroy()

    def Apply_process():
        Staff_reg()
        top1.destroy()

    buttons = [("Login", login_process), ("Apply", Apply_process)]
    i = 0
    for x, (text, cmd) in enumerate(buttons):
        Button(
            top1,
            text=text,
            command=cmd,
            width=20,
            height=2).place(
            x=30,
            y=15 + i)
        i += 40


def Staff_reg():
    top2 = tkinter.Toplevel()
    top2.geometry("300x300+575+240")
    top2.title("Staff Apply")

    labels = [
        "Username:",
        "Mobile:",
        "Email:",
        "UserPassword:",
        "Designation:",
        "Address:",
    ]
    i = 0
    for x in labels:
        tkinter.Label(top2, text=x).place(x=10, y=20 + i)
        i += 40

    textfields = [
        "Username",
        "Mobile",
        "Email",
        "UserPassword",
        "Designation",
        "Address",
    ]
    entries = []
    i = 0

    for x in enumerate(textfields):
        entry = tkinter.Entry(top2, width=20)
        entry.place(x=100, y=20 + i)
        entries.append(entry)
        i += 40

    def Submit_staff_reg():
        mycursor = mydb.cursor()
        values = [entry.get() for entry in entries]

        try:
            mycursor.execute(
                f"INSERT INTO Staff_reg VALUES ('{
                    values[0]}', '{
                    values[1]}', '{
                    values[2]}', '{
                    values[3]}', '{
                        values[4]}', '{
                            values[5]}')")
            mydb.commit()
        except BaseException:
            messagebox.showerror(
                "Database Error", "Error inserting staff registration data."
            )
        finally:
            top2.destroy()

    Button(
        top2,
        text="Submit",
        width=20,
        height=1,
        command=Submit_staff_reg).place(
        x=30,
        y=20 + i)


def Staff_login():
    def check():
        mycursor = mydb.cursor()
        try:
            mycursor.execute("SELECT Username, UserPassword FROM Employees")
            myresult = mycursor.fetchall()
        except BaseException:
            messagebox.showerror(
                "Database Error",
                "Error fetching login data.")
            return

        username = user.get()
        password = passw.get()
        login = 0
        for db_username, db_pass in myresult:
            if username == db_username and password == db_pass:
                login = 1
                break
        if login == 1:
            messagebox.showinfo(
                "Login Success",
                "Username and password are correct!")
            top1.destroy()
            staff()
        else:
            messagebox.showerror(
                "Login Error",
                "Incorrect username or password.")
            top1.destroy()

    top1 = tkinter.Toplevel()
    top1.geometry("200x120+600+250")
    top1.title("Login")
    user_label = Label(top1, text="Username:")
    user_label.place(x=10, y=10)
    pass_label = Label(top1, text="Password:")
    pass_label.place(x=10, y=50)
    user = tkinter.Entry(top1, width=15)
    user.place(x=80, y=10)
    passw = tkinter.Entry(top1, width=15, show="*")
    passw.place(x=80, y=50)
    login = Button(top1, text="Login", command=check, width=5, height=1)
    login.place(x=60, y=80)


def staff():
    top1 = tkinter.Toplevel()
    top1.geometry("300x350+575+240")
    top1.title("Staff Panel")
    i = 0
    buttons = [
        ("BOOK ALLOCATION", Book_allot),
        ("STOCK UPDATE REQUEST", Stock_update_req),
        ("SEARCH BOOK", Book_search),
        ("ALLOCATED BOOKS", Allocated),
        ("UPDATE FINE", Update_fine),
    ]
    for x, (text, cmd) in enumerate(buttons):
        Button(
            top1,
            text=text,
            command=cmd,
            width=20,
            height=2).place(
            x=80,
            y=15 + i)
        i += 70


def Allocated():

    top2 = tkinter.Toplevel()
    top2.geometry("1300x500")
    top2.title("Stock Panel")
    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT * FROM Book_list_stu")
        myresult = mycursor.fetchall()
    except BaseException:
        messagebox.showerror(
            "Database Error",
            "Error fetching allocated books.")
        return

    columns = [
        ("Studentname", 10),
        ("Bookid", 10),
        ("Bookname", 25),
        ("Authorname", 15),
        ("Pages", 10),
        ("Publications", 25),
        ("Date of Publication", 20),
        ("Price", 10),
        ("Subject", 15),
        ("Category", 15),
    ]

    x_positions = []
    current_x = 10
    for _, width in columns:
        x_positions.append(current_x)
        current_x += width * 8

    for o, (header, _) in enumerate(columns):
        label = tkinter.Label(top2, text=header, width=columns[o][1])
        label.place(x=x_positions[o], y=10)

    for i, x in enumerate(myresult):
        for o in range(min(len(x), len(columns))):
            y = x[o]
            text = tkinter.Entry(top2, width=columns[o][1])
            text.place(x=x_positions[o], y=40 + i * 30)
            text.insert(END, str(y))
            text.config(state=DISABLED)


def Book_allot():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("800x500")
        top2.title("Stock Panel")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT * FROM Book_req_stu")
        myresult = mycursor.fetchall()

        columns = [("Studentname", 10), ("Bookid", 25),
                   ("Bookname", 15), ("Time", 10)]

        x_positions = []
        current_x = 4
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):
            Entry_stored = []
            name = x[0]
            Buttons = []

            try:
                mycursor.execute(
                    f"SELECT Bookid,BOOKNAME,Authorname,Pages,Publications,Date_of_purchase,Price,Sub,Category FROM Inventory_stock WHERE Bookid IN (SELECT Bookid FROM Book_req_stu WHERE Bookid='{
                        x[1]}')")
                myresult1 = mycursor.fetchall()
            except BaseException:
                messagebox.showerror("Data Not Found")
                top2.destroy()
                continue

            list_data = []

            for z in myresult1:
                list_data = list(z)

            for o in range(min(len(x), len(columns))):
                y = x[o]
                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
                Entry_stored.append(text)

            def Approve(a, b, c):
                try:
                    mycursor.execute(
                        f"INSERT INTO Book_list_stu VALUES('{c}','{
                            list_data[0]}','{
                            list_data[1]}','{
                            list_data[2]}','{
                            list_data[3]}','{
                            list_data[4]}','{
                            list_data[5]}','{
                                list_data[6]}','{
                                    list_data[7]}','{
                                        list_data[8]}')")
                    mycursor.execute(
                        f"DELETE FROM Book_req_stu WHERE Studentname='{c}'"
                    )
                    mydb.commit()
                    for y in a:
                        y.destroy()
                    for button in b:
                        button.destroy()
                except BaseException:
                    messagebox.showerror(
                        "Database Error", "Error processing approval.")

            def Reject(a, b, c):
                try:
                    for y in a:
                        mycursor.execute(
                            f"DELETE FROM Book_req_stu WHERE Studentname='{c}'"
                        )
                        mydb.commit()
                        y.destroy()
                    for button in b:
                        button.destroy()
                except BaseException:
                    messagebox.showerror(
                        "Database Error", "Error processing rejection."
                    )

            b1 = Button(
                top2,
                text="Approve",
                width=20,
                height=1,
                command=lambda e=Entry_stored,
                b=Buttons,
                n=name: Approve(
                    e,
                    b,
                    n),
            )
            b1.place(x=x_positions[o] + 80, y=40 + i * 30)
            Buttons.append(b1)
            b2 = Button(
                top2,
                text="Reject",
                width=20,
                height=1,
                command=lambda e=Entry_stored,
                b=Buttons,
                n=name: Reject(
                    e,
                    b,
                    n),
            )
            b2.place(x=x_positions[o] + 220, y=40 + i * 30)
            Buttons.append(b2)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Stock_update_req():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("300x500+575+240")
        top2.title("Staff Apply")

        labels = [
            "BOOKNAME:",
            "AUTHORNAME:",
            "PAGES:",
            "PUBLISHER:",
            "PURCHASE DATE:",
            "PRICE:",
            "COPIES:",
            "SUBJECT:",
            "CATEGORY:",
        ]
        i = 0
        for x in labels:
            tkinter.Label(top2, text=x).place(x=10, y=20 + i)
            i += 40

        textfields = [
            "BOOKNAME",
            "AUTHORNAME",
            "PAGES",
            "PUBLISHER",
            "PURCHASE DATE",
            "PRICE",
            "COPIES",
            "SUBJECT",
            "CATEGORY",
        ]
        entries = []
        i = 0
        for x in enumerate(textfields):
            entry = tkinter.Entry(top2, width=20)
            entry.place(x=100, y=20 + i)
            entries.append(entry)
            i += 40

        def Submit_staff_reg():
            try:
                mycursor = mydb.cursor()
                values = [entry.get() for entry in entries]

                mycursor.execute("")

                mycursor.execute(
                    f"INSERT INTO Stock_update_req VALUES ('{
                        values[0]}', '{
                        values[1]}', '{
                        values[2]}', '{
                        values[3]}' ,'{
                        values[4]}' ,'{
                            values[5]}',{
                                values[6]},'{
                                    values[7]}','{
                                        values[8]}')")

                mydb.commit()
                top2.destroy()
            except BaseException:
                messagebox.showerror(
                    "Database Error", "Error submitting stock update request."
                )

        Button(
            top2,
            text="Submit",
            width=20,
            height=1,
            command=Submit_staff_reg).place(
            x=30,
            y=20 + i)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Update_fine():
    pass


def Student_reg():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("300x500+575+240")
        top2.title("Staff Apply")

        labels = [
            "Studentname:",
            "Age:",
            "Address:",
            "Stream_Enrolled:",
            "Class:",
            "Mobile:",
            "Email:",
            "Username:",
            "UserPassword:",
        ]
        i = 0
        for x in labels:
            tkinter.Label(top2, text=x).place(x=10, y=20 + i)
            i += 40

        textfields = [
            "Studentname",
            "Age",
            "Address",
            "Stream_Enrolled",
            "Class",
            "Mobile",
            "Email",
            "Username",
            "UserPassword",
        ]
        entries = []
        i = 0
        for x in enumerate(textfields):
            entry = tkinter.Entry(top2, width=20)
            entry.place(x=100, y=20 + i)
            entries.append(entry)
            i += 40

        def Submit_student_reg():
            try:
                mycursor = mydb.cursor()
                values = [entry.get() for entry in entries]

                mycursor.execute(
                    f"INSERT INTO Student_reg VALUES ('{
                        values[0]}', '{
                        values[1]}', '{
                        values[2]}', '{
                        values[3]}' ,'{
                        values[4]}' ,'{
                            values[5]}','{
                                values[6]}','{
                                    values[7]}','{
                                        values[8]}')")
                mydb.commit()
                top2.destroy()
            except BaseException:
                messagebox.showerror(
                    "Database Error",
                    "Error submitting student registration data.")

        Button(
            top2, text="Submit", width=20, height=1, command=Submit_student_reg
        ).place(x=30, y=20 + i)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


global username
username = None


def Student_login():
    try:

        def check():
            try:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT Username,UserPassword FROM Users")
                myresult = mycursor.fetchall()
                global username
                username = user.get()
                password = passw.get()
                login = 0
                for db_username, db_pass in myresult:
                    if username == db_username and password == db_pass:
                        login = 1
                        break
                if login == 1:
                    messagebox.showinfo(
                        "Login Success", "Username and password are correct!"
                    )
                    top1.destroy()
                    student()
                else:
                    messagebox.showerror(
                        "Login Error", "Incorrect username or password."
                    )
                    top1.destroy()
            except BaseException:
                messagebox.showerror("Database Error", "Error during login.")

        top1 = tkinter.Toplevel()
        top1.geometry("200x120+600+250")
        top1.title("Login")
        user_label = Label(top1, text="Username:")
        user_label.place(x=10, y=10)
        pass_label = Label(top1, text="Password:")
        pass_label.place(x=10, y=50)
        user = tkinter.Entry(top1, width=15)
        user.place(x=80, y=10)
        passw = tkinter.Entry(top1, width=15, show="*")
        passw.place(x=80, y=50)
        login = Button(top1, text="Login", command=check, width=5, height=1)
        login.place(x=60, y=80)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Book_list_stu():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1300x500")
        top2.title("Stock Panel")
        mycursor = mydb.cursor()

        global username

        mycursor.execute(
            f"SELECT Bookid,BOOKNAME,Authorname,Pages,Publications,Date_of_purchase,Price,Sub,Category FROM Book_list_stu WHERE Studentname IN (SELECT Studentname FROM Users WHERE Username='{username}')"
        )
        myresult = mycursor.fetchall()

        columns = [
            ("Bookid", 10),
            ("Bookname", 25),
            ("Authorname", 15),
            ("Pages", 10),
            ("Publications", 25),
            ("Date of Publication", 20),
            ("Price", 10),
            ("Subject", 15),
            ("Category", 15),
        ]

        x_positions = []
        current_x = 9
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):
            for o in range(min(len(x), len(columns))):
                y = x[o]
                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
    except BaseException:
        messagebox.showerror("Database Error", "Error fetching book list.")


def student_select():
    Harman.withdraw()
    try:
        top1 = tkinter.Toplevel()
        top1.geometry("200x120+600+250")
        top1.title("Select an option")

        def login_process():
            Student_login()
            top1.destroy()

        def Apply_process():
            Student_reg()
            top1.destroy()

        buttons = [("Login", login_process), ("Apply", Apply_process)]
        i = 0
        for x, (text, cmd) in enumerate(buttons):
            Button(top1, text=text, command=cmd, width=20, height=2).place(
                x=30, y=15 + i
            )
            i += 40
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def student():
    try:
        top1 = tkinter.Toplevel()
        top1.geometry("300x350+575+240")
        top1.title("Student Panel")

        i = 0
        buttons = [
            ("REQUEST FOR ALLOCATION", Book_request),
            ("RETURN BOOK", Book_return_stu),
            ("SEARCH BOOK", Book_search),
            ("FINE PAYMENT", Pay_fine),
            ("BOOK LIST", Book_list_stu),
        ]
        for x, (text, cmd) in enumerate(buttons):
            Button(top1, text=text, command=cmd, width=20, height=2).place(
                x=80, y=15 + i
            )
            i += 70
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Book_request():
    try:
        top1 = tkinter.Toplevel()
        top1.geometry("300x300+575+240")
        top1.title("Book Allocation Request")

        Textfields = ["Studentname", "Bookid", "Bookname", "Time"]
        i = 0
        entries = []
        for x in enumerate(Textfields):
            entry = tkinter.Entry(top1, width=20)
            entry.place(x=100, y=20 + i)
            entries.append(entry)
            i += 40

        def Submit_stu():
            try:
                mycursor = mydb.cursor()
                values = [entry.get() for entry in entries]

                mycursor.execute(
                    f"""INSERT INTO Book_req_stu SELECT Studentname, '{
                        values[1]}', '{
                        values[2]}','{
                        values[3]}'FROM Users WHERE Username='{username}'""")
                mydb.commit()
                top1.destroy()
            except BaseException:
                messagebox.showerror(
                    "Database Error",
                    "Error submitting book request.")

        labels = ["STUDENTNAME:", "BOOKID:", "BOOKNAME:", "TIME PERIOD:"]

        i = 0
        for x in labels:
            tkinter.Label(top1, text=x).place(x=10, y=20 + i)
            i += 40

        Button(
            top1,
            text="Submit",
            command=Submit_stu,
            width=20,
            height=2).place(
            x=50,
            y=180)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Book_return_stu():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1300x500")
        top2.title("Stock Panel")
        mycursor = mydb.cursor()

        global username

        def Return_book(a, c):
            try:
                mycursor = mydb.cursor()
                for x in a:
                    x.destroy()
                global username
                mycursor.execute(
                    f"DELETE FROM Book_list_stu WHERE Bookid ='{bookid}' AND Studentname IN (SELECT Studentname FROM Users WHERE Username='{username}')")
                mydb.commit()
                for m in c:
                    m.destroy()
            except BaseException:
                messagebox.showerror("Database Error", "Error returning book.")

        mycursor.execute(
            f"SELECT Bookid,BOOKNAME,Authorname,Pages,Publications,Date_of_purchase,Price,Sub,Category FROM Book_list_stu WHERE Studentname IN (SELECT Studentname FROM Users WHERE Username='{username}')"
        )
        myresult = mycursor.fetchall()

        columns = [
            ("Bookid", 10),
            ("Bookname", 25),
            ("Authorname", 15),
            ("Pages", 10),
            ("Publications", 25),
            ("Date of Publication", 20),
            ("Price", 10),
            ("Subject", 15),
            ("Category", 15),
        ]

        x_positions = []
        current_x = 9
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):

            Entry_stored = []
            Buttons = []

            for o in range(min(len(x), len(columns))):
                y = x[o]

                global bookid

                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
                Entry_stored.append(text)
                bookid = x[0]
            b1 = Button(
                top2,
                text="Return",
                command=lambda e=Entry_stored, c=Buttons: Return_book(e, c),
            )
            b1.place(x=x_positions[o] + 120, y=40 + i * 30)
            Buttons.append(b1)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def Pay_fine():
    try:
        print()
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


def stock_check():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1300x500")
        top2.title("Stock Panel")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM Inventory_stock")
        myresult = mycursor.fetchall()

        columns = [
            ("Bookid", 10),
            ("Bookname", 25),
            ("Authorname", 15),
            ("Pages", 10),
            ("Publications", 25),
            ("Date of Publication", 20),
            ("Price", 10),
            ("Copies", 10),
            ("Subject", 15),
            ("Category", 15),
        ]

        x_positions = []
        current_x = 10
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):
            for o in range(min(len(x), len(columns))):
                y = x[o]
                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
    except BaseException:
        messagebox.showerror("Database Error", "Error fetching stock data.")


def staff_list():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1000x500")
        top2.title("Staff List")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM employees")
        myresult = mycursor.fetchall()

        columns = [
            ("Empid", 10),
            ("Username", 25),
            ("Mobile no.", 15),
            ("Email id", 20),
            ("User password", 25),
            ("Designation", 10),
            ("Address", 10),
        ]

        x_positions = []
        current_x = 7
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):
            for o in range(min(len(x), len(columns))):
                y = x[o]
                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
    except BaseException:
        messagebox.showerror("Database Error", "Error fetching staff list.")


def student_list():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1300x500")
        top2.title("Student List")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM Users")
        myresult = mycursor.fetchall()

        columns = [
            ("Roll no.", 10),
            ("Student Name", 25),
            ("Age", 15),
            ("Address", 10),
            ("Stream_Enrolled", 25),
            ("class", 10),
            ("Mobile no.", 10),
            ("Email id", 10),
            ("Username", 15),
            ("User password", 20),
        ]

        x_positions = []
        current_x = 10
        for _, width in columns:
            x_positions.append(current_x)
            current_x += width * 8

        for o, (header, _) in enumerate(columns):
            label = tkinter.Label(top2, text=header, width=columns[o][1])
            label.place(x=x_positions[o], y=10)

        for i, x in enumerate(myresult):
            for o in range(min(len(x), len(columns))):
                y = x[o]
                text = tkinter.Entry(top2, width=columns[o][1])
                text.place(x=x_positions[o], y=40 + i * 30)
                text.insert(END, str(y))
                text.config(state=DISABLED)
    except BaseException:
        messagebox.showerror("Database Error", "Error fetching student list.")


def Book_search():
    try:
        top2 = tkinter.Toplevel()
        top2.geometry("1500x500")
        top2.title("Search Panel")
        mycursor = mydb.cursor()

        search_entry = tkinter.Entry(top2, width=30)
        search_entry.place(x=200, y=10)

        selected_criteria = tkinter.StringVar(value="None")
        search_result = []

        def search_by():
            try:
                for prev_search in search_result:
                    prev_search.destroy()
                search_result.clear()

                criteria = selected_criteria.get()
                search_term = search_entry.get()
                mycursor.execute(
                    f"SELECT * FROM Inventory_stock WHERE {criteria} LIKE %s",
                    ("%" + search_term + "%",),
                )
                myresult = mycursor.fetchall()

                columns = [
                    ("Bookid", 10),
                    ("Bookname", 25),
                    ("Authorname", 15),
                    ("Pages", 10),
                    ("Publications", 20),
                    ("Date of Publication", 15),
                    ("Price", 5),
                    ("Copies", 5),
                    ("Subject", 10),
                    ("Category", 10),
                ]

                x_positions = []
                current_x = 10
                for _, width in columns:
                    x_positions.append(current_x)
                    current_x += width * 8

                for o, (header, _) in enumerate(columns):
                    label = tkinter.Label(
                        top2, text=header, width=columns[o][1])
                    label.place(x=x_positions[o] + 200, y=80)

                for i, row in enumerate(myresult):
                    for o in range(min(len(row), len(columns))):
                        y = row[o]
                        text = tkinter.Entry(top2, width=columns[o][1])
                        text.place(x=x_positions[o] + 200, y=110 + i * 30)
                        text.insert(END, str(y))
                        text.config(state=DISABLED)
                        search_result.append(text)
            except BaseException:
                messagebox.showerror(
                    "Database Error", "Error performing search.")

        search_options = [
            ("Search by name", "BOOKNAME"),
            ("Search by Bookid", "Bookid"),
            ("Search by Authorname", "Authorname"),
            ("Search by Pages", "Pages"),
            ("Search by Publisher", "Publications"),
            ("Search by Date of Purchase", "Date_of_purchase"),
            ("Search by Price", "Price"),
            ("Search by Copies", "Copies"),
            ("Search by Subject", "Sub"),
            ("Search by Category", "Category"),
        ]

        for i, (text, criteria) in enumerate(search_options):
            tkinter.Radiobutton(
                top2,
                text=text,
                variable=selected_criteria,
                value=criteria,
                command=search_by,
            ).place(x=10, y=40 + i * 30)
    except BaseException:
        messagebox.showerror("Error", "An unexpected error occurred.")


b1 = Button(Harman, text="ADMIN", command=Admin_login, width=10, height=2)
b1.place(x=80, y=20)
b2 = Button(Harman, text="STAFF", command=staff_select, width=10, height=2)
b2.place(x=80, y=80)
b3 = Button(Harman, text="STUDENT", command=student_select, width=10, height=2)
b3.place(x=80, y=140)

Harman.mainloop()
