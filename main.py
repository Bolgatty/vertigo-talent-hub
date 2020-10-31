"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : Main file that is responsible for the app to run"""

import tkinter as tk
from src.gui.talenthub_GUI import TalentHubGUI


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes("-topmost", False)
    root.lower()
    obj = TalentHubGUI(root)
    root.mainloop()
