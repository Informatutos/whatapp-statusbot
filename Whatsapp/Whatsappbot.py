#coding:utf-8
#-------------------------------------------------------------------------------------------------------------#
#--------------------------------------------WhatsApp Bot-----------------------------------------------------#
import time, shutil, os, sys, glob

R = "\033[31;1m"
V = "\033[32;1m"
B = "\033[0m"
C = "\033[36;1m"
J = '\033[93m'
M = '\033[94m'
    
class WhatsAppBot():

    def __init__(self):
        pass
    def WhatsApp(self):

        sourceSdcard = "/sdcard/WhatsApp/Media/.Statuses/"
        sourceStorage = "/storage/emulated/legacy/WhatsApp/Media/.Statuses/"
        destinationSdcard = "/sdcard/WhatsBot"
        destinationStorage = "/storage/emulated/legacy/WhatsBot"
        fichier_jpg = "/sdcard/WhatsBot/whatBot_img"
        fichier_mp4 = "/sdcard/WhatsBot/whatBot_vid"
        fichiers_jpg = "/storage/emulated/legacy/WhatsBot/whatBot_img"
        fichiers_mp4 = "/storage/emulated/legacy/WhatsBot/whatBot_vid" 

        def ShotBanier():
            print(C+"""
            ------------------------------------
             [$] - 1- Image Statuts
             [$] - 2- Video Statuts
             [$] - 3- Acceuil 
            ------------------------------------
            \n"""+B) 

        def bot_sdcard():
            os.system("clear")
            ShotBanier()
            bot_S = input(C+" ==> ")
            try:
                bot_S = int(bot_S)
            except:
                print(R+"[!] Entrer invalide ! \n")
                time.sleep(2)
                bot_sdcard()
            if bot_S == 1:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du dossier 'whatBot_img'")
                try :
                    os.mkdir(fichier_jpg)
                except:
                    pass
                if os.path.exists(fichier_jpg):
                    print(V+"[!]-Dossier 'whatBot_img créer avec succès'")
                    image = glob.glob(sourceSdcard+"*.jpg")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    if len(image) > 1:
                        print(M+"[!] [{}] Fichiers Photo Trouvés !".format(len(image)))
                    else :
                        print(M+"[!] [{}] Fichier Photo Trouvé !".format(len(image)))
                    time.sleep(2)
                    try:
                        for i in range(len(image)):
                            shutil.copy(image[i], fichier_jpg)
                            time.sleep(2)
                            print(C+"[*] Téléchargement de la Photo N° {}".format(i))
                    except:
                        print(R+"[!] Téléchargement de la photo échoué !")
                        time.sleep(2.2)
                        bot_sdcard()
                    print(V+"[!] Téléchargement Terminé !")
                    time.sleep(2.2)
                    bot_sdcard()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_sdcard()
            elif bot_S == 2:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du Dossier 'whatBot_vid'")
                try :
                    os.mkdir(fichier_mp4)
                except:
                    pass
                if os.path.exists(fichier_mp4):
                    print(V+"[!]-Dossier 'whatBot_vid' créer avec succès")
                    video = glob.glob(sourceSdcard+"*.mp4")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    def copy(i):
                        shutil.copy(video[i], fichier_mp4)
                        time.sleep(2)
                        print(C+"[*] Téléchargement de la Vidéo N° {}".format(i))
                    if len(video) > 1:
                        print(M+"[!] [{}] Fichiers Vidéo Trouvés !".format(len(video)))
                    else :
                        print(M+"[!] [{}] Fichier Vidéo Trouvé !".format(len(video)))
                    time.sleep(2)
                    try:
                        for i in range(len(video)):
                            copy(i)
                    except:
                        print(R+"[!] Téléchargement de la Vidéo échoué !")
                        time.sleep(2.2)
                        bot_sdcard()
                    print(V+"[!] Téléchargement Terminé !")
                    time.sleep(2.2)
                    bot_sdcard()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_sdcard()
            elif bot_S == 3:
                print("[!] Programme Fermé !")
                sys.exit()
            else :
                print(R+"[!] Aucun résultat ne correspond à ['"+B+"{}".format(bot_S)+R+"']")
                time.sleep(2)
                bot_sdcard() 

        def bot_storage():
            os.system("clear")
            ShotBanier()
            bot_S = input(C+" ==> ")
            try:
                bot_S = int(bot_S)
            except:
                print(R+"[!] Entrer invalide ! \n")
                time.sleep(2)
                bot_storage()
            if bot_S == 1:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du dossier 'whatBot_img'")
                try :
                    os.mkdir(fichiers_jpg)
                except:
                    pass
                if os.path.exists(fichiers_jpg):
                    print(V+"[!]-Dossier 'whatBot_img créer avec succès'")
                    image = glob.glob(sourceStorage+"*.jpg")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    if len(image) > 1:
                        print(M+"[!] [{}] Fichiers Photo Trouvés !".format(len(image)))
                    else :
                        print(M+"[!] [{}] Fichier Photo Trouvé !".format(len(image)))
                    time.sleep(2)
                    try:
                        for i in range(len(image)):
                            shutil.copy(image[i], fichiers_jpg)
                            time.sleep(2)
                            print(C+"[*] Téléchargement de la Photo N° {}".format(i))
                    except:
                        print(R+"[!] Téléchargement de la photo échoué !")
                        time.sleep(2.2)
                        bot_storage()
                    print(V+"[!] Téléchargement Terminé ! ")
                    time.sleep(2.2)
                    bot_storage()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_storage()
            elif bot_S == 2:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du Dossier 'whatBot_vid'")
                try :
                    os.mkdir(fichiers_mp4)
                except:
                    pass
                if os.path.exists(fichier_mp4):
                    print(V+"[!]-Dossier 'whatBot_vid' créer avec succès")
                    video = glob.glob(sourceStorage+"*.mp4")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    def copy(i):
                        shutil.copy(video[i], fichiers_mp4)
                        time.sleep(2)
                        print(C+"[*] Téléchargement de la Vidéo N° {}".format(i))
                    if len(video) > 1:
                        print(M+"[!] [{}] Fichiers Vidéo Trouvés !".format(len(video)))
                    else :
                        print(M+"[!] [{}] Fichier Vidéo Trouvé !".format(len(video)))
                    time.sleep(2)
                    try:
                        for i in range(len(video)):
                            copy(i)
                    except:
                        print(R+"[!] Téléchargement de la Vidéo échoué !")
                        time.sleep(2.2)
                        bot_storage()
                    print(V+"[!] Téléchargement Terminé !")
                    time.sleep(2.2)
                    bot_storage()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_storage()
            elif bot_S == 3:
                print("[!] Programme Fermé !")
                sys.exit()
            else :
                print(R+"[!] Aucun résultat ne correspond à ['"+B+bot_S+R+"']")
                time.sleep(2)
                bot_storage()   
        def sdcard():
            print(J+"[*] Vérififcation de la mémoire Externe ")
            time.sleep(1.1)
            if os.path.exists(sourceSdcard):
                print(J+"[*] Obtention d'accès vers la mémoire extène !")
                time.sleep(1.1)
                try :
                    os.mkdir(destinationSdcard)
                except :
                    pass
                if os.path.exists(destinationSdcard):
                    time.sleep(2)
                    print(V+"[*] Accès obtenu......")
                else :
                    time.sleep(1.1)
                    print(R+"[*] L'obtention d'accèes à échouer !")
                    sys.exit()
            else :
                print(M+"[*] Vous n'avez pas une  Mémoire de Stockage Externe !")
                print(B+"[!] Répondez Non à la question !")
                typeStockage()

        def storage():
            print(J+"[*] Vérification de la mémoire Interne ")
            time.sleep(1.1)
            if os.path.exists(sourceStorage):
                print(J+"[*] Obtention d'accès vers la mémoire interne !")
                time.sleep(2)
                try :
                    os.mkdir(destinationStorage)
                except:
                    pass
                if os.path.exists(destinationStorage):
                    time.sleep(2)
                    print(V+"[*] Accès obtenu.......")
                else :
                    time.sleep(1.1)
                    print(R+"[*] L'Obtention d'accès à échouer ! ")
                    sys.exit()
            else :
                print(M+"[*] Votre mémoire de stockage est définie sur l'externe ! ")
                print(B+"[!] Répondez Oui à la question !")
                typeStockage()

        def MemoireBanier():
            print(B+"""
            ++++++++++++++++++++++++++++++++++++
              VERIFICATION DU TYPE DE STOCKAGE 
            ++++++++++++++++++++++++++++++++++++
            \n""")
        
        def typeStockage():
            MemoireBanier()
            print(B+"[?] Avez vous une carte mémoire dans votre SmartPhone ? ")
            print("[!] -- Oui ou Non -- ?")
            type_S = input(C+" ==> ")
            if type_S in ["oui", "Oui", "OUI"]:
                sdcard()
                bot_sdcard()
            elif type_S in ["Non", "NON", "non"]:
                storage()
                bot_storage()
            else :
                os.system("clear")
                print(R+"[!] Veuillez répondre par Oui ou Non !"+B)
                typeStockage()
        typeStockage()
        

    def GbwatsApp(self):
        sourceSdcard = "/sdcard/GBWhatsApp/Media/.Statuses/"
        sourceStorage = "/storage/emulated/legacy/GBWhatsApp/Media/.Statuses/"
        destinationSdcard = "/sdcard/WhatsBot"
        destinationStorage = "/storage/emulated/legacy/WhatsBot"
        fichier_jpg = "/sdcard/WhatsBot/GbwhatBot_img"
        fichier_mp4 = "/sdcard/WhatsBot/GbwhatBot_vid"
        fichiers_jpg = "/storage/emulated/legacy/WhatsBot/GbwhatBot_img"
        fichiers_mp4 = "/storage/emulated/legacy/WhatsBot/GbwhatBot_vid"

        def ShotBanier():
            print(C+"""
            ------------------------------------
             [$] - 1- Image Statuts
             [$] - 2- Video Statuts
             [$] - 3- Acceuil 
            ------------------------------------
            \n"""+B)  
        def bot_sdcard():
            os.system("clear")
            ShotBanier()
            bot_S = input(C+" ==> ")
            try:
                bot_S = int(bot_S)
            except:
                print(R+"[!] Entrer invalide ! \n")
                time.sleep(2)
                bot_sdcard()
            if bot_S == 1:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du dossier 'GbwhatBot_img'")
                try :
                    os.mkdir(fichier_jpg)
                except:
                    pass
                if os.path.exists(fichier_jpg):
                    print(V+"[!]-Dossier 'GbwhatBot_img créer avec succès'")
                    image = glob.glob(sourceSdcard+"*.jpg")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    def copy(i):
                        shutil.copy(image[i], fichier_jpg)
                        time.sleep(2)
                        print(C+"[*] Téléchargement de la Photo N° {}".format(i))
                    if len(image) > 1:
                        print(M+"[!] [{}] Fichiers Photo Trouvés !".format(len(image)))
                    else :
                        print(M+"[!] [{}] Fichier Photo Trouvé !".format(len(image)))
                    time.sleep(2)
                    try:
                        for i in range(len(image)):
                            copy(i)
                    except:
                        print(R+"[!] Téléchargement de la photo échoué !")
                        time.sleep(2.2)
                        bot_sdcard()
                    print(V+"[!] Téléchargement Terminé !")
                    time.sleep(2.2)
                    bot_sdcard()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_sdcard()
            elif bot_S == 2:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du Dossier 'GbwhatBot_vid'")
                try :
                    os.mkdir(fichier_mp4)
                except:
                    pass
                if os.path.exists(fichier_mp4):
                    print(V+"[!]-Dossier 'GbwhatBot_vid' créer avec succès")
                    video = glob.glob(sourceSdcard+"*.mp4")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    def copy(i):
                        shutil.copy(video[i], fichier_mp4)
                        time.sleep(2)
                        print(C+"[*] Téléchargement de la Vidéo N° {}".format(i))
                    if len(video) > 1:
                        print(M+"[!] [{}] Fichiers Vidéo Trouvés !".format(len(video)))
                    else :
                        print(M+"[!] [{}] Fichier Vidéo Trouvé !".format(len(video)))
                    time.sleep(2)
                    try:
                        for i in range(len(video)):
                            copy(i) 
                    except:
                        print(R+"[!] Téléchargement de la Vidéo échoué !")
                        time.sleep(2.2)
                        bot_sdcard()
                    print(V+"[!] Téléchargement terminé !")
                    time.sleep(2.2)
                    bot_sdcard()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_sdcard()
            elif bot_S == 3:
                print("[!] Programme Fermé !")
                sys.exit()
            else :
                print(R+"[!] Aucun résultat ne correspond à ['"+B+"{}".format(bot_S)+R+"']")
                time.sleep(2)
                bot_sdcard()
        def bot_storage():
            os.system("clear")
            ShotBanier()
            bot_S = input(C+" ==> ")
            try:
                bot_S = int(bot_S)
            except:
                print(R+"[!] Entrer invalide ! \n")
                time.sleep(2)
                bot_storage()
            if bot_S == 1:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du dossier 'GbwhatBot_img'")
                try :
                    os.mkdir(fichiers_jpg)
                except:
                    pass
                if os.path.exists(fichiers_jpg):
                    print(V+"[!]-Dossier 'GbwhatBot_img créer avec succès'")
                    image = glob.glob(sourceStorage+"*.jpg")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    def copy(i):
                        shutil.copy(image[i], fichiers_jpg)
                        time.sleep(2)
                        print(C+"[*] Téléchargement de la Photo N° {}".format(i))
                    if len(image) > 1:
                        print(M+"[!] [{}] Fichiers Photo Trouvés !".format(len(image)))
                    else :
                        print(M+"[!] [{}] Fichier Photo Trouvé !".format(len(image)))
                    time.sleep(2)
                    try:
                        for i in range(len(image)):
                            copy(i)
                    except:
                        print(R+"[!] Téléchargement de la photo échoué !")
                        time.sleep(2.2)
                        bot_storage()
                    print(V+"[!] Téléchargement Terminé !")
                    bot_storage()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_storage()
            elif bot_S == 2:
                print(J+"[*] Initialisation du Système ............. ! ")
                time.sleep(2)
                print(J+"[!]-Création du Dossier 'GbwhatBot_vid'")
                try :
                    os.mkdir(fichiers_mp4)
                except:
                    pass
                if os.path.exists(fichier_mp4):
                    print(V+"[!]-Dossier 'GbwhatBot_vid' créer avec succès")
                    video = glob.glob(sourceStorage+"*.mp4")
                    time.sleep(2)
                    print(J+"[*] Vérification des fichiers en cours !")
                    time.sleep(2)
                    if len(video) > 1:
                        print(M+"[!] [{}] Fichiers Vidéo Trouvés !".format(len(video)))
                    else :
                        print(M+"[!] [{}] Fichier Vidéo Trouvé !".format(len(video)))
                    time.sleep(2)
                    try:
                        for i in range(len(video)):
                            shutil.copy(video[i], fichiers_mp4)
                            time.sleep(2)
                            print(C+"[*] Téléchargement de la Vidéo N° {}".format(i))
                    except:
                        print(R+"[!] Téléchargement de la Vidéo échoué !")
                        time.sleep(2.2)
                        bot_storage()
                    print(V+"[!] Téléchargement Terminé !")
                    time.sleep(2.2)
                    bot_storage()
                else:
                    print(R+"[!] Impossible de créer le dossier !")
                    time.sleep(2.2)
                    bot_storage()
            elif bot_S == 3:
                print("[!] Programme Fermé !")
                sys.exit()
            else :
                print(R+"[!] Aucun résultat ne correspond à ['"+B+bot_S+R+"']")
                time.sleep(2)
                bot_storage()
        def sdcard():
            print(J+"[*] Vérififcation de la mémoire Externe ")
            time.sleep(1.1)
            if os.path.exists(sourceSdcard):
                print(J+"[*] Obtention d'accès vers la mémoire extène !")
                time.sleep(1.1)
                try :
                    os.mkdir(destinationSdcard)
                except :
                    pass
                if os.path.exists(destinationSdcard):
                    time.sleep(2)
                    print(V+"[*] Accès obtenu......")
                else :
                    print(R+"[*] L'obtention d'accèes à échouer !")
                    time.sleep(1.1)
                    sys.exit()
            else :
                print(M+"[*] Vous n'avez pas une  Mémoire de Stockage Externe !")
                print(B+"[!] Répondez Non à la question !")
                typeStockage()

        def storage():
            print(J+"[*] Vérification de la mémoire Interne ")
            time.sleep(1.1)
            if os.path.exists(sourceStorage):
                print(J+"[*] Obtention d'accès vers la mémoire interne !")
                time.sleep(2)
                try :
                    os.mkdir(destinationStorage)
                except:
                    pass
                if os.path.exists(destinationStorage):
                    time.sleep(2)
                    print(V+"[*] Accès obtenu.......")
                else :
                    print(R+"[*] L'Obtention d'accès à échouer ! ")
                    time.sleep(1.1)
                    sys.exit()
            else :
                print(M+"[*] Votre mémoire de stockage est définie sur l'externe ! ")
                print(B+"[!] Répondez Oui à la question !")
                typeStockage()
        
        def MemoireBanier():
            print(B+"""
            ++++++++++++++++++++++++++++++++++++
              VERIFICATION DU TYPE DE STOCKAGE 
            ++++++++++++++++++++++++++++++++++++
            \n""")

        def typeStockage():
            MemoireBanier()
            print(B+"[?] Avez vous une carte mémoire dans votre SmartPhone ? ")
            print("[!] -- Oui ou Non -- ?")
            type_S = input(C+" ==> "+B)
            if type_S in ["oui", "Oui", "OUI"]:
                sdcard()
                bot_sdcard()
            elif type_S in ["Non", "NON", "non"]:
                storage()
                bot_storage()
            else :
                os.system("clear")
                print(R+"[!] Veuillez répondre par Oui ou Non !"+B)
                typeStockage()
        typeStockage() 
    
    def main(self):

        def mainApp():
            print(J+" =================================\n"+B)
            print(B+" [!] Quel whatsApp utilisez-vous ?\n")
            print(J+" ================================="+B)
            print(M+" ================================="+B)
            print("          [!] 1 - WhatsApp     ")
            print("          [!] 2 - GbwhatsApp   ")
            print("          [!] 3 - Quitter      ")
            print(M+" =================================\n"+B)
            main_input = input(C+" ==> "+B)
            try:
                main_input = int(main_input)
            except:
                os.system("clear")
                print(R+"[!] Enter invalide !\n")
                mainApp()
            if main_input == 1:
                whatsApp_Run = WhatsAppBot()
                whatsApp_Run.WhatsApp()
            elif main_input == 2:
                whatsApp_Run = WhatsAppBot()
                whatsApp_Run.GbwatsApp()
            elif main_input == 3:
                os.system("clear")
                print(J+"[*] Fermerture du Programme !")
                time.sleep(2.2)
                print(B+"[!] Programme Fermé !")
                sys.exit()
            else :
                os.system("clear")
                print(R+"[!] Aucun résultat ne correspond à ['"+B+"{}".format(main_input)+R+"']\n")
                mainApp()
        mainApp()