#basic structure
#for item in sequence
    #do something with item

#1. loop through a list
fruits =['apple ', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#2 loop using range()
#prints number from 0 to 4
for i in range(5):
     print(i)

#3 loop with range(start,stop,step)
#prints 2,4,6,8
for i in range(2, 10, 2):
    print(i)

#4 loop through characters in a string
word = 'Hello'
for letter in word:
    print(letter)

#5 Nested for loops
for i in range(3):
     for j in range(2):
         print(f"i={i} , j={j}")