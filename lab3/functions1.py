#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_value = int(input("Введите количество граммов: "))

ounces_result = grams_to_ounces(grams_value)

print(f"{grams_value} граммов равно {ounces_result} унций.")




#2
def fahrenheit_to_celsius(F):
    C = (5 / 9) * (F - 32)
    return C

F_value = int(input("Введите temp по Фаренгейту: "))

С_result = fahrenheit_to_celsius(F_value)

print(f"{F_value} градусов по Фаренгейту равно {С_result} градусов по цельсию.")




#3
def solve(numheads, numlegs):
    
    #количество кур и кроликов
    
    num_chickens = 0
    
    num_rabbits = 0
    
    #подсчет количества кур и кроликов
    
    for chickens in range(numheads + 1):
        
        rabbits = numheads - chickens
    
        total_legs = 2 * chickens + 4 * rabbits
    
        if total_legs == numlegs:
        
            return chickens, rabbits
    
    
    return None, None


numheads = 35

numlegs = 94

chickens, rabbits = solve (numheads, numlegs)


if chickens is not None and rabbits is not None:
    
    print("Количество кур: ", chickens)
    
    print("Количество кроликов: ", rabbits)
    
else: 
    
    print("Error")




#4
def is_prime(n):

    if n < 2:
        
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
    
        if n % i == 0:
    
            return False
    
    return True

def filter_prime(numbers):

    return [num for num in numbers if is_prime(num)]

numbers = [int(x) for x in input("Введите числа: ").split()]

prime_numbers = filter_prime(numbers)
    
print("Простые числа: ", prime_numbers)




#6
def reversed_string(sentence):
    
    words = sentence.split()
    
    reversed_sentence = ' '.join(reversed(words))
    
    return reversed_sentence

sentence = input("Введите предложение: ")

reversed_sentence = reversed_string(sentence)

print(reversed_sentence)




#7
def has_33(nums):
    
    for i in range(len(nums) - 1):
        
        if nums[i] == 3 and nums[i + 1] == 3 :
            
            return True
    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))




#8
def spy_game(nums):

    last_zero_index = None

    for num in nums:
        
        if num == 0:

            last_zero_index = nums.index(num)
            
        elif num == 7 and last_zero_index is not None:

            if nums[last_zero_index+1:].count(0) >= 1:
                
                return True

    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))




#9
def spheres_volume(radius):
    
    volume = (4/3) * 3.14 * radius ** 3
    
    return volume

radius = int(input("Введите радиус: "))

volume = spheres_volume(radius)

print(volume)




#10
def unique_elements(input_list):
    
    unique_list = []
    
    for element in input_list:
        
        if element not in unique_list:
            
            unique_list.append(element)
            
    return unique_list


input_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
result_list = unique_elements(input_list)
print(result_list)




#11
def is_palindrome(word):
    
    word = word.replace(" ", "").lower()

    return word == word[::-1]




#12
def histogram(nums):
    
    for num in nums:
        
        print('*' * num)

histogram([4, 9, 7])




#13
import random

def guess_the_number():
    
    print("Guess the number")
    
    name = input("Hello! What is your name?\n")
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    
    guesses_taken = 0
    
    while True:
        
        guess = int(input("Take a guess.\n"))
        
        guesses_taken += 1
        
        if guess < number:
            
            print("Your guess is too low.")
            
        elif guess > number:
            
            print("Your guess is too high.")
            
        else:
            
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            
            break
        
guess_the_number()

