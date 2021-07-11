
""" Python Version: 3.9.5 Creation Date: 7/11/21
Author: Henry Lee
Purpose: To creat my first successful program while integrating the knowledge of
python that i'v gathered up to this point and putting it into application. """








def start(nice=0,mean=0,name=""):
       #get user's name
       name = describe_game(name)
       nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
       """
              you should check if this is a new game or not,
              if so, get the new user's name.
              If it is not a new game, thank the user for coming back
              and continue with the game.
       """
       if name != "":
              print("\n Thank you for playing again, {}!".format(name))
       else:
              stop = True
              while stop == True:
                     if name == "":
                            name = input("\n What is your name? \n>>> ").capitalize()
                            if name != "":
                                   print('\n Welcome, {}!'.format(name))
                                   print('\n In this game you, will be greeted \nby several different people. \nYou can choose to be nice or mean,')
                                   print("but at the end of the game your fate \nwill be sealed by your actions.")
                                   stop = False

       return name

def nice_mean(nice, mean, name):
       stop = True
       while stop == True:
              show_score(nice, mean, name)
              pick = input("\n A stranger approaches you for a \nconverstation. Will you be nice \n or mean?(N/M) \n>>>: ").lower()
              if pick == "n":
                     print("\nThe Stranger walks away smiling as you give him some cash.")
                     nice = (nice + 1)
                     stop = False
              if pick == "m":
                     print("\n The stranger pushes you and walks \n away after you've insulted him.")
                     mean = (mean + 1)
                     stop = False
       score(nice, mean, name) #pass the 3 variables to the score
       
#second scenario
def nice_mean2(nice, mean, name):
       stop = True
       while stop == True:
              show_score(nice, mean, name)
              pick = input("\n A woman asks for help. Will you be nice \n or mean?(N/M) \n>>>: ").lower()
              if pick == "n":
                     print("\nYou help her and she gives you some cash.")
                     nice = (nice + 1)
                     stop = False
              if pick == "m":
                     print("\n You don't help her, but you rob her instead!")
                     mean = (mean + 1)
                     stop = False
       score2(nice, mean, name) #pass the 3 variables to the score

#third scenario
def nice_mean3(nice, mean, name):
       stop = True
       while stop == True:
              show_score(nice, mean, name)
              pick = input("\n You see a stray dog. Will you be nice \n or mean?(N/M) \n>>>: ").lower()
              if pick == "n":
                     print("\nYou feed it and it becomes your friend.")
                     nice = (nice + 1)
                     stop = False
              if pick == "m":
                     print("\n You shout at it and it runs away!")
                     mean = (mean + 1)
                     stop = False
       score(nice, mean, name) #pass the 3 variables to the score


def show_score(nice, mean, name):
       print("\n {}, your current Nice/Mean total is: \n({}, Nice) and ({}, Mean).".format(name, nice, mean))

#first score function
def score(nice, mean, name):
       #score function is being passed the values stored within the 3 variables.
       if nice > 2:# if the condition is valid, call win function passing the variables so it can use them.
              win(nice, mean, name)
       if mean > 2: #If the condition is valid, call lose function passing the the variables so it can use them.
              lose(nice, mean, name)
       else:
              nice_mean2(nice, mean, name)
              
#second score function
def score2(nice, mean, name):
       #score function is being passed the values stored within the 3 variables.
       if nice > 2:# if the condition is valid, call win function passing the variables so it can use them.
              win(nice, mean, name)
       if mean > 2: #If the condition is valid, call lose function passing the the variables so it can use them.
              lose(nice, mean, name)
       else:
              nice_mean3(nice, mean, name)


              
def win(nice, mean, name):
       print("\n Nice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!" .format(name))
       again (nice, mean, name)


def lose(nice, mean, name):
       print("\n Aww you lose. That's what you get for having bad manners!". format(name))
       again(nice, mean, name)
       

def again(nice, mean,name):
       stop = True
       while stop == True:
              choice = input("\n Do you want to play again? (y/n):\n>>> ").lower()
              if choice == "y":
                     stop = False
                     reset(nice, mean, name)
              if choice == "n":
                     print("\n Oh, so sorry to see you go!")
                     stop = False
                     quit()
              else:
                     print("\n Enter (Y) for 'YES' , (N) for 'NO': \n>>>")

def reset(nice, mean, name):
       nice = 0
       mean = 0
       #don't reset the name as the same person is still playing
       start(nice, mean, name)
              

if __name__ == "__main__":
       start()
