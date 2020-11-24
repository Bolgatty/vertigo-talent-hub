"""Author : Padmavathi Vempadi
Date : 30/11/2020
Program : Is a thread program along with the progress bar gui using queues. which acts like an interface between
Job Manage GUI through Jobs_table_display_gui and jd_manager for database JIRA.
"""
import tkinter as tk
import tkinter.ttk as ttk
import time
from threading import *
import queue
from src.db.jd_manager import JDManager

class ThreadPoolJDM:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = queue.Queue()

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        self.thread1 = Thread(target=self.workerThread1)
        print(self.thread1)
        self.thread1.start()
        print("control on child thread", current_thread().getName())
        print("is child thread active", self.thread1.is_alive())  # to check the thread is still alive or not
        self.thread1.join()
        print("is child thread active", self.thread1.is_alive())  # to check the thread is still alive or not

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()
        # control to come back to the mainscreen.
        self.master.deiconify()

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """

        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following two lines with the real
            # thing.

            msg = "Child Thread is in the Queue"
            jobs = JDManager().fetch_all_jobs()
            self.queue.put(msg)
            return jobs

