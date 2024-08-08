#The Information About two fandom fusions
#characters keys: name,title,personality,powers,abilites,ETC.
import pickle
class fandomfusion:
    #fandomnames=(FandomA,FandomB)
    #fusioncharacters = [[{Character Data},{Character Data}],[{Character Data},{Character Data}]]
    #Combination Data = {(Character A,Character B)={INFROMATION ABOUT FUSION}}
    def __init__(self,fandomnames,fusioncharacters,combinationdata):
        pass
    def isnameslegal(self,firstcharactername,secondcharactername):
        matchflag=False
        for character in self.fusioncharacters[0]:
            if character["name"]==firstcharactername:
                matchflag=True
                break
        if not matchflag:
            return False
        matchflag=False
        for character in self.fusioncharacters[1]:
            if character["name"]==secondcharactername:
                matchflag=True
                break
        return matchflag        
    def getfusiondata(self,firstcharactername,secondcharactername):
        return 
    def addfusion(self,firstcharactername,secondcharactername,fusioninfomation):
        if not self.isnameslegal(self,firstcharactername,secondcharactername):
            return False
        if (firstcharactername,secondcharactername) in self.combinationdata:
            return False
        self.combinationdata[(firstcharactername,secondcharactername)]=fusioninfomation
        return True
        

#list of fusioncharacters
#Where you contain 
class fandominformation:
    #fandoms={FandomName:{}}
    def __init__(self,fandomnames=[]):
        self.fandoms={}
        for name in fandomnames:
            self.fandoms[name]=[]
        pass
    def createfandomfusion(self,firstfandomname,secondfandomname):
        pass
        newfandomfusion=fandomfusion()
        return newfandomfusion
    def getfandomcharacternames(self,fandomname):
        if fandomname in self.fandoms:
            return [characterdata["name"] for characterdata in self.fandoms[fandomname]]
        return []

    def insertfandom(self,fandomname,charactersdata=[]):
        if not (fandomname in self.fandoms and self.fandoms[fandomname]):
            self.fandoms[fandomname]=charactersdata
        else:
            fandomnames = self.getfandomcharacternames(fandomname)
            for characterdata in charactersdata:
                if not characterdata["name"] in fandomnames:
                    self.fandoms[fandomname].append(characterdata)

        pass

def loadobject(filename):
    # Deserialize and load the object from the file
    with open(filename, 'rb') as file:
        loaded_object = pickle.load(file)
    return loaded_object
def savefandoms(fandominfo,filename):
    # Serialize and save the object to the file
    with open(filename, 'wb') as file:
        pickle.dump(fandominfo, file)
    pass
def savefusions(fusioninfo,filename):
    # Serialize and save the object to the file
    with open(filename, 'wb') as file:
        pickle.dump(fusioninfo, file)
    pass