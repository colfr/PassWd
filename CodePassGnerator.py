# -*- coding: utf-8 -*-
import random

doc = """ Retourne une liste Alpha MinMaj"""

index =0

def getAlpha() :

        isCapitalize = random.randrange(1500)%2

        if(isCapitalize):
            return chr(random.randrange(65,90))
        else:
            return chr(random.randrange(97,122))


def getNumeric():

    return random.randrange(0,9)




def getWithSpecialCaract(index):


        return chr(index)




def getPassWord(num, default=0):
    """
     obtient une liste de lettre en fonction de deux params
     params 1 : nombre de lettres
     params2 : choix de type de mot de passe

    """

    num = int(num)
    listPassWd = ""
    i = 1

    if(default):

        while(i<=num):

            listPassWd+= getAlpha()
            i = i +1
    else:
        while(i<=num):
            index = random.randrange(33,126)
            if(isOutOfList(index)):
                listPassWd+= getWithSpecialCaract(index)
            else:
                i= i-1
            i = i +1

    return  listPassWd



def isOutOfList(index):

    listeNumber = [34, 39, 40, 41,44, 46,58, 59,91,92,93,94, 96, 123, 124, 125]

    for item in listeNumber :

        if(item == index):
            return False

    return True


if __name__ == "__main__":

    num = input("Choisissez le nombre de caractères pour le mot de passe : ")

    print (getPassWord(int(num)))

