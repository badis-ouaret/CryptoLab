import customtkinter as ctk

from abc import ABC, abstractmethod
from tkinter import messagebox


FRAME_WIDTH = 1200
FRAME_HEIGHT = 700

#--------------------------------------------
#MainFrame
MAIN_FRAME_BG_COLOR = "black"
#--------------------------------------------
#MENU
MENU_HEIGHT = FRAME_HEIGHT
MENU_WIDTH = 200
MENU_TEXT_COLOR = "white"
MENU_BG_COLOR = "black"
MENU_FONT = ("Arial", 16)
PADY_RADIO_MENU = 20
PADY_FIRST_RADIO_MENU = (80, PADY_RADIO_MENU)
PADX_RADIO_MENU = (10, 0)
#--------------------------------------------
# PanelDroit
RIGHT_PANEL_WIDTH = FRAME_WIDTH - MENU_WIDTH
RIGHT_PANEL_HEIGHT = FRAME_HEIGHT
RIGHT_PANEL_BG_COLOR = "white"
RIGHT_PANEL_FONT = ("Arial", 20)
RIGHT_PANEL_TEXT_COLOR = "black"
RIGHT_PANEL_TITLE_FONT = ("Arial", 40)
RIGHT_PANEL_TITLE_COLOR = "black"

OPTION_PANEL_HEIGHT = 70

PADY_RADIO_OPTION_PANEL = 20
OPTION_PANEL_BG_COLOR = "gray"
OPTION_PANEL_FONT = ("Arial", 16)
OPTION_PANEL_TEXT_COLOR = "white"
KEY_ENTRY_FONT = ("Arial", 16)
#--------------------------------------------
#boutons
BUTTON_BG_COLOR_HOVER = "gray"
BUTTON_BG_COLOR = "black"
BUTTON_TEXT_COLOR_HOVER = "white"
BUTTON_TEXT_COLOR = "white"
BUTTON_BORDER_COLOR = "black"
BUTTON_BORDER_WIDTH = 3
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 200
BUTTON_FONT = ("Arial", 16)
BUTTON_BORDER_COLOR_HOVER = "black"
BUTTON_BORDER_WIDTH_HOVER = 3

#--------------------------------------------


class ToolBox(ABC,ctk.CTk):

   
    
    @staticmethod
    def configureGrid(pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1}):

        for line,weight in dictR.items():
            pannel.grid_rowconfigure(line, weight=weight)
        for col,weight in dictC.items():
            pannel.grid_columnconfigure(col, weight=weight)
        
    
    @staticmethod
    def createTextsEntrys(pannel,ligne = 3,colonne = 0,textLabel = "Texte en clair",resultLabel = "Texte chiffré",entryWidth = 300,entryHeight = 200,entryBorderColor = "black",entryBorderWidth=3, entryFgColor = "white" ,entryTextColor = RIGHT_PANEL_TEXT_COLOR,entryFont = RIGHT_PANEL_FONT,label1Text = "Texte en clair",label2Text = "Texte chiffré",label1Font = RIGHT_PANEL_FONT,label2Font = RIGHT_PANEL_FONT,label1TextColor= RIGHT_PANEL_TEXT_COLOR,label2TextColor = RIGHT_PANEL_TEXT_COLOR):
        textLabel = ctk.CTkLabel(pannel,text=label1Text,font=label1Font, text_color=label1TextColor)
        textLabel.grid(row=ligne-1, column=colonne+1, pady=0, padx=(10,0), sticky="nesw")

        resultLabel = ctk.CTkLabel(pannel,text=label2Text,font=label2Font, text_color=label2TextColor)
        resultLabel.grid(row=ligne-1, column=colonne+3, pady=0, padx=(0, 10), sticky="nesw")
        
        textEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        textEntry.grid(row=ligne, column=colonne, pady=30, padx=(30, 0),columnspan=2, sticky="nesw")
        textEntry.focus_set()

        resultEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        resultEntry.grid(row=ligne, column=colonne+3, pady=30, padx=(0, 30),columnspan=2, sticky="nesw")
        resultEntry.configure(state="readonly")

        return textLabel,resultLabel,textEntry,resultEntry
    



