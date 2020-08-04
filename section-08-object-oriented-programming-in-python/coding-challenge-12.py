class Computer:


    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def getspecs(self):
        self.price  = input('Enter the price: ')
        self.brand  = input('Enter the brand: ')
    def displayspec(self):
        print(self.price)
        print(self.brand)
class Desktop(Computer):
    

    def __init__(self, price, brand,location):
        super().__init__(price, brand)
        self.location = location
    
    def getspecs(self):
        super().getspecs()
        self.location = input('Enter the location')
    def displayspec(self):
        super().displayspec()
        print(self.location)
class Laptop(Computer):
    

    def __init__(self, price, brand,batery):
        super().__init__(price, brand)
        self.batery = batery
    
    def getspecs(self):
        super().getspecs()
        self.batery = input('Enter the batery')
    def displayspec(self):
        super().displayspec()
        print(self.batery)
desktop_1 = Desktop(0,'','')
desktop_1.getspecs()
desktop_1.displayspec()

laptop_1 = Laptop(0,'','')
laptop_1.getspecs()
laptop_1.displayspec()
