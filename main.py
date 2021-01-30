import tic_tac_toe as ttt


while(True):
    
    user_input = input("nTo start a game type 'start'  \nTo end the programm type 'end' \nYour Input: ")

    if user_input == "start":
        ttt.multiplayer()
    elif user_input == "end" :
        break
    else:
        print("Input was not exepted")

def singelplayer():
    pass

def multiplayer():
    pass
