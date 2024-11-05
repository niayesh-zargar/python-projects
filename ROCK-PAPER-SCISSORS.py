# player and pc 
# input from player
# pc randomly choose => random 
# 3 times repit 
# winner
import random
user_point = int('0')
pc_point = int('0')
GameRunning = True
print ("'p' means paper\n'r' means rock \n's' means scissors " )

def winner ():
    global user_point
    global pc_point
    if user == pc :
        print("it's a tie.")
    elif user == 's':
        if pc == 'r':
            pc_point += 1 
        else:
            user_point += 1
    elif user == 'p':
        if pc == 'r':
            user_point += 1 
        else :
            pc_point += 1 
    elif user == 'r':
        if pc == 'p':
            pc_point += 1 
        else :
            user_point += 1
    
    print(f'you\'r point :{user_point} \t 🤖\'s point :{pc_point} ')
    
while  GameRunning :
    user= input("you : ").lower()
    if  not user in ['r','p','s'] :
        print("invalid choose.")
        continue
    pc = random.choice(['r','p','s'])
    print(f'🤖 : {pc}')
    winner()
    if user_point == 3 :
        print("Congratulations! You win the game! 🎉")
        GameRunning = False
    elif pc_point == 3 :
        print("🤖 wins the game! Better luck next time!")
        GameRunning = False