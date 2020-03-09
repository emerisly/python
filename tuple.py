# tuple's value cannot be modified
# is not sorted
x = (1, 5, 3, 4, 8)
# did not sorted
print(x)
print(x[0])
y = (1, 'max', 1.6)
z = x + y
print(z)
# remember to add comma
a = ('hi',) * 5
print(a)
print(max(x))
del x
# print(x)

# tuple cannot be copied
