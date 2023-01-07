

def mancala():
   
    
    movePeice()
    
    




def movePeice():
    bord = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    playerOne = True
    print str(bord)
    intMove = 8
    
    while intMove > 6 or intMove < 0:
        intMove = int(input("choose a move.(num les than 7)(not 0)")) 
    numAt = bord[intMove]
   
    if playerOne and intMove > 0 and intMove < 7 and numAt != 0:
        del bord[intMove]
        bord.insert(intMove, 0)
        for num in range(numAt):
            if  num == numAt -1:
                   if intMove + num + 1 == 0 or intMove + num + 1 == 7:
                       modifAmnt = bord[intMove + num + 1] + 1
                       del bord[intMove + num + 1]
                       bord.insert(intMove + num + 1, modifAmnt)
                       print str(bord)
                       intMove = 8
                       

                   elif bord[intMove + num + 1] == 0:
                        modifAmnt = bord[intMove + num + 1] + 1
                        del bord[intMove + num + 1]
                        bord.insert(intMove + num + 1, modifAmnt)
                        playerOne = not(playerOne)
                        print str(bord)

                   else:
                       intMove = intMove + num + 1
                       

                

            else:   
                modifAmnt = bord[intMove + num + 1] + 1
                del bord[intMove + num + 1]
                bord.insert(intMove + num + 1, modifAmnt)
    if not(playerOne) and intMove > 0 and intMove < 7 and numAt != 0:
        pTwoIntMove = intMove + 7
        del bord[pTwoIntMove]
        bord.insert(pTwoIntMove, 0)
        for num in range(numAt):
            if  num == numAt -1:
                   if intMove + num + 1 == 0 or intMove + num + 1 == 7:
                       intMove = 8

                   elif bord(pTwoIntMove + num + 1) == 0:
                        modifAmnt = bord[pTwoIntMove + num + 1] + 1
                        del bord[pTwoIntMove + num + 1]
                        bord.insert(pTwoIntMove + num + 1, modifAmnt)
                        playerOne = not(playerOne)

                   else:
                       intMove = pTwoIntMove + num + 1
                       

                

            else:   
                modifAmnt = bord[pTwoIntMove + num + 1] + 1
                del bord[pTwoIntMove + num + 1]
                bord.insert(pTwoIntMove + num + 1, modifAmnt)




            
            
