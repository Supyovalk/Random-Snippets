#{(JDMap,TouhouCharacter):[[Spell name,Type,Comments],[]]}
#{"TouhouCharacter":(Tips about spell card naming schemes for the character)} Acts a storage
import pickle
CombinationData={("Bad Habits","Cirno"): [["Cold Habits 'Walking in a snowstorm'","Timeout","It's always nice to take a walk on a cold night... if it wasn't just full of ice faries making a mess."]]} #IDCODE
CharacterData=[{},{}]
def loaddata(type,filename):
    with open(filename, 'rb') as f: 
        if type==0:
            global CombinationData
            CombinationData = pickle.load( f )
        else:
            global CharacterData
            CharacterData = pickle.load(  f )
def savedata(type,filename):
    with open(filename, 'wb') as f: 
        if type==0:
            global CombinationData
            pickle.dump( CombinationData, f )
        else:
            global CharacterData
            pickle.dump (CharacterData,f)
def addcombination(JDMap,TouhouCharacter,Spelldata): #Add Checking
    global CombinationData
    if(not (JDMap,TouhouCharacter) in CombinationData.keys()):
        CombinationData[(JDMap,TouhouCharacter)]=[]
    CombinationData[(JDMap,TouhouCharacter)].append(Spelldata)
def inputaction():
    return int(input("Actions:0-Exit,1-Load,2-Save,3-Add JD maps,4-Add Touhou Characters,5-Add spell cards,6-print data,7-view spells\n"))
def main():
    actionid=inputaction()
    while(actionid!=0):
        if(actionid==1):
            loaddata(0,"CombinationData.bin")
            loaddata(1,"CharacterData.bin")
            print("Data Loaded From Files")
        if(actionid==2):
            if(not CombinationData or not CharacterData):
                print("[ERROR!] Cant save Data due to Data being empty.")
            else:
                savedata(0,"CombinationData.bin")
                savedata(1,"CharacterData.bin")
                print("Data Saved To Files")
        if(actionid==3):
            print("Map feautre TBA")
        if(actionid==4):
            touhouname,touhoutips=(input("Enter Touhou Character:"),input("Enter Touhout Spell Writing Tips:"))
            if(CharacterData[0]):
                if touhouname in CharacterData[0].keys():
                    print("[ERROR!] Character already in characterdata")
                else:
                    CharacterData[0][touhouname]=touhoutips
            else:
                CharacterData[0]={touhouname:touhoutips}

        if(actionid==5):
            JDMap=input("Enter JD map:")
            TouhouCharacter=input("Enter Touhou Character:")
            Spelldata=[input("Enter Spell Name:"),input("Enter Spell type (Normal/Timeout/LastWord/Harvest's Overdrive/Etc.):"),input("Enter Spell comment:")]
            addcombination(JDMap,TouhouCharacter,Spelldata)
        if(actionid==6):
            if (not CharacterData or not CombinationData):
                print("[ERROR!] Can't Write Infomation as some of it is empty")
            else:
                print("====Combinaition Data===")
                for combikey in CombinationData.keys() :
                    print(str(combikey)+"\n====")
                    for spell in CombinationData[combikey]:
                        print(spell[0]+" [Type:"+spell[1]+"] ==== "+ spell[2])
                    #print(str(CombinationData[combikey])+"\n")
                print("====End of Combination Data====\n===Character data===\n===Touhou===")
                for TohuouKey in CharacterData[0].keys():
                    print(TohuouKey+":"+CharacterData[0][TohuouKey])
                print("===Just Dance===")
                for DanceKey in CharacterData[1].keys():
                    print(DanceKey+":"+CharacterData[1][DanceKey])
        actionid=inputaction()
main()