import math


class box():
    '''This object is the simulated mass that "bounces" off
        of another box in a specific way to calculate digits 
        of pi. It defauls to all zeros, but can be changed'''
    def __init__(self, inMass = 0.0, inX = 0.0, inVel = 0.0):
        self.mass = inMass # kg
        self.x = inX # m
        self.vel = inVel # m/s
        self.width = 1 #Width is always 1 meter wide



class platform():
    def __init__(self, timeStep):
        '''This timestep detirmines how finely the movement
            is simulated'''
        self.timeStep = timeStep #In fractions of a second
        self.boxA = box(inMass = 1.0, inX = 1.0, inVel = 1.0)
        self.boxB = box(inMass = 2.0, inX = 3, inVel= 0.0)
        self.collisions = 0
    
    def stepOnce(self):
        '''This function moves physics along one 'tick' 
            according to the timestep above'''
        self.boxA.x += self.boxA.vel * self.timeStep
        self.boxB.x += self.boxB.vel * self.timeStep

        

        if (self.boxA.x >= self.boxB.x) or (self.boxB.x <= self.boxA.x):
            #Collision has happened
            self.collisions += 1
            mA = float(self.boxA.mass)
            mB = float(self.boxB.mass)
            print("Collision")

            #These equations calculate the new velocity of both boxes post-collision
            newAVel = (((2* mB)/(mB + mA)) * self.boxB.vel) - ((mB - mA)/(mB + mA) * self.boxA.vel)
            newBVel = (((2* mA)/(mA + mB)) * self.boxA.vel) - ((mA - mB)/(mA + mB) * self.boxB.vel)

            #Set the velocites to the newly calculated value
            self.boxB.vel = newBVel
            self.boxA.vel = newAVel
        
        if self.boxA.x <= 0:
            #This calculates the collision of boxA to the "wall"
            #located at x=0
            self.boxA.vel = -self.boxA.vel
            self.collisions += 1



    def getPositions(self):
        '''Getter that returns all objects in the space
            and their positions'''
        print("BoxA: " +  str(self.boxA.x))
        print("BoxB: " + str(self.boxB.x))
        print("Collisions: " + str(self.collisions))
        print("#############")


newPlatform = platform(0.1)

for i in range(1, 100):
    newPlatform.getPositions()
    newPlatform.stepOnce()
