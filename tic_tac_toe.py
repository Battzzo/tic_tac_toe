gamemap = [["1","2","3"],["4","5","6"],["7","8","9"]]

        

def multiplayer():
    game_map_reset()
    player_one = True

    for x in range(9):
        print_game_map()
        if(player_one):
            user_input = input("Player one type one number 1-8: ")
            need_again = change_game_map(user_input, "X")
            while need_again:
                user_input = input("Player one type one number 1-8: ")
                need_again = change_game_map(user_input, "X")
            player_one = False
        else:
            user_input = input("Player two type one number 1-8: ")
            need_again = change_game_map(user_input, "O") 
            while need_again:
                user_input = input("Player two type one number 1-8: ")
                need_again = change_game_map(user_input, "O")
            player_one = True
        won = check_won(player_one)

        if(won):
            return
    print_game_map()
        
def print_game_map():
    print("      |         |      ")
    print("  "+gamemap[0][0]+"   |    "+gamemap[0][1]+"    |   "+gamemap[0][2]+"  ")
    print("      |         |      ")
    print("-----------------------")
    print("      |         |      ")
    print("  "+gamemap[1][0]+"   |    "+gamemap[1][1]+"    |   "+gamemap[1][2]+"  ")
    print("      |         |      ")
    print("-----------------------")
    print("      |         |      ")
    print("  "+gamemap[2][0]+"   |    "+gamemap[2][1]+"    |   "+gamemap[2][2]+"  ")
    print("      |         |      ")

def change_game_map(number,playersymbol):
    if(number == gamemap[0][0]):
        gamemap[0][0] = playersymbol
        return False
    elif(number == gamemap[0][1]):
        gamemap[0][1] = playersymbol
        return False
    elif(number == gamemap[0][2]):
        gamemap[0][2] = playersymbol
        return False
    elif(number == gamemap[1][0]):
        gamemap[1][0] = playersymbol
        return False
    elif(number == gamemap[1][1]):
        gamemap[1][1] = playersymbol
        return False
    elif(number == gamemap[1][2]):
        gamemap[1][2] = playersymbol
        return False
    elif(number == gamemap[2][0]):
        gamemap[2][0] = playersymbol
        return False
    elif(number == gamemap[2][1]):
        gamemap[2][1] = playersymbol
        return False
    elif(number == gamemap[2][2]):
        gamemap[2][2] = playersymbol
        return False
    else:
        
        print("somthing went wrong")
        return True


def game_map_reset():
    gamemap = [["1","2","3"],["4","5","6"],["7","8","9"]]

def check_won(player):
    if(player):
        player = "Player two"
    else:
        player = "Player one"

    player_symbols = ["X","O"] 
    for x in range(2):
        if gamemap[0][0] == player_symbols[x] and gamemap[0][1] == player_symbols[x] and gamemap[0][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game")
        elif gamemap[1][0] == player_symbols[x] and gamemap[1][1] == player_symbols[x] and gamemap[1][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game")   
        elif gamemap[2][0] == player_symbols[x] and gamemap[2][1] == player_symbols[x] and gamemap[2][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game")    
        elif gamemap[0][1] == player_symbols[x] and gamemap[1][1] == player_symbols[x] and gamemap[2][1] == player_symbols[x]:
            print_game_map()
            print(player + " won the game")
        elif gamemap[0][2] == player_symbols[x] and gamemap[1][2] == player_symbols[x] and gamemap[2][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game") 
        elif gamemap[0][0] == player_symbols[x] and gamemap[1][0] == player_symbols[x] and gamemap[2][0] == player_symbols[x]:
            print_game_map()
            print(player + " won the game") 
        elif gamemap[0][0] == player_symbols[x] and gamemap[1][1] == player_symbols[x] and gamemap[2][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game")  
        elif gamemap[2][0] == player_symbols[x] and gamemap[1][1] == player_symbols[x] and gamemap[0][2] == player_symbols[x]:
            print_game_map()
            print(player + " won the game") 
        else:
            return False       
        return True
