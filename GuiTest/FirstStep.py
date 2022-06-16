#!/usr/bin/python3
import tkinter as tk

x = ""
add1 = 0
add2 = 0
ope = ""
res = ""
root = tk.Tk()
result = tk.Label(root, text="test")

def addNum(num):
    global ope
    if(ope != ""):
        print("invalid")
    else:
        global x
        x += num

def op(ope):
    global add1
    global x
    global operator
    operator = ope
    add1 = int(x)
    x = ""

def update():
    result.config(text=res)

def equals():
    global add2
    global x
    global res 
    add2 = int(x)
    x = ""
    res =  add1+add2
    update()
    print (add1, " + ", add2, " = ", res)


btn1 = tk.Button(
        text="1",
        width="5",
        height="5",
        command=lambda: addNum("1")
        )


btn2 = tk.Button(
        text="2",
        width="5",
        height="5",
        command=lambda: addNum("2")
        )
btn3 = tk.Button(
        text="3",
        width="5",
        height="5",
        command=lambda: addNum("3")
        )
btn4 = tk.Button(
        text="4",
        width="5",
        height="5",
        command=lambda: addNum("4")
        )
btn5 = tk.Button(
        text="5",
        width="5",
        height="5",
        command=lambda: addNum("5")
        )
btn6 = tk.Button(
        text="6",
        width="5",
        height="5",
        command=lambda: addNum("6")
        )
btn7 = tk.Button(
        text="7",
        width="5",
        height="5",
        command=lambda: addNum("7")
        )
btn8 = tk.Button(
        text="8",
        width="5",
        height="5",
        command=lambda: addNum("8")
        )

btn9 = tk.Button(
        text="9",
        width="5",
        height="5",
        command=lambda: addNum("9")
        )

btn0 = tk.Button(
        text="0",
        width="5",
        height="5",
        command=lambda: addNum("0")
        )

btnPlus = tk.Button(
        text="+",
        width="5",
        height="5",
        command=lambda: op("+")
        )

btnEq = tk.Button(
        text="=",
        width="5",
        height="5",
        command=equals
        )


btn0.grid(row=3, column = 1, sticky = tk.W, pady = 2)
btn1.grid(row=2, column = 0, sticky = tk.W, pady = 2)
btn2.grid(row=2, column = 1, sticky = tk.W, pady = 2)
btn3.grid(row=2, column = 2, sticky = tk.W, pady = 2)
btn4.grid(row=1, column = 0, sticky = tk.W, pady = 2)
btn5.grid(row=1, column = 1, sticky = tk.W, pady = 2)
btn6.grid(row=1, column = 2, sticky = tk.W, pady = 2)
btn7.grid(row=0, column = 0, sticky = tk.W, pady = 2)
btn8.grid(row=0, column = 1, sticky = tk.W, pady = 2)
btn9.grid(row=0, column = 2, sticky = tk.W, pady = 2)


btnPlus.grid(row=0, column = 3, sticky = tk.W, pady = 2)
btnEq.grid(row=1, column = 3, sticky = tk.W, pady = 2)
result.grid(row=4, column = 1, sticky = tk.W, pady = 2)

root.mainloop()
