import random

while True:
    my_answer=input("Choose: rock, paper, scissors: ")
    my_answer=my_answer.lower()

    if my_answer == "quit":
        print('Get outta here')
        break

    if my_answer != 'rock' and my_answer != 'paper' and my_answer != 'scissors':
        print ('please choose the correct answer')
        continue

    computer_answer = random.choice(['rock', 'paper', 'scissors'])
    print(f'Computer chose the :{computer_answer}')

    if my_answer == computer_answer:
        print ('You Tied')
        continue

    elif my_answer == 'paper' and computer_answer == 'rock':
        print('Hey Computer you win')
        break
    
    elif my_answer == 'rock' and computer_answer == 'scissors':
        print('Ha ha,im win')
        break

    elif my_answer == 'paper' and computer_answer == 'scissors':
        print('You Win')
        break

    else:
        print('You lose Try Again')
        
