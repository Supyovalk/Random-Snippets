#Purpose: Forgotten
def r1(x):
    if x==0:
        return 3
    if x==1:
        return 5
    return 3*r1(x-1)+2*r1(x-2)
def r2(x,y):
    return (2*x*y)/(x+y)
print(r2(0.82753,0.82132))