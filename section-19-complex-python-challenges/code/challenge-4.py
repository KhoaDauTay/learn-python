class Product:
    
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Product ID: {self.id}")
        print(f"Product Price: {self.price}")
        print(f"Product Quantity: {self.quantity}")

    def edit_product(self):
        self.id = int(input("Edit Product ID: "))
        self.price = int(input("Edit Product Price: "))
        self.quantity = int(input("Edit Product Quantity: "))

product_object = [("ID", "Price", "Quantity"),]

def program():
    print("Menu management command: \n"
          "1. Add new Product \n"
          "2. Delete product with id \n"
          "3. Show product \n"
          "4. Edit product \n"
          "5. Exit Program")
    choose = input(" Enter the choice: ")
    if choose == "1":
        num = int(input("Number of products you want to import: "))
        for i in range(0,num):
            id = int(input("Enter Product ID: "))
            price = int(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product_object.append(Product(id, price, quantity))
        program()
    elif choose == "2":
        id = int(input("Enter the Product ID for delete: "))
        del product_object[id]
        program()
    elif choose == "3":
        for i in range(1, len(product_object)):
            print(product_object[i].show_info())
        program()
    elif choose == "4":
        id = int(input("Enter the Product ID for edit: "))
        product_object[id].edit_product()
        program()
    elif choose == "5":
        exit()
    else:
        print("Error command, Try again !!!")
        program()
program()