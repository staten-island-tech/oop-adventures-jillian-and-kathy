first_digit = 1
second_digit = 2
third_digit = 2
fourth_digit = 9
first = input("Guess the first digit: ")
if first == first_digit:
    print('Correct!')
    if first < first_digit:
        print('Incorrect! Guess higher.')
    if first > first_digit:
        print('Incorrect! Guess lower.')

second = input("Guess the second digit: ")
if second == second_digit:
    print('Correct')
    if second < second_digit:
        print('Incorrect! Guess higher.')
        if second > second_digit:
            print('Incorrect! Guess lower.')

third = input('Guess the third digit: ')
if third == third_digit:
    print('Correct')
    if third < third_digit:
        print('Incorrect! Guess higher.')
        if third > third_digit:
            print('Incorrect! Guess lower.')

fourth = input('Guess the fourth digit: ')
if fourth == fourth_digit:
    print('Correct')
    if fourth < fourth_digit:
        print('Incorrect! Guess higher.')
        if fourth > fourth_digit:
            print('Incorrect! Guess lower')