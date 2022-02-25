# Programmers: Fady
# Start Date: Tuesday January 11, 2022
# End Date: Tuesday January 25, 2022

# Game Name: BlackJack
# File Name: BlackJack.py

# Description: Blackjack is a game where players compete
# against the house rather than against each other.
# The objective is to get a hand sum closer to 21
# than the dealer without going over 21, known as busting.
# At the start of a Blackjack game,
# the players and the dealer receive two cards each.
# The players' cards are normally shown,
# while the dealer has one card shown and another hidden.
# The dealer will always stand on 17, aces can be worth 11 or 1,
# and all face cards are worth 10.
# The player and the cpu both have a max hand of 5 cards.


# Importing funtions
from graphics import *      # graphics module used to create graphics
from cbutton import *       # cbutton module used to create usable buttons
import random               # random module used to randomize the hands
import time                 # time module used to delay some actions
import winsound             # winsound module used to create sound effects
from operations import *    # operations module used to add pot to balance


# function tpo make the game GUI
def createsGUI():
    """making GUI for BlackJack game

    Arguments:
        n(graphics): GUI

    Returns:
        graphics: makes the GUI
    """
    # set background color
    win.setBackground(color_rgb(6, 103, 27)) 

    # user score oval
    userScoreOval = Oval(Point(180, 75), Point(620, 205))
    userScoreOval.draw(win)
    userScoreOval.setFill(color_rgb(8, 148, 32))
    userScoreOval.setOutline(color_rgb(0, 0, 0))
    userScoreOval.setWidth(4)

    # user score lines
    scoreLine1 = Line(Point(330, 75), Point(330, 200))
    scoreLine1.draw(win)
    scoreLine1.setWidth(4)
    scoreLine1 = Line(Point(470, 75), Point(470, 200))
    scoreLine1.draw(win)
    scoreLine1.setWidth(4)

    # card box
    cardBox = Rectangle(Point(180, 0), Point(620, 140))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(8, 128, 32))
    cardBox.setOutline(color_rgb(0, 0, 0))
    cardBox.setWidth(4)

    # cpu score circle
    cpuScoreCircle = Circle(Point(620, 780), 70) 
    cpuScoreCircle.draw(win)
    cpuScoreCircle.setFill(color_rgb(8, 148, 32))
    cpuScoreCircle.setOutline(color_rgb(0, 0, 0))
    cpuScoreCircle.setWidth(4)

    # cpu card box
    cpuCardBox = Rectangle(Point(180, 710), Point(620, 850))
    cpuCardBox.draw(win)
    cpuCardBox.setFill(color_rgb(8, 128, 32))
    cpuCardBox.setOutline(color_rgb(0, 0, 0))
    cpuCardBox.setWidth(4)

    # cpu Text
    cpuText = Text(Point(400, 885), "CPU")
    cpuText.setTextColor(color_rgb(211,211,211)) 
    cpuText.draw(win)
    cpuText.setSize(30)

    # balance box
    balanceBox = Rectangle(Point(0, 900), Point(325, 950))
    balanceBox.draw(win)
    balanceBox.setWidth(2)
    
    # balance text
    balanceText = Text(Point(85, 925), "Balance:")
    balanceText.setSize(30)
    balanceText.draw(win)

# function to create the boxes in which the cards will be placed in
def drawCardBoxes():
    """making the boxes for the cards to be placed in

    Arguments:
        n(graphics): boxes on GUI

    Returns:
        graphics: boxes on GUI
    """
    # user card boxes
    cardBox = Rectangle(Point(190, 15), Point(266, 125))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(276, 15), Point(352, 125))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(438, 15), Point(362, 125))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(448, 15), Point(524, 125))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(534, 15), Point(610, 125))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    
    # cpu card boxes
    cardBox = Rectangle(Point(190, 725), Point(266, 835))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(276, 725), Point(352, 835))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(438, 725), Point(362, 835))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(448, 725), Point(524, 835))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))
    cardBox = Rectangle(Point(534, 725), Point(610, 835))
    cardBox.draw(win)
    cardBox.setFill(color_rgb(6, 103, 27))


