import time
import os 

def encodeduo(x,y):
    return (2**x+(2*y+1))-1
def decodeduo(n):
    n+=1
    x=0
    while(n%2==0):
        n=n//2
        x+=1
    return (x,(n+1)//2)
def decodetrio(n):
    x,m=decodeduo(n)
    y,z=decodeduo(m)
    return (x,y,z)
def encodetrio(x,y,z):
    return encodeduo(x,encodeduo(y,z))
print(decodetrio(144387))
def writetriostofile(division100):
    path = './Ggroup'
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)  
    with open(path+'/GgroupInstructTrios'+str(division100),'w') as file:
        for i in [j+100*division100 for j in range(1,101)]:
            x,y,z=decodetrio(i)
            file.write(str(i)+"=<"+str(x)+",<"+str(y)+","+str(z)+">>\n")
            import time

start = time.time()
for i in range(1):
    writetriostofile(i)
end = time.time()  
print(end - start)
