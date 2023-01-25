# parent class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gesture_list = [ "Rock", "Paper", "Scissors", "Lizard", "Spock" ] 
        self.current_gesture = ""  
        pass

    def choose_gesture(self):
        pass