# function to make clickable buttons
def createsButtons():
    """making buttons in GUI

    Arguments:
        n(graphics): buttons on GUI

    Returns:
        graphics: buttons on GUI
    """
    # Hit button
    global hitcButton
    hitcButton = CButton(win, Point(710, 240), 65, "HIT")
    hitcButton.setSize(24)
    hitcButton.setFill(color_rgb(220, 70, 37))
    hitcButton.setWidth(3)

    # Stand button
    global standcButton
    standcButton = CButton(win, Point(710, 90), 65, "STAND")
    standcButton.setSize(24)
    standcButton.setFill(color_rgb(153, 204, 0))
    standcButton.setWidth(3)

    # deal 100 button
    global deal_100cButton
    deal_100cButton = CButton(win, Point(90, 90), 65, "100")
    deal_100cButton.setSize(35)
    deal_100cButton.setFill(color_rgb(37, 201, 152))
    deal_100cButton.setWidth(3)

    # deal 200 button
    global deal_200cButton
    deal_200cButton = CButton(win, Point(90, 245), 65, "200")
    deal_200cButton.setSize(35)
    deal_200cButton.setFill(color_rgb(244, 171, 97))
    deal_200cButton.setWidth(3)

    # deal 500 button
    global deal_500cButton
    deal_500cButton = CButton(win, Point(90, 400), 65, "500")
    deal_500cButton.setSize(35)
    deal_500cButton.setFill(color_rgb(208, 69, 99))
    deal_500cButton.setWidth(3)

    # exit button
    global exitcButton
    exitcButton = CButton(win, Point(770, 920), 20, "X")
    exitcButton.activate()
    exitcButton.setSize(20)
    exitcButton.setFill(color_rgb(0, 0, 0))
    exitcButton.setOutline(color_rgb(255, 0, 0))
    exitcButton.setFontColour(color_rgb(255, 0, 0))
    exitcButton.setWidth(3)

    # help button
    global helpcButton
    helpcButton = CButton(win, Point(720, 920), 20, "?")
    helpcButton.activate()
    helpcButton.setSize(20)
    helpcButton.setFill(color_rgb(0, 0, 0))
    helpcButton.setOutline(color_rgb(0, 255, 0))
    helpcButton.setFontColour(color_rgb(0, 255, 0))
    helpcButton.setWidth(3)

    
# displays balance for player
def balance(money):
    """keeping balance of money bet

    Arguments:
        n(int): Keeping track on money being bet

    Returns:
        int: returns money being bet
    """
    global bankText
    # choosing location
    bankText = Text(Point(240, 925), ("$" + str(money)))
    
    # choosing colour and size
    bankText.setTextColor(color_rgb(211,211,0)) 
    bankText.setSize(30)
    bankText.draw(win)

    
# function to activate the hit and stand buttons
def enableHitStand():
    """activating hit and stand button

    Arguments:
        n(graphics): Making the hit and stand button clickable

    Returns:
        graphics: making buttons clickable
    """
    # activating the hit and stand buttons
    hitcButton.activate()
    standcButton.activate()

    # deactivating all deal buttons
    deal_100cButton.deactivate()
    deal_200cButton.deactivate()
    deal_500cButton.deactivate()

    
# function that defines what each deal button does when clicked
def dealButtonClicked(win, hitcButton, standcButton, deal_100cButton,\
                  deal_200cButton, deal_500cButton, exitcButton, balance, \
                      helpcButton):
    """dealing money to player

    Arguments:
        n(int): adding money to the player's account

    Returns:
        int: returns a number
    """
    global potText, potAmount

    # making condition for buttons
    loop = True
    while loop == True:
        pt = win.getMouse()

        # event loop
        while not deal_100cButton.clicked(pt) and not \
              deal_200cButton.clicked(pt) and not deal_500cButton.clicked(pt) \
              and not exitcButton.clicked(pt) and not helpcButton.clicked(pt):
            pt = win.getMouse()
            
        # exit program if button clicked
        if exitcButton.clicked(pt):
            win.close()
            winsound.PlaySound('quit.wav', winsound.SND_FILENAME)
            loop = False
            raise SystemExit
            quit

        # when help clicked, disable all other buttons
        if helpcButton.clicked(pt):
            winsound.PlaySound('help.wav', winsound.SND_FILENAME)
            drawHelpText()
            deal_500cButton.deactivate()
            deal_200cButton.deactivate()
            deal_100cButton.deactivate()
            exitcButton.deactivate()
            # when help isn't clicked, activate all buttons
            pt = win.getMouse()
            while not helpcButton.clicked(pt):
                pt = win.getMouse()
            winsound.PlaySound('help.wav', winsound.SND_FILENAME)                
            undrawHelpText()
            deal_500cButton.activate()
            deal_200cButton.activate()
            deal_100cButton.activate()
            exitcButton.activate()
            exitcButton.setFontColour(color_rgb(255, 0, 0))
            
        # dealing 100
        if deal_100cButton.clicked(pt):

            # writing the value of the pot
            potText = Text(Point(400, 230), ("Pot: $" + str(200)))
            potText.setSize(30)
            potText.draw(win)

            enableHitStand()

            # setting base pot amount
            potAmount = 200

            # adjusting bank with new value
            bank = balance - 100
            loop = False
            return bank

        # dealing 200
        elif deal_200cButton.clicked(pt):

            # writing the value of the pot
            potText = Text(Point(400, 230), ("Pot: $" + str(400)))
            potText.setSize(30)
            potText.draw(win)
            
            enableHitStand()

            # setting base pot amount
            potAmount = 400

            # adjusting bank with new value
            bank = balance - 200
            loop = False
            return bank
        
        # dealing 500
        elif deal_500cButton.clicked(pt):

            # writing the value of the pot
            potText = Text(Point(400, 230), ("Pot: $" + str(1000)))
            potText.setSize(30)
            potText.draw(win)
            
            enableHitStand()

            # setting base pot amount
            potAmount = 1000

            # adjusting bank with new value
            bank = balance - 500
            loop = False
            return bank


