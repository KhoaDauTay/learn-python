import tkinter as tk
from functools import partial


def call_result(label_result, n1, n2, n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    result = int(num1) * int(num2) * 20
    label_result.config(text="Result = %d" % result)
    return


root = tk.Tk()
root.geometry('200x200')

root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()

labelNum1 = tk.Label(root, text="Width").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="Height").grid(row=2, column=0)

labelNum3 = tk.Label(root, text="Copoun").grid(row=3, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)

call_result = partial(call_result, labelResult, number1, number2, number3)

buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=4, column=0)

root.mainloop() 