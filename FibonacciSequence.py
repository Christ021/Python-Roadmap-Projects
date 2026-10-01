
n = int(input("\t ** WELCOME TO FIBONACCI SEQUENCE TO GOLDEN RATIO ** \n \n Input the number you want to stop: "))
a, b = 0, 1
print(f"\t ** WELCOME TO FIBONACCI SEQUENCE TO GOLDEN RATIO ** \nFibonacci Sequence: {a}")

for _ in range(n - 1):
    print(f"Fibonacci Sequence: {b}")
    a, b = b, a + b
    for _ in range(n-1, n):
        print(f"Golden Ratio: {b/a}")
