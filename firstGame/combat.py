import random


def knightActions(*args):
    action = args[0]
    
    enemy = args[2][0]
    enemysHP = args[2][1]
    enemyDogeChance = args[2][5]
    enemyBlock = args[2][4]
    if action == "slice":
        dogechance = random.randint(1,100)
        print(dogechance)
        if dogechance > enemyDogeChance:
            attackDamage = args[1][3]
            enemysHP = enemysHP + enemyBlock - attackDamage #+++++++++ if block> attack skip calculation
            if enemysHP < 0:
                enemysHP = 0
            return enemysHP
        return enemysHP

def archerActions(*args):
    action = args[0]
    attackDamage = args[1]
    enemy = args[2]
    enemysHP = args[3]
    enemyDogeChance = args[4]
    enemyBlock = args[5]
    if action == "arrow":
        dogechance = random.randint(1,100)
        print(dogechance)
        if dogechance > enemyDogeChance:
            enemysHP = enemysHP + enemyBlock - attackDamage 
            return enemysHP
        return enemysHP
def mageActions(*args):
    action = args[0]
    
    enemy = args[2][0]
    enemysHP = args[2][1]
    enemyDogeChance = args[2][5]
    enemyBlock = args[2][4]
    if action == "staf":
        dogechance = random.randint(1,100)
        print(dogechance)
        if dogechance > enemyDogeChance:
            attackDamage = args[1][3]
            enemysHP = enemysHP + enemyBlock - attackDamage
            if enemysHP < 0:
                enemysHp = 0
            return enemysHP

        return enemysHP
    elif action == "MagicMisile":
        dogechance = random.randint(1,100)
        print(dogechance)
        if dogechance > enemyDogeChance:
            attackDamage = args[1][4]
            enemysHP = enemysHP + enemyBlock - attackDamage 
            if enemysHP < 0:
                enemysHp = 0
            return enemysHP
        return enemysHP

def swordsmanAction(*args):
    action = args[0]
    attackDamage = args[1]
    enemy = args[2]
    enemysHP = args[3]
    enemyDogeChance = args[4]
    enemyBlock = args[5]
    if action == "slice":
        dogechance = random.randint(1,100)
        print(dogechance)
        if dogechance > enemyDogeChance:
            enemysHP = enemysHP + enemyBlock - attackDamage 
            return enemysHP
        return enemysHP
#missing enemy attacking
def CombatActioin(*args):
    attackDamage = args[0]
    enemyBlock = args[1]
    enemysHP = args[2]
    enemyDogeChance = args[3]
    dogechance = random.randint(1,100)
    if dogechance > enemyDogeChance:
            if enemyBlock < float(attackDamage):
                enemysHP = enemysHP + enemyBlock - attackDamage 
                return enemysHP
    return enemysHP

def enemyAttack(*args):
    HeroData = args[0]
    HeroHp = HeroData[2] 
    HeroDefence = HeroData[5]
    HeroDoge = HeroData[6]
    
    enemyData = args[1] 
    enemyDamage = enemyData[2]
    enemyActions = enemyData[len(enemyData) - 1]
    
    
    while True:
        randomActions = random.randint(0,len(enemyActions) - 1)
        if enemyActions[randomActions] == "swing":
            HeroHp = CombatActioin(enemyDamage,HeroDefence,HeroHp,HeroDoge)
            break
        elif enemyActions[randomActions] == "poke":
            HeroHp = CombatActioin(enemyDamage,HeroDefence,HeroHp,HeroDoge)
            break
    return HeroHp