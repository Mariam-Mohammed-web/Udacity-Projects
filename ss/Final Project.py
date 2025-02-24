import time 

def print_pause(writings , seconds):
    print(writings)
    time.sleep(seconds)

def stop_game_lost ():
    print("you lost the end of the game")

def stop_game_win ():
    print("you win want to play again?")

def while_True ( no1,text1,sec1,x,no2,text2,sec2,y):
    your_choice= input("Please enter 1 or 2")
    while True:
        if your_choice == no1 :
            print_pause(text1,sec1)
            x
            break
        elif your_choice == no2 :
            print_pause(text2,sec2)
            y
            break
        else:
            your_choice = input("Please enter 1 or 2")

def help_in_cold_3():
    print_pause("she takes the medicin and then feels better ",2)
    print_pause("but you find there is no food in the house ",2)
    print_pause("so what will you do bring food or clean the house ?",2)
    print_pause("Enter 1 to bring food",2)
    print_pause("Enter 2 to clean the house",2)
    player_choice = input("Please enter 1 or 2")
    while True:
        if player_choice == "1":
            print_pause("great job now they are feeling better",2)
            stop_game_win()
            break
        elif player_choice == "2":
            print_pause("oops! she is starving and you go to clean !?",2)
            stop_game_lost()
            break
        else:
            player_choice = input("Please enter 1 or 2")

def help_in_cold_2 ():
    print_pause("they thank you very much but you find his mum very sick",2)
    print_pause("what are you going to do go and take her to the club or bring her medecin ?",2)
    print_pause("Enter 1 to take her to the club",2)
    print_pause("Enter 2 to bring her medecine",2)
    player_choice = input("Please enter 1 or 2")
    while True:
        if player_choice == "1":
            print_pause("oops! how can you play with her she is sick !?",2)
            stop_game_lost()
            break
        elif player_choice =="2":
            print_pause("well done you are very kind :D ",2)
            help_in_cold_3()
            break
        else:
            player_choice= input("Please enter 1 or 2")

def help_in_cold ():
    print_pause("you find his house very old and dilapidated",2)
    print_pause("the windows are broken and the wind and the snow are blowing",2)
    print_pause("what are you going to do light a fire or build a window?",2)
    print_pause("Enter 1 to light a fire",2)
    print_pause("Enter 2 to build a window",2)
    player_choice = input("Please enter 1 or 2")
    while True:
        if player_choice == "1":
            print_pause("oops! the wind and snow are blowing very hard so the fire is off",2)
            stop_game_lost()
        elif player_choice == "2":
            print_pause("very good now the wind and the snow cant enter the house so they can feel warmer",2)
            help_in_cold_2()
        else:
            player_choice =input("Please enter 1 or 2")

def cold_weather ():
    print_pause("today's weather is very cold and it's snowing" , 2)
    print_pause("and suddenly while you are walking You find a small boy on the street " , 2)
    print_pause("he is shivering from the cold" , 2)
    print_pause("what will you do help him or leave him ?" ,2)
    print_pause("Enter 1 to help him" ,2)
    print_pause("Enter 2 to leave him", 2)
    player_choice = input("please enter 1 or 2")
    while True:
        if player_choice == "1":
            print("great now lets go to his house to help him")
            help_in_cold()
            break
        elif player_choice == "2":
            print("oops!! you lost bec. you didnt help him")
            stop_game_lost()
            break
        else:
            player_choice = input("please enter 1 or 2")

def help_in_storm_3 ():
    print_pause("the doctor asked him to take some medication",2)
    print_pause("but you realize that he cant afford it",2)
    print_pause("so what will you do bring him medication or go to zoo",2)
    print_pause("Enter 1 to bring him medication",2)
    print_pause("Enter 2 to go to the zoo",2)
    your_choice = input("PLease enter 1 or 2")
    while True:
        if your_choice == "1":
            print_pause("Perfect now he can feel better",2)
            stop_game_win()
            break
        elif your_choice == "2":
            print_pause("oops ! how can he heal without medication !?",2)
            stop_game_win()
            break
        else:
            your_choice = input("Please enter 1 or 2")

