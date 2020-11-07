import os
import getpass
os.system("tput setaf 4")
print("\t\t\tWelcome to the Knowledge Store")

password = getpass.getpass()
if (password!="redhat"):
    print("Wrong password entered")
    exit()

os.system("clear")

os.system("tput setaf 1")
ch = input("Do you want to run system locally (y/n): ")
if(ch=="y"):
    from menulocal import localmenu

else:
    from menussh import sshmenu   

