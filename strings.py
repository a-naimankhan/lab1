b0 = "Hello , World!"
print(b0) #prints the whole word

b = "Hello, World!"
print(b[2:5]) #prints the word from the indexex 2 , 5

b1 = "Hello, World!"
print(b[:5]) #prints the word untill the 5 index

b2 = "Hello, World!"
print(b[2:]) #prints the word from the second index

b3 = "Hello, World!"
print(b[-5:-2]) #print from the reverse form

a = "hello world!"
print(a.upper()) #prints the upper one

a1 = "HELLO WORLD!"
print(a1.lower()) #prints the wise a verse lower one

a2 = " Hello, World! "
print(a.strip()) # returns "Hello, World!" deletes spaces from both sides.

a3 = "Hello, World!"
print(a.replace("H", "J")) # replaces the characters by its meaning 

a4 = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a5 = "Hello"
b4 = "World"
c = a + " " + b
print(c)


age = "36" #if it is just 36 in TypeError: can only concatenate str (not "int") to str
txt = "My name is John, I am " + age
print(txt)

age1 = 36
txt2 = f"My name is John, I am {age}"
print(txt)


txt3 = "We are the so-called \"Vikings\" from the north." 

# \'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value
