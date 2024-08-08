import pyperclip
def formtable(maps):
    newtxt=""
    mapcount=len(maps)
    newtxt+=chr(9)

    for map in maps:
        newtxt+=map+chr(9)
    newtxt=newtxt[:-1]+chr(10)
    for map in maps:
        row=map
        row+=chr(9)*mapcount
        newtxt+=row+chr(10)
    return newtxt
maps=[]
inp=input("Add map or rows of map:")
while(not inp==""):
    if('\n' in inp):
        maps.append(inp.split('\n'))
    else:
        maps.append(inp)
    inp=input("Add map or rows of map:")
pyperclip.copy(formtable(maps))
print("COPIED")