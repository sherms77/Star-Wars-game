# Star Wars Trivia Game

# Question variables q1 - q10
q1 = """Who was Luke's real father?
a.Yoda
b.Lando
c.Darth Vader"""
q2 = """What colour is Darth Vader's lightsaber?
a.Yellow
b.Red
c.Blue"""
q3 = """What colour is Yoda?
a.Green
b.Blue
c.Purple"""
q4 = """In what movie does Luke use a green lightsaber?
a.Revenge of the Sith
b.The Last Jedi
c.Return of the Jedi"""
q5 = """What is the name of Han Solo's ship?
a.The Starship Enterprise
b.The Millennium Falcon
c.The Delorian"""
q6 = """What number episode is Star Wars?
a.IV
b.VII
c.V"""        
q7 = """What is the name of the space station in Star Wars?
a.Mount Doom
b.Hog Warts
c.The Death Star"""
q8 = """Who killed Han Solo?
a.Kylo Ren
b.Luke Skywalker
c.The Emperor"""         
q9 = """Who is Jango Fett's son?
a.R2D2
b.Boba Fett
c.Anakin Skywalker"""             
q10 = """What is the name of the order Darth Sidious gives the clone troopers, which means that they will kill all Jedi?
a.Order 72
b.Order 93
c.Order 66"""

import random, datetime 
questions = {q1:'c', q2:'b', q3:'a', q4:'c', q5:'b', q6:'a', q7:'c', q8:'a', q9:'b', q10:'c'} # questions and answers dictionary
allQs = list(questions.keys()) # saves dictionary as a list in a variable
score = 0
leaderBoard = {} # leaderboard

print("**********WELCOME TO THE STAR WARS TRIVIA GAME**********")
print("\n************THIS IS FOR THE FAURE KIDS******************")

def mainMenu():
    print("\nMAIN MENU")
    print("Choose one of the options below by selecting a number and then press enter.")
    print("1.Game rules \n2.Leaderboard \n3.Previous scores \n4.Play game \n5.Quit")
    menuChoice = input("\nEnter your choice: ")

    if menuChoice == '1':
        gameRules()
    elif menuChoice == '2':
        lBoard()
    elif menuChoice == '3':
        showScore()
    elif menuChoice == '4':
        game()
    elif menuChoice == '5':
        saveScores() # saves scores to .txt file on exit
        quit()
    else:
        print("Invalid input try again.")
        mainMenu() # recursive call
        
def returnMain():
    while True:
        rMainmenu = input("Press m and enter to return to the main menu or q and enter to quit: ")
        if rMainmenu not in ('m', 'q'):
            print("INVALID INPUT. ENTER m or q.\n")
        else:
            break    
    if rMainmenu == 'm':
            mainMenu()
    elif rMainmenu == 'q':
            saveScores() # saves scores to .txt file on exit
            quit()
    
def gameRules():
    print("\nGAME RULES")
    print("""1.The player will be asked five multiple choice questions.
             2.Each question has three choices.
             3.If the player chooses the correct answer they will be given 1 point.",
             4.If the player chooses the incorrect answer they will be given 0 points.",
             5.After all five questions are asked the player will be given a total score out of 5.\n""")
    returnMain()
    
def saveScores():
    scoreFile = open('scoreData.txt', 'a') # appends the updated dictionary and saves file to cwd
    stamp = datetime.datetime.now()
    scoreFile.write('\nGame date: ')
    scoreFile.write(str(stamp))
    scoreFile.write(' Scores: ')
    scoreFile.write(str(leaderBoard)) 
    scoreFile.close()
    
def showScore():    
    try:
        scoreFile = open('scoreData.txt')
    except FileNotFoundError:
        print("""Previous scores are displayed here after you have played a game.
                 Your scores are saved when you quit. 
                 Play a game to start saving scores.
                 You will now return to main menu.""")
        mainMenu()
    else:
        print("Previous game scores below.")
        data = scoreFile.read()
        print(data)
        scoreFile.close()
        returnMain()
        
def lBoard():
    print("\nLEADERBOARD")
    if len(leaderBoard) ==  0:
        print("No games have been played yet, so no scores have been saved. \nPlay a game to save a score. \nYou will now return the main menu.")
        mainMenu()
    else:
        print("Your name and score is displayed below.")
        sortPlayers = sorted(leaderBoard.items(), key=lambda x: x[1], reverse=True) # this sorts scores in descending order.
        for i in sortPlayers:
            print(i[0], i[1])
        returnMain()

def game():
    global score
    print("\nGAME")
    name = input("Please enter your name and press enter: ")
    print("Welcome " + name)
    print("You will now have to answer 5 questions. Each correct answer is worth 1 point.")
    input("Press enter to continue...\n")
    random.shuffle(allQs) # list is shuffled everytime you enter the function
    
    for q in allQs[:5]:
            while True:
                print(q)
                ans = input("Enter your answer: ")
                if ans not in ('a', 'b', 'c'): # loops the same question until valid input entered
                    print("\nINVALID INPUT, TRY AGAIN. \n") 
                elif ans == questions[q]:                 
                    print("\nYou are correct! You have scored 1 point.")
                    score += 1
                    print("Score:",score, "\n")
                    break # if correct answer breaks loop and goes to next question
                else:
                    print("\nYou are wrong. No points scored.")
                    print("The correct answer is: ", questions[q])
                    print("Score:",score, "\n")
                    break  # if incorrect answer (but valid input) breaks loop and goes to next question            
    
    print(name, "- Your total is:",score,"out of 5.\nYou can view your score by choosing the Leaderboard option from the Main Menu.\n")
    leaderBoard[name] = score
    score = 0 # resets score to 0
    returnMain()
    
mainMenu()