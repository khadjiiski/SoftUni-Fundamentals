n = int(input())

for i in range(1, n + 1):
    message = int(input())

    if message == 88:
        print('Hello')
    elif message == 86:
        print("How are you?")
    elif message != 86 and message != 88 and message < 88:
        print('GREAT!')
    elif message > 88:
        print('Bye.')