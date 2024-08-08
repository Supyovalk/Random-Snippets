#Made to make excel lists
#[Name (N),Letter value (L),number (I)]
#->=COUNTA('[N]'![L][I]:[I])+COUNTA('[N]'![L-1]2:[L-1][I-1])
#Starts in [N,3,2] and raises by [=,+1,+1]
#NOTE: The last one needs to manually fixed to remove the first part!
import pyperclip
import xlsxwriter 
def getcountaline(name,letter,number):
    l1,l2=(xlsxwriter.utility.xl_col_to_name(letter-1),xlsxwriter.utility.xl_col_to_name(letter-2))
    str1= "=COUNTA('{N}'!{L1}{N1}:{N1})".format(N=name,L1=l1,N1=number)
    if(number>2):
        str1+="+COUNTA('{N}'!{L2}2:{L2}{N2})".format(N=name,L2=l2,N2=number-1)
    return str1
def getcountalinescount(name,count):
    start=3
    lines=[getcountaline(name,start+i,start-1+i) for i in range(count)]
    return "\n".join(lines)
pyperclip.copy(getcountalinescount('Winter Collab',21))
print("copied")
