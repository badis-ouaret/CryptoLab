import customtkinter as ctk

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

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{FRAME_WIDTH}x{FRAME_HEIGHT}")

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
            ("Transposition", "Transpo")
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
            # Panel principal
        self.panelPrincipal = ctk.CTkFrame(self.right_panel)
        self.panelPrincipal.pack(side="bottom", fill="both", expand=True)
        self.update_panel_for_method()
        self.choixMethode.trace_add("write",self.update_panel_for_method)
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def update_panel_for_method(self, *args):
        
        # Effacer le contenu précédent du panel principal
        for widget in self.panelPrincipal.winfo_children():
            widget.destroy()
        if hasattr(self, "traceOperationId"):  # Vérifie qu'on a bien un trace enregistré
            self.choixOperation.trace_remove("write", self.traceOperationId)
            del self.traceOperationId



        self.choixOperation.set("Chiffrer")  # Réinitialiser le choix d'opération à "Chiffrer"

        # Créer un nouveau panneau selon la méthode choisie
        method = self.choixMethode.get()

        if method == "Cesar":
            self.createCesarPanel()
        elif method == "Vigenere":
            self.createVigenerePanel()
        elif method == "Playfair":
            self.createPlayfairPanel()
        elif method == "AmelioCesar":
            self.createAmelioCesarPanel()
        elif method == "Polybe":
            self.createPolybePanel()
        elif method == "Hill":
            self.createHillPanel()
        elif method == "Affine":
            self.createAffinePanel()
        elif method == "Transpo":
            self.createTranspoPanel()

    def update_panel_for_operation(self,label1,label2,buttonLabel,*args):
        label1.configure(text="Texte en clair" if self.choixOperation.get() == "Chiffrer" else "Texte chiffré")
        label2.configure(text="Texte chiffré" if self.choixOperation.get() == "Chiffrer" else "Texte en clair")
        buttonLabel.configure(text="Chiffrer" if self.choixOperation.get() == "Chiffrer" else "Déchiffrer")



    def createPanel(self):
        panel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="white")
        panel.pack(side="bottom",fill="both",expand=True)
        return panel
    def only_numbers(self,char):
        return char.isdigit()
    
    def only_alphabetic(self,char):
        return char.isalpha() and char.isascii()
    

    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1}):

        for line,weight in dictR.items():
            pannel.grid_rowconfigure(line, weight=weight)
        for col,weight in dictC.items():
            pannel.grid_columnconfigure(col, weight=weight)
        
    def createKeyEntry(self,pannel,ligne = 1,colonne = 2,validate = "key",vcmd = None,labelFont = RIGHT_PANEL_FONT,labelTextColor = RIGHT_PANEL_TEXT_COLOR ,entryFont = KEY_ENTRY_FONT,    entryTextColor = RIGHT_PANEL_TEXT_COLOR):
        cleLabel = ctk.CTkLabel(pannel, text="Clé", font=labelFont, text_color=labelTextColor)
        cleLabel.grid(row=ligne, column=colonne-1, pady=30, padx=(0, 10), sticky="e")

        cleEntry = ctk.CTkEntry(pannel, width=300,height=35,font=entryFont, text_color=entryTextColor ,validate = validate ,validatecommand=vcmd)
        cleEntry.grid(row=ligne, column=colonne, pady=30 ,padx=0, sticky="nesw")
    
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
        
        
    

    
   
    def createClassicCypherPannel(self,pannel,validate = "key",vcmd = None,title = "Chiffrement classique",labelFont = RIGHT_PANEL_FONT,labelTextColor = RIGHT_PANEL_TEXT_COLOR ,entryFont = KEY_ENTRY_FONT,    entryTextColor = RIGHT_PANEL_TEXT_COLOR): 
        titleFrame = ctk.CTkFrame(pannel.master,fg_color=pannel.cget("fg_color") ,corner_radius=0,height=100)
        titleFrame.pack(side="top",fill="x")
        titre = ctk.CTkLabel(titleFrame, text=title, font=RIGHT_PANEL_TITLE_FONT, text_color=RIGHT_PANEL_TITLE_COLOR)
        titre.pack(expand = True,anchor = 'center' ,pady=30)        
        
        self.configureGrid(pannel,dictC={0: 0, 1: 1, 2: 1, 3: 1})
        self.createKeyEntry(pannel,ligne = 1,colonne = 2,validate = validate,vcmd = vcmd)       


        textLabel = ctk.CTkLabel(pannel,text= "texte en clair",font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        textLabel.grid(row=2, column=1, pady=0, padx=(10,0), sticky="nesw")

        resultLabel = ctk.CTkLabel(pannel,text= "texte en clair",font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
        resultLabel.grid(row=2, column=3, pady=0, padx=(0, 10), sticky="nesw")
        
        textEntry = ctk.CTkTextbox(pannel, width=300,height=200,font=RIGHT_PANEL_FONT, text_color="black",wrap="word",activate_scrollbars=True,fg_color="white",border_width=3,border_color="black")
        textEntry.grid(row=3, column=0, pady=30, padx=(30, 0),columnspan=2, sticky="nesw")
        textEntry.focus_set()

        resultEntry = ctk.CTkTextbox(pannel, width=300,height=200,font=RIGHT_PANEL_FONT, text_color="black",wrap="word",activate_scrollbars=True,fg_color="white",border_width=3,border_color="black")
        resultEntry.grid(row=3, column=3, pady=30, padx=(0, 30),columnspan=2, sticky="nesw")
        resultEntry.configure(state="disabled")

        operationButton = self.createButton(pannel, text="Chiffrer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(20,10))
        clearButton = self.createButton(pannel, text="Effacer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",command=lambda: self.clearButtonAction(textEntry,resultEntry,cleEntry),ligne = 5,colonne = 2,padx=(0, 10),pady=(20,10))
        
        self.traceOperationId = self.choixOperation.trace_add("write", lambda *args: self.update_panel_for_operation(textLabel,resultLabel,operationButton))
        

    def createCesarPanel(self):
        cesarPanel = self.createPanel()
        self.createClassicCypherPannel(cesarPanel,title="Chiffrement de César",validate = "key",vcmd =(cesarPanel.register(self.only_numbers), "%S") )
    
    def createVigenerePanel(self):
        cesarPanel = self.createPanel()
        self.createClassicCypherPannel(cesarPanel,title="Chiffrement de Vigenère",validate = "key",vcmd =(cesarPanel.register(self.only_alphabetic), "%S") )
    
        
    def createPlayfairPanel(self):
        playfairPanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="green")
        playfairPanel.pack(side="top",fill="both",expand=True)
    def createAmelioCesarPanel(self):
        amelioCesarPanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="yellow")
        amelioCesarPanel.pack(side="top",fill="both",expand=True)
    def createPolybePanel(self):
        polybePanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="purple")
        polybePanel.pack(side="top",fill="both",expand=True)
    def createHillPanel(self):
        hillPanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="orange")
        hillPanel.pack(side="top",fill="both",expand=True)
    def createAffinePanel(self):
        affinePanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="red")
        affinePanel.pack(side="top",fill="both",expand=True)
    def createTranspoPanel(self):
        transpoPanel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="gray")
        transpoPanel.pack(side="top",fill="both",expand=True)

    
    def clearButtonAction(self,textEntry,resultEntry,cleEntry):
        textEntry.delete("0.0", "end")
        resultEntry.delete("0.0", "end")
        cleEntry.delete(0, "end")
        textEntry.focus_set()

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
    
    #=======================================================================

    #Methodes pannel des entrées et des boutons ==================================================

    
if __name__ == "__main__":
    app = Interface()
    app.mainloop()
