import random as rand
import string as string

letterNum = int(input("How many letters would you like in your password?"))
symbNum = int(input("How many symbols would you like?"))
numNum = int(input("How many numbers would you like?"))


def get_random_letter(length):
    letters = string.ascii_letters
    result_letters = ''.join(rand.choice(letters)for i in range(length))
    return result_letters
    print(result_letters)


def get_random_number(length):
    number = ''
    for i in range(length):
        number = rand.randint(0, 9).__str__() + number
    return number
    print(number)


def get_random_symbol(length):
    symbol = string.punctuation
    result_symb = ''.join(rand.choice(symbol) for i in range(length))
    return result_symb
    print(result_symb)



finalLetter = get_random_letter(letterNum)
finalNumber = get_random_number(numNum)
finalSymbol = get_random_symbol(symbNum)

total = finalLetter.__str__() + finalNumber.__str__()  + finalSymbol.__str__()

finalPassword = list(total)
rand.shuffle(finalPassword)
print(''.join(finalPassword))
