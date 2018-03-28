#main game using python 3

from string import ascii_lowercase
from wrods import picked

def get_num_attempts():
    #ask user for number of inputs we should allow him
    while True:
        num_attempts = int(input('How many incorrect attempts should we allow you?  [1-25] '))
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 99:
                print('\n')
                return num_attempts
            else:
                print('\n')
                print('That number is not between 1 and 25')
                print('\n')
        except ValueError:
            print('\n')
            print('That is not an integer!')
            print('\n')

def get_min_word_length():
    #get user input for minimum word length#
    while True:
        min_word_length = input('What is the minimum word length you want?  [4-16] ')
        try:
            min_word_length = int(min_word_length)
            if 4<= min_word_length <=16:
                print('\n')
                print('Okay LET US START! \n')
                return min_word_length
            else:
                print('\n')
                print('That number is not between 4 and 16')
                print('\n')
        except ValueError:
            print('\n')
            print('That is not an integer!')
            print('\n')
   
def displayword():
    displayword.hidden = []
    for i in range(len(picked.one)):
        displayword.hidden.append('*')
    print(' '.join(displayword.hidden))
    print('\n')

def getguess():
    guess = str(input('Guess: '))
    print ('\n')
    return guess


def matching(guess): #checking if the letter guessed, well actually all the letters guessed in the array are present in the word, if they are replace the * with that letter
    if len(guess) == 1:
        for i in range(len(picked.one)): #need to adjust this for entire words
            if guess == picked.one[i]:
                displayword.hidden[i] = guess
        print(' '.join(displayword.hidden))
        print('\n')
    if len(guess) == len(picked.one):
        if guess == picked.one:
           displayword.hidden = guess
           print(' '.join(displayword.hidden))
    if len(guess) != 1 and len(guess) != len(picked.one):
        print('You messed up the letter count!\n')
            
def winner():
    if '*' not in displayword.hidden:
        return True
    else:
        return False

def check(guess, storage):
    while guess in storage:
        print('You already guess this!\n')
        guess = getguess()

def playagain():
    print('Do you want to play again?\n')
    answer= input('Y/N : \n')
    if answer == 'y' or answer == 'Y':
        start()
    if answer =='n' or answer == 'N':
        print('Okay bye!')
    else:
        print('That is not an answer try again\n')
        playagain()
       
        
def play(count, storage, num_attempts):
    while count < num_attempts:
        count = count + 1
        guess = getguess()
        check(guess, storage)
        if guess not in storage:
            storage.append(guess)
        print('You have ', num_attempts - count, 'guesses left!\n')
        print ('Already guessed: \n \n', storage, '\n')
        matching(guess)
        if winner() is True:
            print('Winner!')
            break
    if count >= num_attempts:
        print('game over\n')
        print('The word was ', picked.one.upper(), '\n')
        playagain()
 
def start():
    print(' H A N G M A N\n')
    num_attempts = get_num_attempts()
    min_word_length = get_min_word_length()
    picked(min_word_length)
    displayword()
    count = 0
    storage = []
    play(count, storage, num_attempts)

start()