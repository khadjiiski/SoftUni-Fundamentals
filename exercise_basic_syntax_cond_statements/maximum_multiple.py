import sys

divisor = int(input())
boundary = int(input())
greatest_number = -sys.maxsize

for i in range(1, boundary + 1):
    number = i

    if number % divisor == 0 and boundary >= number > 0:
        greatest_number = number

print(greatest_number)
