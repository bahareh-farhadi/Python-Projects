from random import randint

#infinite loop
while True:
    
    #get the user input
    player = input('Rock(r), Paper(p) or Scissors(s)?')
    
    #based on the user input display text shapes to represent rock,paper, or scissors
    if player == 'r':
        p_shape = 'O'
    elif player == 'p':
        p_shape = '___'
    elif player == 's':
        p_shape = '>8'
        
    #error message
    else:
        print('ERROR: BAD INPUT, CHOOSE AMONG THE GIVEN OPTIONS.\nTRY AGAIN')
        continue
    
    #random integer from 1-3, each number represents rock,paper or scissors
    computer = randint(1, 3)
    if computer == 1:
        c = 'r'
        c_shape = 'O'
    elif computer == 2:
        c = 'p'
        c_shape = '___'
    elif computer == 3:
        c = 's'
        c_shape = '>8'
        
    #print the user input vs. computer's
    print(p_shape, 'vs', c_shape)
    
    #considering different inputs by user and computer, the result messages are printed
    if player == c:
        print('DRAW')
    elif player == 'r' and c == 'p':
        print('COMPUTER WINS')
    elif c == 'r' and player == 'p':
        print('PLAYER WINS')
    elif player == 'r' and c == 's':
        print('PLAYER WINS')
    elif c == 'r' and player == 's':
        print('COMPUTER WINS')
    elif player == 'p' and c == 's':
        print('COMPUTER WINS')
    elif c == 'p' and player == 's':
        print('PLAYER WINS')
