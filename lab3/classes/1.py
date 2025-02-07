class Stroperations:
    def __init__(self):
        self.thestring = ""
        
    def getString(self):
        self.thestring = str(input())

    def printString(self):
        print(self.thestring.upper())

text = Stroperations()
text.getString()
text.printString()