# function that makes and returns the card value
def deal():
    """making deck and dealing out cards

    Arguments:
        n(str): The cards that are dealt

    Returns:
        list: returns a list with the dealt cards
    """

    global deck
    global userHand
    global cpuHand

    #2D list for the values of the deck
    deck = [["AS", "AH", "AC", "AD"], ["2S", "2H", "2C", "2D"], \
            ["3S", "3H", "3C", "3D"], ["4S", "4H", "4C", "4D"], \
            ["5S", "5H", "5C", "5D"], ["6S", "6H", "6C", "6D"], \
            ["7S", "7H", "7C", "7D"], ["8S", "8H", "8C", "8D"], \
            ["9S", "9H", "9C", "9D"], ["1S", "1H", "1C", "1D"], \
            ["JS", "JH", "JC", "JD"], ["QS", "QH", "QC", "QD"], \
            ["KS", "KH", "KC", "KD"]]

    # empty lists to use for the value of the hands
    userHand = []
    cpuHand = []

    # picking random cards from deck list
    try:
        ran1 = random.randint(0, len(deck) - 1)
        cardSet = deck[ran1]
        ran2 = random.randint(0, len(cardSet) - 1) 
        card = deck[ran1][ran2]

    # picking random cards from deck list
    except:
        del(deck[ran1])
        ran1 = random.randint(0, len(deck) - 1)
        cardSet = deck[ran1]
        ran2 = random.randint(0, len(cardSet) - 1) 
        card = deck[ran1][ran2]

    # assigning cards to CPU and playing sound effect
    deck[ran1].pop(ran2)
    cpuHand.append(card)
    winsound.PlaySound('deal.wav', winsound.SND_FILENAME)

    # for loop to run 2 times since CPU only gets 2 cards
    for i in range(2):
        try:
            
            # same as above, just pick random cards
            ran1 = random.randint(0, len(deck) - 1)
            cardSet = deck[ran1]
            ran2 = random.randint(0, len(cardSet) - 1) 
            card = deck[ran1][ran2]
            
        except:

            # same as above, just pick random cards
            del(deck[ran1])
            ran1 = random.randint(0, len(deck) - 1)
            cardSet = deck[ran1]
            ran2 = random.randint(0, len(cardSet) - 1) 
            card = deck[ran1][ran2]

        # assigning cards to user
        deck[ran1].pop(ran2)
        userHand.append(card)


