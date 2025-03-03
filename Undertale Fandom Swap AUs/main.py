import json
def auInfoPath(FandomName):
    return 'AUs\\'+FandomName+'.json'
def getUndertaleCharacters():
    with open("Characters.json") as json_file:
        dict=json.load(json_file)
    return list(dict.keys())
def getPlotElements():
    with open("LoreAndGameplayElements.json") as json_file:
        dict=json.load(json_file)
    return dict["Plot Elements"]
def getGameplayElements():
    with open("LoreAndGameplayElements.json") as json_file:
        dict=json.load(json_file)
    return dict["Gameplay Elements"]
def getSongs():
    pass
def getAURenames():
    pass
def modifyInputJson(AUDict,ModifyName=False,ModifyCharacters=False,ModifyPlot=False,ModifyGameplay=False,ModifySongs=False,ModifyAUs=False):
    if(ModifyName):
        AUDict["Name"]=input("Enter AU Name:")
    if(ModifyCharacters):
        characters=getUndertaleCharacters()
        for character in characters:
            SwapName=input("Enter Replacement Name for %s (Nothing to skip,$z to stop):"%(character))
            if SwapName =="$z":
                break
            if SwapName == "":
                continue
            AUDict["Character Swaps"][character]=SwapName
    if(ModifyPlot):
        elements=getPlotElements()
        for element in elements:
            Aspects=input("Enter Plot Information for %s (Nothing to skip,$z to stop):"%(character))
            if SwapName =="$z":
                break
            if SwapName == "":
                continue
            AUDict["Plot Elements"][character]=SwapName
    if(ModifyGameplay):
        elements=getGameplayElements()
        for element in elements:
            Aspects=input("Enter Plot Information for %s (Nothing to skip,$z to stop):"%(character))
            if SwapName =="$z":
                break
            if SwapName == "":
                continue
            AUDict["Gameplay Elements"][character]=SwapName
    if(ModifySongs):
        pass
    if(ModifyAUs):
        pass
def createFandomSwap(FandomName):
    AUDict={"Fandom":FandomName,"Name":"","Character Swaps":{},"Plot Elements":{},"Gameplay Elements":{},"Songs":{},"AU Renames":{}}
    modifyInputJson(AUDict,ModifyName=True,ModifyCharacters=True,ModifyPlot=True,ModifyGameplay=True,ModifySongs=True,ModifyAUs=True)
    with open(auInfoPath(FandomName),"w") as json_file:
        json.dump(AUDict, json_file, indent=4)
def userMainInput():
    return input("0-Exit\n1-Basic Addition\n2-Basic Modfication\n3-Complex Process\n")
def UserLoop():
    userInput=userMainInput()
    while(userInput!=0):
        if(userInput==1):
            input("1-Add Fandom File,2-Add Base AU,3-Add Song,3-Add AU Rea")
        elif(userInput==2):
            input("1- Song")
        elif(userInput==3):
            input("1 - Complete Song Renaming,2 - Complete AU Renaming, 3 - Complete")
        userInput=userMainInput()


createFandomSwap("Devil May Cry")
#print(getUndertaleCharacters())