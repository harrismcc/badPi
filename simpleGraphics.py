

import sys

class graphics:

    def __init__(self):
        self.currentStep = 0

    def draw(self, x1, x2, length):
        
        x1 = int(x1)
        x2 = int(x2)

        mainStr = "|"
        mainStr += '_' * (x1-1)
        mainStr += "X"
        mainStr += '_' * ((x2-1)-x1)
        mainStr += 'X'
        mainStr += '_' * (length - x2)
        #print(mainStr)
        return mainStr


    def stepAnimation(self):
        length = 10
        animationSteps = [
            (3, 6),
            (3, 5),
            (3, 4),
            (2, 4),
            (1, 4),
            (2, 4),
            (3, 4),
            (3, 5),
            (3, 6),
            (3, 7),
            (3, 8),
            (3, 7)
        ]

        if self.currentStep > 1000: self.currentStep = 0
        self.currentStep += 1
        #print(int(self.currentStep / 1000))
        return self.draw(animationSteps[int(self.currentStep / 100)][0], animationSteps[int(self.currentStep / 100)][1], 10)


gEngine = graphics()

    