# function to determine the sum of the user's hands
def sumOfUserHands():
    """adding a value to each player card

    Arguments:
        n(int): The value which corresponds with each card

    Returns:
        int: returns a value for player
    """
    global valuesOfUserHand
    valuesOfUserHand = []

    # finding the value that corresponds with the card
    for i in userHand:
        if i[0] == "A":
            valuesOfUserHand.append(11)
        elif i[0] == "2":
            valuesOfUserHand.append(2)
        elif i[0] == "3":
            valuesOfUserHand.append(3)
        elif i[0] == "4":
            valuesOfUserHand.append(4)
        elif i[0] == "5":
            valuesOfUserHand.append(5)
        elif i[0] == "6":
            valuesOfUserHand.append(6)
        elif i[0] == "7":
            valuesOfUserHand.append(7)
        elif i[0] == "8":
            valuesOfUserHand.append(8)
        elif i[0] == "9":
            valuesOfUserHand.append(9)
        elif i[0] == "1":
            valuesOfUserHand.append(10)
        elif i[0] == "J":
            valuesOfUserHand.append(10)
        elif i[0] == "Q":
            valuesOfUserHand.append(10)
        elif i[0] == "K":
            valuesOfUserHand.append(10)

    # use insertion sort to sort values from greatest to least
    insertionSort(valuesOfUserHand)

    
# function to determine the sum of the CPU's hands
def sumOfCpuHands():
    """adding a value to each dealer card

    Arguments:
        n(int): The value which corresponds with each card

    Returns:
        int: returns a value for dealer
    """
    global valuesOfCpuHand
    valuesOfCpuHand = []

    # finding the value that corresponds with the card
    for i in cpuHand:
        if i[0] == "A":
            valuesOfCpuHand.append(11)
        elif i[0] == "2":
            valuesOfCpuHand.append(2)
        elif i[0] == "3":
            valuesOfCpuHand.append(3)
        elif i[0] == "4":
            valuesOfCpuHand.append(4)
        elif i[0] == "5":
            valuesOfCpuHand.append(5)
        elif i[0] == "6":
            valuesOfCpuHand.append(6)
        elif i[0] == "7":
            valuesOfCpuHand.append(7)
        elif i[0] == "8":
            valuesOfCpuHand.append(8)
        elif i[0] == "9":
            valuesOfCpuHand.append(9)
        elif i[0] == "1":
            valuesOfCpuHand.append(10)
        elif i[0] == "J":
            valuesOfCpuHand.append(10)
        elif i[0] == "Q":
            valuesOfCpuHand.append(10)
        elif i[0] == "K":
            valuesOfCpuHand.append(10)

    # use insertion sort to sort values from greatest to least    
    insertionSort(valuesOfCpuHand) 


# function that determines the sum of the list
def sumList(n):
    """sum of the values in list

    Arguments:
        n(int): The sum of the values


    Returns:
        int: returns the sum
    """
    # adding the values inside of the list

    # if there is only 1 value in the list
    if len(n) == 1:
        return n[0]

    # if there is more than 1 value in the list
    else:
        return n[0] + sumList(n[1:])


# function to reset the CPU sum
def resetCpuSum():
    """resets the value of the CPU

    Arguments:
        n(graphics): Text with the CPU's hand sum


    Returns:
        graphics: returns the CPU sum
    """

    # resetting the CPU sum
    global sumCpuText
    sumCpuText = Text(Point(652, 785), "00")
    sumCpuText.setSize(30)
    sumCpuText.draw(win)

    #resetting the user sum
    global sumUserText
    sumUserText = Text(Point(400, 170), "00")
    sumUserText.setSize(30)
    sumUserText.draw(win)  


# function that updates the user sum
def updateUserSum():
    """shows the sum of the user hand

    Arguments:
        n(graphics): Text showing the value of the user hand


    Returns:
        graphics: text showing the value of user hand
    """

    # choosing the location to show the value
    global sumUserText
    sumUserText = Text(Point(400, 170), sumOfUserHand)
    sumUserText.setSize(30)
    sumUserText.draw(win)    


# function that updates the user sum
def updateCpuSum():
    """shows the sum of the CPU hand

    Arguments:
        n(graphics): Text showing the value of the CPU hand


    Returns:
        graphics: text showing the value of CPU hand
    """

    # choosing the location to show the value
    global sumCpuText
    sumCpuText = Text(Point(652, 785), sumOfCpuHand)
    sumCpuText.setSize(30)
    sumCpuText.draw(win)

    
# function to insert image that corresponds with user hand
def drawUserCard(win):
    """inputs an image as a card to notify player of his hand

    Arguments:
        n(graphics): a png of a card for the user


    Returns:
        graphics: a png of a card for the user
    """
    global userHand, card

    # choosing location and size for image to appear in png form
    x = 228
    for i in userHand:
        card = Image(Point(x, 70), i + ".png")
        card.draw(win)
        x += 86


