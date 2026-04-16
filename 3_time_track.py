# def run_timing():
#     userTimeList = []
#     while True:
#         userTime = input('Введите время пробега 10км: ')
#         if not userTime:
#             break
#         try:
#             userTimeList.append(float(userTime))
#         except ValueError as e:
#             print('нудно число')
#     sumTime = sum(userTimeList)
#     print(f'Средний покащатель {sumTime/len(userTimeList)}, более {len(userTimeList)} пробежек')
        
# run_timing()

# def before_after_float(number:float,before:int,after:int):
#     result = list(str(number))
#     dotPost = result.index('.')
#     print(dotPost)
#     print("".join(result[dotPost-before:dotPost+after+1]))
#     return 

# before_after_float(123.56,2,1)


from decimal import Decimal
test1 = Decimal(input("Цена: "))
test2= Decimal(input("Цена: "))
total=test1+test2
print(total)
