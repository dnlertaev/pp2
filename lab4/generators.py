def squares(n):
    
    for i in range(1, n + 1):
        
        yield i ** 2

x = int(input())

generator = squares(x)

for sq in generator:
    
    print(sq, end=" ")
    


#2
def even_numbers_generator(N):
    
    for i in range(N + 1):
        
        if i % 2 == 0:
            
            yield i

n = int(input("Enter the value of n: "))

even_numbers = even_numbers_generator(n)

print("Even numbers between 0 and", n, ":", end=" ")

for num in even_numbers:
    
    print(num, end=", ")