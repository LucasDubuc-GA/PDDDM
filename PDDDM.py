#coding:utf-8

"""
Fuking Stupide Donjon
@autor: Lucas Dubuc aka un idiot bête
"""
import os #utiliser pour éfacer le cmd et faire des pauses
import random # postion des murs, fun, potions
import keyboard # dérecter les action du joueur
import time # faire des pauses
import threading #jouer de la musique en jouen


"""
class sac dédier à toutes les variables
que je peut vouloir utiliser dans plusieurs fonction du code
"""
class sac:
    job = ""
    potionForce = 1 
    potionEndur = 1
    life = 3  
    mort = ""
    mamelou = 0
    chemiseHawaien = 0
    tekila = 3
    robinéMagique = 0
    cptWin = 0
    actionMax = 25
    vieMax = 6
    limiteOverDose = 3
    competenec = 1
    kwinaman = 0
    fumisterie = 0    
      

"""
fonction dédier à l'affichage
du jeux
"""        
def afficherTab(tab, cptAction, dificulté):
    print("\n\033[1;49;32mfloor:", sac.cptWin, "\033[0m")
    
    action = sac.actionMax - cptAction
   
    print(" +---------------------------------------+")
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if action <= dificulté + 3 or sac.life == 0 and sac.job != "Athlète   ":
                chaine = " | \033[1;49;31m" + tab[i][j] + "\033[0m"
                print( chaine, end= '')
            else:
                print(" |", tab[i][j], end='')
        print(" |")
    print(" +---------------------------------------+")
    if sac.cptWin == 0 and cptAction == 0:
        print("                         \033[1;49;34msortie -------^\033[0m  ")
    
    
    print("action:", action, " ",end = '')
    for i in range(action):  
        if action > 24:
            print("\033[1;49;34m#", end = '')
        elif action <=24 and action > 16:
            print("\033[1;49;32m#", end = '')
        elif action <= 16 and action > 8:
            print("\033[0;49;33m#", end = '')
        else:
            print("\033[1;49;31m#", end = '')
    print("\033[0m")
    if sac.job != "Athlète   ":
        i = 0
        strVie = ""
        while i < sac.life:
            strVie += "<3 "
            i += 1
        print("\033[0;49;35mLife:", strVie, "\033[0m\n")

