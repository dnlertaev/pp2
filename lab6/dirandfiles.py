#1
import os

def list_directories_files(path):
    
    print("Directories:")
    directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    print(directories)

    print("\nFiles:")
    files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
    print(files)

    print("\nAll Directories and Files:")
    all_items = os.listdir(path)
    print(all_items)

path = "/path/to/your/directory"

list_directories_files(path)



#2
import os

def check_path_access(path):
    
    if os.path.exists(path):
        
        print(f"Path '{path}' exists.")

        if os.access(path, os.R_OK):
            
            print(f"Path '{path}' is readable.")
 
        else:
 
            print(f"Path '{path}' is not readable.")

        if os.access(path, os.W_OK):
       
            print(f"Path '{path}' is writable.")
       
        else:
       
            print(f"Path '{path}' is not writable.")

        if os.access(path, os.X_OK):
            
            print(f"Path '{path}' is executable.")
 
        else:
 
            print(f"Path '{path}' is not executable.")

    else:
        
        print(f"Path '{path}' does not exist.")

path = "/path/to/your/directory_or_file"

check_path_access(path)



#3
import os

def analyze_path(path):

    if os.path.exists(path):

        print(f"Path '{path}' exists.")

        filename = os.path.basename(path)
        print(f"Filename: {filename}")

        directory = os.path.dirname(path)
        print(f"Directory: {directory}")

    else:
        
        print(f"Path '{path}' does not exist.")

path = input("Enter the path: ")

analyze_path(path)



#4
def count_lines(filename):
    
    try:
        
        with open(filename, 'r') as file:

            line_count = sum(1 for line in file)
           
            return line_count
    
    except FileNotFoundError:
  
        print(f"Error: File '{filename}' not found.")
  
        return -1

filename = input("Enter the name of the text file: ")

lines = count_lines(filename)

if lines != -1:

    print(f"The file '{filename}' has {lines} lines.")
    
    
    
#5
def write_list_to_file(filename, data):
   
    try:
        with open(filename, 'w') as file:
       
            for item in data:
       
                file.write(str(item) + '\n')
       
        print(f"List has been written to '{filename}' successfully.")
    
    except Exception as e:
      
        print(f"Error occurred while writing to file: {e}")

my_list = ['apple', 'banana', 'orange', 'grape']

filename = input("Enter the name of the file to write to: ")

write_list_to_file(filename, my_list)



#6
import string
import os

def generate_text_files():
    
    try:
        
        for letter in string.ascii_uppercase:
            
            filename = letter + ".txt"
           
            with open(filename, 'w') as file:
           
                pass
        
        print("Text files created successfully.")

    except Exception as e:

        print(f"Error occurred while creating text files: {e}")

generate_text_files()



#7
def copy_file(source_file, destination_file):
    
    try:
      
        with open(source_file, 'r') as source:
      
            with open(destination_file, 'w') as destination:
                
                destination.write(source.read())
        
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    
    except FileNotFoundError:
   
        print(f"Error: File '{source_file}' not found.")
   
    except Exception as e:
   
        print(f"Error occurred while copying file: {e}")

source_filename = input("Enter the name of the source file: ")
destination_filename = input("Enter the name of the destination file: ")

copy_file(source_filename, destination_filename)



#8
import os

def delete_file(path):
    
    try:
        
        if os.path.exists(path):
            
            if os.access(path, os.W_OK):
                
                os.remove(path)
              
                print(f"File '{path}' has been deleted successfully.")
            
            else:
            
                print(f"Error: You don't have write access to '{path}'.")
        
        else:
        
            print(f"Error: File '{path}' does not exist.")
    
    except Exception as e:
    
        print(f"Error occurred while deleting file: {e}")

file_path = input("Enter the path of the file to delete: ")

delete_file(file_path)

