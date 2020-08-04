from tkinter import *

def taxamount(price, tax):
    cost = price * (tax/100)
    totalcost = price + cost
    return totalcost

def butter():
    entryField.delete(0,'end') #Clears the entire entry field from index 0 to 'end
    price = int(pricefield.get())
    age = int(agefield.get())
    if age <= 60:
        if price <= 20000:
            tax = 0
            amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        elif price >= 20001 and price < 50000:
            tax = 20
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        elif price >= 50001 and price < 100000:
            tax = 30
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        else:
            tax = 40
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
    else:
        if price <= 20000:
            tax = 0
            amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        elif price >= 20001 and price < 50000:
            tax = 10
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        elif price >= 50001 and price < 100000:
            tax = 20
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))
        else:
            tax = 30
            amount = amount = taxamount(price, tax)
            entryer.set("The total cost after tip is: " + str(amount))




root = Tk()

root.title("Milos Tax Calculator")
root.resizable(1,0)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

entryer = StringVar()
entryField = Entry(root, textvariable=entryer,background="LightYellow2",foreground="blue4",justify=CENTER)
entryField.grid(row=0,column=0,columnspan=2,sticky=W+E)
entryField.columnconfigure(0,weight=1)

labelage = Label(root, text="Age",background="blue4",foreground="PaleTurquoise1")
labelage.grid(row=1,column=0, sticky=E)
labelprice = Label(root, text="Price",background="blue4",foreground="PaleTurquoise1")
labelprice.grid(row=2,column=0, sticky=E)


agefield = Entry(root,background="SkyBlue2",foreground="blue4")
agefield.grid(row=1,column=1,sticky=W)
pricefield = Entry(root,background="SkyBlue2",foreground="blue4")
pricefield.grid(row=2,column=1,sticky=W)


button = Button(root, text="Find total cost", command=butter)
button.grid(row=3, columnspan=2)


root.mainloop()