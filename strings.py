a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[0])
b = "Hello, World!"
print(b)
# exclusive 5 and-5
print(b[1:5])
print(b[-5:-2])
print(len(b))
# strip removes whitespace at both ends
a = "   hey   "
print(a.strip())
a="Whaats up"
print(a.upper())
print(a.lower())
print(a.replace("a", "o"))
print(a.split(" "))

txt = "how are you doing"
x = "you" in txt
print(x)
y = "you" not in txt
print(y)

a = "hello"
b = "world"
c = a + b
print(c)
c = a + " " + b
print(c)

# using format() method
age = 17
year = 2019
txt = "Hey it is {1} and I am {0} years old"
print(txt.format(age, year))
