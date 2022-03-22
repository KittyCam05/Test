guesses = {
        3 : 'True',
        1 : 'True',
        }

your_guess = int(input('Please enter guess \n'))

if guesses[your_guess] == 'True':
    print('You won!')
else:
    raise IndexError ('You lost')