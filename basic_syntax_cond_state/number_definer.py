number = float(input())

if number == 0:
    print('zero')

elif number > 0:
    if number > 1000:
        print("large positive")
    elif 0 < number < 1:
        print("small positive")
    else:
        print("positive")

elif number < 0:
    if abs(number) > 1000:
        print("large negative")
    elif 0 > number > -1:
        print("small negative")
    else:
        print("negative")