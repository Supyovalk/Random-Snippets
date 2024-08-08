import pickle
def texttodict(filename,failsafe=True):
    file1 = open("Wordattempt.txt","r",encoding='utf-8')
    wordlist=file1.readlines()
    worddict={}
    counter=1
    for word in wordlist:
        wordtrue=word.replace('\n','')
        if(not wordtrue in worddict.keys() and(not failsafe or not (" " in wordtrue or "\t" in wordtrue))):
            worddict[wordtrue]=counter
            counter+=1
    file1.close()
    return worddict
def save_dict_to_file(dic,name):
    with open(name,'w',encoding='utf-8') as f:
        f.write(str(dic))

def load_dict_from_file(name):
    data=""
    with open(name,'w',encoding='utf-8') as f:
        data=f.read()
    return eval(data)
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
def vectorizehebrewlist(lst,dict):
    vector=[]
    expendflag=False
    for word in lst:
        if word in dict.keys():
            vector.append(dict[word])
        else:
            if isEnglish(word):
                vector.append(0)
            else:
                expendflag=True
                newindex=max(dict.values())+1
                dict[word]=newindex
                vector.append(newindex)
    return (vector,expendflag)
                
#print(texttodict("Wordattempt.txt")["של"])

#save_dict_to_file(texttodict("Wordattempt.txt"),"Worddict.text")

dict=load_dict_from_file("dict.txt")
print(vectorizehebrewlist(["הוא","אהב","תות"],dict))