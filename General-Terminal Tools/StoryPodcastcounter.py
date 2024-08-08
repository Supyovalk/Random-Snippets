#https://www.youtube.com/@amithegenius for an example of such
import pyperclip
def formattimestamp(timestamp,format,counter="",t1="",t2="",t3="",t4=""):
    formatedstamp=format.format(format=format,t1=t1,t2=t2,t3=t3,t4=t4,counter=counter,timestamp=timestamp)
    return formatedstamp
def createstorytimestamp(timestamplist,iswithoutro=False):
    finallist=[]
    counter=0
    for timestamp in timestamplist:
        counter+=1
        if counter==len(timestamplist) and iswithoutro:
            finallist.append(formattimestamp(timestamp,"{timestamp} - Outro"))
        else:
            finallist.append(formattimestamp(timestamp,"{timestamp} - Story {counter}",counter))
    return "\n".join(finallist)
def inputtimestamps():
    timestamps=[]
    put=input("Enter New Timestamp (#1):")
    count=1
    while(len(put)>1):
        timestamps.append(put)
        count+=1
        put=input("Enter New Timestamp (#"+str(count)+"):")
    return timestamps
def copycliptimestamps():
    timestamps=inputtimestamps()
    withoutro=input("Does It Include An Outro? [Y for yes,else for no]:")
    output=createstorytimestamp(timestamps,withoutro=="Y")
    pyperclip.copy(output)
    print("Cliped!")
copycliptimestamps()
