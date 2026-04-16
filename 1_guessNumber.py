import random
def guessing_game():
    number = random.choice([0,100,2])
    print(f'{number}')
    attempts = 0
    while True:
        userBase = int(input('Введите систему счисления: '))
        userInput = input('Введите число: ')
        if int(userInput,userBase) == int(number):
            print('Вы угадали число')
            break
        attempts+=1
        if attempts==3:
            print('too many attempts')
            break
        
guessing_game()