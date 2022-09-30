from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    def __init__(self):
        self.console = Console()
        self.word = Word() #generate the word here. correctWord is generated on Word init
        self.jumper = Jumper(self.word.correctWord) #needs the correct word to generate length of underscore array
        self.keep_playing = True

        
    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        message = ""
        for element in self.jumper.displayArray:    # Line added
            message = message + element + " "     # Line added
        self.console.write(message) # Original line
        message = self.jumper.picture()
        self.console.write(message)
        oneLetterResponse = False
        while not oneLetterResponse:
            self.guess = self.console.read("Guess a letter [a-z]: ")
            if len(self.guess) != 1:
                print("\nPlease enter one letter. No more, no less.\n")
            else:
                oneLetterResponse = True

        
    def do_updates(self):
        self.positionsOfCorrect = self.word.checkLetter(self.guess)
        self.jumper.updateArray(self.positionsOfCorrect, self.guess)
        self.checkVictory = self.jumper.checkVictory()
        self.checkDefeat = self.jumper.checkDefeat()
        
    def do_outputs(self):
        if self.checkVictory == True: #Checks to see if you've won. Still needs lots of testing
            message = "Congratulations, you won! The word was: "
            self.console.write(message)
            message = "\n" + self.word.correctWord
            self.console.write(message)

            self.keep_playing = False #If you've won, game ends. 

        elif self.checkDefeat == True: #checks to see if you've lost, still needs lots of testing. 
            message = self.jumper.picture()
            self.console.write(message)

            message ="\nSorry! Try again! Your word was: "
            self.console.write(message)

            message ="\n" + self.word.correctWord
            self.console.write(message)

            self.keep_playing = False