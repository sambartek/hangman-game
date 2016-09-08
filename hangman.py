import random # premade list of words

places = ['evansville', 'chicago', 'toronto', 'lafayette'] # makes a list of the alphabet
things = ['football', 'chair', 'computer', 'apples']
spelling = ['guerdon', 'autochthonous', 'serrefine', 'prospicience']

alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)] # makes the list look good

alphabet = ''.join(alpha)


# intro to the game, and explanation of how the game works
def start():
   pass

# function to make sure each guess is just one character long
def allowed(guess):
    if len(guess) == 1:
        return True
    else:
        print "You can only submit a single letter."
        begin()
               
# function that begins the game
def begin():
    print "This is a game of hangman."
    print "Enter the number for the category of words you would like to play."
    category = int(raw_input("Cities (1), Things (2), Spelling Bee Words (3) >>> "))

    if category == 1: # chooses a random word from places
        word = random.choice(places)
    elif category == 2: # word from things
        word = random.choice(things)
    elif category == 3: # word from spell
        word = random.choice(spelling)

    lives = 7 # sets the number of lives
    guesses = '' # total of guesses made, starts with none
    print len(word) * '_ ' # shows how long the word is
    print "Lives: 7" # tells the player how many lives they have

    while lives > 0:  # loop that continues until lives are gone
        guess = str(raw_input("What letter do you guess? >> ")) # promts for a guess
        failed = 0 # variable to check if you guess all the letters
        allowed(guess) # checks if the user inputed single character
        
        if guess in guesses:  # checks if you guess a letter twice
            print "You already guessed that!"
            lives += 1
        guesses += guess

        
        for x in word: # main part of the game
            if x in guesses: # if guess is in the word then shows letter
                print x,
            else: # if guess not in word then fills the spot with a blank
                print "_",
                failed += 1
        print # the print puts the words on a new line

        for x in alphabet: # function to show the alphabet
            if x not in guesses: # if user hadn't guessed the word it takes it out of the alphabet
                print x,
        print

        if failed == 0: # if there are no more blanks then the player wins
            print "You won"
            break

        if guess not in word: # takes a life for wrong guess
            lives -= 1 # takes a life away if answer not in word
            print "Lives left: %s." % lives
            if lives == 0: # when lives hit zero the game ends
                print "You lose!"
                print "The word was: %s." % word
                break
        
        print
               
begin()
