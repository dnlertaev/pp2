#math - математический модуль для представления каких либо математических значений

#1
import math

def degree_to_radians(degree):
    radians = degree * (math.pi / 180)
    return radians

degrees = int(input())

radians = degree_to_radians(degrees)

print(f"{degrees} equal to {radians} radians.")



#2
height = int(input())

first_value = int(input())

second_value = int(input())

area = 1/2 * (first_value + second_value) * height

print(area)



#3
import math

number_of_sides = int(input())

length_of_a_side = int(input())

area_of_the_polygon = (number_of_sides * length_of_a_side**2) / (4 * math.tan(math.pi / number_of_sides))

print(area_of_the_polygon)



#4
Length_of_base = int(input())

Height_of_parallelogram = int(input())


area = Length_of_base * Height_of_parallelogram

print(area)