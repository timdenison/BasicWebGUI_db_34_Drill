# A script that creates a basic web page.
import sys

class basicHTML():

    def createHTML(self, usrString, usrItem, usrPrice, usrQty):
        file = open('index.html', 'w')
        file.write('<html> \n'
                   '<body> \n'
                   '<h1>' + usrString + '</h1> \n'
                   '<p><b>Item:</b> ' + usrItem + '  <b>Price: </b>' + usrPrice + '  <b>Quantity: </b>' + usrQty + '</p> \n'
                   '</body> \n'
                   '</html>')
        self.viewHTML()

    def viewHTML(self):
        import webbrowser
       # url = 'file://index.html'
        new = 2 # open in new tab if possible
        webbrowser.open('index.html', new = new)

def main():
    createHTML()
if __name__ == "__main__": main()