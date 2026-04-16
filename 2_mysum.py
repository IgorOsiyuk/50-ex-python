# def mysum(numbers,start=0):
#     result = start
#     print(start)
#     for arg in numbers:
#          result+=arg
#     # i=0
#     # while i< len(args):
#     #     result+=args[i]
#     #     i+=1
#     print(result)
    
# mysum(numbers=(1,2,3,4,5))

# def average(*args):
#     sum = 0
#     for arg in args:
#         sum+=arg
#     print(sum/len(args) )
#     return sum/len(args) 

# average(1,2,3,4,5)
# import math 
# def checkWords(list):
#     maxLen = 0
#     minLen = math.inf
#     sumLen = 0
#     for word in list:
#         sumLen+=len(word)
#         if len(word) > maxLen:
#             maxLen = len(word)
#         if len(word) < minLen:
#             minLen = len(word)
#     print(f'maxLen={maxLen}; minLen={minLen}; average={sumLen/len(list)}')
    
# checkWords(('test','test2','test423123','te'))

def sum_int_like(objects):
    sum = 0
    for object in objects:
        if isinstance(object,bool)!=True:
            try:
                sum+=int( object)
            except (ValueError, TypeError):
                continue      
    return sum

data = [1, "2", 3.0, "4", "5.5", None, True, "abc", -7]

print(sum_int_like(data))
