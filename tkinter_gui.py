
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550,200))
        self.master.title('Check Files')
        

        self.varsearchfiles = StringVar()
        self.varbrowsefiles = StringVar()

        self.txtFName = Entry(self.master,text=self.varsearchfiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtFName.grid(row=0,column=1, columnspan=3, padx=(0,0), pady=(40,0))

        self.txtLName = Entry(self.master,text=self.varbrowsefiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtLName.grid(row=1, column=1, columnspan=3, padx=(0,0), pady=(10,0))

        self.btnSubmit = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnSubmit.grid(row=2, column=0, padx=(50,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2)
        self.btnCancel.grid(row=2, column=3, padx=(0,10), pady=(30,0), sticky=NE)
        
        self.btnSubmit = Button(self.master, text="Browse...", width=10)
        self.btnSubmit.grid(row=0, column=0, padx=(20,0), pady=(40,0), sticky=N)

        self.btnSubmit = Button(self.master, text="Browse...", width=10)
        self.btnSubmit.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=N)




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
