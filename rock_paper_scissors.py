# ROCK, PAPER, SCISSORS
import random

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
win = 0
losse = 0
tie = 0

while True: # The main game loop.
    result = f"{win} Wins, {loss} Losses, {tie} Ties \n" 
    move = f"Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit"
    print(result, move)
    answer = input(">>> ")
    # if you choose 'ROCK'
    if answer == 'r':
        pc = random.choice(elements)
        print('ROCK versus', pc)
        # selection probabilities of the PC, when you chose ‘rock’
        if pc == 'ROCK':
            print("It is a tie!")
            tie += 1
        elif pc == 'PAPER':
            print('You lose!')
            loss += 1
        else:
            print('You win!')
            win += 1
    # if you choose 'PAPER'
    elif answer == 'p':
        pc = random.choice(elements)
        print('PAPER versus', pc)
        # selection probabilities of the PC, when you chose ‘paper’
        if pc == 'PAPER':
            print("It is a tie!")
            tie += 1
        elif pc == 'SCISSORS':
            print('You lose!')
            loss += 1
        else:
            print('You win!')
            win += 1
    # if you choose 'SCISSORS'
    elif answer == 's':
        pc = random.choice(elements)
        print('SCISSORS versus', pc)
        # selection probabilities of the PC, when you chose ‘scissors’
        if pc == 'SCISSORS':
            print("It is a tie!")
            tie += 1
        elif pc == 'ROCK':
            print('You lose!')
            loss += 1
        else:
            print('You win!')
            win += 1
    # when the program's finished, the final results are displayed
    elif answer == 'q':
        print(result)
        break
    else:
        print('Please enter only the characters mentioned.')
