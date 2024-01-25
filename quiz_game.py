print("Welcome to my motorsport quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Let's Play") 
score = 0   

answer = input("How many Driver championships does Sebastian Vettal have? ")
if answer.lower() == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow")    

answer = input("Lewis Hamilton won his first Formula One World Championship title while racing for which team? ")
if answer.lower() == "mclaren":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow")    

answer = input("When did Michael Schumacher make his debut? ")
if answer.lower() == "1991":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow")    

answer = input("Mick Schumacher was on course for his first F1 points in 2022 before colliding with who in Miami? ")
if answer.lower() == "sebastian vettel":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow")    

answer = input("How many cars reached the chequered flag in the 2022 Saudi Arabia Grand Prix? ")
if answer.lower() == "13":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow")    

answer = input("Kevin Magnussen made a stunning return to Formula 1 in 2022 with what result in Bahrain? ")
if answer.lower() == "6":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow") 

answer = input("At the 2021 Azerbaijan Grand Prix, Max Verstappen and which other driver suffered tyre blowouts during the race? ")
if answer.lower() == "lance stroll":
    print("Correct!")
    score += 1
else:
    print("Incorrect - you slow") 

print("You got " + str(score) +  " Questions correct")
print("You got " + str((score / 7) * 100) + "%")