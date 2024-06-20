import sys

num1 = int(input())
num2 = int(input())
num3 = int(input())

largest_num = -sys.maxsize

if num1 > num2 and num1 > num3:
    largest_num = num1

elif num2 > num1 and num2 > num3:
    largest_num = num2

elif num3 > num2 and num3 > num1:
    largest_num = num3

print(largest_num)