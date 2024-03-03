#1
import math

x = input()

list = [int(n) for n in x.split()]

mult = math.prod(list)

print(mult)



#2
def number_of_upper_lower(string):

    upper_count = sum(1 for char in string if char.isupper())

    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count

str = input("Enter a string: ")

upper_count, lower_count = number_of_upper_lower(str)

print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)



#3
def is_palindrome(s):
    
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    return s == s[::-1]

str = input("Enter a string: ")

if is_palindrome(str):
    
    print("string is a palindrome.")

else:

    print("string is not a palindrome.")
    
    

#4
import time
import math

def delayed_sqrt(number, milliseconds):
   
    time.sleep(milliseconds / 1000)

    sqrt_result = math.sqrt(number)

    return sqrt_result

input_number = 25100
wait_time = 2123

result = delayed_sqrt(input_number, wait_time)

print(f"Square root of {input_number} after {wait_time} milliseconds is {result}")



#5
def all_true(tup):

    return all(element for element in tup)

sample = (True, True, False, True)

result = all_true(sample)

print("All elements of the tuple are True:", result)

