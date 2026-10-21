import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk

harry = tkinter.Tk()
harry.geometry("300x500")

f = font.Font(family='italic', size=15)
g = font.Font(family='italic', size=40)

text = tkinter.Entry(harry, width=15, font=g)
text.pack(padx=10, pady=10)


def Hex():
    harry.geometry("460x500")
    A = tkinter.Button(
        harry,
        text="A",
        font=f,
        command=one1).place(
        x=290,
        y=100,
        height=70,
        width=70)
    B = tkinter.Button(
        harry,
        text="B",
        font=f,
        command=two1).place(
        x=360,
        y=100,
        height=70,
        width=70)
    C = tkinter.Button(
        harry,
        text="C",
        font=f,
        command=three1).place(
        x=290,
        y=170,
        height=70,
        width=70)
    D = tkinter.Button(
        harry,
        text="D",
        font=f,
        command=four1).place(
        x=360,
        y=170,
        height=70,
        width=70)
    E = tkinter.Button(
        harry,
        text="E",
        font=f,
        command=five1).place(
        x=290,
        y=240,
        height=70,
        width=70)
    F = tkinter.Button(
        harry,
        text="F",
        font=f,
        command=six1).place(
        x=360,
        y=240,
        height=70,
        width=70)


def equal1():
    try:
        result = eval(text.get())
        text.delete(0, END)
        text.insert(END, str(result))
    except BaseException:
        text.delete(0, END)
        text.insert(END, "Error")


def one1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(1))


def two1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(2))


def three1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(3))


def four1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(4))


def five1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(5))


def six1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(6))


def seven1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(7))


def eight1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(8))


def nine1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(9))


def zero1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + str(0))


def add1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + '+')


def sub1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + '-')


def mul1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + '*')


def div1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + '/')


def AC():
    text.delete(0, END)


def mplus1():
    pass  # You can implement memory functionality here


def mminus1():
    pass  # You can implement memory functionality here


def dele1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x[:-1])


def per1():
    x = text.get()
    text.delete(0, END)
    text.insert(END, x + '%')


def scientific(event):
    harry.geometry("460x500")
    sin = tkinter.Button(
        harry,
        text="Sin",
        font=f,
        command=one1).place(
        x=290,
        y=100,
        height=70,
        width=70)
    cos = tkinter.Button(
        harry,
        text="Cos",
        font=f,
        command=two1).place(
        x=360,
        y=100,
        height=70,
        width=70)
    tan = tkinter.Button(
        harry,
        text="Tan",
        font=f,
        command=three1).place(
        x=290,
        y=170,
        height=70,
        width=70)
    expo = tkinter.Button(
        harry,
        text="X^y",
        font=f,
        command=four1).place(
        x=360,
        y=170,
        height=70,
        width=70)
    root = tkinter.Button(
        harry,
        text="X^1/2",
        font=f,
        command=five1).place(
        x=290,
        y=240,
        height=70,
        width=70)
    square = tkinter.Button(
        harry,
        text="X^2",
        font=f,
        command=six1).place(
        x=360,
        y=240,
        height=70,
        width=70)
    cube = tkinter.Button(
        harry,
        text="X^3",
        font=f,
        command=seven1).place(
        x=290,
        y=310,
        height=70,
        width=70)
    log = tkinter.Button(
        harry,
        text="Log",
        font=f,
        command=one1).place(
        x=360,
        y=310,
        height=70,
        width=70)


frame = Frame(harry)
frame.pack()
frame.place(x=80, y=470)

langs = ["Simple", "Scientific", "Hex"]

Combo = ttk.Combobox(frame, values=langs)
Combo.pack(padx=5, pady=5)
Combo.set("Simple")
Combo.bind("<<ComboboxSelected>>", scientific)
Combo.bind("<<ComboboxSelected>>", Hex)


one = tkinter.Button(
    harry,
    text="1",
    font=f,
    command=one1).place(
        x=10,
        y=100,
        height=70,
    width=70)
two = tkinter.Button(
    harry,
    text="2",
    font=f,
    command=two1).place(
        x=80,
        y=100,
        height=70,
    width=70)
three = tkinter.Button(
    harry,
    text="3",
    font=f,
    command=three1).place(
        x=150,
        y=100,
        height=70,
    width=70)
four = tkinter.Button(
    harry,
    text="4",
    font=f,
    command=four1).place(
        x=220,
        y=100,
        height=70,
    width=70)
five = tkinter.Button(
    harry,
    text="5",
    font=f,
    command=five1).place(
        x=10,
        y=170,
        height=70,
    width=70)
six = tkinter.Button(
    harry,
    text="6",
    font=f,
    command=six1).place(
        x=80,
        y=170,
        height=70,
    width=70)
seven = tkinter.Button(
    harry,
    text="7",
    font=f,
    command=seven1).place(
        x=150,
        y=170,
        height=70,
    width=70)
eight = tkinter.Button(
    harry,
    text="8",
    font=f,
    command=eight1).place(
        x=220,
        y=170,
        height=70,
    width=70)
nine = tkinter.Button(
    harry,
    text="9",
    font=f,
    command=nine1).place(
        x=10,
        y=240,
        height=70,
    width=70)
zero = tkinter.Button(
    harry,
    text="0",
    font=f,
    command=zero1).place(
        x=80,
        y=240,
        height=70,
    width=70)
add = tkinter.Button(
    harry,
    text="+",
    font=f,
    command=add1).place(
        x=150,
        y=240,
        height=70,
    width=70)
sub = tkinter.Button(
    harry,
    text="-",
    font=f,
    command=sub1).place(
        x=220,
        y=240,
        height=70,
    width=70)
mul = tkinter.Button(
    harry,
    text="*",
    font=f,
    command=mul1).place(
        x=10,
        y=310,
        height=70,
    width=70)
div = tkinter.Button(
    harry,
    text="/",
    font=f,
    command=div1).place(
        x=80,
        y=310,
        height=70,
    width=70)
clear = tkinter.Button(
    harry,
    text="C",
    font=f,
    command=AC).place(
        x=150,
        y=310,
        height=70,
    width=70)
mplus = tkinter.Button(
    harry,
    text="M+",
    font=f,
    command=mplus1).place(
        x=220,
        y=310,
        height=70,
    width=70)
mminus = tkinter.Button(
    harry,
    text="M-",
    font=f,
    command=mminus1).place(
        x=10,
        y=380,
        height=70,
    width=70)
dele = tkinter.Button(
    harry,
    text="DEL",
    font=f,
    command=dele1).place(
        x=80,
        y=380,
        height=70,
    width=70)
equal = tkinter.Button(
    harry,
    text="=",
    font=f,
    command=equal1).place(
        x=150,
        y=380,
        height=70,
    width=70)
per = tkinter.Button(
    harry,
    text="%",
    font=f,
    command=per1).place(
        x=220,
        y=380,
        height=70,
    width=70)

harry.mainloop()
