digit1 = 1
digit2 = 2
digit3 = 2
digit4 = 9

digits = [digit1, digit2, digit3, digit4]

class puzzle1():
    print('This is a safe, to open it you have to get the four-digit code right. I wonder whats inside?')
    def get_all_digits():
        for i in range(3):
            print('Guess the digit:   (hint: use your resources)')
            guess = int(input("Guess a number from 1-10: "))
            history = []
            if guess != digit1:       
                history.append(guess)
                print (f'Guess history: {history}')
                while digit1!= guess:
                    if guess == digit1:
                        print('Your guess is correct!')
                    elif guess < digit1:
                        print('Your guess is too low! Try again!')
                        guess = int((input('Guess again: ')))
                        history.append(guess)
                        print(f'Guess history: {history}')
                    elif guess > digit1:
                        print('Your guess is too high! Try again!')
                        guess = int((input('Guess again: ')))
                        history.append(guess)
                        print(f'Guess history: {history}')
                    else:
                        print('Error. Try again!')
                    if guess == digit1:
                        print('Your guess is correct!')
    get_all_digits()








#og code
    """ def firstdigit():
        print('Guess the first digit:   (hint: use your resources)')
        guess1 = int(input("Guess a number from 1-10: "))
        history1 = []
        if guess1 != digit1:       
            history1.append(guess1)
            print (f'Guess history: {history1}')
            while digit1!= guess1:
                if guess1 == digit1:
                    print('Your guess is correct!')
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
    firstdigit() """
    
    
    """ def seconddigit():
        print('Congrats! You got the first digit correct, now guess the second digit: ')
        guess2 = int(input("Guess a number from 1-10: "))
        history2 = []
        if guess2 != digit2:       
            history2.append(guess2)
            print (f'Guess history: {history2}')
            while digit2!= guess2:
                if guess2 == digit2:
                    print('Your guess is correct!')
                elif guess2 < digit2:
                    print('Your guess is too low! Try again!')
                    guess2 = int((input('Guess again: ')))
                    history2.append(guess2)
                    print(f'Guess history: {history2}')
                elif guess2 > digit2:
                    print('Your guess is too high! Try again!')
                    guess2 = int((input('Guess again: ')))
                    history2.append(guess2)
                    print(f'Guess history: {history2}')
                else:
                    print('Error. Try again!')
                if guess2 == digit2:
                    print('Your guess is correct!')
    seconddigit()
    def thirddigit():
        print('Guess the third digit: ')
        guess3 = int(input("Guess a number from 1-10: "))
        history3 = []
        if guess3 != digit3:       
            history3.append(guess3)
            print (f'Guess history: {history3}')
            while digit3!= guess3:
                if guess3 == digit3:
                    print('Your guess is correct!')
                elif guess3 < digit3:
                    print('Your guess is too low! Try again!')
                    guess3 = int((input('Guess again: ')))
                    history3.append(guess3)
                    print(f'Guess history: {history3}')
                elif guess3 > digit3:
                    print('Your guess is too high! Try again!')
                    guess3 = int((input('Guess again: ')))
                    history3.append(guess3)
                    print(f'Guess history: {history3}')
                else:
                    print('Error. Try again!')
                if guess3 == digit3:
                    print('Your guess is correct!')
    thirddigit()
    def fourthdigit():
        print('Guess the fourth (and last) digit: ')
        guess4 = int(input("Guess a number from 1-10: "))
        history4 = []
        if guess4 != digit4:       
            history4.append(guess4)
            print (f'Guess history: {history4}')
            while digit4!= guess4:
                if guess4 == digit4:
                    print('Your guess is correct!')
                elif guess4 < digit4:
                    print('Your guess is too low! Try again!')
                    guess4 = int((input('Guess again: ')))
                    history4.append(guess4)
                    print(f'Guess history: {history4}')
                elif guess4 > digit4:
                    print('Your guess is too high! Try again!')
                    guess4 = int((input('Guess again: ')))
                    history4.append(guess4)
                    print(f'Guess history: {history4}')
                else:
                    print('Error. Try again!')
                if guess4 == digit4:
                    print('Your guess is correct!')
    fourthdigit() """




















