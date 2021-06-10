


for x in range(1, 11):
    print(x, end=" ")

print()


for number in range(1, 21):
    if number % 2 == 1:
        continue
    print(number, end=" ")

print()


for number in range(1, 21):
    if number % 2 == 1:
        print(number, end=" ")

print()


for number in range(1, 50, 3):
    print(number, end=" ")

print()


for number in range(40, 0, -4):
    print(number, end=" ")

print()


for number in range(1, 100):
    if number == 1:
        continue
    temp = 2
    while temp <= number:
        if number == temp:
            print(number, end=" ")
            break
        if number % temp == 0:
            break
        temp += 1