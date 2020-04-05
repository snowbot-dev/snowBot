import os

'''
Run this file in the command line and the project will be automatically uploaded to git
EX: python3 AutoUploader.py
'''

os.system("git pull && git add .&& git commit -m\"autoloaded\"&&git push")
