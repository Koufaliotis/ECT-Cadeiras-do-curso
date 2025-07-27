
#caracter criation
from os import name
import random
import LoadSaveCaracters
import stageDisplay
#combat
import combat

mycaracters = LoadSaveCaracters.mycaracters
print(__name__)



#load enemys
    #stage 1 enemys
#enemyDic = {}
#enemysdata = open("enemysfolder.txt","r")
#for data in enemysdata:
 #   caracterdata = data.split(",")
  #  name = caracterdata[0]
  #  hp = int(caracterdata[1])
  #  damage = int(caracterdata[2])
  #  magicdamage = int(caracterdata[3])
  #  blockDamage = int(caracterdata[4])
  #  dogeChance = int(caracterdata[5])

  #  enemyDic[name] =[name,hp,damage,magicdamage,blockDamage,dogeChance]
  #  print(enemyDic)
#enemysdata.close()
#+++++++
QuitOption = False
while QuitOption == False:
    #+++++ caracter turn
    
    print("""
#########################################################################################################################
#      _____                                                                                                            #
#     |Fight| stage: []                                                                                                 #
#                                                                                                                       #
#      ____                                                                                                             #
#     |Shop|                                                                                                            #
#                                                                                                                       #
#      _______                                                                                                          #
#     |levelup|                                                                                                         #
#                                                                                                                       #
#      ________                                                                                                         #
#     |QuitGame|                                                                                                        #
#########################################################################################################################
    \n""")
    enemyDic = {}
    enemyDic = LoadSaveCaracters.EnemyLoader()
    
    print(enemyDic)
    

    MenuOption = input("menu select: ")
    while MenuOption == "Fight":
   #++++actions missing
        for key in mycaracters.keys():
            
            if mycaracters[key][2] != 0:
                selectedCar = key
            else:
                selectedCar = ""
            stageDisplay.display(mycaracters,enemyDic,key)
            
        #attack faze
            attacking = False
            if selectedCar != "":
                while True:
                    enemy = input("write the enemys name to select them: ")
                    #missing special attck item in inventory validation
                    actionOption = input("whats your action: ")
                    if enemyDic[enemy][1] != 0:
                        break
                    print(f"the {enemy} is deads")
                attacking = True
            while attacking == True:
                #import combat.py
                if selectedCar == "knight":
                    enemyDic[enemy][1] = combat.knightActions(actionOption,mycaracters[selectedCar],enemyDic[enemy])
                    attacking = False

                if selectedCar == "archer":
                    enemyDic[enemy][1] = combat.archerActions()
                    attacking = False

                if selectedCar == "mage":
                    enemyDic[enemy][1] = combat.mageActions(actionOption,mycaracters[selectedCar],enemyDic[enemy])
                    attacking = False

                if selectedCar == "swordsman":
                    enemyDic[enemy][1] =combat.swordsmanAction()
                    attacking = False
                    
                # missing all enemys dead
                    
        #difence faze
        print("difence faze")
        caractersLstKeys = []
        for character in mycaracters.keys():
            caractersLstKeys.append(mycaracters[character][1])
                #++++++
        for enemySelect in enemyDic.keys():

            #missing update screen make costome one

            if enemyDic[enemySelect][1] > 0: #if enemy alive
                #verify if caracter exists and if he is alive
                while True:
                    randcar = random.randint(0,3)
                    if caractersLstKeys[randcar]!= "carclass" and mycaracters[caractersLstKeys[randcar]][2] > 0: #why my hp is str
                        #attack
                        break
                    # missing all heros dead
                mycaracters[caractersLstKeys[randcar]][2] = combat.enemyAttack(mycaracters[caractersLstKeys[randcar]],enemyDic[enemySelect]) # update hero hp
                #attack mycharacter
            
    enemyKeys= enemyDic.keys()
    if enemyDic[enemyKeys[0]][1] == 0 and enemyDic[enemyKeys[1]][1] == 0 and enemyDic[enemyKeys[2]][1] == 0 and enemyDic[enemyKeys[3]][1] == 0:
        break
        #end batle