class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{FRAME_WIDTH}x{FRAME_HEIGHT}")
        self.title("CryptoLab")
        self.choixMethode = ctk.StringVar(value="Cesar")
        self.choixOperation = ctk.StringVar(value="Chiffrer")

        self.main_frame = ctk.CTkFrame(self, fg_color=MAIN_FRAME_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        # Panel de menu
        self.menuPanel = ctk.CTkFrame(self.main_frame, width=MENU_WIDTH, height=MENU_HEIGHT, fg_color=MENU_BG_COLOR)
        self.menuPanel.pack(side="left", fill="y")

        # Liste des méthodes de chiffrement
        chiffrement_methods = [
            ("Cesar", "Cesar"),
            ("Vigenère", "Vigenere"),
            ("Cesar amélioré", "AmelioCesar"),
            ("Polybe", "Polybe"),
            ("Playfair", "Playfair"),
            ("Hill", "Hill"),
            ("Affine", "Affine"),
            ("Transposition", "Transpo"),
            ("Chiffrement DES", "DES")
        ]
        
        # Création dynamique des boutons radio pour les méthodes de chiffrement
        compte = 0
        for text, value in chiffrement_methods:
            compte +=1
            if compte == 1:
                self.radio = ctk.CTkRadioButton(self.menuPanel,
                                                text=text, 
                                                variable=self.choixMethode, 
                                                value=value, 
                                                width=MENU_WIDTH, 
                                                text_color=MENU_TEXT_COLOR, 
                                                font=MENU_FONT)
                self.radio.pack(padx=PADX_RADIO_MENU, pady=PADY_FIRST_RADIO_MENU)
            else:
                self.radio =ctk.CTkRadioButton(self.menuPanel,
                               text=text, 
                               variable=self.choixMethode, 
                               value=value, 
                               width=MENU_WIDTH, 
                               text_color=MENU_TEXT_COLOR, 
                               font=MENU_FONT).pack(padx=PADX_RADIO_MENU, pady=PADY_RADIO_MENU)
                


        # Panel de droite
        self.right_panel = ctk.CTkFrame(self.main_frame, height=RIGHT_PANEL_HEIGHT, width=RIGHT_PANEL_WIDTH, fg_color=RIGHT_PANEL_BG_COLOR)
        self.right_panel.pack(side="left", fill="both", expand=True)
            # Panel de choix d'opération
        self.choixOperationPanel = ctk.CTkFrame(self.right_panel, corner_radius=0, fg_color=OPTION_PANEL_BG_COLOR, height=OPTION_PANEL_HEIGHT)
        self.choixOperationPanel.pack(side="top", fill="x")

        self.centerChoixOperationPanel = ctk.CTkFrame(self.choixOperationPanel, fg_color=OPTION_PANEL_BG_COLOR)
        self.centerChoixOperationPanel.place(relx=0.5, rely=0.5, anchor="center")

        self.radioChiffrer = ctk.CTkRadioButton(self.centerChoixOperationPanel, text="Chiffrer", variable=self.choixOperation, value="Chiffrer", text_color=OPTION_PANEL_TEXT_COLOR, font=OPTION_PANEL_FONT)
        self.radioDechiffrer = ctk.CTkRadioButton(self.centerChoixOperationPanel, text="Déchiffrer", variable=self.choixOperation, value="Dechiffrer", text_color=OPTION_PANEL_TEXT_COLOR, font=OPTION_PANEL_FONT)

        self.radioChiffrer.pack(side="left", padx=10, pady=PADY_RADIO_OPTION_PANEL)
        self.radioDechiffrer.pack(side="left", padx=10, pady=PADY_RADIO_OPTION_PANEL)
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Panel principal++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.panelPrincipal = ctk.CTkFrame(self.right_panel,fg_color=RIGHT_PANEL_BG_COLOR,corner_radius=0)
        self.panelPrincipal.pack(side="bottom", fill="both", expand=True)
        self.operationButton,self.clearButton,self.textEntry,self.resultEntry,self.textLabel,self.resultLabel,self.title = self.mainPart(self.panelPrincipal,title="Chiffrement")        
                
        self.keyDefButton = self.createButton(self.panelPrincipal, text="Définir la clé",ligne=1,colonne=2,pady=(0,20))
        
        


        self.update_panel_for_method()
        self.choixMethode.trace_add("write",self.update_panel_for_method)
        #self.update_panel_for_operation()
        self.traceOperationId = self.choixOperation.trace_add("write",self.update_panel_for_operation)
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #geters ========================================
    def getMethodeDeChiffrement(self):
        return self.choixMethode.get()
    def getOperation(self):
        return self.choixOperation.get()    
    def getTextEntry(self):
        return self.textEntry
    def getResultEntry(self):
        return self.resultEntry
    #==========================================================
    #seters ===================================================
    def messageAlerte(self,message,title="Erreur",buttonText="OK"):
        messagebox.showwarning(title=title, message=message)

    def setResultEntryText(self,text):
        self.resultEntry.configure(state="normal")
        self.resultEntry.delete("0.0",'end')         # Efface tout le texte
        self.resultEntry.insert("0.0",text)  # Insère le texte à la position 0
        self.resultEntry.configure(state="disabled")
    #==========================================================
    

    #Gestion de l'affichage selon les boutons radios selectionnés
    def update_panel_for_method(self, *args):         
        method = self.choixMethode.get()

        if method == "Cesar":
            self.title.configure(text = "Chiffrement de César")
        elif method == "Vigenere":
            self.title.configure(text = "Chiffrement de Vigenère")
        elif method == "Playfair":
            self.title.configure(text = "Chiffrement de Playfair")
        elif method == "AmelioCesar":
            self.title.configure(text = "Chiffrement de César Amélioré")
        elif method == "Polybe":
            self.title.configure(text = "Chiffrement de Polybe")
        elif method == "Hill":
            self.title.configure(text = "Chiffrement de Hill")
        elif method == "Affine":
            self.title.configure(text = "Chiffrement Affine")
        elif method == "Transpo":
            self.title.configure(text = "Chiffrement par Transposition")
        elif method == "DES":
            self.title.configure(text = "Chiffrement DES")

    def update_panel_for_operation(self,*args):
        self.textLabel.configure(text="Texte en clair" if self.choixOperation.get() == "Chiffrer" else "Texte chiffré")
        self.resultLabel.configure(text="Texte chiffré" if self.choixOperation.get() == "Chiffrer" else "Texte en clair")
        self.operationButton.configure(text="Chiffrer" if self.choixOperation.get() == "Chiffrer" else "Déchiffrer")
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def start(self):
        self.mainloop()







    

    #Methodes de creation de panel et de configuration de la grille ============================
    def createPanel(self):
        panel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="white")
        panel.pack(side="bottom",fill="both",expand=True)
        return panel
    
    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1}):

        for line,weight in dictR.items():
            pannel.grid_rowconfigure(line, weight=weight)
        for col,weight in dictC.items():
            pannel.grid_columnconfigure(col, weight=weight)
    
    def createTextsEntrys(self,pannel,ligne = 3,colonne = 0,textLabel = "Texte en clair",resultLabel = "Texte chiffré",entryWidth = 300,entryHeight = 200,entryBorderColor = "black",entryBorderWidth=3, entryFgColor = "white" ,entryTextColor = RIGHT_PANEL_TEXT_COLOR,entryFont = RIGHT_PANEL_FONT,label1Text = "Texte en clair",label2Text = "Texte chiffré",label1Font = RIGHT_PANEL_FONT,label2Font = RIGHT_PANEL_FONT,label1TextColor= RIGHT_PANEL_TEXT_COLOR,label2TextColor = RIGHT_PANEL_TEXT_COLOR):
        textLabel = ctk.CTkLabel(pannel,text=label1Text,font=label1Font, text_color=label1TextColor)
        textLabel.grid(row=ligne-1, column=colonne+1, pady=0, padx=(10,0), sticky="nesw")

        resultLabel = ctk.CTkLabel(pannel,text=label2Text,font=label2Font, text_color=label2TextColor)
        resultLabel.grid(row=ligne-1, column=colonne+3, pady=0, padx=(0, 10), sticky="nesw")
        
        textEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        textEntry.grid(row=ligne, column=colonne, pady=30, padx=(30, 0),columnspan=2, sticky="nesw")
        textEntry.focus_set()

        resultEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        resultEntry.grid(row=ligne, column=colonne+3, pady=30, padx=(0, 30),columnspan=2, sticky="nesw")
        resultEntry.configure(state="disabled")

        return textLabel,resultLabel,textEntry,resultEntry
   
    
   
    
    def mainPart(self,pannel,title = "",titleFont = RIGHT_PANEL_TITLE_FONT,titleTextColor = RIGHT_PANEL_TITLE_COLOR,isGrid = True,dictC ={0: 0, 1: 1, 2: 1, 3: 1},dictR={}):
        titleFrame = ctk.CTkFrame(pannel.master,fg_color=pannel.cget("fg_color") ,corner_radius=0,height=100)
        titleFrame.pack(side="top",fill="x")
        titre = ctk.CTkLabel(titleFrame, text=title, font=titleFont, text_color=titleTextColor)
        titre.pack(expand = True,anchor = 'center' ,pady=30) 
        if isGrid:
            self.configureGrid(pannel,dictC=dictC,dictR=dictR)

        textLabel,resultLabel,textEntry,resultEntry = self.createTextsEntrys(pannel)    

        operationButton = self.createButton(pannel, text="Chiffrer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",ligne = 4,colonne = 2,padx=(0, 10),pady=(20,10))
        clearButton = self.createButton(pannel, text="Effacer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",ligne = 5,colonne = 2,padx=(0, 10),pady=(20,10))
        
        
        return operationButton,clearButton,textEntry,resultEntry,textLabel,resultLabel,titre
    #=====================================================================
    
    #Methodes gestion boutons ====================================================================
    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)
    def clearButtonAction(self,textEntry,resultEntry,cleEntry):
        textEntry.delete("0.0", "end")
        resultEntry.delete("0.0", "end")
        cleEntry.delete(0, "end")
        textEntry.focus_set()
    
            
    #=======================================================================

    #Methodes pannel des entrées et des boutons ==================================================

    def only_numbers(self,char):
        return char.isdigit()
    
    def only_alphabetic(self,char):
        return char.isalpha() and char.isascii()






class defineAmelioCesarKeyFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)
        self.configureGrid(self.main_frame,lineWay=True,nbrLine=6,nbrCol=10,lineVal=1,colVal=1)
        self.LETTRE_DE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lettresRestantes = list(self.LETTRE_DE_ALPHABET) 
        vcmd = (self.register(self.gestionDesLettres),'%P','%s') 
        self.entryDict = {}    
        line = 0
        col = 0
        for c in range(ord('A'),ord('Z')+1):
            self.letter = ctk.CTkLabel(self.main_frame, text=chr(c)+" :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
            self.letter.grid(row=line, column=col, pady=10, padx=(20, 0), sticky="w")

            self.Entry = ctk.CTkEntry(self.main_frame,width=35,height=35,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key" ,validatecommand=vcmd)
            self.Entry.grid(row=line, column=col+1, pady=10 ,padx=(0,0), sticky="w")

            self.entryDict[chr(c)] = self.Entry

            col += 2
            if col == 10 :
                line = line +1
                col = 0
    
        self.buttonFrame = ctk.CTkFrame(self,fg_color=RIGHT_PANEL_BG_COLOR,corner_radius=0)
        self.buttonFrame.pack(side="bottom",fill="x")
        self.configureGrid(self.buttonFrame,lineWay=True,nbrLine=2,nbrCol=3,lineVal=1,colVal=1)
        self.submitButton = self.createButton(self.buttonFrame, text="Valider",ligne=0,colonne=1,pady =10)
        self.clearButton = self.createButton(self.buttonFrame, text="Effacer",command=self.clearButtonAction,ligne= 1,colonne=1,pady=10)

    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)
    
    def clearButtonAction(self):
        for entry in self.entryDict.values():
            entry.delete(0, "end")
        


        
    

    
    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1},nbrLine=0,nbrCol = 0,lineWay = False,lineVal = 0,colVal = 0):
        if not lineWay :
            for line,weight in dictR.items():
                pannel.grid_rowconfigure(line, weight=weight)
            for col,weight in dictC.items():
                pannel.grid_columnconfigure(col, weight=weight)
        else:
            for i in range(nbrLine):
                pannel.grid_rowconfigure(i, weight=lineVal)
            for i in range(nbrCol):
                pannel.grid_columnconfigure(i, weight=colVal)

    def gestionDesLettres(self,lettreApres,lettreAvant):

        if (lettreApres in self.lettresRestantes) and len(lettreApres) <=1 :
            self.lettresRestantes.remove(lettreApres)
            return True
        elif lettreApres == "" and lettreAvant.isalpha() and len(lettreAvant) == 1 and lettreAvant.isascii() and lettreAvant.isupper():
            self.lettresRestantes.append(lettreAvant)
            return True
        else:
            return False
        


