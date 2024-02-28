#1
import re

def match_pattern(text):
    
    pattern = r'ab*'
    
    if re.fullmatch(pattern, text):
        
        return True
    
    else:
        
        return False

str = ["a", "ab", "abb", "abbb", "abc", "ac", "b"]

for string in str:
    
    if match_pattern(string):
        
        print(f"'{string}' matches")
        
    else:
        
        print(f"'{string}' does not match")
        


#2
import re

def match_pattern(text):
    
    pattern = r'ab{2,3}'
    
    if re.fullmatch(pattern, text):
        
        return True
    
    else:
        
        return False

str = ["ab", "abb", "abbb", "abbbb", "abc", "ac", "b"]

for string in str:
    
    if match_pattern(string):
        
        print(f"'{string}' matches")
        
    else:
        
        print(f"'{string}' does not match")



#3
import re

str = "Hello_world, how_are_you_doing_today?"

pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, str)

print(matches)



#4
import re

str = "I want to go to the Everest with my hiking bro Zhantu."

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, str)

print(matches)



#5
import re

def match_pattern(text):
    
    pattern = r'a.*b$'
    
    if re.fullmatch(pattern, text):
    
        return True
    
    else:
    
        return False

str = ["acb", "aab", "abb", "abc", "acb"]

for string in str:

    if match_pattern(string):

        print(f"'{string}' matchesn")

    else:

        print(f"'{string}' does not match")
        


#6
import re

str = "In the summer I will go to Big Almaty Peak."

pattern = r'[ ,.]'

replacement = ":"

new_str = re.sub(pattern, replacement, str)

print(new_str)



#7
def snake_to_camel(snake_str):
    
    components = snake_str.split('_')
    
    return ''.join(x.title() for x in components)

snake_case = "this_is_a_sample_snake_case_string"

camel_case = snake_to_camel(snake_case)

print(camel_case)



#8
import re

text = "ILoveToGoToTheMountains."

pattern = r'[A-Z][a-z]*'

matches = re.findall(pattern, text)

print(matches)



#9
import re

def insert_spaces(text):
    
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

camel_case = "ThisIsACamelCaseString"

result = insert_spaces(camel_case)

print(result)


#10
import re

def camel_to_snake(camel_str):
    
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_case = "ThisIsACamelCaseString"

snake_case = camel_to_snake(camel_case)

print(snake_case)