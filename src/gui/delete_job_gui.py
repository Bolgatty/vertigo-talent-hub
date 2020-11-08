from tkinter import messagebox as mb
from src.gui.jobs_table_display_gui import JobsTable as jt
from src.db.jd_manager import JDManager as jd

class DeleteJob:

    def __init__(self, root, first_frame):
        self.first_frame = first_frame
        self.root = root

    def delete_job(self):
        """
             method called when Delete Job button is clicked from job_management initial screen
        """
        if jt.selected_job_id:
            if mb.askyesno("Confirm Deletion", "Are you sure you want to delete the selected job ?"):
                for i in jt.issue_key_list:
                    jd().delete_job(i)
                mb.showinfo("Info", "Selected Jobs deleted successfully")
                jt(self.root).jobs_table(self.first_frame)
        else:
            mb.showerror("Error", "Please select the job you want to delete")