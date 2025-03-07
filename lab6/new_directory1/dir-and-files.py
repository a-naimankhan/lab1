import os 
import string
##Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

def create_files(folder_name):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for letter in string.ascii_uppercase:
        filename = os.path.join(folder_name, f"{letter}.txt")
        with open(filename , 'w') as file:
            file.write(f"this is {filename}")

f = os.path.join("lab6", "new_directory1")
create_files(f)