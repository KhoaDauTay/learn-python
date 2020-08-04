def taxamount(price, tax):
    cost = price * (tax/100)
    totalcost = price + cost
    return totalcost

def butter():

    price = int(input("Enter the salary in year: "))
    age = int(input("Enter the your age: "))
    if age <= 60:
        if price <= 20000:
            tax = 0
            amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        elif price >= 20001 and price < 50000:
            tax = 20
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        elif price >= 50001 and price < 100000:
            tax = 30
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        else:
            tax = 40
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
    else:
        if price <= 20000:
            tax = 0
            amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        elif price >= 20001 and price < 50000:
            tax = 10
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        elif price >= 50001 and price < 100000:
            tax = 20
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
        else:
            tax = 30
            amount = amount = taxamount(price, tax)
            print("The total cost after tip is: " + str(amount))
butter()