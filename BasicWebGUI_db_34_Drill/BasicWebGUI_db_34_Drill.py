#Create a user interface using Tkinter to allow users to set the text for a basic
#html page and to select from pre-created content stored in a database

import basichtmlpage, sqlite3
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

        ttk.Label(self.body, style = 'TLabel', text = 'Select content to display: ').grid(
            row = 2, column = 0, columnspan = 2, sticky = 'w')

        self.contentList = Listbox(self.body, height = 6, width = 50, selectmode = SINGLE)
        self.scrollbar = Scrollbar(self.body, orient = VERTICAL, command = self.contentList.yview)
        self.contentList.config(yscrollcommand = self.scrollbar.set)
        self.contentList.grid(row = 3, column = 0, columnspan = 2, sticky = 'we')
        self.scrollbar.grid(row = 3, column = 2, sticky = 'ns')
       

        self.productList = []
        conn = sqlite3.connect('content.db')
        c = conn.cursor()
        c.execute('SELECT * FROM products')
        for row in c.fetchall():
            item = row[1]
            price = str(row[2])
            qty = str(row[3])
            self.contentList.insert(END, item + ', ' + price + ', ' + qty)
        self.contentList.select_set(0)

    
    def selectedItem(self):
        selection = self.contentList.curselection()
        usrIndex = int(selection[0]) + 1
        usrIndex = str(usrIndex)
        
        conn = sqlite3.connect('content.db')
        c = conn.cursor()
        c.execute('SELECT item, price, quantity FROM products WHERE id=?' , usrIndex)
        for row in c.fetchall():
            self.usrItem = str(row[0])
            self.usrPrice = str(row[1])
            self.usrQty = str(row[2])
        


    def OnClick(self, root):
        self.usrString = self.usrString.get()
        self.selectedItem()
        p = basichtmlpage.basicHTML()
        p.createHTML(self.usrString, self.usrItem, self.usrPrice, self.usrQty)
        root.destroy()

    def close(root):
        root.destroy()
        

def main():
    root = Tk()
    custompage = Custompage(root)
    
   
    root.mainloop()

if __name__ == "__main__": main()
