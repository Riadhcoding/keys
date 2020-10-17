import os,time,sys
def clear():
    os.system('clear')
clear()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.08)
os.system('git pull')

clear()
logo = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P           

\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P
"""

def list():
    print("\003[1;31m[1] \033[1;34mAdd keys in Termux")
    time.sleep(0.3)
    print("\003[1;31m[2] \033[1;34mRestore the default keys")
    time.sleep(0.3)
    print("\003[1;31m[3] \033[1;34mYoutube")
    time.sleep(0.3)
    print("\003[1;31m[0] \033[1;34mExit")
    time.sleep(0.3)
    print("")
clear()
print(logo)
list()
choose = input("\033[1;31m[?]\033[1;37mChoose an option : ")

if choose == '1':
    os.system('cd $HOME;rm -rf .termux;mkdir .termux;cd $HOME;cd keys/.main;cp termux.properties /data/data/com.termux/files/home/.termux;termux-reload-settings')
    clear()
    print(logo)
    jalan("\033[1;31mButtons have been added")

elif choose =='2':
    os.system('cd $HOME;rm -rf .termux;termux-reload-settings')
    clear()
    print(logo)
    jalan("\033[1;31mThe default buttons have been restored")

elif choose =='3':
    clear()
    print(logo)
    os.system('xdg-open https://www.youtube.com/pythonlife')

elif choose =='0':
    clear()
    print(logo)
    os.system('exit')
    os.system('xdg-open https://www.youtube.com/pythonlife')








