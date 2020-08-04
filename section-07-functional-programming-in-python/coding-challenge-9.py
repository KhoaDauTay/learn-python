def student_discount(price):
    price = price - (price * 10) / 100
    return price
 
def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice
 
selling_price = 100
print(additional_discount(student_discount(selling_price)))