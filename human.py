# child class

from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
    def choose_gesture(self):
        user_input = input("Press 1 for Rock \n Press 2 for Paper \n Press 3 for Scissors \n Press 4 for Lizard \n Press 5 for Spock.")
        if user_input == "1": 
            print(f'{self.name} chose Rock')
        elif user_input == "2":
            print(f'{self.name} chose Paper')
        elif user_input == "3":
            print(f'{self.name} chose Scissors')
        elif user_input == "4":
            print(f'{self.name} chose Lizard')
        elif user_input == "5":
            print(f'{self.name} chose Spock')
        pass