# battle phase
from AIMain import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""
        pass
    def run_game(self):
        self.display_welcome()
        self.choose_a_player()
        self.game_sequence()


    def display_welcome(self):
        print ("Welcome to RPSLS! \n Choose your player \n Choose your gesture \n Best out of 3 wins!")

    def choose_a_player(self):
        user_input = input("Choose a Player: \n Press 1 for Human \n Press 2 for AI.")
        if user_input == "1":
            name = input("Enter in the name for the Human:  ")
            self.player_one = Human(name)
            self.player_two = AI("A Eye")
        elif user_input == "2":
            name_one = input("Enter in the name for the player 1:  ")
            name_two = input("Enter in the name for the player 1:  ")
            self.player_one = Human(name_one)
            self.player_two = Human(name_two) 
        pass

    def game_sequence(self):
        while self.player_one.score < 3 and self.player_two.score < 3 == True:
            self.player_one.choose_gesture() 
            self.player_two.choose_gesture()
            
            if self.player_one.current_gesture == self.player_two.current_gesture:
                self.player_one.score = 0
                self.player_two.score = 0

            elif self.player_one.current_gesture == "Rock" and (self.player_two.current_gesture == "Lizard" or "Scissors"):
                 self.player_one.score += 1

            elif self.player_one.current_gesture == "Scissors" and (self.player_two.current_gesture == "Paper" or "Lizard"):
                self.player_one.score += 1

            elif self.player_one.current_gesture == "Paper" and (self.player_two.current_gesture == "Rock" or "Spock"):
                self.player_one.score += 1 

            elif self.player_one.current_gesture == "Lizard" and (self.player_two.current_gesture == "Spock" or "Paper"):
                self.player_one.score +=1

            elif self.player_one.current_gesture == "Spock" and (self.player_two.current_gesture == "Scissors" or "Rock"):
                self.player_one.score += 1  

            elif self.player_two.current_gesture == "Rock" and (self.player_one.current_gesture == "Lizard" or "Scissors"):
                 self.player_two.score += 1

            elif self.player_two.current_gesture == "Scissors" and (self.player_one.current_gesture == "Paper" or "Lizard"):
                self.player_two.score += 1

            elif self.player_two.current_gesture == "Paper" and (self.player_one.current_gesture == "Rock" or "Spock"):
                self.player_two.score += 1 

            elif self.player_two.current_gesture == "Lizard" and (self.player_one.current_gesture == "Spock" or "Paper"):
                self.player_two.score += 1

            elif self.player_two.current_gesture == "Spock" and (self.player_one.current_gesture == "Scissors" or "Rock"):
                self.player_two.score += 1   
            pass         






# Rock crushes Scissors
# Scissors cuts Paper 
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock

        
