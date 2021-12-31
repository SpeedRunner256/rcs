import json; import random
#Importing the json and asking the users name
save = {}
with open('savedata.json') as saved:
    save = json.load(saved)
save['username'] = str(input("What is your name? "))
print("your name is", save['username'])

#Asking user to start playing or exit:
playing = str(input("Do you wanna play? "))
while playing == "yes":
    compresonse = random.randint(0,2)
    #Say 0 is rock, 1 is paper and 2 is scissor
    humanresponse = str(input("Start by typing rock, paper or scissor: "))
    if humanresponse == "rock":   humanresponse = 0
    elif humanresponse == "paper":  humanresponse = 1
    elif humanresponse == "scissor":    humanresponse = 2
    else:
        print("Maybe you should write something useful lol, for now you should restart")
        continue
    #game code
    #player wins
    if compresonse == humanresponse:
        print("That's a draw! Nobody wins or loses!")
        save['totalgames'] += 1
    elif compresonse == 0 and humanresponse == 1:
        print("The computer picked rock while you picked paper, thus thats a win for the player!")
        save['win'] += 1
        save['totalgames'] += 1

    elif compresonse == 1 and humanresponse == 2:
        print("The computer picked paper and you picked scissor, thus thats a win for the player!")
        save['totalgames'] += 1
        save['win'] += 1

    elif compresonse == 2 and humanresponse == 0:
        print("The computer picked scissor while you picked rock, this thats a win for the player!")
        save['win'] += 1
        save['totalgames'] += 1

    elif humanresponse == 0 and compresonse == 1:
        print("The computer picked paper while you picked rock, thus this is a loss for the player!")
        save['loss'] += 1
        save['totalgames'] += 1

    elif humanresponse == 1 and compresonse == 2:
        print("The computer picked scissor while you picked paper, thus thats a loss for the player!")
        save['loss'] += 1
        save['totalgames'] += 1

    elif humanresponse == 2 and compresonse == 0:
        print("The computer picked rock while you picked scissor, thus thats a loss for the player!")
        save['loss'] += 1
        save['totalgames'] += 1

    #calculating winrate and lossrate
    #making sure to not divide by zero
    if save['totalgames'] != 0:
        save['winrate'] = (save['win']/save['totalgames'])*100
        save['loserate'] = (save['loss']/save['totalgames'])*100
        print("Your current winrate is",save['winrate'],"percent and your current lossrate is",save['loserate'],"percent")
    else:
        print("You haven't played a game yet, so we cant determine your win or loss rate!")
    playing = str(input("Do you want to play again? "))
else:
    print("Thats a wrap!")
    with open('savedata.json', 'w') as saved:
        json.dump(save,saved)
    print("Your staticstics are as follows: \n", save)
    exit()