# MSMU 0.4.1
# Mutipurpose SFS Management Utility
# Or MSMU: SFS Management Utility to make it recursive.
# By Engine
# ========== Configs ========== #

import sys
import os
import shutil
import subprocess
import webbrowser
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

Ver = "0.4.1"
State = "Beta"

# ========== Varibles ========== #

# the profile to launch from
option = "Modded"

dictionary = os.getcwd()

# ========== Functions ========== #

def ToVanilla():  # FIXED
    os.removedirs(f"{SFS_DIR}/Mods")

def ToModded():
    profilefold = folder, option, "Mods"
    global profilefolder
    profilefolder = "/".join(profilefold)
    shutil.rmtree(f"{SFS_DIR}/Mods")
    shutil.copytree(profilefolder,f"{SFS_DIR}/Mods",)

def launch(): # Temp version
    webbrowser.open("steam://rungameid/1718870")

#def launch():  # Launches the game
#    if option == "Vanilla":
#        ToVanilla()
#        webbrowser.open("steam://rungameid/1718870")
#    else:
#        ToModded()
#        webbrowser.open("steam://rungameid/1718870")

def option_open():
    profilefold = dictionary, folder, option, "Mods"
    profilefolder = r"/".join(profilefold)
    os.startfile(profilefolder)

# ========== GUI code ========== #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"MSMU {State} {Ver}")
        button = QPushButton("Launch SFS")
        button.clicked.connect(launch)
        self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
