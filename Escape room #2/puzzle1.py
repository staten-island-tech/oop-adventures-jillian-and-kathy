digit1 = 1
digit2 = 2
digit3 = 2
digit4 = 9



guess1 = int(input("Guess a number from 1-10: "))
history1 = []
if guess1 != digit1:       
    history1.append(guess1)
    print (f'Guess history: {history1}')
while digit1!= guess1:
    if guess1 == digit1:
        print('Your guess is correct!')
        break
    elif guess1 < digit1:
        print('Your guess is too low! Try again!')
        guess1 = int((input('Guess again: ')))
        history1.append(guess1)
        print(f'Guess history: {history1}')
    elif guess1 > digit1:
        print('Your guess is too high! Try again!')
        guess1 = int((input('Guess again: ')))
        history1.append(guess1)
        print(f'Guess history: {history1}')
    else:
        print('Error. Try again!')
if guess1 == digit1:
    print('Your guess is correct!')






















""" class firstpuzzle():
    def guess_code1():
        first = int(input("Guess the first digit: "))
        first_history = []
        if first != digit1:
            first_history.append(first)
            print(f'Guess history: {first_history}')
        while digit1 != first:
            if first < digit1:
                print('Your guess is too low, guess again.')
                first_again = int((input('Guess again: ')))
                first_history.append(first_again)
                print(f'Guess history: {first_history}')
            elif first > digit1:
                print('Your guess is too high, guess again.')
                first_again = int((input('Guess again: ')))
                first_history.append(first_again)
                print(f'Guess history: {first_history}')
            else:
                print('Error. Try Again!')
        if first_again == digit1:
            print('Your guess is correct!')
    guess_code1() """
