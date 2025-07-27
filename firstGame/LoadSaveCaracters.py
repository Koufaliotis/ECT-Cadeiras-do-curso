#load caracter
#global mycaracters
import caracterselector

def EnemyLoader():#the variable may be stage num
    #missing select enemy by stage
    enemyDic = {}
    enemysdata = open("enemysfolder.txt","r")# may change 
    for data in enemysdata:
         RowDiv = data.split("|")
         caracterdata = RowDiv[0].split(",")
         
         name = caracterdata[0]
         hp = int(caracterdata[1])
         damage = int(caracterdata[2])
         magicdamage = int(caracterdata[3])
         blockDamage = int(caracterdata[4])
         dogeChance = int(caracterdata[5])

         characterActions = RowDiv[1].split(",")

         enemyDic[name] =[name,hp,damage,magicdamage,blockDamage,dogeChance,characterActions]
    
    enemysdata.close()
    print("Load ended")
    return enemyDic


print(__name__)

#opening menu
print("""
#########################################################################################################################
#    _______                                                                                                            #
#   |NewGame|                                                                                                           #
#    ________                                                                                                           #
#   |continue|                                                                                                          #
#    _______                                                                                                            #
#   |credits|                                                                                                           #
#                                                                                                                       #
#                                                                                                                       #
#########################################################################################################################
""")

#
caractersDic = {}
menuinput = input("write one of the option to select them: ")
if menuinput == "NewGame":
    caracterselector.CaracterCreation()

with open('maincaracter.txt', "r") as mycaracter:
    carclasses =["knight","archer","swordsman","mage"]
    for line in mycaracter:
        playerData = line.split(",")
        caracterData = caracterselector.StatAtribute(playerData)
        caractersDic[caracterData[1]] = caracterData
        print(caractersDic.keys())
        for carclass in carclasses:
            if carclass not in caractersDic.keys():
                caractersDic[carclass] =["missing car","carclass",0,0,0,0,0,0]
        mycaracters = caractersDic 
    #print(playerData)
    #print(StatAtribute(playerData)) #global var
