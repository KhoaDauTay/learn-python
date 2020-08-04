class Number:

    def __init__(self,num):
        self.num = num

    def __mul__(self,other):
        return self.num + other.num

num_1 = Number(3)
num_2 = Number(4)
print(num_1 * num_2)