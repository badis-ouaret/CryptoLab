import View.Frames as fr
import Model.chiffreur as ch
class MainController():
    
    def __init__(self):
        self.frame = fr.Interface()
        self.cesar = ch.CesarChiffreur()
        self.vigenere = ch.VigenereChiffreur()
        self.amelioCesar = ch.AmelioredCesarChiffreur()
        self.polybe=ch.PoybeChiffreur()
        self.playfair = ch.PlayfairChiffreur()
        self.affine = ch.AffineChiffreur()
        self.hill = ch.HillChiffreur()
        
        self.frame.keyDefButton.configure(command=self.keyDefButtonFunction)        
        self.frame.operationButton.configure(command=self.operationButtonFunction)
        self.frame.clearButton.configure(command=self.clearButtonAction2)


        


    
    def keyDefButtonFunction(self):
        print("bonjour")
    def operationButtonFunction(self):
        print("est une catastrophe")
    def clearButtonFunction():
         print("j'ai jamais fait un code aussi catastrophique que celui ci")

         


    def clearButtonAction2(self):
            self.frame.textEntry.delete("0.0", "end")
            self.frame.resultEntry.delete("0.0", "end")
            self.frame.textEntry.focus_set()
            self.clearButtonFunction()

    def go(self):
        self.frame.start()    
    
