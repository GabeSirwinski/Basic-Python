
import tkinter
from tkinter import *
import tkinter.filedialog
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Check Files')
        

        self.varsearchfiles = StringVar()
        self.varbrowsefiles = StringVar()

        self.txtF1name = Entry(self.master,text=self.varsearchfiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF1name.grid(row=0,column=1, columnspan=3, padx=(20,0), pady=(40,0))

        self.txtF2name = Entry(self.master,text=self.varbrowsefiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF2name.grid(row=1, column=1, columnspan=3, padx=(20,0), pady=(10,0))

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=lambda: ask_quit())
        self.btnCancel.grid(row=2, column=3, padx=(0,10), pady=(30,0), sticky=NE)
        
        self.btnSubmit = Button(self.master, text="Browse...", width=10, command=lambda: searchFiles())
        self.btnSubmit.grid(row=0, column=0, padx=(30,0), pady=(40,0), sticky=N)

        self.btnSubmit = Button(self.master, text="Browse...", width=10, command=lambda: browseFiles())
        self.btnSubmit.grid(row=1, column=0, padx=(30,0), pady=(10,0), sticky=N)

  
        def browseFiles():
            file = tkinter.filedialog.askdirectory()
            print(file)
            self.varbrowsefiles.set(file)

        def searchFiles():
            file = tkinter.filedialog.askdirectory()
            print(file)
            self.varsearchfiles.set(file)

        def ask_quit():
            self.master.destroy()
            os._exit(0)
    



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