# function to insert image that corresponds with CPU hand
def drawCpuCard(win):
    """inputs an image as a card for CPU

    Arguments:
        n(graphics): a png of a card for CPU


    Returns:
        graphics: a png of a card for CPU
    """
    global cpuHand, card

    # choosing location and size for image to appear in png form
    x = 228
    for i in cpuHand:
        card = Image(Point(x, 780), i + ".png")
        card.draw(win)
        x += 86

            
# function that sets the rules for the game 
def hitStandButtonClicked(win, hitcButton, standcButton, exitcButton, \
                          helpcButton):
    """sets the rules for the game

    Arguments:
        n(graphics): sets the rules for when a button is to activate/deactivate/
                     and when to stop the game


    Returns:
        graphics: retuns conditions for the rest of the program
    """
    global sumOfUserHand, sumOfUserHands, sumUserText, hitCount, userHand, \
           valuesOfUserHand
    
    loopall = True
    while loopall == True:
        loop = True
               
        hitCount = 0
        
        while loop == True:
            pt = win.getMouse()

            #event loop
            while not hitcButton.clicked(pt) and not standcButton.clicked(pt) \
                  and not exitcButton.clicked(pt) and not \
                  helpcButton.clicked(pt):
                pt = win.getMouse()
             
            #exiting the program
            if exitcButton.clicked(pt):
                win.close()
                winsound.PlaySound('quit.wav', winsound.SND_FILENAME)
                raise SystemExit
                loopall = False
                quit

            #help button clicked    
            if helpcButton.clicked(pt):
                winsound.PlaySound('help.wav', winsound.SND_FILENAME)
                drawHelpText()
                hitcButton.deactivate()
                standcButton.deactivate()
                exitcButton.deactivate()
                pt = win.getMouse()
                while not helpcButton.clicked(pt):
                    pt = win.getMouse()
                    
                #help button not clicked
                winsound.PlaySound('help.wav', winsound.SND_FILENAME)
                undrawHelpText()
                hitcButton.activate()
                standcButton.activate()
                exitcButton.activate()
                exitcButton.setFontColour(color_rgb(255, 0, 0))

            #stand button clicked     
            if standcButton.clicked(pt):
                winsound.PlaySound('stand.wav', winsound.SND_FILENAME)
                loop = False
                loopall = False

            #hit button clicked    
            elif hitcButton.clicked(pt):
                loopall = False

                #adds one to the hit count
                hitCount += 1
                try:

                    #random card is selected from the deck
                    ran1 = random.randint(0, len(deck) - 1)
                    cardSet = deck[ran1]
                    ran2 = random.randint(0, len(cardSet) - 1) 
                    card = deck[ran1][ran2]
                    
                except:

                    #random card is selected from the deck
                    del(deck[ran1])
                    ran1 = random.randint(0, len(deck) - 1)
                    cardSet = deck[ran1]
                    ran2 = random.randint(0, len(cardSet) - 1) 
                    card = deck[ran1][ran2]

                #removes card from deck and adds it to user's hand
                deck[ran1].pop(ran2)
                userHand.append(card)
                drawUserCard(win)

                #determines sum of values of cards
                sumOfUserHands()
                sumOfUserHand = sumList(valuesOfUserHand)
                winsound.PlaySound('hit.wav', winsound.SND_FILENAME)
                
                count = -1

                #condition if user has ace in first slot and sum is greater than
                #21
                if sumOfUserHand > 21:
                    for i in valuesOfUserHand:
                        count += 1
                        if i == 11:
                            valuesOfUserHand[count] = 1
                            count = -1
                            break
                        
                sumOfUserHand = sumList(valuesOfUserHand)        
                count1 = -1

                #condition if user has ace in second slot and sum is greater
                #than 21
                if sumOfUserHand > 21:
                    for i in valuesOfUserHand:
                        count1 += 1
                        if i == 11:
                            valuesOfUserHand[count1] = 1
                            count1 = -1
                            break
                    #condition if user has ace in third slot and sum is greater
                    #than 21    
                    sumOfUserHand = sumList(valuesOfUserHand)                           
                    count2 = -1          
                    if sumOfUserHand > 21:                    
                        for i in valuesOfUserHand:
                            count2 += 1
                            if i == 11:
                                valuesOfUserHand[count2] = 1
                                print(count2)
                                count2 = -1
                                break

                        #condition if user has ace in fourth slot and sum is
                        #greater than 21
                        sumOfUserHand = sumList(valuesOfUserHand)        
                        count3 = -1          
                        if sumOfUserHand > 21:                    
                            for i in valuesOfUserHand:
                                count3 += 1
                                if i == 11:
                                    valuesOfUserHand[count3] = 1
                                    print(count3)
                                    count3 = -1
                                    break
                            #condition if user has ace in last slot and sum is
                            #greater than 21
                            sumOfUserHand = sumList(valuesOfUserHand)
                            count4 = -1
                            if sumOfUserHand > 21:                    
                                for i in valuesOfUserHand:
                                    count4 += 1
                                    if i == 11:
                                        valuesOfUserHand[count4] = 1
                                        print(count4)
                                        count4 = -1
                                        break
                            
                    sumOfUserHand = sumList(valuesOfUserHand)
                    
                    #condition if sum of values of cards is greater than 21 and
                    # no aces are present in user's hand        
                    if 11 not in valuesOfUserHand and \
                       sumOfUserHand > 21:
                        sumUserText.undraw()
                        updateUserSum()            
                        gameLoss()
                        loop = False

                #updates the user's sum of values of cards
                sumOfUserHand = sumList(valuesOfUserHand)
                sumUserText.undraw()
                updateUserSum()            

                #limiting the number of hits to 3
                if sumOfUserHand <= 21:
                    if hitCount >= 3:
                        loop = False
                        
                    else:
                        loop = True


