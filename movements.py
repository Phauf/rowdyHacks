from random import randint

health = 200
enemyhealth = 10
bosshealth = 20
dbhealth = 20
key = 0



def main():
    x, y = 6, 3
    while(True):
        print("Where do you wanna go next?", end=" ")
        if (x == 6 and y == 2):
            print("East or West?")
        elif (x == 6 and y == 3):
            print("East or West?")
        elif (x == 6 and y == 1):
            print("East, West or North?")
        elif (x == 6 and y == 0):
            print("North or East?")
        elif (x == 6 and y == 4):
            print("East or West?")
        elif (x == 6 and y == 5):
            print("East or West?")
        elif (x == 6 and y == 6):
            print("North or West?")
        elif (x == 5 and y == 2):
            print("North or East?")
        elif (x == 5 and y == 1):
            print("North or South?")
        elif (x == 5 and y == 0):
            print("North or South?")
        elif (x == 5 and y == 4):
            print("North or West?")
        elif (x == 5 and y == 5):
            print("You can only go North")
        elif (x == 5 and y == 6):
            print("North or South?")
        elif (x == 5 and y == 3):
            print("North, East or West?")
        elif (x == 4 and y == 2):
            print("East or South?")
        elif (x == 4 and y == 1):
            print("North or South?")
        elif (x == 4 and y == 0):
            print("You can only go South")
        elif (x == 4 and y == 4):
            print("West or South?")
        elif (x == 4 and y == 5):
            print("North, South or West?")
        elif (x == 4 and y == 6):
            print("West or South?")
        elif (x == 4 and y == 3):
            print("South, West or East?")
        elif (x == 3 and y == 2):
            print("East or West?")
        elif (x == 3 and y == 1):
            print("South or East?")
        elif (x == 3 and y == 0):
            print("You can only go North")
        elif (x == 3 and y == 4):
            print("East or West?")
        elif (x == 3 and y == 5):
            print("East or West?")
        elif (x == 3 and y == 6):
            print("North or West?")
        elif (x == 3 and y == 3):
            print("South, East or West?")
        elif (x == 2 and y == 2):
            print("East or West?")
        elif (x == 2 and y == 1):
            print("East or West?")
        elif (x == 2 and y == 0):
            print("North, East or South?")
        elif (x == 2 and y == 4):
            print("East or West?")
        elif (x == 2 and y == 5):
            print("East or West?")
        elif (x == 2 and y == 6):
            print("North, West or South?")
        elif (x == 2 and y == 3):
            print("East or West?")
        elif (x == 1 and y == 2):
            print("North or West?")
        elif (x == 1 and y == 1):
            print("East or West?")
        elif (x == 1 and y == 0):
            print("South or East?")
        elif (x == 1 and y == 4):
            print("East or West?")
        elif (x == 1 and y == 5):
            print("You can only go West")
        elif (x == 1 and y == 6):
            print("North or South?")
        elif (x == 1 and y == 3):
            print("North or East?")
        elif (x == 0 and y == 2):
            print("West or South?")
        elif (x == 0 and y == 1):
            print("East or West?")
        elif (x == 0 and y == 0):
            print("North or East?")
        elif (x == 0 and y == 4):
            print("East or West?")
        elif (x == 0 and y == 5):
            print("East or West?")
        elif (x == 0 and y == 6):
            print("West or South?")
        elif (x == 0 and y == 3):
            print("South or East?")

        nextMove = input()
        if (nextMove == "E"):
            y = y+1
            bobo = econd(x, y, key)
            if (bobo == False):
                break
            else:
                continue

        elif (nextMove == "W"):
            y = y-1
            bobo = wcond(x, y, key)
            if (bobo == False):
                break
            else:
                continue

        elif (nextMove == "N"):
            x = x - 1
            bobo = ncond(x, y, key)
            if (bobo == False):
                break
            else:
                continue

        elif (nextMove == "S"):
            x = x+1
            bobo = scond(x, y, key)
            if (bobo == False):
                break
            else:
                continue

        else:
            print("Duhh!! You're moving in the wrong direction!!")


def ncond(x, y, key):
    enemy = isEnemy(x, y)
    if (enemy):
        if(EnemyFight(health, enemyhealth) == False):
            return False
    Key = isKey(x, y, key)
    boss = isBoss(x, y)
    if (boss):
        if(BossFight(health, bosshealth) == False):
            return False

    villager = isVillager(x, y)
    doubleEnemey = isDoubleEnemy(x, y)
    if (doubleEnemey):
        if(DoubleEnemyFight(health, dbhealth) == False):
            return False
        elif(DoubleEnemyFight(health, dbhealth) == True):
            key = key+1

    return True


