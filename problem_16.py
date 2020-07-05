"""
16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.
"""

class Mario:
    def __init__(self, cap, moustache, type):
        self.cap = cap
        self.moustache = moustache
        self.type =type
    
    def jump(self):
        print("jump mario character")
    
    def bend(self):
        print("bend mario character")

mario = Mario("yes", "yes", "small")
mario.jump()
mario.bend()

