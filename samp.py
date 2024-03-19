def squares(a, b) :
    
    for i in range(a, b + 1) :
        
        yield i * i
    
a = 0

b = int(input())

for square in squares(a, b) :
    
    print(square, end=" ")
    
    

import re

str = "I go to Kbtu"

pattern = r'[ ]'

replacement = "-"

newstr = re.sub(pattern, replacement, str) #(вот это, заменить вот этим, вот здесь)

print(newstr)



import re

text = "ILoveToGoToTheMountains."

pattern = r'[A-Z][a-z]*'

matches = re.findall(pattern, text)

print(matches)



import datetime

x = datetime.datetime.now()

from datetime import timedelta

x0 = datetime - timedelta(days=1)

x1 = datetime + timedelta(days=1)

print(x0.strftime("%x"))

print(x1.strftime("%x"))



def squares(n) :
    
    for i in range(1, n + 1) :
        
        yield i**2
        
x = int(input)

generator = squares(x)

for square in generator :
    
    print(square, end=" ")
    
    
    
import re

str = "olzhas rakhat andrew"

pattern = r'[a]'

replacement = "b"

newstr = re.sub(pattern, replacement, str)

print(newstr)



def numbers(n) :
    
    for i in range(n + 1) :
        
        yield i
        
x = int(input())

for num in numbers(x) :
    
    print(num, end=" ")
    
    
    
import re

str = "banana, apple, grape"

pattern = r'[a]'

replacement = "o"

newstr = re.sub(pattern, replacement, str)

print(newstr)



# Открываем файл для добавления ('a' - append)
with open('example.txt', 'a') as f:
    f.write("\nolzhas loh")