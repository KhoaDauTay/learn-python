product = {
    'Meat':30,
    'Fish':25,
    'Noodle':45,
    'Vegetable':30,
    'Egg':10
}

new_pro = input('Enter the Name : ')
if new_pro in product:
    print(product.get(new_pro))
else:
    print('No Found')