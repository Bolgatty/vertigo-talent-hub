from docx2pdf import convert
#from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx import Document
from docx.shared import Inches
from src.db.jd_manager import JDManager as jd
from src.gui.jobs_table_display_gui import JobsTable as jt
from tkinter import messagebox as mb

class JobGeneratepdf:

    def generate_pdf(self):
        """
            method called when Generate Job button is clicked from job_management initial screen
        """
        if jt.selected_job_id:
            if mb.askyesno("PDF Generate Confirmation", "Are you sure you want to generate pdf for the selected job ?"):
                for i in jt.issue_key_list:
                    self.pdf_generator(i)
                mb.showinfo("Info", "PDF and DOCx files generated successfully!")
        else:
            mb.showerror("Error", "Please select the job you want to generate pdf for")


    def pdf_generator(self, issue_key):

        final = Document()
        final.add_picture('check.png', width=Inches(1.25))
        last_pic = final.paragraphs[-1]
        last_pic.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        about_us = Document('about.docx')
        all_paras = about_us.paragraphs
        print(len(all_paras))
        for para in all_paras:
            print(para.text)
            final.add_paragraph(para.text)

        # for element in about_us.element.body:
        #     final.element.body.append(element)

        job_dict = jd().get_particular_desc(issue_key)

        final.add_heading('Job ID:', 1)
        final.add_paragraph(job_dict['job_id'])

        final.add_heading('Job Description:', 1)
        final.add_paragraph(job_dict['job_description'])

        filename = job_dict['job_id']
        final.save(filename+'.docx')

        convert(filename+'.docx', filename+'.pdf')
