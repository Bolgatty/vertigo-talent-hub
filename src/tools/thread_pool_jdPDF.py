"""Author : Padmavathi Vempadi
Date : 30/11/2020
Program : Is a thread program along with the progress bar gui using queues. which acts like an interface between
import_resumeGUI and resume_analyser
"""
import tkinter as tk
import tkinter.ttk as ttk
import time
from threading import *
import queue
from src.db.jd_manager import JDManager as jd

class GuiProgressbar:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        # Add more GUI stuff here depending on your specific needs
        # Create a progressbar widget

        '''console = tk.Button(master, text='Done', command=endCommand)
        console.pack()'''
        progress_bar = ttk.Progressbar(master, orient="horizontal",
                                       mode="determinate", maximum=100, value=0)
        label_1 = tk.Label(master, text="Progress Bar")
        label_1.grid(row=0, column=0)
        progress_bar.grid(row=0, column=1)

        # Necessary, as the master object needs to draw the progressbar widget
        # Otherwise, it will not be visible on the screen
        master.update()

        progress_bar['value'] = 0
        master.update()

        while progress_bar['value'] < 100:
            progress_bar['value'] += 20
            # Keep updating the master object to redraw the progress bar
            master.update()
            time.sleep(0.1)

        # The application mainloop

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                print(msg)
            except queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass

class ThreadPooljdPDF:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master, issue_key):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui_jd_pdf = GuiProgressbar(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        try:
            self.thread1 = Thread(target=self.workerThread1, args=(issue_key))
            print(self.thread1)
            self.thread1.start()
            print("control on child thread", current_thread().getName())
            print("is child thread active", self.thread1.is_alive())  # to check the thread is still alive or not
            self.thread1.join()
            print("is child thread active", self.thread1.is_alive())  # to check the thread is still alive or not

            # Start the periodic call in the GUI to check if the queue contains
            # anything
            self.periodicCall()
            self.master.withdraw()
        except Exception as e:
            print(e)

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui_jd_pdf.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.periodicCall)

    def workerThread1(self, issue_key):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """

        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following two lines with the real
            # thing.

            msg = "Generate pdf thread in the Queue"
            job_dict = jd().get_particular_desc(issue_key)
            self.queue.put(msg)
            return job_dict

    def endApplication(self):
        self.running = 0