#function that defines the actions that the cpu will take during it's turn
def cpuTurn():
    """sets the rules for the game

    Arguments:
        n(graphics): sets the rules for when a button is to activate/deactivate/
                     and when to stop the game


    Returns:
        graphics: returns conditions for the rest of the program
    """
    global cpuHand, card, sumOfCpuHand
    cpuHits = 0

    #the cpu stands once their sum of values is 17 or higher. they are also
    #limited to 4 hits as they start off with 1 card
    while sumOfCpuHand < 17 and cpuHits < 4:
        time.sleep(.5)
        try:

            #random card is selected from the deck
            ran1 = random.randint(0, len(deck) - 1)
            cardSet = deck[ran1]
            ran2 = random.randint(0, len(cardSet) - 1) 
            card = deck[ran1][ran2]
            
        except:

            #random card is selected from the deck
            del(deck[ran1])
            ran1 = random.randint(0, len(deck) - 1)
            cardSet = deck[ran1]
            ran2 = random.randint(0, len(cardSet) - 1) 
            card = deck[ran1][ran2]

        #removes card from deck and adds it to cpu's hand
        deck[ran1].pop(ran2)
        cpuHand.append(card)
        cpuHits += 1

        #determines cpu's sum of values of cards
        sumOfCpuHands()
        sumOfCpuHand = sumList(valuesOfCpuHand)
        winsound.PlaySound('hit.wav', winsound.SND_FILENAME)
        drawCpuCard(win)

        #condition if cpu has an ace in first slot and sum is greater than 21
        if sumOfCpuHand > 21:
            count = -1
            if sumOfCpuHand > 21:
                for i in valuesOfCpuHand:
                    count += 1
                    if i == 11:
                        valuesOfCpuHand[count] = 1
                        count = -1
                        break
            sumOfCpuHand = sumList(valuesOfCpuHand)        
            count1 = -1

            #condition if cpu has an ace in second slot and sum is greater than
            #21
            if sumOfCpuHand > 21:
                for i in valuesOfCpuHand:
                    count1 += 1
                    if i == 11:
                        valuesOfCpuHand[count1] = 1
                        count1 = -1
                        break
                #condition if cpu has an ace in third slot and sum is greater
                #than 21    
                sumOfCpuHand = sumList(valuesOfCpuHand)                           
                count2 = -1          
                if sumOfCpuHand > 21:                    
                    for i in valuesOfCpuHand:
                        count2 += 1
                        if i == 11:
                            valuesOfCpuHand[count2] = 1
                            print(count2)
                            count2 = -1
                            break
                    #condition if cpu has an ace in fourth slot and sum is
                    #greater than 21
                    sumOfCpuHand = sumList(valuesOfCpuHand)        
                    count3 = -1          
                    if sumOfCpuHand > 21:                    
                        for i in valuesOfCpuHand:
                            count3 += 1
                            if i == 11:
                                valuesOfCpuHand[count3] = 1
                                print(count3)
                                count3 = -1
                                break
                        #condition if cpu has an ace in last slot and sum is
                        #greater than 21
                        sumOfCpuHand = sumList(valuesOfCpuHand)
                        count4 = -1
                        if sumOfCpuHand > 21:                    
                            for i in valuesOfCpuHand:
                                count4 += 1
                                if i == 11:
                                    valuesOfCpuHand[count4] = 1
                                    print(count4)
                                    count4 = -1
                                    break
                        
                sumOfCpuHand = sumList(valuesOfCpuHand)

                #condition if sum of values of cards is greater than 21 and
                #no aces are present in cpu's hand
                if 11 not in valuesOfCpuHand and \
                   sumOfCpuHand > 21:
                    sumCpuText.undraw()
                    updateCpuSum()            
                    gameWon()
                    loop = False
                    
        #updating the cpu's sum of value of cards
            sumOfCpuHand = sumList(valuesOfCpuHand)
        sumCpuText.undraw()
        updateCpuSum()


