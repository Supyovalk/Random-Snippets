import pyperclip
def formtable(maps):
    newtxt=chr(9)
    for map in maps:
        newtxt+=map+chr(9)
    newtxt=newtxt[:-1]+chr(10)
    mapcount=len(maps)
    for map in maps:
        row=map
        row+=chr(9)*mapcount
        newtxt+=row+chr(10)
    return newtxt
def main():
    maps=[]
    input=input("Add map or rows of map:")
    while not input=="":
        if '\n' in input:
            maps.append(input.split('\n'))
        else:
            maps.append(input)
        input=input("Add map or rows of map:")
    pyperclip.copy(formtable(maps))
    print("COPIED")
main()