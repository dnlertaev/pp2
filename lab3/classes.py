#1
class StringManipulator:
    
    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())
        
        

#2
class Shape:
    
    def area(self):
        return 0

class Square(Shape):
    
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
    

#3
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    

#4
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    

#5
class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted")
        else:
            print("Insufficient funds")
            
            

#6
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

filtered_primes = filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers)

print(list(filtered_primes))

