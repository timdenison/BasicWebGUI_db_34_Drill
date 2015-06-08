#Create a user interface using Tkinter to allow users to set the text for a basic
#html page which will then be created and displayed in a browser

import basichtmlpage
from tkinter import *
from tkinter import ttk

class Custompage:
    def __init__(self, master):
        master.title('Update Company Webpage')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TLabel', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.header = ttk.Frame(master)
        self.header.pack()
        ttk.Label(self.header, style = 'Header.TLabel', text = 'Update Company Website').pack(padx = 10)

        self.body = ttk.Frame(master)
        self.body.pack(pady = 20)
        ttk.Label(self.body, style = 'TLabel', text = 'Text to display: ').grid(row = 0, column = 0, stick = 'w')
        self.usrString = ttk.Entry(self.body, width = 60)
        self.usrString.grid(row = 1, column = 0, columnspan = 2)
        ttk.Button(self.body, text = 'Update Website', command = lambda: self.OnClick(master)).grid(
            row = 0, column = 1, rowspan = 1, sticky = 'e')

    def OnClick(self, root):
        self.usrString = self.usrString.get()
        p = basichtmlpage.basicHTML()
        p.createHTML(self.usrString)
        root.destroy()

    def close(root):
        root.destroy()
        

def main():
    root = Tk()
    custompage = Custompage(root)
    
   
    root.mainloop()

if __name__ == "__main__": main()