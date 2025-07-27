def display(heros,enemys,Herodata):
    #+++missing inventory
    AttackTipes, SpecialAttacks= HeroActions(heros,Herodata)
    mycaracters = heros
    enemyDic = enemys
    print("""
#########################################################################################################################
#                                                                                                                       #
#                                                                                                                       #
#                                                                                                                       #
#                        {} hp: {}                                                                     {} hp: {}        #
#                        0                                                                            0                 #
#                       /|\                                                                          /|\                #
#                       / \                                                                          / \                #          
#                                                                                                                       #
#                        {} hp: {}                                                                     {} hp: {}        #
#                        0                                                                            0                 #
#                       /|\                                                                          /|\                #
#                       / \                                                                          / \                #
#                                                                                                                       #
#                        {} hp: {}                                                                     {} hp: {}        #
#                        0                                                                            0                 #
#                       /|\                                                                          /|\                #
#                       / \                                                                          / \                #
#                                                                                                                       #
#                        {} hp: {}                                                                     {} hp: {}        #
#                        0                                                                            0                 #
#                       /|\                                                                          /|\                #
#                       / \                                                                          / \                #
#_______________________________________________________________________________________________________________________#
#        Actions                                                                                                        #
#        Attack tipes:{}                                                                                                #
#        special attacks:{}                                                                                             #
#        items:                                                                                                         #
#                                                                                                                       #
#                                                                                                                       #
#########################################################################################################################
        """.format(mycaracters["knight"][0],mycaracters["knight"][2],
           enemyDic["goblin1"][0],enemyDic["goblin1"][1],
           mycaracters["archer"][0],mycaracters["archer"][2],
           enemyDic["goblin2"][0],enemyDic["goblin2"][1],
           mycaracters["mage"][0],mycaracters["mage"][2],
           enemyDic["goblin3"][0],enemyDic["goblin3"][1],
           mycaracters["swordsman"][0],mycaracters["swordsman"][2],
           enemyDic["goblin4"][0],enemyDic["goblin4"][1],AttackTipes,SpecialAttacks,))

def HeroActions(*args):
    heroLst = args[0]
    heroName = args[1]
    ActionData = ""
    heroCalss = heroLst[heroName][1]
    myFile = open("CaractersActions.txt","r")
    for line in myFile:
        data = line.split(",")
        if data[0] == heroCalss:
            ActionData = data

    myFile.close()
    switch = False
    AttackTipes = ""
    SpecialAttacks = ""
    for data in ActionData[1:len(ActionData)-1]:
        if switch == False and data != ":":
            AttackTipes += data + " "
        else:
            if data == ":":
                switch = True
            else:
                # remember to varrify if can use special attacks by inventory 
                SpecialAttacks += data + " "



    return AttackTipes, SpecialAttacks

