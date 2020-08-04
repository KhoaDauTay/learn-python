x =list(x for x in range(10,20) if x % 2 == 0)
print(x)
def dis_cout(price):
    return price - (price * 10) / 100
new_price = map(dis_cout,x)
print(list(new_price))