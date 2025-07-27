#caracter creation
#may have a problem with values int beter round the nums!!!!!!!
from os import write
def StatAtribute(playerData):
    if playerData[1] == "knight":
        damage = 0.65 * int(playerData[3])+ 0.35 * int(playerData[6]) 
        magicdamage = int(playerData[5])
        blockDamage = 0.6 * int(playerData[4])
        dogeChance = 0.2 * int(playerData[6])
        Hp = int(playerData[2])
        lvl = playerData[7]
        name = playerData[0]
        data = [name,playerData[1],Hp,damage,magicdamage,blockDamage,dogeChance,lvl]
        print(data)
        return data

    elif playerData[1] == "archer":
        damage = 0.20 * int(playerData[3])+ 0.80 * int(playerData[6])
        magicdamage = int(playerData[5])
        blockDamage = 0.2 * int(playerData[4])
        dogeChance = 0.4 * int(playerData[6])
        Hp = int(playerData[2])
        lvl = playerData[7]
        name = playerData[0]
        data = [name,playerData[1],Hp,damage,magicdamage,blockDamage,dogeChance,lvl]
        print(data)
        return data

    elif playerData[1] == "mage":
        damage = 0.65 * int(playerData[3])+ 0.35 * int(playerData[6]) 
        magicdamage = (0.9 * int(playerData[5]) +0.1 * int(playerData[6])/ int(playerData[3]))
        blockDamage = 0.6 * int(playerData[4])
        dogeChance = 0.2 * int(playerData[6])
        Hp = int(playerData[2])
        lvl = playerData[7]
        name = playerData[0]
        data = [name,playerData[1],Hp,damage,magicdamage,blockDamage,dogeChance,lvl]
        print(data)
        return data

    elif playerData[1] == "swordsman":
        damage = 0.65 * int(playerData[3])+ 0.35 * int(playerData[6]) + 0.1 * int(playerData[5])
        magicdamage = playerData[5]
        blockDamage = 0.6 * int(playerData[4])
        dogeChance = 0.2 * int(playerData[6])
        Hp = int(playerData[2])
        lvl = playerData[7]
        name = playerData[0]
        data = [name,playerData[1],Hp,damage,magicdamage,blockDamage,dogeChance,lvl]
        print(data)
        return data
def CaracterCreation():
    caracter_files = open("maincaracters.txt","r")
    caracters = []
    for caracterData in caracter_files:
        Data = caracterData.split(",")
        Class_name = Data[0]
        MaxHp = Data[1]
        Attack = Data[2]
        Diffence = Data[3]
        MagicPower = Data[4]
        Speed = Data[5]
        LVL = Data[6]
        caracters.append((Class_name,MaxHp,Attack,Diffence,MagicPower,Speed,LVL))
    print(caracters)

    CaracterSelect = input("select your caracter:")
    #input with button after
    caracterName = input("Name your caracter: ")
    for maincaracter in caracters:
        if maincaracter[0] == CaracterSelect:
            maincaracterfile = open("maincaracter.txt","w")
            writendata = caracterName
            for i in range(0,7):
                writendata +="," + maincaracter[i]
            maincaracterfile.write(writendata)
            maincaracterfile.close()

    caracter_files.close()
print(__name__)