# fcuntion to determine winner of the game
def whoWon():
    """determines the winner of the game

    Arguments:
        n(int): determines the winner of the game by comparing
                the values of the user and CPU to 21


    Returns:
        int: the winner of the game
    """
    # finding the winner by comparing the value to 21
    if sumOfUserHand <= 21 and sumOfCpuHand <= 21:
        UserAmountFrom21 = 21 - sumOfUserHand  
        cpuAmountFrom21 = 21 - sumOfCpuHand  

        # if both user and CPU have the same sum, the game ends in a draw
        if UserAmountFrom21 == cpuAmountFrom21:
            gameDraw()

        # if the CPU busts, the user wins
        if UserAmountFrom21 < cpuAmountFrom21:
            gameWon()

        # if the player busst, the user loses
        if UserAmountFrom21 > cpuAmountFrom21:
            gameLoss()

            
# function to show that the game ends in a tie
def gameDraw():
    """graphics and sound to illustrate a draw

    Arguments:
        n(graphics): Text telling the user that the game ends in a tie


    Returns:
        graphics: returns text illustrating a tie and a sound effect
    """
    global drawText, bank

    # the text and it's location
    drawText = Text(Point(400, 570), "You both tied!\n+$" + \
                    str(round(potAmount / 2)))
    drawText.setSize(35)
    drawText.draw(win)
    bankText.undraw()
    bank = round(add(bank, (potAmount / 2)))
    balance(bank)

    # the sound effect
    winsound.PlaySound('tie.wav', winsound.SND_FILENAME)
    drawText.undraw()


# function to show that the game ends in a win for the user
def gameWon():
    """graphics and sound to illustrate a win for the user

    Arguments:
        n(graphics): Text telling the user that the game ends in win


    Returns:
        graphics: returns text illustrating a win and a sound effect
    """
    global wonText, bank
    
    # the text and it's location
    wonText = Text(Point(400, 570), "You won!\n+$" + str(potAmount))
    wonText.setSize(35)
    wonText.draw(win)
    bankText.undraw()
    bank = round(add(bank, potAmount))
    balance(bank)

    # the sound effects
    winsound.PlaySound('win.wav', winsound.SND_FILENAME)
    winsound.PlaySound('money.wav', winsound.SND_FILENAME)
    wonText.undraw()

    
# function to do an insertion sort
def insertionSort(sort):
    """a sorting algorithm for the dealer and player card values 

    Arguments:
        n(int): Sorting a list from greatest to least

    Returns:
        int: returns a sorted list from greatest to least
    """
    
    # check all values through in the list
    for i in range(1, len(sort)):
  
        value = sort[i]
  
        # move elements of sort[0 - i-1], that are
        # greater than value, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and value > sort[j] :
                sort[j+1] = sort[j]
                j -= 1
        sort[j+1] = value


# function to show that the game ends in a loss for the user
def gameLoss():
    """graphics and sound to illustrate a loss for the user

    Arguments:
        n(graphics): Text telling the user that the game ends in loss


    Returns:
        graphics: returns text illustrating a loss and a sound effect
    """
    global lossText, bank

    # the text and it's location
    lossText = Text(Point(400, 570), "You lost")
    lossText.setSize(35)
    lossText.draw(win)

    # the sound effect
    winsound.PlaySound('loss.wav', winsound.SND_FILENAME)
    lossText.undraw()


