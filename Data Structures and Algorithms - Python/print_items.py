# n numbers; proportional time complexity = O(n)
def print_items_1(n):
    for i in range(n):
        print(i)

# 2*n numbers; proportional time complexity = O(2n) = O(n)
def print_items_2(n):
    for i in range(n):
        print(i)
    for j in range (n):
        print(j)

# n^2 numbers; exponential time complexity = O(n^2)
def print_items_3(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# n^3 numbers; exponential time complexity = O(n^3) = O(n^2)
def print_items_4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

# a + b numbers; different terms for inputs = O(a + b)
def print_items_5(a, b):
    for i in range(a):
        print(i)
    for j in range (b):
        print(j)

# a + b numbers; different terms for inputs = O(a * b)
def print_items_6(a, b):
    for i in range(a):
        for j in range (b):
            print(i, j)


print_items_3(10)

