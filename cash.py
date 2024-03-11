from cs50 import get_float
while True:
    cents = get_float('Change: ')
    if cents > 0
    break

count = 0

cents = round(100*cents)

while cents >= 25:
    cents = cents - 25
    count += 1

while cents >= 10:
    cents = cents - 10
    count += 1

while cents >= 1:
    cents = cents - 1
    count +=1

print("Change: ", count)
