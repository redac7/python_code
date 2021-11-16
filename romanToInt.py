def romanToInt(s: str) -> int:
    number = 0
    previous_char =''
    for char in s:
        if char == 'M' and previous_char != 'C':
            number+=1000
        if char == 'M' and previous_char == 'C':
            number+=800
        if char == 'D' and previous_char != 'C':
            number+=500
        if char == 'D' and previous_char == 'C':
            number+=300
        if char == 'C' and previous_char != 'X':
            number+=100
        if char == 'C' and previous_char == 'X':
            number+=80
        if char == 'L' and previous_char != 'X':
            number+=50
        if char == 'L' and previous_char == 'X':
            number+=30
        if char == 'X' and previous_char != 'I':
            number+=10
        if char == 'X' and previous_char == 'I':
            number+=8
        if char == 'V' and previous_char != 'I':
            number+=5
        if char == 'V' and previous_char == 'I':
            number+=3
        if char == 'I':
            number+=1
        previous_char = char
    return number

print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
