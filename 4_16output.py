# def hex_output():
#     userInput = input('ВВедите число в 16 системе: ')
#     decNumber = 0
#     for index, one_letter in enumerate (reversed(userInput)):
#         # print(f'{index}: {one_letter}')
#         decNumber +=int(one_letter,16)*(16**index)
#         # print(f'{index}: {int(one_letter,16)*(16**index)}')
#     # for one_letter in reversed (userInput):
#     #     print(f' {one_letter}')
#     # print(userInput[::-1])
#     return decNumber
# def hex_output():
#     userInput = input('ВВедите число в 16 системе: ')
#     result = 0
#     for ch in userInput:
#         if '0' <= ch <= '9':
#             decNumber = ord(ch) - ord('0')
#         else:
#             decNumber = ord(ch) - ord('A') + 10
#         result=result*16 + decNumber
#     return     result
# print(hex_output())

def nameTriangle():
    userInput = input("Введите свое имя: ")
    for index, ch in enumerate(userInput):
        print(userInput[0:index+1])

nameTriangle()

