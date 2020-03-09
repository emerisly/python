# all set values are unique
# is sorted
a = {1, 2, 5, 4, 7, 9, 2}
print(a)
print(len(a))
a.add(10)
print(a)
a.update([15, 18, 17, 14])
print(a)
a.remove(18)
a.discard(17)
a.discard(11)
# discard does not return error if no such value found
print(a)
# pop a random index in set
a.pop()
print(a)

name = {'max', 'tom', 'den'}
print(name)
name.clear()
print("name set is now", name)
del name
# print("name set is now", name)

name = set(('max', 'tom', 'den'))
print(name)
z = set([1, 2, 3, 4])
print(z)

a = {1, 2, 5, 7, 9, 10, 13}
b = {10, 11, 12, 13, 14, 15}
print("union", a|b)
print("union", a.union(b))
print("intersection", a&b)
print("intersection", a.intersection(b))
print(a,b)
print("a difference b", a-b)
print("b difference a", b-a)

# set has no index
# no methods with index

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)