import random

print('Bienvenido!')

def play():
    player = input('Choose an option\n Rock = R, Paper = P, Scissors = S\n')
    ai = random.choice(['R','P','S'])
    print('PC: ' + ai)
    if player != ai:
        if (player == 'P' and ai == 'R') \
            or (player == 'S' and ai == 'P') \
            or (player == 'R' and ai == 'S'):
            print('YOU WIN!')
        else:
            print('PC WINS!')
        return False
    else: 
        print('DRAW!')
        return True

while play():
    print()