def linktostring(linktuple,lineseperate=" "):
    if(linktuple[0]):
        return "[["+linktuple[2]+lineseperate+linktuple[1]+"]]"
    else:
        return linktuple[2]

#{title:"",sections:[{header:"",links:[[isbracketed,title,link],[sbracketed,title,link]]},{}}
def navDictTransformTropeTv(dict):
    finalstr="[[WMG:[[center: [- "
    finalstr=finalstr+"''"+dict["title"]+"'' \\\\\n"
    for section in dict["sections"]:
        sectiontext=section["header"]+": "+" - ".join([linktostring(i) for i in section["links"]])
        finalstr=finalstr+sectiontext+" \\\\\n"
    finalstr=finalstr+"-] ]]]]"
    return finalstr
#needs header variables
def navDictTransformFandom(dict):
    finalstr='{|class="mw-collapsible mw-collapsed" width="100%" style="border:1px solid #330033; text-align:center; clear:both; font-size:90%; font-family:Arial;" \n| align=center class="color-base" style="background:#FB49ED;font-size:80%;" colspan=2 | <span style="float:left;" class="plainlinks"><font style="font-size:10px;">[[Template:MusicNav|v]] • [{{fullurl:Template:MusicNav|action=edit}} e]</font></span> <span class="color-text" style="absolute:center;font-size:150%;font-family:Arial">'+dict["title"]+'</span>\n|-\n'
    for section in dict["sections"]:
        sectiontext='! colspan="8" style="background:#FB49ED" align="center"|<font color="white">'+section["header"]+'</font>\n|-\n| '
        sectiontext=sectiontext+" - ".join([linktostring(i,"|") for i in section["links"]])+"\n|-\n"
        finalstr=finalstr+sectiontext
    finalstr=finalstr+"|}"
    return finalstr
def CreateNav():
    dict=Inputnavdict()
    mode=input("Dictoanary is initaied! Enter conversion mode [1-TropeTv,2-Fandom]")
    if(mode=='1'):
        return navDictTransformTropeTv(dict)
    if(mode=='2'):
        return navDictTransformFandom(dict)
    return "Contraction Code Invaild"
def Inputnavdict():
    finaldict={}
    finaldict["title"]=input("Enter NavBox Header:")
    finaldict["sections"]=[]
    sectionheader=input("Input Section Header:")
    while(not sectionheader==""):
        linklst=[]
        link=input("Enter Link:")
        while (not link==""):
            linktitle=input("Enter Title (Optional):")
            isbracketed = not linktitle==""
            linklst.append((isbracketed,linktitle,link))
            link=input("Enter Link:")
        sectiondict={"header":sectionheader,"links":linklst}
        finaldict["sections"].append(sectiondict)
        sectionheader=input("Input Section Header:")
    return finaldict
print(CreateNav())
#print(navDictTransformFandom({"title":"hope"}))
###[[WMG:[[center: [- ''Role Association - Video Games''\\
### English ([[RoleAssociation/VideoGamesEnglishAToK 0-9 & A-K]] | [[RoleAssociation/VideoGamesEnglishLToZ L-Z]]) | [[RoleAssociation/VideoGamesFrench French]] | [[RoleAssociation/VideoGamesItalian Italian]] | [[RoleAssociation/VideoGamesJapanese Japanese]] | [[RoleAssociation/VideoGamesKorean Korean]] | '''Polish''' | [[RoleAssociation/VideoGamesSpanish Spanish]] \\
###Individual Games: ''RoleAssociation/{{Danganronpa}}'' | ''RoleAssociation/FireEmblem'' (''[[RoleAssociation/FireEmblemAwakening Awakening]]'' | ''[[RoleAssociation/FireEmblemThreeHouses Three Houses]]'' | ''[[RoleAssociation/FireEmblemEngage Engage]]'' | ''[[RoleAssociation/FireEmblemHeroes Heroes]]'') | ''RoleAssociation/GenshinImpact'' | ''RoleAssociation/{{Persona}}'' | ''RoleAssociation/SuperSmashBros'' ]] -]]]