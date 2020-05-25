import random, time
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','orange', 'grapefruit','strawberry','coconut']
Sports = ['football', 'boxing', 'bodybuilding', 'aerobics', 'cycling', 'judo', 'wrestling', 'tennis', 'bowling', 'golf']
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

name = input("Enter your name")
print("Hello", name.capitalize(), "»et's start the game!")
time.sleep(1)
print("The purpose of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)


while True:

    while True:
        if category.upper() == 'S':
            secretWord = random.choice(Sports)
            break
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        else:
            category = input("Please select a valid categary: F for Fruits / S for Sports; X to exit")

        if category.upper() == 'X':
            print("Bye.")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)


        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))



        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", attempts)



        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    printGuessedLetter()



            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("You won!")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.upper())
                break


        continueGame = input("Do you want to play again? Y to continue, any other key to quit")
        if continueGame.upper() == 'Y':
            category = input("Please select a valid categary: F for Fruits / S for Sports")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing.")
            break
    else:
        break
