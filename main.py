#grrkek
import random

def computer():
    num = random.randint(1,3)
    if (num<2):
        return ('rock')
    elif(num>2):
        return ('scissors')
    else:
        return ('paper')

def main():
    user_pick=input("please type rock, paper or scissors: ")
    pc_pick=computer()
    print('the computer has picked', pc_pick)
    result(pc_pick,user_pick)

def result(n1,n2):
    if(n1==n2):
        print('Draw, please try again')
        main()
    elif(n1=='rock' and n2=='scissors'):
        print('computer wins')
    elif (n1 == 'scissors' and n2 == 'paper'):
        print('computer wins')
    elif (n1 == 'paper' and n2 == 'rock'):
        print('computer wins')
    elif (n2 == 'rock' and n1 == 'scissors'):
        print('you win')
    elif (n2 == 'scissors' and n1 == 'paper'):
        print('you win')
    elif (n2 == 'paper' and n1 == 'scissors'):
        print('you win')
    else:
        print('Error, You have not typed rock, paper or scissors please tpye one of the three correct and try again')
        main()
main()