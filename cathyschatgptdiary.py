1. I am trying to revise my code so that it will check for each digit every time it loops
2. my original code was:
    digit1 = 1
digit2 = 2
digit3 = 2
digit4 = 9
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
3. the code that ai gave me was:
digit1 = 1
digit2 = 2
digit3 = 2
digit4 = 9
class puzzle1():
    print('This is a safe, to open it you have to get the four-digit code right. I wonder whats inside?')
    def get_all_digits():
        correct_digits = [digit1, digit2, digit3, digit4]
        history = []
        for i in range(4):
            print(f'Guess the digit {i + 1}:  (hint: use your resources)')
            guess = int(input("Guess a number from 1-10: "))
            digit_history = []
            while guess != correct_digits[i]:       
                digit_history.append(guess)
                print (f'Guess history for digit {i + 1}: {digit_history}')
                if guess == correct_digits[i]:
                    print('Your guess is correct!')
                elif guess <  correct_digits[i]:
                    print('Your guess is too low! Try again!')
                    guess = int((input('Guess again: ')))
                    print(f'Guess history: {history}')
                elif guess >  correct_digits[i]:
                    print('Your guess is too high! Try again!')
                    guess = int((input('Guess again: ')))
                    print(f'Guess history: {history}')
                else:
                    print('Error. Try again!')
                if guess ==  correct_digits[i]:
                    print('Your guess is correct!')
    get_all_digits()