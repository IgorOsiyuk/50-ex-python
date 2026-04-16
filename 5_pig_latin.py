from string import punctuation 
def pig_latin(str):
    vowel = 'aeiou'
    res=''
    punctuation_char = str[-1] if str[-1] in punctuation else ""
    str = str[:-1] if punctuation_char else str
    
    foundedVowels = set()
    for ch in str:
        if ch.lower() in vowel:
            foundedVowels.add(ch)
    print(foundedVowels)      
    # if str[0] in vowel or str[0].isupper():
    if len(foundedVowels) >= 2:
        res=str + 'way' + punctuation_char
    else:
        res=str[1:] + str[0] + 'ay' + punctuation_char
    return res

print(pig_latin("Tesdgue!"))