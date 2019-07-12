#coding:utf-8
#-------------------------------------------------------------------------------------------------------------#
#------------------------------------------------SocialBot----------------------------------------------------#
import os, sys
if sys.version[0] == '3' :
    if sys.platform in ["linux", "linux2"] :
        clear = "clear"
        R = "\033[31;1m"
        V = "\033[32;1m"
        B = "\033[0m"
        C = "\033[36;1m"
        J = '\033[93m'
        M = '\033[94m'
    else :
        R = ""
        V = ""
        B = ""
        C = ""
        J = ""
        M = ""
        clear = "cls"
    os.system(clear)
else:
    print("[!] Programme uniquement éxécutable sous python3")
    print("[!] Exemple : python3 script.py")
    sys.exit()
try:
    from Whatsapp.Whatsappbot import WhatsAppBot as BotWhatsApp
except ModuleNotFoundError:
    print("[!] Impossible de démarrer le Programme !")
    print("[!] Un module manque !")
    sys.exit()

def main():
    def verify_sys():
        if sys.platform != "linux2" :
            sys_r = False
        else :
            sys_r = True
        return sys_r
    get_sys_version = verify_sys()
    if get_sys_version :
        RunApp = BotWhatsApp()
        RunApp.main()
    else:
        print(R+"[!] Vous ne pouvez pas utilisez WhatsAppBot sur Pc")
#main function started for Only WhatsappBot
main()