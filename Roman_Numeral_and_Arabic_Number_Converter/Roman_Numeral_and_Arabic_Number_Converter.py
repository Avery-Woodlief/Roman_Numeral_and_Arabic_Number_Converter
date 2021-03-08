def main():
    '''
    This function allows the user to have three options:
    roman(x) ... where x is an integer from 1 to 3999
    arabic(y) ... where y is a roman numeral to be converted to an integer between 1 and 3999
    quit
    '''
    
    while True:
        command = input('> ')
        tok = command.replace('(', ' ').replace(')', ' ').split()
        if tok[0] == 'roman':
            print(roman(int(tok[1])))
        elif tok[0] == 'arabic':
            print(arabic(tok[1]))
        elif tok[0] == 'quit':
            break


def roman(n):
    '''
    Convert the given arabic number to roman numerals.
    INPUT the arabic number to convert
    RETURN roman numerals equivalent to the given arabic number

    If the input, n, is in a certain range then it will fall under a certain condition. The first thing that happens is that
    it determines how many roman numeral characters are needed for a specific number and that value
    will be added to the roman variable. Also, n becomes decremented so the if statements can eventually make n become 0.
    This means that once n becomes 0, there will be a roman numeral for each corresponding value and place holder in n.
    '''

    roman = ''

     
    if n >= 1000:
        M = n // 1000
        roman += 'M' * M
        n = n % 1000
        
    if (n < 1000) and (n >= 500):
        if (n < 1000) and (n >= 900):
            CM = n // 900
            roman += 'CM' * CM
            n = n % 900
        elif (n <= 899) and (n >= 500):
            D = n // 500
            roman += 'D' * D
            n = n % 500
        
    if (n < 500) and (n >= 100):
        if (n <= 499 and n >= 400):
            CD = n // 400
            roman += 'CD' * CD
            n = n % 400
        elif (n <= 399) and (n >= 100):
            C = n // 100
            roman += 'C' * C
            n = n % 100
        
    if (n < 100) and (n >= 50):
        if (n <= 99) and(n >= 90):
            XC = n // 90
            roman += 'XC' * XC
            n = n % 90
        elif (n <= 89) and (n >= 50):
            L = n // 50
            roman += 'L' * L
            n = n % 50
        
    if (n < 50) and (n >= 10):
        if (n >= 40):
            XL = n // 40
            roman += 'XL' * XL
            n = n % 40
        elif (n <= 39 and n >= 10):
            X = n // 10
            roman += 'X' * X
            n = n % 10
        
    if (n < 10) and (n >= 5):
        if (n % 9 == 0):
            IX = n // 9
            roman += 'IX' * IX
            n = n % 9
        elif (n < 9) and (n >= 5):
            V = n // 5
            roman += 'V' * V
            n = n % 5
        
    if (n < 5) and (n >= 1):
        if (n % 4 == 0):
            IV = n // 4
            roman += 'IV' * IV
            n = n % 4
        elif (n < 4) or (n >= 1):
            I = n // 1
            roman += 'I' * I
            n = n % 1
       
    return roman

def arabic(n):
    '''
    Convert the given roman numerals to an arabic number.
    INPUT the roman numerals to convert
    RETURN arabic number equivalent to the given roman numerals

    In a way, this function works similarly to the roman().
    If the user input contains a certain roman numeral, then it falls under a certain condition.
    The value is determined by the number of occurences of a specifc sequence of roman numerals multiplied by the roman numeral value.
    Once the value is determined and added to the arabic variable, the sequence is removed from the user input and it continues to go down the if statements
    until the user input becomes an empty string.
    This means that once n becomes an empty string, there will be an integer for each roman numeral value and place holder.
    '''

    arabic = 0


    if (n.count('M') >= 1):
        if (n.count('CM') >= 1):
            CM = n.count('CM') * 900
            arabic += CM
            n = n.replace('CM', '', n.count('CM'))
        if (n.count('CM') == 0):
            M = n.count('M') * 1000
            arabic += M
            n = n.replace('M', '', n.count('M'))

    if (n.count('D') >= 1):
        if (n.count('CD') >= 1):
            CD = n.count('CD') * 400
            arabic += CD
            n = n.replace('CD', '', n.count('CD'))
        if (n.count('CD') == 0):
            D = n.count('D') * 500
            arabic += D
            n = n.replace('D', '', n.count('D'))

    if (n.count('C') >= 1):
        if (n.count('XC') >= 1):
            XC = n.count('XC') * 90
            arabic += XC
            n = n.replace('XC', '', n.count('XC'))
        if (n.count('XC') == 0):
            C = n.count('C') * 100
            arabic += C
            n = n.replace('C', '', n.count('C'))

    if (n.count('L') >= 1):
        if (n.count('XL') >= 1):
            XL = n.count('XL') * 40
            arabic += XL
            n = n.replace('XL', '', n.count('XL'))
        if (n.count('XL') == 0):
            L = n.count('L') * 50
            arabic += L
            n = n.replace('L', '', n.count('L'))

    if (n.count('X') >= 1):
        if (n.count('IX') >= 1):
            IX = n.count('IX') * 9
            arabic += IX
            n = n.replace('IX', '', n.count('IX'))
        if (n.count('IX') == 0):
            X = n.count('X') * 10
            arabic += X
            n = n.replace('X', '', n.count('X'))

    if (n.count('V') >= 1):
        if (n.count('IV') >= 1):
            IV = n.count('IV') * 4
            arabic += IV
            n = n.replace('IV', '', n.count('IV'))
        if (n.count('IV') == 0):
            V = n.count('V') * 5
            arabic += V
            n = n.replace('V', '', n.count('V'))

    if (n.count('I') >= 1):
        I = n.count('I') * 1
        arabic += I
        n = n.replace('I', '', n.count('I'))
        
    return arabic



if __name__ == '__main__':
    main()
