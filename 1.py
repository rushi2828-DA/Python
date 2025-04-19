#1.Concatenation (combining strings):
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # output: Hello World

#2.Repetition (Repeating a string)
str3 = "Hello"
repeated = str3 *3 
print(repeated) #output : Hello Hello Hello

#3. Indexing(Accessing a character in a string):
str4 = "Python"
print(str4[0]) #output P(first character)
print(str4[-1]) #output n(first character)

#4. Slicing (Extracting a portion of a string)
str5= 'Hello World'
print(str5[0:5]) #output : Hello
print(str5[6:]) #output : World
print(str5[:5]) #output : Hello

#5. Length (Finding the length od a string):
str6 = "python"
print(len(str6)) # output : 6

#6. Changing case (converting string to uppercase or lowercase)
str7 = "Hello"
print(str7.upper()) # output : Hello
print(str7.capitalize()) # output : Hello
print(str7.title()) # output : Hello

#7. Finding Substrings (Searching for a substring within a string):
str8 = 'Hello World'
print(str8.find('World')) #output: 6 (index of "World")
print(str8.find('Python')) #output: -1 (not found)

#8. Replacing Substrings
str9 = 'Hello World'
new_str = str9.replace('World', 'Python')
print(new_str) # output: Hello Python

#9. Trimming whitespaces:
str10 = "Hello World     "
print(str10.strip()) # output: "Hello World"


