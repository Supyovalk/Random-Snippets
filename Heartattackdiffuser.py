import pandas as ps
import csv  
def extractdata(csvpath):
    with open(csvpath, 'r') as f:          # Read lines separately
        reader = csv.reader(f, delimiter='t')
        for i, line in enumerate(reader):
            if(i>1):
                line=line[0].split(',')
                print(line)
                line=[float(value) for value in line]
                showcaseentry(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13])

def showcaseentry(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall,output):
    conditions=[age>65,sex>0,cp<=1,trtbps>140,chol>200,fbs>0,thalachh>140,restecg>0,exng>1,oldpeak>3,caa>1,thall>1]
    value=sum([1 if True==x else 0 for x in conditions])
    print("Conditions count:"+str(value)+ "/13,FINAL OUTPUT:"+ str(output))
extractdata("heart.csv")