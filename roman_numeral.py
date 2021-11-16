def romanToInt(s: str) -> int:
        number = int(s)
        numeral = ""
        while number >= 1000:
            numeral+='M'
            number-=1000
        while number >= 500:
            numeral+='D'
            number-=500
        while number >= 100:
            numeral+=C
            number-=100
        while number >= 50:
            numeral+='L'
            number-=50
        while number >= 10:
            numeral+='V'
            number-=10
        if number == 9:
            numeral+='IX'
            return numeral
        elif number == 4:
            numeral+='IV'
            return numeral
        while number >= 5:
            numeral+='V'
            number-=5
        while number > 0:
            numeral+='I'
            number-=1
        return numeral

print(romanToInt(60))
print(romanToInt(59))
