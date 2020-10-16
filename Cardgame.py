import random
import time


def games():
    colour = ["Red", "Black"]  # colours of cards
    deck = []  #deck

    for i in range(20):
        x = random.randint(1,20)
        y = random.choice(colour)
        deck.append([x, y])
    return deck

decks = games() # store the results of the function games

player1 =input("Player 1, Enter your name :") # ask player1's name
player2 =input("Player2, Enter your name :")  # ask player2's name

time.sleep(1)
print("Starting Game...")
time.sleep(1)

random.shuffle(decks)  #shuffle decks

p1score = 0  #record player1 score
p2score = 0

while True :
    print("")

    if not decks: # check if deck is empty
        break    # exits while loop if deck is empty

    while True:
        play1 = input("Player 1: {} enter x to pick the top card : ".format(player1))  # input from player1
        card1 = decks.pop(0)
        if play1 =="x":
            break

    print("Player1: {} your card drawn from top of the deck is {} {}".format(player1, card1[0], card1[1])) # output


    if not decks: # check if deck is empty
     break   # exits the while loop if deck is empty

    while True:
        play2 = input("Player 2: {} enter x to pick the top card : ".format(player2)) # input from player2
        card2 = decks.pop(0)
        if play2 == "x":
            break

    print("Player2: {} your card drawn from top of the deck is {} {}".format(player2, card2[0], card2[1]))


    if card1[0] > card2[0]:    # player1's card is greater than player2'card
        print("Player1:{} You have won the cards".format(player1))  # player1 won

    elif card1[0] < card2[0]:  # player1's card is less than player2's card
        print("Player2:{} you have won the cards".format(player2)) # player2 won
        p2score +=2  # increment by 2

    if card1[0] == card2[0] and card1[1] =="Red": # if player1's card has the same number as player2's card, then red card wins
        print("{} Your cards are the same number, but player1's{} card is red so they win the cards ".format(player1, player2))  # print output
        p1score +=2  #increment by 2

    elif card2[0] ==card1[0] and card2[1] =="Red":  #if player2's card has the same number as player1's card , then red card wins
        print("{} Your cards are the same number, but player2's{} card is red so they win the cards ".format(player2, player1)) #print output
        p1score += 2

    print("player1 {} score: {}        player2 {} score: {}".format(player1, p1score, player2, p2score))  # print play1 and play2 score
    time.sleep(1)


print("")


if p1score > p2score: # player1 card is greater than player2
    print("Congratulations player1: {} you've  won the game with {} cards" .format(player1, p1score)) # print output
else:
    print("Congratulations palyer2: {} you've won the game with {} cards".format(player2, p2score)) # print output
print("")
print("games is over")