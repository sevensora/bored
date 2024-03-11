from cs50 import get_int

while True:
    n = get_int('Please enter height!: ')
    if n > 0 and n < 9:
        break

for x in range(0, n , 1):
    for y in range(0, n , 1):
        if (x + y < n - 1):
            print(" ", ends="")
        else:
            print('#', end="")
    print()
