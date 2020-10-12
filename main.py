"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : Main file that is responsible for the app to run"""

import tkinter as tk
from src.import_resumeGUI import ImportResumeGUI


if __name__ == '__main__':
    root = tk.Tk()
    obj = ImportResumeGUI(root)
    root.mainloop()
