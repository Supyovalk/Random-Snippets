import random
def playgamenormal(fullship=[6,5,4]):
    diceonplay=6
    shipstage=[]
    for i in range(3):
        print("Roll "+str(i+1))
        rolls=[random.randrange(1,7) for i in range(diceonplay)]
        print(rolls)
        #Force Fullship
        #Optional Dice Play (Always Play Max Value)
playgamenormal()