
import tkinter
from tkinter import *
import tkinter.filedialog
import os
import shutil


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500,550))
        self.master.title('File Helper')
        

        self.varfromfiles = StringVar()
        self.vartofiles = StringVar()
        self.varfileext = StringVar()
        self.varfromdir = StringVar()
        self.varlistfield = StringVar()
        self.varmovefileext = StringVar()

        # FROM DIR

        self.txtF1name = Entry(self.master,text=self.varfromfiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF1name.grid(row=0,column=1, columnspan=3, padx=(20,0), pady=(40,0))

        # FILE EXT

        self.txtF2name = Entry(self.master,text=self.varmovefileext, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF2name.grid(row=1, column=1, columnspan=3, padx=(20,0), pady=(10,0))

        self.lbl_fname = Label(self.master,text='File type: ')
        self.lbl_fname.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N)

        # TO DIR

        self.txtF2name = Entry(self.master,text=self.vartofiles, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF2name.grid(row=2, column=1, columnspan=3, padx=(20,0), pady=(10,0))

        # CLOSE

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=lambda: ask_quit())
        self.btnCancel.grid(row=15, column=3, padx=(0,0), pady=(20,0), sticky=NE)

        # MOVE FILES

        self.btnCancel = Button(self.master, text="Move Files", width=10, height=2, command=lambda: move_files())
        self.btnCancel.grid(row=3, column=0, padx=(30,0), pady=(10,20), sticky=N)

        #SELECT FROM
        
        self.btnSubmit = Button(self.master, text="From...", width=10, command=lambda: fromFiles())
        self.btnSubmit.grid(row=0, column=0, padx=(30,0), pady=(40,0), sticky=N)

        #SELECT TO

        self.btnSubmit = Button(self.master, text="To...", width=10, command=lambda: toFiles())
        self.btnSubmit.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=N)

        #THIS IS THE FILE DIR

        self.txtF1name = Entry(self.master,text=self.varfromdir, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF1name.grid(row=4,column=1, columnspan=3, padx=(20,0), pady=(10,0))

        #THIS IS THE FILE EXT

        self.txtF2name = Entry(self.master,text=self.varfileext, font=("Times New Roman", 12),fg='black', bg='white', width=40)
        self.txtF2name.grid(row=5, column=1, columnspan=3, padx=(20,0), pady=(10,20))

        #BROWSE DIR

        self.btnSubmit = Button(self.master, text="Browse...", width=10, command=lambda: browseDir())
        self.btnSubmit.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=N)

        self.lbl_fname = Label(self.master,text='File type: ')
        self.lbl_fname.grid(row=5,column=0,padx=(27,0),pady=(10,0),sticky=N)

        #SEARCHES FOR FILES

        self.btnCancel = Button(self.master, text="Search", width=10, height=2, command=lambda: search_files())
        self.btnCancel.grid(row=6, column=0, padx=(30,0), pady=(0,0), sticky=N)

        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=6,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstList1.grid(row=6,column=1,rowspan=7,columnspan=3,padx=(20,0),pady=(0,0),sticky=N+E+S+W)
    

  
        def fromFiles():
            file = tkinter.filedialog.askdirectory()
            self.varfromfiles.set(file)

        def toFiles():
            file = tkinter.filedialog.askdirectory()
            self.vartofiles.set(file)

        def ask_quit():
            self.master.destroy()
            os._exit(0)

        def browseDir():
            file = tkinter.filedialog.askdirectory()
            self.varfromdir.set(file)

        
        def search_files():
            self.lstList1.delete(0,END)
            directory = self.varfromdir.get()
            counter = 0
            fileext = self.varfileext.get()
            self.lstList1.insert(END, 'Searching for {} files...'.format(fileext))
            for f in os.listdir(directory):
                if f.endswith(fileext):
                    self.lstList1.insert(END, directory + f)
                    counter = (counter + 1)
                    continue
                else:
                    continue

            self.lstList1.insert(END, "{} {} files in this directory.".format(counter,fileext))

        def move_files():
            self.lstList1.delete(0,END)
            directory = self.varfromfiles.get()
            counter = 0
            fileext = self.varmovefileext.get()
            todirectory = self.vartofiles.get()
            self.lstList1.insert(END, "Moving {} files...".format(fileext))
            for f in os.listdir(directory):
                if f.endswith(fileext):
                    self.lstList1.insert(END, directory + '/' + f)
                    shutil.move(directory + '\\' + f, todirectory + '\\' + f)
                    counter = (counter + 1)
                    continue
                else:
                    continue
            if counter < 1:
                self.lstList1.insert(END, "0 files moved. Ensure correct file extension and try again.")
            else:
                self.lstList1.insert(END, "{} {} files from {} were".format(counter,fileext,directory))
                self.lstList1.insert(END, "successfully moved to {}.".format(todirectory))
            
    


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
