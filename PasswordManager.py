from TableManager import TableManager
from rich import print as p
from os import sys
import main
from getpass import getpass
import os as os
class PasswordManager:
    def __init__(self):
        main.setup()
        self.tm = TableManager()
    def createGUI(self):
        while True:
            # os.system('cls')
            p(  """                     Password Manager
                1. Create Password      2. Update Password      3. Read Password
                4. Delete Password      5. Exit                 6. Clear screen
                """)
            ch = int(input('Enter your choice (1-6) : '))
            if ch == 1:
                # print('Inserting a password : ')
                pw = input('password: ')
                url = input('app: ')
                app = input('url: ')
                pas = getpass('pas: ')
                self.tm.insertData((pw,url,app,pas))
            elif ch == 2:
                # print('Update the password')
                url = input('url/app: ')
            elif ch == 3:
                # 'Fetching Password
                self.tm.selectData()
                input('')
            elif ch == 4:
                # delete password as per given password if it matches
                temp = input('Enter password to delete: ')
                t = input("Are you want to sure[Y/y] default n :")
                if temp != '' and (t == 'y' or t == 'Y'):
                    self.tm.deleteData(temp)
            elif ch == 5:
                # Clears screen before exiting
                os.system('cls')
                sys.exit(0)
            #Clears screen
            elif ch == 6:
                os.system('cls')

pm = PasswordManager()
pm.createGUI()