class keyType1Frame(ctk.CTk):#cesar,vigenere,polybe,playfair,DES
    def __init__(self,width = 400,height = 100):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)  
        self.main_frame = ctk.CTkFrame(self,fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)    
        self.top_frame = ctk.CTkFrame(self.main_frame, fg_color=RIGHT_PANEL_BG_COLOR)
        self.top_frame.pack(side="top",fill ="x")
        self.configureGrid(self.top_frame)
        self.keyEntry = self.createKeyEntry(self.top_frame)
    
    def createKeyEntry(self,pannel,ligne = 1,colonne = 2,validate = "key",vcmd = None,labelFont = RIGHT_PANEL_FONT,labelTextColor = RIGHT_PANEL_TEXT_COLOR ,entryFont = KEY_ENTRY_FONT,    entryTextColor = RIGHT_PANEL_TEXT_COLOR):
        cleLabel = ctk.CTkLabel(pannel, text="Clé", font=labelFont, text_color=labelTextColor)
        cleLabel.grid(row=ligne, column=colonne-1, pady=30, padx=(0, 10), sticky="e")

        cleEntry = ctk.CTkEntry(pannel, width=300,height=35,font=entryFont, text_color=entryTextColor ,validate = validate ,validatecommand=vcmd)
        cleEntry.grid(row=ligne, column=colonne, pady=30 ,padx=0, sticky="nesw")
        return cleEntry
    
    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1},nbrLine=0,nbrCol = 0,lineWay = False,lineVal = 0,colVal = 0):
        if not lineWay :
            for line,weight in dictR.items():
                pannel.grid_rowconfigure(line, weight=weight)
            for col,weight in dictC.items():
                pannel.grid_columnconfigure(col, weight=weight)
        else:
            for i in range(nbrLine):
                pannel.grid_rowconfigure(i, weight=lineVal)
            for i in range(nbrCol):
                pannel.grid_columnconfigure(i, weight=colVal)
    
    def getKeyEntry(self):
        return self.keyEntry
    
    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)

    
