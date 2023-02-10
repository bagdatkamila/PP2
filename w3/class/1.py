class Notmy:
    def __init__(self):
        self.a = ""
    def getString(self):
        self.a = input()
    def printString(self):
        print(self.a.upper())

a = Notmy()
a.getString()
a.printString()