# function to help the user understand the game
def drawHelpText():
    """prints text on the screen to help user understand the game

    Arguments:
        n(graphics): use Text to help clarify the game to the user


    Returns:
        graphics: Text appears on the window
    """
    global instructionsText, hitStandText, dealText, sumText

    # using Text to write on the graphics window to explain the game
    instructionsText = Text(Point(400, 600), "The goal of BlackJack is to hit \
a sum closest to 21 without exceeding! \
\nThe closest player to 21 wins!\n The cpu stands on 17, \
and will always match your bet!\n All face cards are worth \
10 and an ace can be worth either 11 or 1!\n You have a limit of 5 cards!\
\n\n (click the help button to remove overlay)")
    instructionsText.setSize(15)
    instructionsText.draw(win)

    hitStandText = Text(Point(680, 340), "'""'Hit'""' deals you a card\n '""'\
stand'""' ends your turn")
    hitStandText.setSize(15)
    hitStandText.draw(win)
    
    dealText = Text(Point(90, 500), "Bet an amount \nto start")
    dealText.setSize(15)
    dealText.draw(win)
    
    sumText = Text(Point(400, 300), "This is the sum of your hand.\n This \
will pick the best value for your aces.")
    sumText.setSize(15)
    sumText.draw(win)


# function to remove the text from the window
def undrawHelpText():
    """removes the text on the screen

    Arguments:
        n(graphics): removes all text on the window


    Returns:
        graphics: removes all text on the window
    """
    global instructionsText, hitStandText, sumText

    # remove all text from the window
    instructionsText.undraw()
    hitStandText.undraw()
    dealText.undraw()
    sumText.undraw()


# Creates Main Program.
def main():
    """main program which combines all the functions above to run the code correctly

    Arguments:
        n(int): combine all the functions in the program


    Returns:
        int: a fully functional BlackJack game
    """
    global win, sumOfUserHand, sumOfCpuHand, bank
    #Process: Creates a window with width = 800 and height = 950 
    win = GraphWin("BlackJack: Fady, Aariz, Youssef", 800, 950)
    win.setCoords(0, 0, 800, 950)
    createsGUI()
    drawCardBoxes()
    createsButtons()
    bank = 5000
    balance(bank)

    # checking condition to the run the program when user wants to play
    playLoop = True
    while playLoop == True:

        # reset game to original stage
        resetCpuSum()
        deal_100cButton.activate()
        deal_200cButton.activate()
        deal_500cButton.activate()
        hitcButton.deactivate()
        standcButton.deactivate()

        # set the parameters for the bank
        bank = dealButtonClicked(win, hitcButton, standcButton, deal_100cButton, \
        deal_200cButton, deal_500cButton, exitcButton, bank, helpcButton)

        # keeping track of the sum of both the user and CPU
        bankText.undraw()
        balance(bank)
        deal()
        sumOfUserHands()
        sumOfCpuHands()
        sumOfUserHand = sumList(valuesOfUserHand)
        sumOfCpuHand = sumList(valuesOfCpuHand)

        # update all values to decide on the outcome of the game
        drawCpuCard(win)
        sumUserText.undraw()
        updateUserSum()
        sumCpuText.undraw()
        updateCpuSum()
        drawUserCard(win)
        hitStandButtonClicked(win, hitcButton, standcButton, exitcButton, \
                              helpcButton)
        
        # check if CPU can continue
        if sumOfUserHand < 22:
            cpuTurn()

        # show the winner and remove all text
        whoWon()
        drawCardBoxes()
        potText.undraw()
        sumUserText.undraw()
        sumCpuText.undraw()

        # values of hands for user and CPU
        print("Starting Deck:")
        print(deck)
        print()
        print("Cpu Hand:")
        print(cpuHand)
        print(sumOfCpuHand)
        print()
        print("User Hand:")
        print(userHand)
        print(sumOfUserHand)


        # TEST CASES
        
        # if standcButton clicked:
            # CPU turn
        # else:
            # program waits for input

        # if hitcButton clicked:
            # user recieves another card
        # else:
            # program waits for input

        # if deal_100cButton clicked:
            # user deals $100
        # else:
            # program waits for input

        # if deal_200cButton clicked:
            # user deals $200
        # else:
            # program waits for input

        # if deal_500cButton clicked:
            # user deals $500
        # else:
            # program waits for input

        # if exitcButton clicked:
            # program ends
        # else:
            # program waits for input

        # if helpcButton clicked:
            # text appears that explain the game to the user
        # else:
            # program waits for input


# Main Program:
main()
