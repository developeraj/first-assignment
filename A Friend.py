print("Hii....")
print("What is your name?")
#myName = input()
#print("Nice to meet you " + myName)
print("From where do you belong?")
#cameFrom = input()
#print("OH! my mom is also from " + cameFrom + ".")
print ("what type of games do you play in this Quarantine period.")
print("online/offline")
print("Plz enter in the format used above:")
games = ("XYz") 
def function:
    if(games == 'online'):
        print("My mom says that children shouldn't play online games.")
        print("you shouldn't also play online games.")
        print("Will you not play online games.")
        print("yes or no")
        print("Instruction :- please answer in small letters and only yes or no")
        AnsWer = input()
        if(AnsWer == 'yes'):
            print("that's Good ^__^")
        elif(AnsWer == 'no'):
            print("I'm just giving you advice as a friend")
            print("Your life your decisions")
        else:
            print("Invalid format used please restart the game.")
    elif(games == 'offline'):
        print("Which one?")
        Which = input ()
        print('Is ' + Which + " available on playstore?")
        isThis = input()
        if(isThis == 'yes'):
            print("That's Good because I have an Android phone")
        elif(isThis == 'no'):
            print("That's Bad But I'll try to do something anyway")
        else:
            print("Ok I'll try")
    else:
        print("Invalid format used please restart the game")

while((games != "online") or "offline"):
    #print("Plz try again and enter in valid format")
    games = input()
    print("Ok Byeee....")
print("See you later, Alligator")
print('press any key to exit')
ExIt = input()

