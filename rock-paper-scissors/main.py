select = ['rock', 'paper', 'scissors']

print("------- Rock Paper Scissors Game ---------")
print("Select one of the following: rock, paper, scissors")
print("-------------------------------------------")

for i, item in enumerate(select) :
    print(f"{i}: {item}")

player1 = input('select player 1: ')
player2 = input('select player 2: ')

def findTheWinner(a, b):
    if a == 0 or a == 'rock':
        if b == 1 or b == 'paper':
            return 'player 2 win'
        elif b == 2 or b == 'scissors':
            return 'player 1 win'
    elif a == 1 or a == 'paper':
        if b == 0 or b == 'rock':
            return 'player 1 win'
        elif b == 2 or b == 'scissors':
            return 'player 2 win'
    elif a == 2 or a == 'scissors':
        if b == 1 or b == 'paper':
            return 'player 1 win'
        elif b == 0 or b == 'rock':
            return 'player 2 win'