def help_in_storm_2 ():
    print_pause("now he is better and he can breathe but he is still ill",2)
    print_pause("is suffering from sinus sensitivity",2)
    print_pause("so what will you do ?",2)
    print_pause("get him to the doctor or take him to the gym ?",2)
    print_pause("Enter 1 to get him to the doctor",2)
    print_pause("Enter 2 to take him to the gym",2)
    your_choice = input("Please enter 1 or 2")
    while True:
        if your_choice == "1":
            print_pause("excellent !! now take a taxi and go there",2)
            help_in_storm_3()
            break
        elif your_choice == "2":
            print_pause("oops! he is ill he cant go to the gym")
            stop_game_lost()
            break
        else:
            your_choice = input("Please enter 1 or 2")

def help_in_storm ():
    print_pause("as we mentioned before he cant breathe",2)
    print_pause("what will you do bring her a mask or bring her food ?",2)
    print_pause("Enter 1 to bring her a mask",2)
    print_pause("Enter 2 to bring her food",2)
    your_choice = input("Please enter 1 or 2")
    while True:
        if your_choice == "1":
            print_pause("well done !! now she will avid breathing the dust",2)
            help_in_storm_2()
            break
        elif your_choice == "2":
            print_pause("oops! what will she do with food 1 !?",2)
            stop_game_lost()
            break
        else:
            your_choice=input("Please enter 1 or 2")

def stormy_weather ():
    print_pause("today's weather is stormy and there is dust you cant even see",2)
    print_pause("and suddenly you find a small boy on the street",2)
    print_pause("he is suffering from dust and he cant breathe",2)
    print_pause("what will you do help him or leave him ?",2)
    print_pause("Enter 1 to help him",2)
    print_pause("Enter 2 to leave him",2)
    your_choice = input("Please enter 1 or 2",2)
    while True:
        if your_choice =="1":
            print_pause("great lets go and help him",2)
            help_in_storm()
            break
        elif your_choice == "2":
            print_pause("oops! you lost bec. you didnt help him",2)
            stop_game_lost()
            break
        else :
            your_choice = input("Please enter 1 or 2")

def help_in_hot_2 ():
    print_pause("as we mentioned before she is suffering from sunstroke",2)
    print_pause("so what will you do to reduce her body temperature",2)
    print_pause("pour cold water on her or pour hot water ?",2)
    print_pause("Enter 1 to pour cold water on her",2)
    print_pause("Enter 2 to pour hot water on her",2)
    your_choice = input("Olease enter 1 or 2")
    while True:
        if your_choice == "1":
            print_pause("well done ! now you have reduced her body temperature and she is feeling better",2)
            stop_game_win()
            break
        elif your_choice == "2":
            print_pause("oops! her body temperature increased and now she got worse",2)
            stop_game_lost()
            break
        else:
            your_choice = input("Please enter 1 or 2")

def help_in_hot():
    print_pause("as we mentioned before she is very thirsty ",2)
    print_pause("what will you do bring her a bottle of water to drink or bring her food to eat?",2)
    print_pause("Enter 1 to bring her water",2)
    print_pause("Enter 2 to bring food")
    your_choice = input("Please enter 1 or 2")
    while True:
        if your_choice == "1":
            print_pause("great job ! now she feels better")
            help_in_hot_2()
            break
        elif your_choice == "2":
            print_pause("oops! she is thirsty not hungry")
            stop_game_lost()
            break
        else:
            your_choice = input("Please enter 1 or 2")

def hot_weather () :
    print_pause("today's weather is hot and the sun is burning the skin",2)
    print_pause("and suddenly you find a small girl on the street ",2)
    print_pause("she is suffering from thirst and sunstroke",2)
    print_pause("what will you do help her or leave her ?",2)
    print_pause("Enter 1 to help her",2)
    print_pause("Enter 2 to leave her",2)
    print_pause("So what will you do?",2)
    while_True("1","2","great lets go and help her",2,"oops! you lost bec. you didnt help her",2,help_in_hot,stop_game_lost)
   
print_pause("Hi in this game you are trying to help people in different weathers" , 2)
print_pause("now you have three sitiuations and you have to choose one of them" , 2)
print_pause("Enter 1 to help people in cold weather ", 2)
print_pause("Enter 2 to help people in hot weather " , 2)
print_pause("Enter 3 to help people in stormy weather " , 2)
print_pause("so what will you choose" , 2)
your_choice = input("Please Enter 1, 2 or 3")
while True :
    if your_choice == "1":
        cold_weather()
        break
    elif your_choice == "2":
        hot_weather()
        break
    elif your_choice == "3":
        stormy_weather()
        break
    else :
       your_choice=  input("please enter 1, 2 or 3")
        

        

