import random # to import random module
import time #to import time module

Player_Score = 0#the variable of score before playing

def win_or_lose ():
        if Player_Score <9:
            print("You lost")
        elif Player_Score >=9:
            X = ["Hurray you Won","Congratulations you Won","You are a Hero"]
            choose = random.choice(X)

def total_score_counter(x): #a function to calculate the player's score
    global Player_Score
    if x == "1":
       Player_Score +=3
    else :
       Player_Score
    return Player_Score
        
def THE_GAME (): #the function that contains the whole game

    def print_pause(writings , seconds):#a function to make each line appeare after the other line by specific time 
        print(writings)
        time.sleep(seconds)

    def help_in_cold_3(): # a function that contains a scene from the cold weather story
        print_pause("she takes the medicin and then feels better ",2)
        print_pause("but you find there is no food in the house ",2)
        print_pause("so what will you do bring food or clean the house ?",2)
        print_pause("Enter 1 to bring food",2)
        print_pause("Enter 2 to clean the house",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("great job now they are feeling better",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            elif your_choice == "2":
                print_pause("oops! she is starving and you go to clean !?",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")
    
    def help_in_cold_2 ():# a function that contains a scene from the cold weather story
        print_pause("they thank you very much but you find his mum very sick",2)
        print_pause("what are you going to do?",2)
        print_pause("go and take her to the club or bring her medecin ?",2)
        print_pause("Enter 1 to bring her medecation",2)
        print_pause("Enter 2 to take her to the club",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("well done you are very kind :D",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_cold_3()
                break
            elif your_choice =="2":
                print_pause("oops! how can you play with her she is sick !?",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice= input("Please enter 1 or 2")
        
    def help_in_cold ():# a function that contains a scene from the cold weather story
        print_pause("you find his house very old and dilapidated",2)
        print_pause("the windows are broken and the wind and the snow are blowing",2)
        print_pause("what are you going to do light a fire or build a window?",2)
        print_pause("Enter 1 to build a window",2)
        print_pause("Enter 2 to light a fire",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("very good now the wind and the snow can't enter the house ",2)
                print_pause("so they can feel warmer",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_cold_2()
                break
            elif your_choice == "2":
                print_pause("oops! the wind and snow are blowing very hard",2)
                print_pause("so the fire is off",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice =input("Please enter 1 or 2")
    
    def cold_weather ():# a function that contains the start of cold weather story
        print_pause("today's weather is very cold and it's snowing",2)
        print_pause("and suddenly while you are walking",2)
        print_pause("You find a small boy on the street ",2)
        print_pause("he is shivering from the cold" , 2)
        print_pause("what will you do help him or leave him ?" ,2)
        print_pause("Enter 1 to help him" ,2)
        print_pause("Enter 2 to leave him", 2)
        your_choice = input("please enter 1 or 2")
        while True:
            if your_choice == "1":
                print("great now lets go to his house to help him")
                total_score_counter("1")
                print("Your score is") 
                print(Player_Score)
                help_in_cold()
                break
            elif your_choice == "2":
                print("oops!! you lost bec. you didnt help him")
                total_score_counter("2")
                print("Your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("please enter 1 or 2")
        
    def help_in_storm_3 ():# a function that contains a scene from the stormy weather story
        print_pause("the doctor asked him to take some medication",2)
        print_pause("but you realize that he cant afford it",2)
        print_pause("so what will you do bring him medication or go to zoo",2)
        print_pause("Enter 1 to bring him medication",2)
        print_pause("Enter 2 to go to the zoo",2)
        your_choice = input("PLease enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("Perfect now he can feel better",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            elif your_choice == "2":
                print_pause("oops ! how can he heal without medication !?",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")

    def help_in_storm_2 ():# a function that contains a scene from the stormy weather story
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
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_storm_3()
                break
            elif your_choice == "2":
                print_pause("oops! he is ill he cant go to the gym")
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")

    def help_in_storm ():# a function that contains a scene from the stormy weather story
        print_pause("as we mentioned before he cant breathe",2)
        print_pause("what will you do bring her a mask or bring her food ?",2)
        print_pause("Enter 1 to bring her a mask",2)
        print_pause("Enter 2 to bring her food",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("well done !! now she will avid breathing the dust",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_storm_2()
                break
            elif your_choice == "2":
                print_pause("oops! what will she do with food 1 !?",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice=input("Please enter 1 or 2")

    def stormy_weather ():# a function that contains the start of stormy weather story
        print_pause("today's weather is stormy and there is dust you cant even see",2)
        print_pause("and suddenly you find a small boy on the street",2)
        print_pause("he is suffering from dust and he cant breathe",2)
        print_pause("what will you do help him or leave him ?",2)
        print_pause("Enter 1 to help him",2)
        print_pause("Enter 2 to leave him",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice =="1":
                print_pause("great lets go and help him",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_storm()
                break
            elif your_choice == "2":
                print_pause("oops! you lost bec. you didnt help him",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else :
                your_choice = input("Please enter 1 or 2")

    def help_in_hot_2 ():# a function that contains a scene from the hot weather story
        print_pause("as we mentioned before she is suffering from sunstroke",2)
        print_pause("so what will you do to reduce her body temperature",2)
        print_pause("pour cold water on her or pour hot water ?",2)
        print_pause("Enter 1 to pour cold water on her",2)
        print_pause("Enter 2 to pour hot water on her",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("well done ! now you have reduced her body temperature",2)
                print_pause("and she is feeling better",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            elif your_choice == "2":
                print_pause("oops! her body temperature increased",2)
                print_pause("and now she got worse",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")

    def help_in_hot():# a function that contains a scene from the hot weather story
        print_pause("as we mentioned before she is very thirsty ",2)
        print_pause("what will you do ?",2)
        print_pause("bring her a bottle of water to drink or bring her food to eat?",2)
        print_pause("Enter 1 to bring her water",2)
        print_pause("Enter 2 to bring food",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("great job ! now she feels better",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_hot_2()
                break
            elif your_choice == "2":
                print_pause("oops! she is thirsty not hungry",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")

    def hot_weather () :# a function that contains the start of the hot weather story
        print_pause("today's weather is hot and the sun is burning the skin",2)
        print_pause("and suddenly you find a small girl on the street ",2)
        print_pause("she is suffering from thirst and sunstroke",2)
        print_pause("what will you do help her or leave her ?",2)
        print_pause("Enter 1 to help her",2)
        print_pause("Enter 2 to leave her",2)
        print_pause("So what will you do?",2)
        your_choice = input("Please enter 1 or 2")
        while True:
            if your_choice == "1":
                print_pause("great lets go and help her",2)
                total_score_counter("1")
                print("your score is")
                print(Player_Score)
                help_in_hot()
                break
            elif your_choice == "2":
                print_pause("oops! you lost bec. you didnt help her",2)
                total_score_counter("2")
                print("your score is")
                print(Player_Score)
                win_or_lose()
                break
            else:
                your_choice = input("Please enter 1 or 2")


    # the start of the game 
    print_pause("Hi in this game ",1)
    print_pause("you are trying to help people in different weathers" , 2)
    print_pause("now you have three sitiuations",1)
    print_pause("and you have to choose one of them" , 2)
    print_pause("Enter 1 to help people in cold weather ", 2)
    print_pause("Enter 2 to help people in hot weather " , 2)
    print_pause("Enter 3 to help people in stormy weather " , 2)
    print_pause("so what will you choose" , 2)
    global your_choice
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

def Restart_Game (): # a function that restarts the game
    your_choice = input("Want to play again y/n ?")
    global Player_Score
    Player_Score =0
    while True:
        if your_choice == "y":
            THE_GAME()
            Restart_Game()
            break
        elif your_choice == "n":
            print("Thanks for playing :)")
            break
        else:
            your_choice= input("Please enter y/n")

THE_GAME()
Restart_Game()