class defineCesarKeyFrame(keyType1Frame):
    def __init__(self, width=600, height=250):
        super().__init__(width, height)
        self.title("Cesar Key Frame")
        vcmd = (self.register(self.gestionKeyEntryCesar),'%P')
        self.keyEntry.configure(validatecommand=vcmd)
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color=RIGHT_PANEL_BG_COLOR)
        self.bottom_frame.pack(side="bottom",fill ="x")
        self.configureGrid(self.bottom_frame,lineWay=True,nbrLine=4,nbrCol=11,lineVal=1,colVal = 1)

        self.clearButton = self.createButton(self.bottom_frame,text="Effacer",command=self.clearButtonAction,ligne=0,colonne=4,pady=(0,5))
        self.validateButton= self.createButton(self.bottom_frame,text="Valider",ligne=2,colonne=4,pady=(5,40))
        self.clearButton.grid_configure(columnspan=3,rowspan=1)
        self.validateButton.grid_configure(columnspan=3,rowspan=1)
        
                


    def gestionKeyEntryCesar(self,apres):
        return apres.isdigit() and apres.isascii() and int(apres)<=27 or apres ==""
    
    def clearButtonAction(self):
        self.keyEntry.delete(0,"end")

    def getValidateButton(self): 
        return self.validateButton    
    def getKeyEntry(self):
        return self.keyEntry



class defineVigenereKeyFrame(keyType1Frame):
    def __init__(self, width=600, height=250):
        super().__init__(width, height)
        self.title("Vigenere Key Frame")
        vcmd = (self.register(self.gestionKeyEntryVigenere),'%P')
        self.keyEntry.configure(validatecommand=vcmd)
        self.bottom_frame = ctk.CTkFrame(self.main_frame, fg_color=RIGHT_PANEL_BG_COLOR)
        self.bottom_frame.pack(side="bottom",fill ="x")
        self.configureGrid(self.bottom_frame,lineWay=True,nbrLine=4,nbrCol=11,lineVal=1,colVal = 1)

        self.clearButton = self.createButton(self.bottom_frame,text="Effacer",command=self.clearButtonAction,ligne=0,colonne=4,pady=(0,5))
        self.validateButton= self.createButton(self.bottom_frame,text="Valider",ligne=2,colonne=4,pady=(5,40))
        self.clearButton.grid_configure(columnspan=3,rowspan=1)
        self.validateButton.grid_configure(columnspan=3,rowspan=1)    

    def getValidateButton(self): 
        return self.validateButton    
    def getKeyEntry(self):
        return self.keyEntry 

    def gestionKeyEntryVigenere(self,apres):
        return apres.isascii() and apres.isalpha() or apres == ""
    
    def clearButtonAction(self):
        self.keyEntry.delete(0,"end")
        
    


