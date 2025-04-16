# Identity Operators: is, is not

# Example with integers
a = 10
b = 10

print("a =", a)
print("b =", b)

# 'is' checks if both variables point to the same object in memory
print("a is b:", a is b)        # True (small integers are cached in Python)

# 'is not' checks if they are different objects
print("a is not b:", a is not b)  # False

# Example with lists (mutable objects)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nlist1 =", list1)
print("list2 =", list2)
print("list3 =", list3)

print("list1 is list2:", list1 is list2)     # False (different objects, same content)
print("list1 == list2:", list1 == list2)     # True (contents are the same)
print("list1 is list3:", list1 is list3)     # True (same object in memory)

print("list1 is not list2:", list1 is not list2)  # True
