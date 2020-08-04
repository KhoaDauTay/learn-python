width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
copoun = input("Do you have copoun ? yes or no  ")


def sumary(width, height, copoun):
    s = width * height
    count = s * 20
    if copoun == "Yes" or copoun =="yes":
        values = int(input("Enter the % copoun: "))
        sum = count - (values * count // 100)
        return "The total bill is: %s" %sum
    else:
        return "The total bill is: %s" %count

print(sumary(width, height, copoun))
