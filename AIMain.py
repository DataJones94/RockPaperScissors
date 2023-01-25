# child class

from player import Player
import random

class AI(Player):
    def __init__(self,name):
        super().__init__(name)
        pass


        
    def choose_gesture(self):
        self.current_gesture = self.gesture_list [random.randint(0,4)] 
        print(f'{self.name} has picked {self.current_gesture}')
        pass