def scond(x, y, key):
    enemy = isEnemy(x, y)
    if (enemy):
        if(EnemyFight(health, enemyhealth) == False):
            return False

    Key = isKey(x, y, key)
    boss = isBoss(x, y)
    if(boss):
        if(BossFight(health, bosshealth) == False):
            return False

    villager = isVillager(x, y)
    doubleEnemey = isDoubleEnemy(x, y)
    if (doubleEnemey):
        if(DoubleEnemyFight(health, dbhealth) == False):
            return False
        elif(DoubleEnemyFight(health, dbhealth) == True):
            key = key+1
    return True


def econd(x, y, key):

    enemy = isEnemy(x, y)
    if (enemy):
        if(EnemyFight(health, enemyhealth) == False):
            return False
    Key = isKey(x, y, key)
    boss = isBoss(x, y)
    if (boss):
        if(BossFight(health, bosshealth) == False):
            return False
    villager = isVillager(x, y)
    doubleEnemey = isDoubleEnemy(x, y)
    if (doubleEnemey):
        if(DoubleEnemyFight(health, dbhealth) == False):
            return False
        elif(DoubleEnemyFight(health, dbhealth) == True):
            key = key+1
    return(True)


def wcond(x, y, key):
    enemy = isEnemy(x, y)
    if (enemy):
        if(EnemyFight(health, enemyhealth) == False):
            return False

    Key = isKey(x, y, key)
    boss = isBoss(x, y)
    if (boss):
        if(BossFight(health, bosshealth) == False):
            return False
    villager = isVillager(x, y)
    doubleEnemey = isDoubleEnemy(x, y)
    if (doubleEnemey):
        if(DoubleEnemyFight(health, dbhealth) == False):
            return False
        elif(DoubleEnemyFight(health, dbhealth) == True):
            key = key+1
    return True


def isEnemy(x, y):
    if((x == 0 and y == 0) or (x == 1 and y == 1) or (x == 0 and y == 4) or (x == 1 and y == 6) or (x == 3 and y == 1) or (x == 4 and y == 3) or (x == 6 and y == 0) or (x == 6 and y == 4)):
        print("There is an enemy right in front of you!")
        return True
    else:
        return False


def EnemyFight(health, enemyhealth):

    while(health > 0 and enemyhealth > 0):
        pdice = randint(2, 12)
        edice = randint(2, 12)

        health = health - pdice
        enemyhealth = health - edice

    if(health <= 0):
        print("YOU HAVE DIED")
        return False
    elif(enemyhealth <= 0):
        print("Good job, you defeated the enemy")
        return True


def isKey(x, y, key):
    if((x == 1 and y == 5) or (x == 5 and y == 3)):
        key = key + 1
        print("You found a key! You need 3 in total to escape the maze. You have", key, " keys.")

    return key


def isBoss(x, y):
    if(x == 4 and y == 0):
        print("There is a boss in front of you. Get ready to fight!")
        return True
    else:
        return False


def BossFight(health, bosshealth):

    while(health > 0 and bosshealth > 0):

        pdice = randint(2, 12)
        bdice = randint(2, 12)

        health = health - pdice
        bosshealth = bosshealth - bdice

    if(health <= 0):
        print("YOU HAVE DIED")
        return False
    elif(bosshealth <= 0):
        print("You have killed the boss! Good job!")
        return True


def isVillager(x, y):

    if(x == 4 and y == 6):
        print("Villager: Help me! There are 2 enemies to your west, kill them and I will reward you.")
        return True
    else:
        return False


def isDoubleEnemy(x, y):
    if(x == 4 and y == 5):
        print("There are 2 enemies about to attack you! Roll your dice!")
        return True
    else:
        return False


def DoubleEnemyFight(health, dbhealth):
    while(health > 0 and dbhealth > 0):

        pdice = randint(2, 12)
        dbdice = randint(2, 12)

        health = health - pdice
        dbhealth = dbhealth - pdice

    if(health <= 0):
        print("YOU HAVE DIED")
        return False
    elif(dbhealth <= 0):
        print("Good job, you defeated the 2 enemies! The villager has given you a key.")
        return True


main()
