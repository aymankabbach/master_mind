import random
winner=False
End_of_the_game=False
colors=["Yellow","Purple","Pink","Red","Blue","Green"]
computer_color=[]
def choose_randomly_four_color():
    global colors
    for x in range(4):
        computer_color.append(random.choice(colors))
    return computer_color
def show_options_to_the_player():
    x=0
    for color in colors:
        print(x+1,color)
        x+=1
def read_player_choice():
    player_choice=input("choose a color")
    return player_choice
def is_player_choice_integer():
    try:
        player_choice=int(read_player_choice())
    except ValueError:
        return False
    else:
        return player_choice
def is_player_choice_valid():
    player_choice=is_player_choice_integer()
    if player_choice!=False:
        if player_choice>=1 and player_choice<=len(colors):
            return colors[player_choice-1]
        else:
            return False
    else:
        return False
def let_the_player_choose_colors():
    players_colors=[]
    while len(players_colors)<4:
        player_choice=is_player_choice_valid()
        if player_choice!=False:
            players_colors.append(player_choice)
        else:
            print("invalid input")
    return players_colors
def is_the_color_right_and_in_the_right_position(computer_color_clone,players_colors_clone,judgment):
    position=0
    for POSITION in range(4):
        if players_colors_clone[position] == computer_color_clone[position]:
            judgment.append("B")
            players_colors_clone.remove(players_colors_clone[position])
            computer_color_clone.remove(computer_color_clone[position])
        else:
            position+=1
    return judgment
def is_the_color_exist(computer_color_clone,players_colors_clone,judgment):
    position=0
    for position in range(len(computer_color_clone)):
        if players_colors_clone[position] in computer_color_clone:
            judgment.append("W")
            computer_color_clone.remove(players_colors_clone[position])
        else:
            judgment.append("N")
    return judgment
def judging(computer_color_clone,players_colors_clone):
    judgment=[]
    judgment=is_the_color_right_and_in_the_right_position(computer_color_clone,players_colors_clone,judgment)
    judgment=is_the_color_exist(computer_color_clone,players_colors_clone,judgment)
    random.shuffle(judgment)
    print(judgment)
    return judgment
def check_win(judgment):
    global winner
    if judgment==["B","B","B","B"]:
        winner=True
        print("you win")
    else:
        judgment=[]
    return judgment
def start_game():
    global winner,End_of_the_game
    attempts=0
    computer_color=choose_randomly_four_color()
    print("try to guess the 4 colors choosen by the computer")
    print("'B' means the color is correct and in in the right position\n'W' means the color is correct but not in the right position\n'N' means the color doesn't exist")
    while winner==False and End_of_the_game==False:
        computer_color_clone=[color for color in computer_color]
        print(f"attempts left {10-attempts}")
        show_options_to_the_player()
        players_colors=let_the_player_choose_colors()
        players_colors_clone=[color for color in players_colors]
        print(f"the color that you choose are {players_colors}")
        judgment=judging(computer_color_clone,players_colors_clone)
        judgment=check_win(judgment)
        if winner==False:
            attempts=attempts+1
        if attempts==10:
            End_of_the_game=True
            print("GAME OVER")
            print(f"computer's color were {computer_color}")
        print("----------")
start_game() 