class definePolybePlayfairKeyFrame(keyType1Frame):
    def __init__(self,width = 800,height = 600,title = "Polybe/Playfair Key Frame"):
        super().__init__(width,height)
        self.title(title)
        #self.keyEntry.configure(state="disabled")
        self.lettresJumleesFrame = ctk.CTkFrame(self.main_frame, fg_color=RIGHT_PANEL_BG_COLOR)
        self.lettresJumleesFrame.pack(side="top",fill ="x")
        self.configureGrid(self.lettresJumleesFrame,lineWay=True,nbrLine=1,nbrCol=10,lineVal=0,colVal=1)
        self.lettresJumleesLabel = ctk.CTkLabel(self.lettresJumleesFrame, text="Lettres jumelées :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        self.lettresJumleesLabel.grid(row=0, column=2, pady=30, padx=(0, 10), sticky="w",columnspan=3)
        self.lettresJumleesEntry1 = ctk.CTkEntry(self.lettresJumleesFrame, width=30,height=30,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key")
        self.lettresJumleesEntry1.grid(row=0, column=3, pady=30 ,padx=(0,10), sticky="e")
        self.lettresJumleesEntry2 = ctk.CTkEntry(self.lettresJumleesFrame, width=30,height=30,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key")
        self.lettresJumleesEntry2.grid(row=0, column=4, pady=30 ,padx=0, sticky="w")

        self.matrice = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR,corner_radius=0)
        self.matrice.pack(side="bottom",fill="both",expand=True)

        self.configureGrid(self.matrice,lineWay=True,nbrLine=11,nbrCol=11,lineVal=1,colVal=1)
        self.LETTRE_DE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lettresRestantes = list(self.LETTRE_DE_ALPHABET)
        vcmdKey = (self.register(self.gestionDesLettresDansKey),'%P','%s')
        #vcmdMat =  (self.register(self.gestionDesLettresDansMatrice),'%P','%s')
        vcmdJumlee2 = (self.register(self.gestionDesLettresDansJumlee2),'%P','%s')
        vcmdJumlee1 = (self.register(self.gestionDesLettresDansJumlee1),'%P','%s')
        self.lettresJumleesEntry2.configure(validatecommand=vcmdJumlee2)
        self.lettresJumleesEntry1.configure(validatecommand=vcmdJumlee1)
        self.keyEntry.configure(validatecommand=vcmdKey)


        
        
        
        

        self.entryList =[]     
        line = 0
        col = 3
        for c in range(25):
            self.Entry = ctk.CTkEntry(self.matrice,width=35,height=35,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key",border_width=2,border_color="black")
            self.Entry.grid(row=line, column=col, pady=0 ,padx=(0,0), sticky="nesw")
            self.Entry.configure(state="readonly")
            

            self.entryList.append(self.Entry)

            col += 1
            if col == 8 :
                line = line +1
                col = 3

        self.clearButton = self.createButton(self.matrice,text="Effacer",command=self.clearButtonAction,ligne=5,colonne=4,pady=(50,0))
        self.fillButton = self.createButton(self.matrice, text="Aperçu",command=self.fillButtonAction,ligne=7,colonne=4,pady=10)
        self.validateButton= self.createButton(self.matrice,text="Valider",ligne=9,colonne=4,pady=(0,50))
        self.validateButton.grid_configure(columnspan=3,rowspan=2)
        self.fillButton.grid_configure(columnspan=3,rowspan=2)
        self.clearButton.grid_configure(columnspan=3,rowspan=2)

        self.matriceFull = False

    
        

    
        

    def gestionDesLettresDansKey(self,lettreApres,lettreAvant):
        if self.lettreJumleeSet() and (lettreApres in self.lettresRestantes) and len(lettreApres) <=1 :
            self.lettresRestantes.remove(lettreApres)
            return True
        elif lettreApres == "" and lettreAvant.isalpha() and len(lettreAvant) == 1 and lettreAvant.isascii() and lettreAvant.isupper():
            self.lettresRestantes.append(lettreAvant)
            return True
        elif len(lettreAvant)>=1 and len(lettreApres) and self.lettreJumleeSet() and (lettreApres[len(lettreApres)-1] in self.lettresRestantes) and len(lettreApres[len(lettreApres)-1] ) <=1 :
            self.lettresRestantes.remove(lettreApres[len(lettreApres)-1] )
            return True
        elif len(lettreApres)>=1 and len(lettreAvant)>=1 and lettreApres == lettreAvant[0:len(lettreAvant)-1] and lettreAvant[len(lettreAvant)-1].isalpha() and len(lettreAvant[len(lettreAvant)-1]) == 1 and lettreAvant[len(lettreAvant)-1].isascii() and lettreAvant[len(lettreAvant)-1].isupper():
            self.lettresRestantes.append(lettreAvant[len(lettreAvant)-1])
            return True         
        elif self.lettreJumleeSet() and len(lettreApres)>len(lettreAvant) and self.lettreEnleveAjoute(lettreApres,lettreAvant) in self.lettresRestantes and len(lettreApres) <=25 :
            self.lettresRestantes.remove(self.lettreEnleveAjoute(lettreApres,lettreAvant))
            return True
        elif len(lettreAvant)>len(lettreApres) and self.lettreEnleveAjoute(lettreAvant,lettreApres).isalpha() and self.lettreEnleveAjoute(lettreAvant,lettreApres).isascii() and self.lettreEnleveAjoute(lettreAvant,lettreApres).isupper():
            self.lettresRestantes.append(self.lettreEnleveAjoute(lettreAvant,lettreApres))
            return True
        elif len(lettreAvant)>len(lettreApres) and lettreApres == "":
            for c in lettreAvant:
                if c.isalpha() and c.isascii and c.isupper():
                    self.lettresRestantes.append(c)
            return True
        else:
            return False  
        
    
    
    def gestionDesLettresDansJumlee2(self,lettreApres,lettreAvant):
        
        if lettreApres != self.lettresJumleesEntry1.get() and (lettreApres in self.lettresRestantes) and len(lettreApres) <=1 :
            self.lettresRestantes.remove(lettreApres)
            return True
        elif lettreApres == "" and lettreAvant.isalpha() and len(lettreAvant) == 1 and lettreAvant.isascii() and lettreAvant.isupper():
            self.lettresRestantes.append(lettreAvant)
            return True
        else:
            return False 
    
    def gestionDesLettresDansJumlee1(self,lettreApres,lettreAvant):
        
        if lettreApres != self.lettresJumleesEntry2.get() and len(lettreApres) ==1 and lettreApres.isascii() and lettreApres.isupper():
            
            return True
        elif lettreApres == "" and lettreAvant.isalpha() and len(lettreAvant) == 1 and lettreAvant.isascii() and lettreAvant.isupper():
            
            return True
        else:
            return False 
        
    def listToWord(self,list):
        word = ""
        for i in range(len(list)):
            if list[i] != "" and list[i].isalpha() and len(list[i]) == 1 and list[i].isupper():
                word += list[i]
        return word
    
    def wordToList(self,word):
        list = []
        for i in range(len(word)):
            if word[i] != "" and word[i].isalpha() and len(word[i]) == 1 and word[i].isupper():
                list.append(word[i])
        return list

    def lettreJumleeSet(self):
        return self.lettresJumleesEntry1.get() != "" and self.lettresJumleesEntry2.get() != ""
    
    def actualiserMat(self):
        list = self.wordToList(self.keyEntry.get())
        for i in range(0,len(list)):
            self.entryList[i].insert(0,list[i])
    def actualiserKey(self):
        list =[]
        for entry in self.entryList:
            list.append(entry.get())
        word = self.listToWord(list)
        self.keyEntry.insert(0,word) 
    
    def lettreEnleveAjoute(self,ajoute,enleve):
        for c1,c2 in zip(ajoute,enleve):
            if c1 != c2:
                return c1
        return ""
    # def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
    #     button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
    #     button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
    #     button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
    #     button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
    #     button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
    #     return button  

    # def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
    #     button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    # def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
    #     button.configure(fg_color=fg_color, text_color=text_color)
    
    def clearButtonAction(self):
        if self.matriceFull:
            for entry in self.entryList:
                entry.configure(state="normal")
                entry.delete(0, "end")
                entry.configure(state="readonly")
            self.matriceFull = False
        self.keyEntry.delete(0,"end")
        self.lettresJumleesEntry1.delete(0,"end")
        self.lettresJumleesEntry2.delete(0,"end")
        self.lettresJumleesEntry1.focus_set()
    
    def fillButtonAction(self):
        if self.lettreJumleeSet():
            # Récupérer la clé entrée
            key = self.keyEntry.get()
            lJumle1 = self.lettresJumleesEntry1.get()
            lJumle2 = self.lettresJumleesEntry2.get()
            
            # Nettoyer tous les champs d'abord
            if self.matriceFull:
                for entry in self.entryList:
                    entry.configure(state="normal")
                    entry.delete(0, "end")
                    entry.configure(state="readonly")

            indEntry = 0

            # Remplir avec les lettres de la clé
            for k in key:
                if indEntry < len(self.entryList):
                    self.entryList[indEntry].configure(state="normal")
                    if k == lJumle1:
                        self.entryList[indEntry].insert(0, k+"/"+lJumle2)
                    else:
                        self.entryList[indEntry].insert(0, k)
                    self.entryList[indEntry].configure(state="readonly")
                    indEntry += 1

            # Compléter avec les lettres restantes
            for c in self.LETTRE_DE_ALPHABET:
                if c not in key:
                    if indEntry < len(self.entryList):                                             
                        if c != lJumle2:
                            self.entryList[indEntry].configure(state="normal")
                            if c == lJumle1:
                                self.entryList[indEntry].insert(0, lJumle1+"/"+lJumle2) 
                            else:                         
                                self.entryList[indEntry].insert(0, c)
                            self.entryList[indEntry].configure(state="readonly")
                            indEntry += 1
                        
            self.matriceFull = True

    def getValidateButton(self): 
        return self.validateButton    
    def getKeyEntry(self):
        return self.keyEntry, self.lettresJumleesEntry1, self.lettresJumleesEntry2

class defineAffineKeyFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x200")
        self.resizable(False, False)  
        self.main_frame = ctk.CTkFrame(self,fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        self.entryFrame = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR)
        self.entryFrame.pack(fill="x", expand=True)
        
        self.keyLabel = ctk.CTkLabel(self.entryFrame, text="Clé inversible mod 26 :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        self.keyEntry = ctk.CTkEntry(self.entryFrame, width=70,height=40,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key")
        self.decalageLabel = ctk.CTkLabel(self.entryFrame, text="Décalage :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        self.decalageEntry = ctk.CTkEntry(self.entryFrame, width=70,height=40,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key")

        self.configureGrid(self.entryFrame,lineWay=True,nbrLine=3,nbrCol=6,lineVal = 1,colVal = 1)
        self.keyLabel.grid_configure(column=1,row=1,padx=10,pady=20,sticky="e")
        self.keyEntry.grid_configure(column=2,row=1,padx=10,pady=20,sticky="w")
        self.decalageLabel.grid_configure(column=3,row=1,padx=10,pady=20,sticky="e")
        self.decalageEntry.grid_configure(column=4,row=1,padx=10,pady=20,sticky="w")

        self.buttonFrame = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR)
        self.buttonFrame.pack(fill="x",expand=True)
        self.configureGrid(self.buttonFrame,lineWay=True,nbrLine=3,nbrCol=3,lineVal=1,colVal=1)
        self.submitButton = self.createButton(self.buttonFrame,text="Valider",ligne=2,colonne=1,padx=0,pady=20)

        vcmd = (self.register(self.gestionDesEntry),'%P')
        self.decalageEntry.configure(validatecommand=vcmd)
        self.keyEntry.configure(validatecommand=vcmd)


    def gestionDesEntry(self,apres):        
        return apres.isdigit() and len(apres)<=3 or apres==""
                

    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1},nbrLine=0,nbrCol = 0,lineWay = False,lineVal = 0,colVal = 0):
        if not lineWay :
            for line,weight in dictR.items():
                pannel.grid_rowconfigure(line, weight=weight)
            for col,weight in dictC.items():
                pannel.grid_columnconfigure(col, weight=weight)
        else:
            for i in range(nbrLine):
                pannel.grid_rowconfigure(i, weight=lineVal)
            for i in range(nbrCol):
                pannel.grid_columnconfigure(i, weight=colVal)


    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)
        
class defineHillKeyFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)  
        self.main_frame = ctk.CTkFrame(self,fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)
        self.sizeMat = 3

        self.entryFrame = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR)
        self.entryFrame.pack(side="top",fill="x", expand=True)
        
        self.keyLabel = ctk.CTkLabel(self.entryFrame, text="Taille de la matrice :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        self.keyEntry = ctk.CTkEntry(self.entryFrame, width=70,height=40,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key")
        
        self.configureGrid(self.entryFrame,lineWay=True,nbrLine=3,nbrCol=6,lineVal = 1,colVal = 1)
        self.keyLabel.grid_configure(column=2,row=1,padx=10,pady=20,sticky="e")
        self.keyEntry.grid_configure(column=3,row=1,padx=10,pady=20,sticky="w")
        
        self.matrixFrame = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR)
        self.matrixFrame.pack(side="top",fill="x",expand=True)
        self.configureGrid(self.matrixFrame,lineWay=True,nbrLine=9+1,nbrCol=9+6,lineVal=1,colVal=1)

        self.entryList =[]     
        

        

        self.buttonFrame = ctk.CTkFrame(self.main_frame,fg_color=RIGHT_PANEL_BG_COLOR)
        self.buttonFrame.pack(side = "bottom",fill="x",expand=True)
        self.configureGrid(self.buttonFrame,lineWay=True,nbrLine=3,nbrCol=3,lineVal=1,colVal=1)
        self.submitButton = self.createButton(self.buttonFrame,text="Valider",ligne=2,colonne=1,padx=0,pady=20)

        self.vcmd = (self.register(self.gestionDesEntry),'%P')
        self.vcmd2 = (self.register(self.gestionDesMatEntry),'%P')
        self.keyEntry.configure(validatecommand=self.vcmd)




    def gestionDesEntry(self,apres):        
        if apres.isdigit() and len(apres)<=1 or apres=="":
            if apres=="":
                self.sizeMat = 0
            else:
                self.sizeMat = int(apres)
                self.creerMatrice()
            return True
        else:
            return False
    
    def gestionDesMatEntry(self,apres):        
        return apres.isdigit() and len(apres)<=2 or apres==""
        
    def creerMatrice(self):

        if len(self.entryList) != 0:
            for entry in self.entryList:
                entry.destroy()
            self.entryList = []
        colDeb = 6-(self.sizeMat-2)//2
        
        line = 0
        col = colDeb
        while line<self.sizeMat:
            self.Entry = ctk.CTkEntry(self.matrixFrame,width=35,height=35,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key",border_width=2,border_color="black")
            self.Entry.grid(row=line, column=col, pady=0 ,padx=(0,0), sticky="nesw") 
            self.Entry.configure(validatecommand=self.vcmd2)          

            self.entryList.append(self.Entry)

            col += 1
            if col-colDeb == self.sizeMat :
                line = line +1
                col = colDeb
        
                

    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1},nbrLine=0,nbrCol = 0,lineWay = False,lineVal = 0,colVal = 0):
        if not lineWay :
            for line,weight in dictR.items():
                pannel.grid_rowconfigure(line, weight=weight)
            for col,weight in dictC.items():
                pannel.grid_columnconfigure(col, weight=weight)
        else:
            for i in range(nbrLine):
                pannel.grid_rowconfigure(i, weight=lineVal)
            for i in range(nbrCol):
                pannel.grid_columnconfigure(i, weight=colVal)


    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)    
    
            

            
    

    




    



    
if __name__ == "__main__":
    app = definePolybePlayfairKeyFrame()
    #app = defineVigenereKeyFrame(600,250)
    app.mainloop()
