def my_function1():
    print("Hello from a function")


def my_function(name):
    print(name + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function1()


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food, fruit):
    for x in food:
        print(x)
    for y in fruit:
        print(y)


food = ["bread", "noodles", "pizza"]
fruits = ["apple", "banana", "cherry"]
my_function(food, fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_list(*kids):
    print("The youngest child is " + kids[2])


my_list("Emil", "Tobias", "Linus")


# *kids will be a tuple

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print("+", k, "=", result)
    else:
        result = 0
    return result


tri_recursion(4)

# lambda arguments : expression
# only one expression
# use them as an anonymous function inside another function

product = lambda a, b: a * b
print(product(5, 6))


def my_func(n):
    return lambda a: a * n

my_doubler = my_func(2)
print(my_doubler(11))