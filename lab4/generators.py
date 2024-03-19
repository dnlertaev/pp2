# yield - возвращает значение, сохраняя состояние функции, позволяя ей продолжить выполнение с места, где она была приостановлена

#1
def squares(n):
    
    for i in range(1, n + 1):
        
        yield i ** 2

x = int(input())

generator = squares(x)

for sq in generator:
    
    print(sq, end=" ")[]
    


#2
def even_numbers_generator(N):
    
    for i in range(N + 1):
        
        if i % 2 == 0:
            
            yield i

n = int(input("value of n: "))

even_numbers = even_numbers_generator(n)

print("Even numbers between 0 and", n, ":", end=" ")

for num in even_numbers:
    
    print(num, end=", ")
    
    
    
#3
def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        
        if i % 3 == 0 and i % 4 == 0:
        
            yield i


start_range = 0

end_range = int(input())

numbers_divisible = divisible_by_3_and_4(start_range, end_range)

print("Numbers divisible by 3 and 4 between", start_range, "and", end_range, ":")

for num in numbers_divisible:

    print(num, end=", ")
    
    
    
#4
def squares(a, b):
    
    for num in range(a, b + 1):
    
        yield num ** 2

a = int(input())

b = int(input())

print("squares of numbers from", a, "to", b, ":")

for square in squares(a, b):

    print(square)
    
    

#5
def countdown(n):
    
    while n >= 0:
        
        yield n
        
        n -= 1


n = int(input())

print("Countdown from", n, "to 0:")

for num in countdown(n):

    print(num)