"""
fonction principal de jeux
"""
def main(dificulté):

    tab = [
        # 0   1   2   3   4   5   6   7   8   9 
        [" "," "," "," "," "," "," "," "," "," "],#0
        [" "," "," "," "," "," "," "," "," "," "],#1
        [" "," "," "," "," "," "," "," "," "," "],#2
        [" "," "," "," "," "," "," "," "," "," "],#3
        [" "," "," "," "," "," "," "," "," "," "],#4
        [" "," "," "," "," "," "," "," "," "," "],#5
        [" "," "," "," "," "," "," "," "," "," "],#6
        [" "," "," "," "," "," "," "," "," "," "],#7
        [" "," "," "," "," "," "," "," "," "," "],#8
        [" "," "," "," "," "," "," "," "," "," "] #9
    ]
    #Position du personage
    posX = 0
    posY = 0
    avatar = "\033[0;49;33mO\033[0m"
    tab[posY][posX] = avatar
    force = False
    cptAction = 0
    laste = ""
    shield = False
    if sac.job == "Chevalier ":
        shield = True
    noTrap = False
    noOD = False
            
    if dificulté == 3 and sac.job != "Alchimiste":
        sac.potionEndur = 0
        sac.potionForce = 0
    
    if sac.cptWin > 10 and sac.cptWin < 20 and sac.job == "Gladiateur" :
            sac.actionMax += 5
            print("Vos effort vous ont rendu plus endurent")
            time.sleep(3)
    
    while tab[9][9] != avatar:
        if sac.life > sac.vieMax:
            sac.life = sac.vieMax
        
        if sac.cptWin % 10 == 0 and sac.job == "Randoneur " and sac.cptWin != 0:
            sac.competenec = 1
        
        
        
        if sac.mamelou == 1:
            force = True
       
        os.system("cls")
        #On affiche un text en fonction du niveaux de dificulté choisie
        if dificulté == 0:
            print("\033[1;49;31mEasy mode\033[0m")
        elif dificulté == 1:
            print("\033[1;49;31mNormal mode\033[0m")
        elif dificulté == 2:
            print("\033[1;49;31mHard mode\033[0m")
        elif dificulté == 3:
            print("\033[1;49;31mBraque mode\033[0m")
        else:
            print("\033[1;49;31mNo unluk no fun mode\nPerfect for you, litle noob\033[0m")
        print(sac.job)
        afficherTab(tab, cptAction, dificulté)
        
       
        touche = keyboard.read_key()
        time.sleep(0.2)
        
        if touche == "b": # touche de sucide
            sac.mort = "sucide"
            print("Potion d'auto destruction, le rêve de tout homme!")
            time.sleep(2)
            break
        
        elif touche == "enter":
            if sac.potionEndur > 0:
                print("Vous utilisez une potion d'endurence,\nvous vous senter capable d'escalader une montagne!")
                sac.potionEndur -= 1
                cptAction -= 10
                
            time.sleep(2)
            continue
            
            
        elif touche == "space":
            if sac.potionForce > 0:
                print("vous utilisez une potion de force,\nvous senter la force ultime couler en vous!")
                sac.potionForce -= 1
                force = True
            time.sleep(2)
            continue
        
        elif touche == "p":
            if sac.job == "D Plombier" and sac.robinéMagique > 0:
                
                for i in range(len(tab)):
                    for j in range(len(tab[i])):
                        if tab[i][j] == "X":
                            tab[i][j] = " "
                sac.robinéMagique -= 1
                print("Vous avez envoyer les murs au Goulp")
                time.sleep(3)
            else:
                p = random.randint(1, 1000000)
                if p == 4:
                    sac.robinéMagique += 1
                    print("\033[0;49;33mVous trouvez un drôlle de robiné sur un baton\nVous le prenez\nça peut servire... mais à quoi?\033[0m")         
                else:
                    print("Vous pomper,\nmais il ne ce passe rien.")           
                time.sleep(1)
            continue
            
                
        elif touche == "e":
            cptAction-= 10
            if sac.job != "Athlète   ":
                if sac.mamelou == 0:
                    sac.life -= 1
                else:
                    sac.life -= 2
            print("Vous sacrifier une partie de votre ame\nvous regagner de l'endurence")
            if sac.life < 0:
                time.sleep(3)
                sac.mort = "Ne sais pas conter"
                break
            time.sleep(3)
            continue
            
        elif touche == "esc":
            
            tabPause = [">", " ", " ", " "]
            pose2 = 0
            while 1:
                os.system("cls")
                print(tabPause[1], "Reprendre")
                print(tabPause[2], "Recommencer")
                print(tabPause[3], "Quiter")
                change = keyboard.read_key()
                time.sleep(0.2)

                if change == "z" and pose2 != 0:
                    tabPause[pose2] = " "
                    pose2 -= 1
                    tabPause[pose2] = ">"

                if change == "s" and pose2 != 3:
                    tabPause[pose2] = " "
                    pose2 += 1
                    tabPause[pose2] = ">"

                if change == "enter":
                    if pose2 == 1:
                        break
                    if pose2 == 2:
                        
                        sac.cptWin = 0
                        sac.potionEndur = 1
                        sac.potionForce = 1
                        sac.mamelou = 0
                        sac.chemiseHawaien = 0
                        sac.robinéMagique = 0
                        sac.life = 3
                        sac.competenec = 1
                        sac.fumisterie = 0
                        sac.kwinaman = 0

                        choixPerso(dificulté)
                        menu()
                    if pose2 == 3:
                        menu()
            continue
        
        elif touche == "m":
            print("Vous sortez votre marteau\net vous préparez à détruire un mur?")
            time.sleep(0.1)
            direction = keyboard.read_key()
            if direction == "haut" and posY != 0:
                if tab[posY-1][posX] == "X":
                    tab[posY-1][posX] = " "
                    if sac.job != "Masson    " and sac.job != "Architect ":
                        cptAction += dificulté + 1
                    
            elif direction == "bas" and posY != 9:
                if tab[posY+1][posX] == "X":
                    tab[posY+1][posX] = " "
                    if sac.job != "Masson    " and sac.job != "Architect ":
                        cptAction += dificulté + 1
                    
                    
            elif direction == "gauche" and posX != 0:
                if tab[posY][posX-1] == "X":
                    tab[posY][posX-1] = " "
                    if sac.job != "Masson    " and sac.job != "Architect ":
                        cptAction += dificulté + 1
                    
            elif direction == "droite" and posX != 9:
                if tab[posY][posX+1] == "X":
                    tab[posY][posX+1] = " "
                    if sac.job != "Masson    " and sac.job != "Architect ":
                        cptAction += dificulté + 1
            
            troll = random.randint(dificulté + 1, 10)
            if troll == dificulté + 1:
                print("\033[1;49;31mLe mur s'éfondre sur vous\033[0m")
                if sac.job != "Athlète   ":
                    sac.life -= 1
                else:
                    cptAction += 5
                time.sleep(3)
                if sac.life < 0:
                    sac.mort = "Enseuveli sous sont incompétence"
                    break
            continue
            
        elif touche == "c":
            if sac.competenec == 1:
                sac.competenec = 0
                print("vous activez votre compétence de :", sac.job)
                if sac.job == "Randoneur ":
                    cptAction -= 5
                    sac.life += 1
                elif sac.job == "Aventurier":
                    noTrap = True
                elif sac.job == "developeur":
                    print("Vous pirater le jeux")
                    sac.mamelou = 1
                    sac.chemiseHawaien = 1
                    sac.robinéMagique += 2
                elif sac.job == "Masson    ":
                    sac.job = "Architect "
                    print("Vous evoluez en architect")
                elif sac.job =="Plombier  ":
                    sac.job = "D Plombier"
                    print("Vous evoluez en devain plombier")
                elif sac.job == "Breuton   ":
                    sac.kwinaman = 0
                    sac.life += 1
                    cptAction -= 5
                    sac.vieMax += 2
                    sac.actionMax += 5
                    sac.limiteOverDose += 2
                    print("Vous manger un délicieux kwinaman")
                else:
                    noOD = True
                time.sleep(3)
                continue
                
        elif touche == "t":
            if sac.tekila != 0:
                sac.tekila -= 1
                sac.life += 3
                if sac.job != "Athlète   ":
                    print("\033[0;49;35mEt une Dose de Tékila\033[0m")
                else:
                    print("\033[0;49;35mEt une Boisson énergigente\033[0m")
                time.sleep(3)
                if sac.tekila == 0 and sac.job != "Athlète   ":
                    guelleDeBoi = random.randint(0, 1)
                    
                    if guelleDeBoi == 0:
                        sac.mort = "L'alcolisme tue!"
                        break
                
                continue
        
        elif touche == "i":
            os.system("cls")
            os.system("mode 60, 30")
            print("Vocation:", sac.job, "\n")
            if sac.tekila != 0:
                if sac.job != "Athlète   ":
                    print("Tékila:             ", sac.tekila)
                else:
                    print("Boisson energigente:", sac.tekila)
            print("Vie:                ", sac.life, "/", sac.vieMax)
            print("Endurence:          ", sac.actionMax - cptAction, "/", sac.actionMax)
            
            if sac.chemiseHawaien != 0:
                print("vous portez chemise hawaien")
            if sac.mamelou != 0:
                print("vous avez consomer de la drogue")
            if sac.fumisterie != 0:
                print("Trésor trouver:     ", sac.fumisterie)
            if sac.robinéMagique != 0:
                print("étrange robiné:     ", sac.robinéMagique)
            
            print("potion endurence:   ", sac.potionEndur)
            print("potion force:       ", sac.potionForce)
            if sac.kwinaman == 1:
                print("Vous n'avez pas encor manger votre kwinaman")
                    
                    
                
            os.system("pause > nul")
            os.system("mode 56, 30")
            continue
                
        if touche != "z" and touche != "s" and touche != "q" and touche != "d":
            continue
        #cas des bord
        elif touche == "z" and posY == 0:
            continue
        elif touche == "s" and posY == 9:
            continue
        elif touche == "q" and posX == 0:
            continue
        elif touche == "d" and posX == 9:
            continue
        #Déplacement
        elif force == False:
            tab[posY][posX] = " "
            if touche == "z":
                if tab[posY -1][posX] == " ": # on vérifi l'absence de mur
                    posY = posY - 1
                    cptAction = cptAction + (sac.fumisterie + 1)
                   
                else:
                    tab[posY][posX] = avatar
                    continue
            else:
                if touche == "s":
                    if tab[posY +1][posX] == " ":
                        posY = posY + 1
                        cptAction = cptAction + (sac.fumisterie + 1)
                        
                    else:
                        tab[posY][posX] = avatar
                        continue
                else:
                    if touche == "q":
                        if tab[posY][posX - 1] == " ":
                            posX = posX - 1
                            cptAction = cptAction + (sac.fumisterie + 1)
                            
                        else:
                            tab[posY][posX] = avatar
                            continue
                    else:
                        if tab[posY][posX + 1] == " ":
                            posX = posX + 1
                            cptAction = cptAction + (sac.fumisterie + 1)
                            
                        else:
                            tab[posY][posX] = avatar
                            continue
                                
            tab[posY][posX] = avatar
            
        else:
            force = False
            tab[posY][posX] = " "
            if touche == "z":
                    posY = posY - 1
            else:
                if touche == "s":
                        posY = posY + 1
                else:
                    if touche == "q":
                            posX = posX - 1
                    else:
                            posX = posX + 1

            tab[posY][posX] = avatar
            cptAction = cptAction + 1
                    
        #Création d'un mur
        nbMur = 1
        
        if sac.cptWin > 32:
            nbMur = 2
        if sac.cptWin > 65:
            nbMur = 3
        
            
        #On regarde pour le maluse de ce tour
        fun = random.randint(1, 200)
        
        if dificulté == 4:
            fun = -1
        
       
        
        if fun > 0 and fun <= 8:
            if noTrap == True:
                noTrap = False
                print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
            else:
                nbMur += dificulté + 2
                print("Vous avez apuillez sur un intérupteur!\n\033[1;49;31mplusieurs murs sortent du sol\033[0m")
            time.sleep(3)
        #perte d'endurence
        elif fun > 8 and fun <= 13:
            if noTrap == True:
                noTrap = False
                print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
            else:
                if sac.job == "Architect ":
                    a = random.randint(0, 1)
                    if a == 0:
                        print("Vos compétences d'architect,\n vous on permis de bétoner la boue")
                        time.sleep(3)
                else:
                    cptAction += dificulté + 2
                    print("Vous vous emborbez dans la boue\n\033[1;49;31mVous vous épuisez pour vous en sortire\033[0m")
                    time.sleep(3)
        elif fun == 200:
            f = random.randint(1, 12 * dificulté) #Comme ça ça peut pas ariver en facile
            if f == 1:
                sac.mort="Vous avez fait une crise cardiac,\npas de bol :-p"
                break
        
        
        if fun > 13:
            r = random.randint(1, 200)
            
            if dificulté == 0:
                if r > 0 and r <= 1:
                    if noTrap == True:
                        noTrap = False
                        print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
                        time.sleep(3)
                    elif shield == True:
                        
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mune flèche vole ver vous,\nvous la stoper grace à votre compétence de",sac.job,"\033[0m")
                        time.sleep(3)
                    else:
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mVous ête transpercer pare une flèche\033[0m")
                        time.sleep(3)
                        if sac.job != "Athlète   ":
                            sac.life -= 1
                        else:
                            cptAction += 5
                        if sac.life < 0 and sac.job != "Athlète   ":
                            sac.mort = "Transpèrcer pare une flèche en plain coeur"
                            break
                elif r > 1 and r <= 6: 
                    h = random.randint(1, (dificulté + 1 ) * 100)
                    if h == 1:
                        print("\033[0;49;33mVous avez trouvez ne potion de saut,")
                        time.sleep(3)
                        print("IMPOSSIBLE!!!")
                        time.sleep(3)
                        print("Ce n'est pas une potion de saut!")
                        time.sleep(3)
                        print("C'est une potion de PÉGAAAAAAAAAAAAAAS!!!!!!!")
                        print("\033[0m")
                        sac.cptWin += 40
                        time.sleep(3)
                    else:
                        print("\033[0;49;33mVous avez trouvez une potion de saut,\nvous la buvez,\nsauter et vous vous retrouvez 4 étage plus haut!\033[0m")
                        sac.cptWin += 4
                        time.sleep(3)
                        h = random.randint(1, 10)
                        if h == 1:
                            if sac.job != "Athlète   ":
                                sac.life -= 2
                            else:
                                cptAction += 5
                            print("\033[1;49;31mVous vous fouler la chevil à l'atérisage\033[0m")
                            time.sleep(3)
                            if sac.life < 0 and sac.job != "Athlète   ":
                                print("vous perdez l'équilibre,\n et vous fracasser le crâne contre un caillous")
                                time.sleep(5)
                                sac.mort = "sélection naturelle."
                                break
                elif r > 6 and r <= 14:
                    if sac.job != "Athlète   ":
                        sac.life += 1
                    else:
                        cptAction -= 5
                    print("\033[0;49;35mPotion de vitalité\033[0m")
                    time.sleep(3)
                    if sac.life > sac.limiteOverDose:
                        overDose = random.randint(1,((dificulté + 10) - (sac.life - sac.limiteOverDose)) )
                        if overDose == 1 and noOD == True:
                                print("Votre compétence d'", sac.job, "\nvous permet d'eviter l'over dose")
                                noOD = False
                                overDose = -4
                                time.sleep(3)
                        if overDose == 1:
                            print("Vous avez fait une over dose à la potion de soin\nvous vous vider sur le sol")
                            if sac.job != "Athlète   ":
                                sac.life = sac.limiteOverDose
                            else:
                                cptAction += 5
                            time.sleep(3)
                
            
            elif dificulté == 1:
                if r > 0 and r <= 3:
                    if noTrap == True:
                        noTrap = False
                        print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
                        time.sleep(3)
                    elif shield == True:
                        
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mune flèche vole ver vous,\nvous la stoper grace à votre compétence de",sac.job,"\033[0m")
                        time.sleep(3)
                    else:
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mVous ête transpercer pare une flèche\033[0m")
                        time.sleep(3)
                        if sac.job != "Athlète   ":
                            sac.life -= 1
                        else:
                            cptAction += 5
                        if sac.life < 0 and sac.job != "Athlète   ":
                            sac.mort = "Transpèrcer pare une flèche en plain coeur"
                            break
                elif r > 3 and r <= 8:
                    h = random.randint(1, (dificulté + 1 ) * 100)
                    if h == 1:
                        print("\033[0;49;33mVous avez trouvez ne potion de saut,")
                        time.sleep(3)
                        print("IMPOSSIBLE!!!")
                        time.sleep(3)
                        print("Ce n'est pas une potion de saut!")
                        time.sleep(3)
                        print("C'est une potion de PÉGAAAAAAAAAAAAAAS!!!!!!!")
                        print("\033[0m")
                        sac.cptWin += 40
                        time.sleep(3)
                    else:
                        print("\033[0;49;33mVous avez trouvez une potion de saut,\nvous la buvez,\nsauter et vous vous retrouvez 4 étage plus haut!\033[0m")
                        sac.cptWin += 4
                        time.sleep(3)
                        h = random.randint(1, 10)
                        if h == 1:
                            if sac.job != "Athlète   ":
                                sac.life -= 2
                            else:
                                cptAction += 5
                            print("\033[1;49;31mVous vous fouler la chevil à l'atérisage\033[0m")
                            time.sleep(3)
                            if sac.life < 0 and sac.job != "Athlète   ":
                                print("vous perdez l'équilibre,\n et vous fracasser le crâne contre un caillous")
                                time.sleep(5)
                                sac.mort = "sélection naturelle."
                                break
                elif r > 8 and r <= 14:
                        if sac.job != "Athlète   ":
                            sac.life += 1
                        else:
                            cptAction -= 5
                        print("\033[0;49;35mPotion de vitalité\033[0m")
                        time.sleep(3)
                        if sac.life > sac.limiteOverDose:
                            overDose = random.randint(1,((dificulté + 10) - (sac.life - sac.limiteOverDose)))
                            if overDose == 1 and noOD == True:
                                print("Votre compétence d'", sac.job, "\nvous permet d'eviter l'over dose")
                                noOD = False
                                overDose = -4
                                time.sleep(3)
                            if overDose == 1:
                                print("Vous avez fait une over dose à la potion de soin\nvous vous vider sur le sol")
                                if sac.job != "Athlète   ":
                                    sac.life = sac.limiteOverDose
                                else:
                                    cptAction += 5
                                time.sleep(3)
                
            elif dificulté == 2:
                if r > 0 and r <= 4:
                    if noTrap == True:
                        noTrap = False
                        print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
                        time.sleep(3)
                    elif shield == True:
                        
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mune flèche vole ver vous,\nvous la stoper grace à votre compétence de",sac.job,"\033[0m")
                        time.sleep(3)
                    else:
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mVous ête transpercer pare une flèche\033[0m")
                        time.sleep(3)
                        if sac.job != "Athlète   ":
                            sac.life -= 1
                        else:
                            cptAction += 5
                        if sac.life < 0 and sac.job != "Athlète   ":
                            sac.mort = "Transpèrcer pare une flèche en plain coeur"
                            break
                elif r > 4 and r <= 7:
                    h = random.randint(1, (dificulté + 1 ) * 100)
                    if h == 1:
                        print("\033[0;49;33mVous avez trouvez ne potion de saut,")
                        time.sleep(3)
                        print("IMPOSSIBLE!!!")
                        time.sleep(3)
                        print("Ce n'est pas une potion de saut!")
                        time.sleep(3)
                        print("C'est une potion de PÉGAAAAAAAAAAAAAAS!!!!!!!")
                        print("\033[0m")
                        sac.cptWin += 40
                        time.sleep(3)
                    else:
                        print("\033[0;49;33mVous avez trouvez une potion de saut,\nvous la buvez,\nsauter et vous vous retrouvez 4 étage plus haut!\033[0m")
                        sac.cptWin += 4
                        time.sleep(3)
                        h = random.randint(1, 10)
                        if h == 1:
                            if sac.job != "Athlète   ":
                                sac.life -= 2
                            else:
                                cptAction += 5
                            print("\033[1;49;31mVous vous fouler la chevil à l'atérisage\033[0m")
                            time.sleep(3)
                            if sac.life < 0 and sac.job != "Athlète   ":
                                print("vous perdez l'équilibre,\n et vous fracasser le crâne contre un caillous")
                                time.sleep(5)
                                sac.mort = "sélection naturelle."
                                break
                elif r > 7 and r <= 11:
                        if sac.job != "Athlète   ":
                            sac.life += 1
                        else:
                            cptAction -= 5
                        print("\033[0;49;35mPotion de vitalité\033[0m")
                        time.sleep(3)
                        if sac.life > sac.limiteOverDose:
                            overDose = random.randint(1,((dificulté + 10) - (sac.life - sac.limiteOverDose)))
                            if overDose == 1 and noOD == True:
                                print("Votre compétence d'", sac.job, "\nvous permet d'eviter l'over dose")
                                noOD = False
                                overDose = -4
                                time.sleep(3)
                            if overDose == 1:
                                print("Vous avez fait une over dose à la potion de soin\nvous vous vider sur le sol")
                                if sac.job != "Athlète   ":
                                    sac.life = sac.limiteOverDose
                                else:
                                    cptAction += 5
                                time.sleep(3)
                
            elif dificulté == 3:
                if r > 0 and r <= 5:
                    if noTrap == True:
                        noTrap = False
                        print("Votre compétence d'", sac.job, "\nvous à permit d'eviter ce piège")
                        time.sleep(3)
                    elif shield == True:
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mune flèche vole ver vous,\nvous la stoper grace à votre compétence de",sac.job,"\033[0m")
                        time.sleep(3)
                    else:
                        print("Vous avez actionner une dalle pièger!\n\033[1;49;31mVous ête transpercer pare une flèche\033[0m")
                        time.sleep(3)
                        if sac.job != "Athlète   ":
                            sac.life -= 1
                        else:
                            cptAction += 5
                        if sac.life < 0 and sac.job != "Athlète   ":
                            sac.mort = "Transpèrcer pare une flèche en plain coeur"
                            break
                elif r > 5 and r <= 6:
                    h = random.randint(1, (dificulté + 1 ) * 100)
                    if h == 1:
                        print("\033[0;49;33mVous avez trouvez ne potion de saut,")
                        time.sleep(3)
                        print("IMPOSSIBLE!!!")
                        time.sleep(3)
                        print("Ce n'est pas une potion de saut!")
                        time.sleep(3)
                        print("C'est une potion de PÉGAAAAAAAAAAAAAAS!!!!!!!")
                        print("\033[0m")
                        sac.cptWin += 40
                        time.sleep(3)
                    else:
                        print("\033[0;49;33mVous avez trouvez une potion de saut,\nvous la buvez,\nsauter et vous vous retrouvez 4 étage plus haut!\033[0m")
                        sac.cptWin += 4
                        time.sleep(3)
                        h = random.randint(1, 10)
                        if h == 1:
                            if sac.job != "Athlète   ":
                                sac.life -= 2
                            else:
                                cptAction += 5
                            print("\033[1;49;31mVous vous fouler la chevil à l'atérisage\033[0m")
                            time.sleep(3)
                            if sac.life < 0 and sac.job != "Athlète   ":
                                print("\033[1;49;31mvous perdez l'équilibre,\n et vous fracasser le crâne contre un caillous\033[0m")
                                time.sleep(5)
                                sac.mort = "sélection naturelle."
                                break
                elif r > 6 and r <= 8:
                        if sac.job != "Athlète   ":
                            sac.life += 1
                        else:
                            cptAction -= 5
                        print("\033[0;49;35mPotion de vitalité\033[0m")
                        time.sleep(3)
                        if sac.life > sac.limiteOverDose:
                            overDose = random.randint(1,((dificulté + 10) - (sac.life - sac.limiteOverDose)))
                            if overDose == 1 and noOD == True:
                                print("Votre compétence d'", sac.job, "\nvous permet d'eviter l'over dose")
                                noOD = False
                                overDose = -4
                                time.sleep(3)
                            if overDose == 1:
                                print("Vous avez fait une over dose à la potion de soin\nvous vous vider sur le sol")
                                if sac.job != "Athlète   ":
                                    sac.life = sac.limiteOverDose
                                else:
                                    cptAction += 5
                                time.sleep(3)
                
                               
        
        #memelou
        if dificulté != 4:
            if sac.job != "Aventurier":
                r = random.randint(1, 4002)
                
                if r == 1:
                    print("\033[0;49;33mVous trouvez des pilules fluorécentes\nvous les ingéré, elles décuplent vos force\033[0m")
                    sac.mamelou += 1
                    time.sleep(3)
                    
                #chemise
                r = random.randint(1, 2001)
                
                if r == 1:
                    print("\033[0;49;33mVous trouvez une chemise Hawaien,\nen la portant,\nvous vous santé capable d'endurer les pires jeux.\033[0m")
                    sac.chemiseHawaien += 1
                    time.sleep(3)
                
                #robiné
                r = random.randint(1, 1444)
                if r == 4:
                    sac.robinéMagique += 1
                    print("\033[0;49;33mVous trouvez un drôlle de robiné sur un baton\nVous le prenez\nça peut servire... mais à quoi?\033[0m")
                    time.sleep(3)
                
                #cofre
                r = random.randint(-666, 404)
                if r == 0:
                    print("\033[0;49;33mVous trouvez un coffre!\nIl est remplit d'or et de pière pressieuse!\033[0m")
                    sac.fumisterie += 1
                    time.sleep(3)
            else:
                r = random.randint(1, 2001)
                
                if r == 1:
                    print("\033[0;49;33mVous trouvez des pilules fluorécentes\nvous les ingéré, elles décuplent vos force\033[0m")
                    sac.mamelou += 1
                    time.sleep(3)
                    
                #chemise
                r = random.randint(1, 1000)
                
                if r == 1:
                    print("\033[0;49;33mVous trouvez une chemise Hawaien,\nen la portant,\nvous vous santé capable d'endurer les pires jeux.\033[0m")
                    sac.chemiseHawaien += 1
                    time.sleep(3)
                
                #robiné
                r = random.randint(1, 544)
                if r == 4:
                    sac.robinéMagique += 1
                    print("\033[0;49;33mVous trouvez un drôlle de robiné sur un baton\nVous le prenez\nça peut servire... mais à quoi?\033[0m")
                    time.sleep(3)
                #cofre
                r = random.randint(0, 404)
                if r == 0:
                    print("\033[0;49;33mVous trouvez un coffre!\nIl est remplit d'or et de pière pressieuse!\033[0m")
                    sac.fumisterie += 1
                    time.sleep(3)
            
            if sac.job == "Alchimiste":
                f = random.randint(1, 200)
                
                if f > 25 and f <= 40:
                    if f > 25 and f <= 30:
                        sac.life += 1
                        print("Votre compétence d'", sac.job, "\nVous permet d'obtenir:")
                        print("\033[0;49;35mune potion de vitalité\033[0m")
                        time.sleep(3)
                    elif f < 30 and f <= 35:
                        sac.potionEndur += 1
                        print("Votre compétence d'", sac.job, "\nVous permet d'obtenir:")
                        print("une potion d'endrence")
                        time.sleep(3)
                    elif f < 35 and f <= 40:
                        sac.potionForce += 1
                        print("Votre compétence d'", sac.job, "\nVous permet d'obtenir:")
                        print("une potion de force")
                        time.sleep(3)
        
        merde = random.randint(1, 1000)
        if merde > 100 and merde < 110:
            if sac.fumisterie > 0:
                print("Vous ête interpeler par les service des impot,\nvous perder de l'or")
                sac.fumisterie -= 1
                time.sleep(3)
        elif merde > 200 and merde < 210:
            if sac.mamelou > 0:
                print("Vous ête arêter pare un agent des force de l'ordre")
                print("Au vue de votre état ils test la présence de drogue dans votre sang.")
                time.sleep(3)
                print("Vous ête mis au poste et en resortez sobrer")
                sac.mamelou = 0
                time.sleep(3)
        elif merde > 300 and merde < 310:
            if sac.chemiseHawaien != 0:
                print("Les services d'une platforme de vidéos vous arète")
                time.sleep(3)
                print("Ils vous arache votre chemise hawaien\nen disent qu'elle enfrin les règles sur le copyright")
                time.sleep(3)
                sac.chemiseHawaien = 0
            
        i = 0
        while i < nbMur:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if tab[y][x] != avatar and tab[y][x] != "X":
                tab[y][x] = "X"
            else:
                pasDeMur = True
                while pasDeMur == True:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    if tab[y][x] != avatar and tab[y][x] != "X":
                        tab[y][x] = "X"
                        pasDeMur = False
            i = i + 1
                    
        # On évite de mètre un mur sur l'ariver
        if tab[9][9] == "X":
            tab[9][9] = " "

        
        #Condition de défaites:
        if sac.actionMax <= cptAction: # cas plus d'action
            sac.mort = "mort d'épuisement"
            break

    if noOD == True or noTrap == True or shield == True:
        sac.competenec = 1
    if tab[9][9] == avatar:     
        return "O"
    else:
        return "DED"

"""
Fonction dédier à lancer la fonction main et donc gérer ce qu'il
ce pace entre deux étage
"""
def interEtage(pose):
    os.system("mode 56, 30")
    sac.potionForce =  1
    sac.potionEndur = 1
    while sac.cptWin < 100:
         
        x = main(pose)
        if x == "O":
            
            sac.cptWin += 1
            
            if sac.cptWin >= 100:
                googEnd(pose)
                break
                
            if sac.chemiseHawaien != 0 and sac.life < sac.vieMax:
                sac.life += 1
        else:
                if sac.robinéMagique == 0:
                    os.system("cls")
                    print(sac.mort)
                    if sac.mamelou != 0:
                        print("Et la drogue ne rend pas plus fort")
                    print("\033[1;49;31mGAME OVER\033[0m")
                    time.sleep(2)
                    print("SCORE:", sac.cptWin)
                    if pose == 0:
                        print("Easy mode")
                    elif pose == 1:
                        print("Normal mode")
                    elif pose == 2:
                        print("Hard mode")
                    elif pose == 3:
                        print ("Braque mode")
                    else:
                        print("No fun mode")
                    print(sac.job)
                    os.system("Pause")
                    break
                else:
                    sac.robinéMagique -= 1
                    print("Vous vous enfoncer le robiné magique ou vous pencez`\nvous vous senter revivre")
                    if sac.job != "Athlète   ":
                        if sac.job != "Gladiateur":
                            sac.life = 3
                        else:
                            sac.life = 0
                    else:
                        sac.life = 0
                    
                    if sac.fumisterie > 0:
                        sac.fumisterie -= 1
                        print("Votre mort vous deleste d'une partie de votre or")
                    time.sleep(3)
                    
                    
           
    

def googEnd(pose):
    os.system("cls")
    os.system("mode 120, 30")
    print("Vous ête arivez au dernier étage,\ndevant vous ce trouve un coffre")
    time.sleep(5)
    print("Vous l'ouvrez et trouver un cookie,\net un parchemain ou est écrit:")
    time.sleep(5)
    print("+--------------------------------------+")
    print("|       Putin De Donjon De Merde       |")
    print("+--------------------------------------+")
    if pose == 0:
        print("| Dificulté: Easy                      |" )
    elif pose == 1:
        print("| Dificulté: Normal                    |" )
    elif pose == 2:
        print("| Dificulté: Hard                      |" )
    elif pose == 3:
        print("| Dificulté: Braque                    |" )
    print("|", sac.job ,"                          |")
    print("+--------------------------------------+")
    print("\nListe d'objet restant:\n")
    print("Vie restants:", sac.life)
    if sac.potionEndur == 1:
        print("Vous n'avez pas consommer votre potion d'endurence")
    if sac.potionForce == 1:
        print("Vous n'avez pas consommer votre potion de force")
    if sac.mamelou != 0:
        print("Vous avez pris de la DROOOOOOOGUE (comme le dev)")
    if sac.chemiseHawaien != 0:
         print("Vous avez trouver:", sac.chemiseHawaien, "chemise hawaien")
    if sac.tekila != 3 and sac.job != "Aqualique":
        print("Vous avez bu:", 3 - sac.tekila, "tékila, sacré déssente!")
    if sac.tekila == 3 or sac.job == "Aqualique":
        print("Vous avez fait preuve d'une sobriété exemplaire")
    if sac.robinéMagique != 0:
        print("Il vous rest:", sac.robinéMagique, "robiné magique,\nl'usage que vous en faite ne regarde que vous")
    if sac.fumisterie != 0:
        print("Vous avez atain le somet malgret tous cette or qui vous à épuisser,\nVous ête le roi des avides")
    if sac.job == "Breuton   " and sac.kwinaman == 1:
        print("Vous n'avez pas manger ce délicieux kwinaman?")
    os.system("pause > nul")
    os.system("cls")
    
    print("merci d'avoir jouer à ce jeux.")
    
    if pose == 0:
        print("Par contre t'est vraiment une merde,")
        time.sleep(3)
        print("non sans déconer faut vraiment être une merdepour jouer en facile")
    elif pose == 1:
        print("t'a terminer le jeux dans sa dificultée de base")
        time.sleep(3)
        print("La prochaine fois tenter de le faire en Harde ")
    elif pose == 2:
        print("tu a réussi à le terminer en Hard")
        time.sleep(3)
        print("Tu êst soit très chancheux sois très determiner!\nDu coup j'imagine que tu vas viser le mode braque maintenant? ")
    elif pose == 3:
        print("Tu à fini le jeux en braque")
        time.sleep(4)
        print("Tu est sans doute fou mais t'a tous mon respet")
        time.sleep(4)
        print("Dans tous les cas merci, merci pour le temps que tu à investi dans PDDDM.")
        time.sleep(4)
        print("Rien ne me fait plus plaisire que de savoir qu'un joueur à été finir le mode braque.")
        time.sleep(5)
        print("MERCI")
    if sac.job == "Gladiateur":
        print("\033[1;49;31m Tu a terminer le jeux avec la vocation Gladiateur!")
        time.sleep(3)
        if pose == 3:
            print("T' a tricher, j'en suis sur! SALO\033[0m")
        
    os.system("pause")

def choixPerso(pose):
    emplacement = 0
    tabMenu = [">", " ", " ", " ", " ", " ", " ", " ", " "]
    while 1:
        os.system("cls")
        print("Quel vocation?")
        print("+---+--------------+")
        print("|", tabMenu[0], "| Aventurier   |")
        print("|", tabMenu[1], "| Chevalier    |")
        print("|", tabMenu[2], "| Randoneur    |")
        print("|", tabMenu[3], "| Aqualique    |")
        print("|", tabMenu[4], "| Plombier     |")
        print("|", tabMenu[5], "| Breuton      |")
        print("|", tabMenu[6], "| Masson       |")
        print("|", tabMenu[7], "| Alchimiste   |")
        print("|", tabMenu[8], "| Athlète      |")
        print("+---+--------------+\n")
        
        print("CARACTERISTIQUE:")
        if emplacement == 0:
            print("Vie Max  :  6")
            print("Endurence: 25")
            print("Tekila   :  3")
            print("risque d'over dose au dela de 3 vies")
            print("Compétence: détection des pièges")
            print("Auce de la probat de trouver un trésor (passif)")
            
        elif emplacement == 1:
            print("Vie Max  :  8")
            print("Endurence: 20")
            print("Tekila   :  3")
            print("Compétence: bouclier contre les flèches (passife)")
            print("Imunité à l'over dose (passife)")
            
        elif emplacement == 2:
            print("Vie Max  :  4")
            print("Endurence: 35")
            print("Tekila   :  3")
            print("risque d'over dose au dela de 3 vies")
            print("Compétence: rations alimentaire")
            print("Regagne une utilisation de compétence tous les 10 étages (passif)")
            
        elif emplacement == 3:
            print("Vie Max  : 12")
            print("Endurence: 25")
            print("Tekila   :  0")
            print("risque d'over dose au dela de 6 vies (passif)")
            print("Compétence: imunité à l'over dose")
            
        elif emplacement == 4:
            print("Vie Max  : 6")
            print("Endurence: 25")
            print("Tekila   :  3")
            print("Commence avec un robiné magique")
            print("\nPeut evoluer en Devin Plombier")
            print("Le devain Plombier peut envoyer les murs au goulp contre un robiné Magique")
            
            
        elif emplacement == 5:
            print("Vie Max  : 6")
            print("Endurence: 25")
            print("Tekila   :  5")
            print("risque d'over dose au dela de 2 vies (passif)")
            print("Peut manger un kwinaman")
        
        elif emplacement == 6:
            print("Vie Max  : 6")
            print("Endurence: 25")
            print("Tekila   :  3")
            print("Ne perd pas d'endurence en utilisent le marteau")
            print("\nPeut évoluer en Architect")
            print("L'architect à une chance de bétoner un piège à boue")
        
        elif emplacement == 7:
            print("Vie Max  : 5")
            print("Endurence: 25")
            print("Tekila   :  3")
            print("A plus de chance de trouver des potions")
            print("Peut trouver des potions de force er d'endurence")
        
        elif emplacement == 8:
            print("VieMax = 0")
            print("Endurence = 30")
            print("Boisson energigente = 3")
            print("Les elément qui font perdre de la vie font perdre de l'endurence")
            
        
        time.sleep(0.2)
        change = keyboard.read_key()
        
        if change == "d":
            time.sleep(0.2)
            print(">")
            change = keyboard.read_key()
            if change == "e":
                time.sleep(0.2)
                print(">")
                change = keyboard.read_key()
                if change == "v":
                    sac.tekila = 3
                    sac.actionMax = 26
                    sac.vieMax = 7
                    sac.life = 4
                    sac.limiteOverDose = 4
                    sac.job = "developeur"
                    interEtage(pose)
                    break
        
        if change == "z" and emplacement != 0:
            tabMenu[emplacement] = " "
            emplacement -= 1
            tabMenu[emplacement] = ">"
            
        
        elif change == "s" and emplacement != 8:
            tabMenu[emplacement] = " "
            emplacement += 1
            tabMenu[emplacement] = ">"
            
        elif change == "G":
            sac.tekila = 0
            sac.life = 0
            sac.actionMax = 18
            sac.vieMax = 100
            sac.limiteOverDose = 101
            sac.job = "Gladiateur"
            interEtage(pose)
            break
            
        elif change == "enter":
            if emplacement == 0:
                sac.tekila = 3
                sac.actionMax = 25
                sac.vieMax = 6
                sac.limiteOverDose = 3
                sac.job = "Aventurier"
                
            elif emplacement == 1:
                sac.tekila = 3
                sac.actionMax = 20
                sac.vieMax = 8
                sac.limiteOverDose = 10
                sac.job = "Chevalier "
                
            elif emplacement == 2:
                sac.tekila = 3
                sac.actionMax = 35
                sac.vieMax = 4
                sac.limiteOverDose = 3
                sac.job = "Randoneur "
                
            elif emplacement == 3:
                sac.tekila = 0
                sac.actionMax = 25
                sac.vieMax = 12
                sac.limiteOverDose = 6
                sac.job = "Aqualique "
                
            elif emplacement == 4:
                sac.tekila = 3
                sac.actionMax = 25
                sac.vieMax = 6
                sac.limiteOverDose = 3
                sac.robinéMagique = 1
                sac.job = "Plombier  "
            
            elif emplacement == 5:
                sac.tekila = 5
                sac.actionMax = 25
                sac.vieMax = 6
                sac.limiteOverDose = 2
                sac.kwinaman = 1
                sac.job = "Breuton   "
            
            elif emplacement == 6:
                sac.tekila = 3
                sac.actionMax = 25
                sac.vieMax = 6
                sac.limiteOverDose = 3
                sac.job = "Masson    "
                
            elif emplacement == 7:
                sac.tekila = 3
                sac.actionMax = 25
                sac.vieMax = 5
                sac.limiteOverDose = 3
                sac.job = "Alchimiste"
                
            elif emplacement == 8:
                sac.tekila = 3
                sac.actionMax = 30
                sac.vieMax = 0
                sac.limiteOverDose = 3
                sac.job = "Athlète   "
            
            
            # googEnd(pose)    
            interEtage(pose)
            break
        elif change == "esc":
            break

"""
fonction du menu du jeux
"""
def menu():
    pose = 1
    
    tabMenu = [" ", ">"," ", " ", " "]
    while 1:
        sac.cptWin = 0
        sac.potionEndur = 1
        sac.potionForce = 1
        sac.mamelou = 0
        sac.chemiseHawaien = 0
        sac.tekila = 3
        sac.robinéMagique = 0
        sac.life = 3      
        sac.competenec = 1
        sac.job = "Ploc"
        sac.fumisterie = 0
        sac.kwinaman = 0
        
        
        os.system("mode 120, 30")
        os.system("cls")
        print("Putin De Donjon De Merde")
        print("+---+--------+")
        print("|\033[1;49;34m", tabMenu[0], "\033[0m| Easy   |")
        print("|\033[1;49;32m", tabMenu[1], "\033[0m| Normal |")
        print("|\033[0;49;33m", tabMenu[2], "\033[0m| Hard   |")
        print("|\033[1;49;31m", tabMenu[3], "\033[0m| Braque |")
        print("|", tabMenu[4], "| Quiter |")
        print("+---+--------+")
        print("l: LE LORE DU JEUX")
        print("c: crédits")
        print("t: touches (contrôle)")
        print("\n\nUn jeux déveloper sous l'impultion sadique d'\033[0;49;33mun idiot bête\033[0m")
		
        
        time.sleep(0.2)
        change = keyboard.read_key()

        if change == "z" and pose != 0:
            tabMenu[pose] = " "
            pose -= 1
            tabMenu[pose] = ">"
            
        
        elif change == "s" and pose != 4:
            tabMenu[pose] = " "
            pose += 1
            tabMenu[pose] = ">"
            
            
        elif change == "enter":
            if pose != 4:
                sac.cptWin = 0
                choixPerso(pose)
                
            else:
                os.system("taskkill /IM py.exe /F")
        elif change == "n":
            interEtage(4)
            
        
        elif change == "l":
            os.system("cls")
            print("Chroniques des avanture d'Oscare chapitre 1.\n")
            time.sleep(2)
            print("Le Béjon est une toure qui dépassais les cieux,\nnul ne savais combien d'étage cette tour faisais.\n")
            time.sleep(3)
            print("J'estais venu tenter ma chance dans ce qui estais surnomer:\nLe cimtière des avanturier\n")
            time.sleep(3)
            print("Bon nombre d'avanturier estais partie dans le Béjon mais personne n'en avais jamais triophé.")
            time.sleep(3)
            print("Cette tour estais en effet bourer de pièges plus sadiques les un que les autres.\n")
            time.sleep(3)
            print("Mais c'est justement ce qui faisais que tous les avanturier du mode ce pressais pour renter")
            time.sleep(3)
            print("Une tour aussi bien garder ne peut être que le repère d'un fauleux trésor!\n")
            time.sleep(3)
            print("En chemain j'ai rencontrer une vieille marchande qui m'a fournie trois potions originair du Béjon,")
            time.sleep(2)
            print("Une potion de force,")
            time.sleep(2)
            print("Une potion d' endurence,")
            time.sleep(2)
            print("Une potion d'auto destruction\n")
            time.sleep(4)
            print("Quand je luis ai demander pourquoi un potion d'auto destruction, elle m'a répondu que je comprendrais\nquand le temps sera venu...\n")
            time.sleep(4)
            print("C'est donc équiper de ses trois potion, de mon fidel marteau et d'une bonne paire de,")
            time.sleep(3)
            print("Chaussure, que je me suis lancer dans le Béjon!")
            os.system("pause")
        elif change == "c":
            os.system("cls")
            print("FSD")
            time.sleep(2)
            print("consept original: \033[0;49;33mun idiot bête\033[0m")
            time.sleep(2)
            print("dévelopeur: \033[0;49;33mun idiot bête\033[0m")
            time.sleep(2)
            print("desineur: \033[0;49;33mun idiot bête\033[0m")
            time.sleep(2)
            print("sous le pseudonime \033[0;49;33md'un idio bête\033[0m: Lucas Dubuc")
            time.sleep(4)
            
            print("FSD est un jeux déveloper dans un but non commercial,")
            print("Le partage de PDDDM est encourager par sont créateur,")
            print("Toute tentative de générer des profit par la vante de ce jeux est prohibée\n et va à l'encontre de la volonté de sont créateur!\nMerci de votre compréhention")
            os.system("pause")
        
        elif change == "t":
            os.system("cls")
            print("Déplacement:")
            print("z => haut")
            print("q => gauche")
            print("s => bas")
            print("d => droite\n")
            
            print("potion:")
            print("enter => potion d'endurence")
            print("space => potion de force")
            print("b     => potion d'auto destruction\n")
            
            print("p => pomper")
            print("m => casser un mur contre de l'endurence")
            print("e => échanger une vie contre 10 d'endurence")
            print("t => Boire une dose de Tékila (+3 coeurs)")
            print("i => Info sur les states")
            print("c => Compétence (une compétence ne peut être utiliser qu'une fois par partie\nsi vous l'activer mais ne l'utiliser pas avant de changer d'etage,")
            print("vous dever la réactiver au nouvel étage pour l'utiliser.")
            print("pause => échap\n")
            os.system("pause")
        
# googEnd(3)               
menu()