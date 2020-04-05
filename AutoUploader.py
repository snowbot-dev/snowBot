import os

'''
Run this file in the command line and the project will be automatically uploaded to git
EX: python3 AutoUploader.py
'''
pull = input('Do you want to pull before you add your file? (yes/no): ')
if pull.lower() == 'yes' or pull.lower() == 'y':
    os.system("git pull && git add .&& git commit -m\"autoloaded\"&&git push")
else:
    os.system("git add .&& git commit -m\"autoloaded\"&&git push")
