# Spec av P-uppgift

# Namn: Andreas Wrife
# Personnummer:990330-0938
# P-uppgift nr: 154
# Titel: Wumpus

from tkinter import *
from tkinter import messagebox
from roomclass import * #Local import
import random


#The class for the Tkinter GUI and the gameboard.
class Game_menUI():
##################################################################################################
                                    #   START MENU    #
##################################################################################################
    #The constructor imports all the values set at the bottom of the page.
    def __init__(self, master, rows, cols, arrows_left, shot, score, position_print):
        self.master = master                    #The master/root for tkinter
        self.rows = rows                        #Amount of rows
        self.cols = cols                        #Amount of columns
        self.rows_original = rows               #The original amounts of rows. changes when player press OKAY in options. Default is 10
        self.cols_original = cols               #The original amounts of columns. changes when player press OKAY in options. Default is 10
        self.arrows_left = arrows_left          #The number of arrows. Value set to 5.
        self.arrows_left_reset = self.arrows_left #If the player choose to play again. the number of arrows reset to the value which it started the program with.
        self.shot = shot                        #The number of shots for one arrowuse. Default is set to 3.
        self.AW_cheat = False                   #Cheats in the game.
        self.position_print = position_print    #CAN BE CHANGE HERE. IF YOU DONT WANT THE RANDOM ROOMS TO BE PRINTED.
        self.score = int(score)                 #The Score of the player. Default is 100.
        self.score_reset = int(score)           #When you reset the game. The score will return to what is was when the game started.
        self.master.title("World of Wumpus")
        self.master.geometry("960x510")
        self.master.minsize(width=900, height=400)
        self.start_menu(False)
      

    #The startmenu which allows the player to choose between Play, Tutorial, Options, Credits and Quit.
    #Displays the name of the game at the top.
    def start_menu(self, generate_again):
        #If the player returns from another window. Generate again will delete the previous window.  
        self.generate(generate_again)
        #Configures the weight of the rows and columns for the frames of the startmenu.
        self.master.grid_columnconfigure(0,weight=1)
        self.master.grid_columnconfigure(1,weight=1)
        self.master.grid_columnconfigure(2,weight=1)
        self.master.grid_rowconfigure(0,weight=1)
        self.master.grid_rowconfigure(1,weight=1)
        self.master.grid_rowconfigure(4,weight=0)
        self.master.grid_rowconfigure(5,weight=0)
        #Frame for all stuff on the startmenu.
        self.frame_master=Frame(self.master, bg="maroon")
        self.frame_master.grid(row=0, column=1, sticky=S)
        #Title label. WORLD OF WUMPUS. 
        self.master_label=Label(self.frame_master,relief=GROOVE, text="World of Wumpus", borderwidth=4,padx=20, pady= 15,font=("Times", 50, "bold"),fg="dimgrey")
        self.master_label.grid(row=0, column =1, pady= 5)
        #F
        self.frame_menu=Frame(self.master)
        self.frame_menu.grid(row=1, column=1)
        self.playb=Button(self.frame_menu, text="PLAY", font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=30, command=self.difficulty_menu)
        self.playb.grid(row=1, column=1)
        self.tutorialb=Button(self.frame_menu, text="TUTORIAL", font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=30, command=self.guide_tut)
        self.tutorialb.grid(row=2, column=1, pady= 5)
        self.quitb=Button(self.frame_menu, text="CREDITS", font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=30, command=self.credits)
        self.quitb.grid(row=3, column=1, pady= 5)
        self.opcd=Frame(self.frame_menu)
        self.opcd.grid(row=5,column=1)
        self.optionsb = Button(self.opcd, text="OPTIONS",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=14, padx=1,command=self.options)
        self.optionsb.grid(row=0, column=0, pady= 5, padx=2)
        self.creditb = Button(self.opcd, text="QUIT",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=15,padx=1, command=lambda:self.master.quit())
        self.creditb.grid(row=0,column=1, pady= 5, padx=2)

    #deletes the frames, labels and buttons from which the program came from.
    def generate(self,generate_again):
        if generate_again == "tutorial": #The player came from the tutorial.
            self.frame_tut.grid_forget()
            self.frame_tut_buttons.grid_forget()
            self.frame_master.grid_forget()
        if generate_again == "back_credits": #The player returned to the startmenu from the credits.
            self.frame_credit.grid_forget()
            self.frame_master.grid_forget()
        if generate_again == "back_options": #The user returned to the startmenu from "Options".
            self.frame_options.grid_forget()
            self.frame_master.grid_forget()
            self.rows_original = self.rows
            self.cols_original = self.cols
        #Play_again_death   =   The player came back to the startscreen from a victorius battle.
        #Play_again_victory =   The player came from the deathscreen, after the player lost the game.
        #quit_midgame       =   The player quit midgame, by using the quitbutton.
        if generate_again == "play_again_death" or generate_again == "play_again_victory" or generate_again == "quit_midgame": 
            self.frame_dirkeys.grid_forget()
            self.frame_action.grid_forget()
            self.shot=3
            self.score= self.score_reset
            self.frame_quit.grid_forget()
            self.arrows_left= self.arrows_left_reset
            self.textbox.grid_forget()
            self.frame_arrows_left.grid_forget()
            self.frame_grid.grid_forget()
            if generate_again == "play_again_death":
                self.frame_highscore.grid_forget()
                self.dead_frame.grid_forget()
            if generate_again == "play_again_victory":
                self.vict_frame.grid_forget()
                self.frame_score.grid_forget()
            if generate_again == "quit_midgame":  #If the user quits during the victory screen or the death screen. This will try to delete either of those.
                try:
                    self.frame_highscore.grid_forget()
                    self.frame_score.grid_forget()
                    self.vict_frame.grid_forget()
                except:
                    pass
                try:
                    self.dead_frame.grid_forget()
                    self.frame_highscore.grid_forget()
                except:
                    pass


##################################################################################################
                                #   TUTORIAL OF THE GAME    #
##################################################################################################

    def guide_tut(self):
        #Delete the frames from the startmenu.
        self.frame_menu.grid_forget()
        self.frame_master.grid_forget()
        #Configures the rows to fit with the textbox.
        self.master.grid_rowconfigure(0,weight=0)
        self.master.grid_rowconfigure(1,weight=1)
        self.master.grid_rowconfigure(2,weight=0)
        #Creates a frame to fill with the tutorial.
        self.frame_tut=Frame(self.master)
        self.frame_tut.grid(row=1, column=0, columnspan=3, rowspan=1) 
        #Creates a frame for the title of the game.
        self.frame_master=Frame(self.master)
        self.frame_master.grid(row=0, column=1)
        self.master_label=Label(self.frame_master, text="World of Wumpus",fg="dimgrey", padx=10, pady= 10, font=("Courier New", 20))
        self.master_label.grid(row=0, column =1)
        #Creates a frame to fill with the textbox, next and close buttons.
        self.tut_textbox=Text(self.frame_tut)
        self.tut_textbox.grid(row=0, column=0)
        self.frame_tut_buttons=Frame(self.master)
        self.frame_tut_buttons.grid(row=2, column=1)
        self.closeb=Button(self.frame_tut_buttons, text="CLOSE", font=("Courier New", 10,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=10, command=lambda:self.start_menu("tutorial"))
        self.closeb.grid(row=0, column=0, pady=5, padx=1)
        self.nextb=Button(self.frame_tut_buttons, text="NEXT",  font=("Courier New", 10,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=10)
        self.nextb.grid(row=0, column=1,pady=5, padx=1)  
        self.tutorial_guide(1)

    #Prints the input into the tutorial textbox.
    def tut_quote(self, entry):
        self.tut_textbox.insert(END, "\n"+entry)
        self.tut_textbox.see(END) 
        
    #Sends different texts depending on which page the user is on.
    def tutorial_guide(self, value):
        value= value+1
        self.nextb.configure(command=lambda:self.tutorial_guide(value))
        #Second page of the Tutorial. Dangers.
        if value > 1:
            self.tut_textbox.delete('1.0', END)
        #Forth page of the tutorial. Action buttons.
        if value == 4:
            self.tut_textbox.delete('1.0', END)
            self.frame_action= Frame(self.frame_tut)
            self.frame_action.grid(row=0, column=0, padx=50, pady=50, sticky=N+E)
            moveb = Button(self.frame_action,text="Move")
            shotb = Button(self.frame_action, text="Shoot")
            moveb.grid(row=1,column=0, ipadx=5, ipady=8,sticky=S)
            shotb.grid(row=1, column=1, ipadx=5, ipady=8,sticky=S) 
        #Fifth page of the tutorial. Direction Keys
        if value == 5:
            self.frame_action.grid_forget()
            self.frame_dirkeys= Frame(self.frame_tut)
            self.frame_dirkeys.grid(row=0, column=0, padx=70, pady=40, sticky=N+E)
            self.nrthb_tut=Button(self.frame_dirkeys,text=" ^ ",state=NORMAL, command=lambda:self.egg(1))
            self.nrthb_tut.grid(row=0,column=2, sticky=N+E+S+W)
            self.sothb_tut=Button(self.frame_dirkeys, text=" v ",state=NORMAL, command=self.fail_egg)
            self.sothb_tut.grid(row=2,column=2, sticky=N+E+S+W)
            self.westb_tut=Button(self.frame_dirkeys,text=" < ",state=NORMAL, command=self.fail_egg)
            self.westb_tut.grid(row=1,column=1, sticky=N+E+S+W)
            self.eastb_tut=Button(self.frame_dirkeys,text=" > ",state=NORMAL, command=self.fail_egg)
            self.eastb_tut.grid(row=1,column=3, sticky=N+E+S+W)
            self.entrb_tut=Button(self.frame_dirkeys, state=DISABLED)
            self.entrb_tut.grid(row=1, column=2, sticky=N+S+W+E)
        #Sixth page of the tutorial. Arrow indicators.
        if value == 6:
            self.frame_dirkeys.grid_forget()
            self.frame_arrows_left=Frame(self.frame_tut)
            self.frame_arrows_left.grid(row=0,column=0, padx=70, pady=40,sticky=N+E)
            self.a5 = Radiobutton(self.frame_arrows_left)
            self.a5.grid(row=0, column=1)
            a4 = Radiobutton(self.frame_arrows_left)
            a4.grid(row=0, column=2)
            a3 = Radiobutton(self.frame_arrows_left)
            a3.grid(row=0, column=3)
            a2 = Radiobutton(self.frame_arrows_left)
            a2.grid(row=0, column=4)
            a1 = Radiobutton(self.frame_arrows_left)
            a1.grid(row=0, column=5)
        #Seventh page of the tutorial. Wasted one arrow.
        if value == 7:
            self.a5.configure(state=DISABLED, disabledforeground="White")
        #Eighth page of the tutorial. Dangers nearby.
        if value == 8:
            self.nextb.grid_forget()
            self.frame_arrows_left.grid_forget()
            frame_warnings_hero = Frame(self.frame_tut)
            frame_warnings_hero.grid(row=0, column=0, padx=70, pady=40, sticky=N+E)
            b1 = Button(frame_warnings_hero, text="H",relief=SUNKEN, bg="grey", width = 3)
            b1.grid(row=0, column=0, ipady=4, ipadx=4, pady=2)
            b2 = Button(frame_warnings_hero, text="H",relief=SUNKEN, bg="purple1", width = 3)
            b2.grid(row=1, column=0, ipady=4, ipadx=4, pady=2)
            b4 = Button(frame_warnings_hero, text="H",relief=SUNKEN, bg="darkslategray", width = 3)
            b4.grid(row=3, column=0, ipady=4, ipadx=4, pady=2)
            b6 = Button(frame_warnings_hero, text="H",relief=SUNKEN, bg="maroon", width = 3)
            b6.grid(row=5, column=0, ipady=4, ipadx=4, pady=2)
        #Print the text for the tutorial page.
        self.tutorial_textprint(value)


    def tutorial_textprint(self, value):
        #Opens the textdocument for the text of the tutorial. 
        #Reads the line related to the tutorial page.
        guide_tut_file = open("handledning.txt","r")
        guide_tut = guide_tut_file.readlines()
        tut_list=[]
        paragraph_list =[]
        for line in guide_tut:
            if line == "\n":
                tut_list.append(paragraph_list)
                paragraph_list = []
            else:
                paragraph_list.append(line)
        for sentence in tut_list[value-1]:
            splitrow = sentence.strip().split("\n")
            a = ', '.join(splitrow)
            self.tut_quote(str(a))


##################################################################################################
                                    #   ?????    #
##################################################################################################

    #Easteregg. Minigame to enable the AW_cheats in the game.
    def egg(self, value):
        if value == 1:#UP
            self.nrthb_tut.configure(command=lambda:self.egg(2))
        if value == 2:#UP
            self.sothb_tut.configure(command=lambda:self.egg(3))
            self.nrthb_tut.configure(command=self.fail_egg)
        if value == 3:#DOWN
            self.sothb_tut.configure(command=lambda:self.egg(4))
        if value == 4:#DOWN
            self.westb_tut.configure(command=lambda:self.egg(5))
            self.sothb_tut.configure(command=self.fail_egg)
        if value == 5:#LEFT
            self.eastb_tut.configure(command=lambda:self.egg(6))
            self.westb_tut.configure(command=self.fail_egg)
        if value == 6:#RIGHT
            self.westb_tut.configure(command=lambda:self.egg(7))
            self.eastb_tut.configure(command=self.fail_egg)
        if value == 7:#LEFT
            self.eastb_tut.configure(command=lambda:self.egg(8))
            self.westb_tut.configure(command=self.fail_egg)
        if value == 8:#RIGHT
            self.eastb_tut.configure(command=self.fail_egg)
            self.AW_cheat=True
            self.tut_quote("Cheats Enabled")


    #If the player fails the minigame, the button resets to the first stage.
    def fail_egg(self):
    	self.nrthb_tut.configure(command=lambda:self.egg(1))
    	self.sothb_tut.configure(command=self.fail_egg)
    	self.westb_tut.configure(command=self.fail_egg)
    	self.eastb_tut.configure(command=self.fail_egg)


##################################################################################################
                                   #   OPTIONS MENU   #
##################################################################################################

    #Displays the optionsmenu.
    def options(self):
        self.quit=0
        #Deletes the menuframe.
        self.frame_menu.grid_forget()
        #Creates a frame for the optionmenu.
        self.frame_options = Frame(self.master)
        self.frame_options.grid(row=1, column=1)
        #Scrollsbars for rows and columns.
        self.scrlrowsb = Scale(self.frame_options, orient=HORIZONTAL, troughcolor="grey",from_=5, to=10, length=200, label="ROWS",font=("Courier New", 16,"bold"), borderwidth=5)
        self.scrlrowsb.grid(row=1, column=0)
        self.scrlcolsb = Scale(self.frame_options, orient=HORIZONTAL, troughcolor="grey",from_=5, to=10, length=200, label="COLUMNS",font=("Courier New", 16,"bold"), borderwidth=5)
        self.scrlcolsb.grid(row=2, column=0)  
        self.rows_label = Label(self.frame_options,relief=GROOVE, text="Note that if you set the values to something other than 10,\nYour score won't be saved.",font=("Courier New", 12,"bold"),bg="grey",fg="Ghostwhite")
        self.rows_label.grid(row=0, column=0, pady=5)   
        #Okay and close buttons. If the Okay button is pressed. The rows and/or the columns are set to the value which the scales are set to. 
        self.okcl_frame = Frame(self.frame_options)
        self.okcl_frame.grid(row=3, column=0)          
        self.close_label = Button(self.okcl_frame, text="CLOSE",font=("Courier New", 10,"bold"),bg="grey",fg="Ghostwhite",command=self.close)
        self.close_label.grid(row=0,column=0, pady=10, ipady=5, ipadx=10)
        self.okay_label = Button(self.okcl_frame, text="OKAY",font=("Courier New", 10,"bold"),bg="grey",fg="Ghostwhite", state=DISABLED,command=lambda:self.start_menu("back_options"))
        self.okay_label.grid(row=0, column=1, pady=10, ipady=5,ipadx=10)
        self.scrlcolsb.set(self.cols)
        self.scrlrowsb.set(self.rows)
        self.scrlrowsb.configure(command=self.rows_okay)
        self.scrlcolsb.configure(command=self.cols_okay)  
        #Displays rooms

    #Enables the Okay button if the rows are different than what is set. 
    def rows_okay(self, rows_value):
        self.rows = int(rows_value)
        if self.rows == self.rows_original and self.cols == self.cols_original:
            self.okay_label.configure(state=DISABLED)
        else:
            self.okay_label.configure(state=NORMAL)


    #Enables the Okay button if the columns are different than what is set. 
    def cols_okay(self, cols_value):
        self.cols = int(cols_value)
        if self.rows == self.rows_original and self.cols == self.cols_original:
            self.okay_label.configure(state=DISABLED)
        else:
            self.okay_label.configure(state=NORMAL)

    #Returns to the columns and rows to what it was before. 
    def close(self):
        self.cols=self.cols_original
        self.rows=self.rows_original
        self.start_menu("back_options")


##################################################################################################
                                    #   CREDITS MENU    #
##################################################################################################

    #Displays the credits wimdow.
    def credits(self):
        self.frame_menu.grid_forget()
        self.master.grid_rowconfigure(0,weight=0)
        self.frame_credit=Frame(self.master)
        self.frame_credit.grid(row=1, column=1)
        self.credit_label1 = Label(self.frame_credit,relief=GROOVE, text="Iza Hedlund\nReviewer and Backer",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=40,padx=1)
        self.credit_label1.grid(row=0, column=1)
        self.credit_label2 = Label(self.frame_credit,relief=GROOVE, text="Ted\nAdjunct",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=40,padx=1)
        self.credit_label2.grid(row=1, column=1, pady=10)
        self.credit_label2 = Label(self.frame_credit,relief=GROOVE, text="David Åstrand\nThe button_list helper",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=40,padx=1)
        self.credit_label2.grid(row=2, column=1, pady=10)
        self.credit_label2 = Label(self.frame_credit,relief=GROOVE, text="Andreas Wrife\nCreator",font=("Courier New", 16,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,width=40,padx=1)
        self.credit_label2.grid(row=3, column=1, pady=10)
        self.back_label = Button(self.frame_credit, pady=5,padx=20, text="Back", font=("Courier New",15,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3,command=lambda:self.start_menu("back_credits"))
        self.back_label.grid(row=4,column=1)


##################################################################################################
                                #   DIFFIUCUTLY SELECT MENU    #
##################################################################################################

    #If the player chooses the option "PLAY" from the startmenu the select difficulty menu is displayed. 
    #Here the player can select a difficulty (Easy, normal or hard).
    #When one is selected the SELECT key will become available for the player to click.
    #If this button is pressed the game will generate itself with the selected (Sunken) difficulty button.
    def difficulty_menu(self):
        self.frame_menu.grid_forget()
        self.frame_diff=Frame(self.master)
        self.frame_diff.grid(row=1, column=1)
        self.diff_label=Label(self.frame_diff, pady=10, text="Select Difficulty:", width =20, font=("Courier New", 15,"bold"),fg="grey",borderwidth=3)
        self.diff_label.grid(row=0, column=1)
        self.easyb=Button(self.frame_diff, text="EASY", width=20, font=("Courier New", 15,"bold"), bg="grey", fg="Ghostwhite",borderwidth=3, command=lambda:self.select_set("EASY", "1"))
        self.easyb.grid(row=1, column=1, pady= 3)
        self.normalb=Button(self.frame_diff, text="NORMAL", width=20, font=("Courier New", 15,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3, command=lambda:self.select_set("NORMAL","2"))
        self.normalb.grid(row=2, column=1, pady= 3)
        self.hardb=Button(self.frame_diff, text=" HARD ", width=20, font=("Courier New", 15,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3, command=lambda:self.select_set("HARD","3"))
        self.hardb.grid(row=3, column=1, pady= 3)
        self.selectb = Button(self.frame_diff, text="SELECT", state=DISABLED, width=20, font=("Courier New", 15,"bold"),bg="grey",fg="Ghostwhite",borderwidth=3)
        self.selectb.grid(row=4, column=1, pady= 3)

    #Raises the select button if any of the difficulty buttons are pressed.
    #Which allows the user to press it and select a difficulty.
    #Sets the selected difficultybutton to sunken and raises the others.
    def select_set(self, diff_name, diff_nr):
        self.selectb.configure(state=NORMAL, bg="maroon")
        if diff_name == "EASY":
            self.easyb.configure(relief=SUNKEN, state=DISABLED)
            self.normalb.configure(relief=RAISED, state=NORMAL)
            self.hardb.configure(relief=RAISED, state=NORMAL)
        if diff_name == "NORMAL":
            self.easyb.configure(relief=RAISED, state=NORMAL)
            self.normalb.configure(relief=SUNKEN, state=DISABLED)
            self.hardb.configure(relief=RAISED, state=NORMAL)
        if diff_name == "HARD":
            self.easyb.configure(relief=RAISED, state=NORMAL)
            self.normalb.configure(relief=RAISED, state=NORMAL)
            self.hardb.configure(relief=SUNKEN, state=DISABLED)   
        self.selectb.configure(command=lambda:self.game_ui(diff_name, diff_nr))


##################################################################################################
                                    #   GAME GUI    #
##################################################################################################
    #The game GUI.
    def game_ui(self, difficulty, difficulty_nr):
        self.difficulty_nr = int(difficulty_nr)
        self.difficulty = difficulty

        #Deletes the menuframe.
        self.frame_diff.grid_forget()
        self.frame_master.grid_forget()
        #Configures the weights of the columns and rows to fit the frame.
        self.master.grid_columnconfigure(0,weight=0)
        self.master.grid_columnconfigure(1,weight=1)
        self.master.grid_columnconfigure(2,weight=1)
        self.master.grid_columnconfigure(2,weight=0)
        self.master.grid_rowconfigure(0,weight=1)
        self.master.grid_rowconfigure(1,weight=1)
        self.master.grid_rowconfigure(2,weight=0)
        self.master.grid_rowconfigure(3,weight=0)
        self.master.grid_rowconfigure(4,weight=0)
        self.master.grid_rowconfigure(5,weight=0)

        #Frame and buttons for the direction-keys.
        self.frame_dirkeys= Frame(self.master)
        self.frame_dirkeys.grid(row=1, column=2, padx=10, pady=5, sticky=N)
        self.nrthb=Button(self.frame_dirkeys,text=" ^ ",bg="grey",fg="Ghostwhite",borderwidth=3,state=DISABLED)
        self.nrthb.grid(row=0,column=2, sticky=N+E+S+W)
        self.sothb=Button(self.frame_dirkeys, text=" v ",bg="grey",fg="Ghostwhite",borderwidth=3,state=DISABLED)
        self.sothb.grid(row=2,column=2, sticky=N+E+S+W)
        self.westb=Button(self.frame_dirkeys,text=" < ",bg="grey",fg="Ghostwhite",borderwidth=3,state=DISABLED)
        self.westb.grid(row=1,column=1, sticky=N+E+S+W)
        self.eastb=Button(self.frame_dirkeys,text=" > ",bg="grey",fg="Ghostwhite",borderwidth=3,state=DISABLED)
        self.eastb.grid(row=1,column=3, sticky=N+E+S+W)
        self.middb=Button(self.frame_dirkeys, state=DISABLED, bg="grey")
        self.middb.grid(row=1, column=2, sticky=N+S+W+E)

        #Textbox to display the warnings and accesiable rooms. 
        self.textbox=Text(self.master, bg ="White")
        self.textbox.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=N+S+W+E)

        #Arrow-radiobuttons to display how many arrows are left. 
        self.frame_arrows_left=Frame(self.master)
        self.frame_arrows_left.grid(row=3,column=2)
        self.arrows_left_radio_list = []
        for i in range(arrows_left):
            a = Radiobutton(self.frame_arrows_left)
            self.arrows_left_radio_list.append(a)
            self.arrows_left_radio_list[i].grid(row=0, column=arrows_left-i)

        #Display label for the highscore for the selected difficulty, aswell as the current playerscore.
        self.frame_highscore=Frame(self.master)
        self.frame_highscore.grid(row=3, column=1)
        self.highscore_label=Label(self.frame_highscore, text="Highscore:")
        self.highscore_label.grid(row=0, column=1, padx=20)
        self.score_label = Label(self.frame_highscore, text="Score:"+str(self.score))
        self.score_label.grid(row=0, column=2, padx=20)

        #If the player wants to quit in the middle of the game.
        self.frame_quit=Frame(self.master)
        self.frame_quit.grid(row=3,column=0, sticky=W)
        self.quit_button=Button(self.frame_quit, text="Quit",bg="grey",fg="Ghostwhite", command=self.quit_midgame)
        self.quit_button.grid(row=0, column=0, sticky=W, padx=1, pady=1)

        #Frame with action buttons (Move or shoot)
        self.frame_action= Frame(self.master)
        self.frame_action.grid(row=0, column=2, padx=20, pady=5, sticky=S)
        self.moveb = Button(self.frame_action,text="Move",bg="grey",fg="Ghostwhite",command = self.set_dirkeys_moving)
        self.shotb = Button(self.frame_action, text="Shoot",bg="grey",fg="Ghostwhite", command = self.set_dirkeys_shooting)
        self.moveb.grid(row=1,column=0,padx=5,ipadx=5, pady=8,ipady=8, sticky=S)
        self.shotb.grid(row=1, column=1,padx=5,ipadx=5, pady=8,ipady=8, sticky=S)

        self.gameboard()                    #Generates the gameboard.  
        self.open_score_file(difficulty)    #Open the scorefile and displays the current highscore for the selected difficulty.
        self.frame_grid = Frame(self.master) #Creats a frame for the gameboardgrid.
        self.frame_grid.grid(row = 0, column =0, rowspan=2, padx=10, pady=10, sticky =N)
        self.display_grid_buttons()         #Runs the function which creates the gridrooms (buttons)
        self.check_nearby()                 #Checks nearby rooms and print warnings within the textbox if wumpus/holes/bats are nearby.
        self.action_quote("\nDo you want to move or shoot with the bow?") #Prints said question in the textbox.
        if self.position_print == True:
            self.print_position()               #Prints the current room and nearby rooms.



    #Generates a list/grid with the rooms. 
    #Fills the frame_grid with the buttons.
    def display_grid_buttons(self):
        self.button_list = []
        self.frame_grid = Frame(self.master)
        self.frame_grid.grid(row = 0, column =0, rowspan=2, padx=10, pady=10, sticky =N)
        for i in range(self.rows):
            self.button_list.append([])
            for j in range(self.cols):

                if self.AW_cheat == True: #If cheats are turned on. This displays the board.
                    if self.grid[i][j].hero == True:
                        figure = "H"
                        colour_figure = "grey"
                    elif self.grid[i][j].wumpus == True:
                        figure = "W"
                        colour_figure = "maroon"
                    elif self.grid[i][j].hole == True:
                        figure = "O"
                        colour_figure = "darkslategray"
                    elif self.grid[i][j].bats == True:
                        figure = "^"
                        colour_figure = "purple1"
                    else:
                        figure = " "
                        colour_figure = "grey"
                    b = Button(self.frame_grid, text = figure, bg=colour_figure,fg="Ghostwhite", relief = SUNKEN, width = 3)

                else: #Otherwise only the hero's position is displayed.
                    b = Button(self.frame_grid, text=" ", width = 3,bg="grey", fg="Ghostwhite")
                    if self.grid[i][j].hero == True:
                        b.configure(relief = SUNKEN, text = "H")
                    else:
                        b.configure(text = " ")
                b.grid(row=i, column=j)
                self.button_list[i].append(b)

    #If the player selects the move action-button, the directionkeys are set to run the funtion "MOVE HERO".
    def set_dirkeys_moving(self):
        self.action_quote("Which direction? (N, S, W, E)")
        self.moveb.config(relief=SUNKEN, state=DISABLED)
        self.shotb.config(state=DISABLED)
        self.nrthb.config(relief=RAISED, state=NORMAL, command = lambda:self.move_hero("N"))
        self.sothb.config(relief=RAISED, state=NORMAL, comman = lambda:self.move_hero("S"))
        self.westb.config(relief=RAISED, state=NORMAL, comman = lambda:self.move_hero("W"))
        self.eastb.config(relief=RAISED, state=NORMAL, comman = lambda:self.move_hero("E"))

    #If the player selects the shoot action-button, the directionkeys are set to run the funtion "MOVE ARROW".
    def set_dirkeys_shooting(self):
        self.set_arrow_start()
        self.action_quote("The arrow leaves the first room: Which direction?")
        self.shotb.config(relief=SUNKEN, state=DISABLED)
        self.moveb.config(relief=RAISED, state=DISABLED)
        self.nrthb.config(relief=RAISED, state=NORMAL, command = lambda:self.move_arrow("N"))
        self.sothb.config(relief=RAISED, state=NORMAL, command = lambda:self.move_arrow("S"))
        self.westb.config(relief=RAISED, state=NORMAL, command = lambda:self.move_arrow("W"))
        self.eastb.config(relief=RAISED, state=NORMAL, command = lambda:self.move_arrow("E"))

    #Opens the scorefile and prints the current highscore on the selected difficulty.
    def open_score_file(self,difficulty):
        highscore = ["NON", -11000000, difficulty]
        file = open("highscore.txt", "r")
        scores = file.readlines()
        for score in scores:
            player_stats = score.strip().split("/")
            if player_stats[2] == difficulty and int(player_stats[1]) > int(highscore[1]):
                highscore = player_stats
        if highscore[1] == -11000000:
            self.action_quote("Noone has played on that difficulty yet!")
            self.highscore_label.config(text=str("Highscore: N/A"))
        else:
            self.action_quote(str("The highscore on "+ difficulty+" difficulty is "+ highscore[1]+" made by: "+highscore[0]))
            self.highscore_label.config(text=str("Highscore: "+highscore[0]+" "+highscore[1]))
        self.action_quote("You have five arrows. Good luck!")
          

    #The function which prints the input into the textbox during the game.
    #Prints the line of text at the bottom (END) of the texbox. This moves the older text upwards.
    def action_quote(self,entry):
        self.textbox.insert(END, "\n"+entry)
        self.textbox.see(END)

    #If the player wants to quit midgame and presses the button at the bottom of the page, a messagebox appers asking if the player is sure.
    def quit_midgame(self):
        quit_ok=messagebox.askokcancel("QUIT",message="Are you sure? Your score won't be saved.")
        if quit_ok == True:
            self.start_menu("quit_midgame")


##################################################################################################
                                #   END OF THE GAME    #
##################################################################################################
    #Disables the dirkeys and action buttons.
    #Creates a button which takes you back to the startscreen. Diplays "YOU DIED".
    def dead_buttons(self, dead_text):
        self.dead_frame = Frame(self.master)
        self.dead_frame.grid(row=0, column=1, rowspan=2)
        self.deadb = Button(self.dead_frame, text = dead_text, font=("Courier New", 20), bg="black", fg="White", borderwidth=5, command = lambda:self.start_menu("play_again_death"))
        self.deadb.grid(row=0, column=0, ipadx=50, ipady=30, sticky=N)
        self.shotb.config(relief=SUNKEN, state=DISABLED)
        self.nrthb.config(relief=SUNKEN, state=DISABLED)
        self.sothb.config(relief=SUNKEN, state=DISABLED)
        self.westb.config(relief=SUNKEN, state=DISABLED)
        self.eastb.config(relief=SUNKEN, state=DISABLED)

    #Displays the nameinput textbox
    #Displays the action-buttons and dirkeys.
    #Diplays the victory button
    def victory(self):
        self.button_list[self.x_wumpus][self.y_wumpus].configure(relief=SUNKEN, text="W")
        self.vict_frame = Frame(self.master)
        self.vict_frame.grid(row=0, column=1, rowspan=2)
        self.victb = Button(self.vict_frame, text = "YOU WON!", font=("Helvetica", 20), command=self.vict_color)
        self.victb.grid(row=1, column=0, ipadx=50, ipady=30, sticky=N)
        self.vict_color()
        self.shotb.config(relief=SUNKEN, state=DISABLED)
        self.nrthb.config(relief=SUNKEN, state=DISABLED)
        self.sothb.config(relief=SUNKEN, state=DISABLED)
        self.westb.config(relief=SUNKEN, state=DISABLED)
        self.eastb.config(relief=SUNKEN, state=DISABLED)
        self.frame_highscore.grid_forget()
        #Only if the columns and rows are set to 10 does the game save.
        if self.cols == 10 and self.rows == 10:
            self.frame_score=Frame(self.master)
            self.frame_score.grid(row=3, column=1)
            self.name_label=Label(self.frame_score, text="Please write your name (ie AWE):")
            self.name_label.grid(row=0, column=0)
            self.entry_string=StringVar()
            self.entry_string.trace("w", self.only_three_inputs)
            self.name_entry_box = Entry(self.frame_score, textvariable=self.entry_string)
            self.name_entry_box.grid(row=0, column=1)
            self.enterb = Button(self.frame_score, text = "ok", bg="grey", fg="Ghostwhite", command=self.save_highscore_file)
            self.enterb.grid(row=0, column = 2)

    #Only allows the player to input three characters into the entry bar.
    def only_three_inputs(self, *args):
        value = str(self.entry_string.get())
        if len(value) >3:
            self.entry_string.set(value[:3])

    #Opens the file colors.txt and puts the colours in a list.
    #Chooses one at random and displays the button with that colour
    def vict_color(self):
        file = open("colors.txt", "r")
        colours = file.readlines()
        colour_nr = random.randint(0,len(colours)-1)
        colour_name = colours[colour_nr].strip("\n")
        self.victb.configure(bg = colour_name,activebackground=colour_name )


    #Saves the score to the highscore.txt file. 
    def save_highscore_file(self):
        player_name= self.entry_string.get()
        player_name = str.upper(player_name)
        if len(player_name)<3:
            self.action_quote("Please write your name with three characters.")
        else:
            file = open("highscore.txt", "a")
            file.write(player_name +"/"+ str(self.score)+"/"+ str(self.difficulty) + "\n")
            file.close()
            self.start_menu("play_again_victory")


##################################################################################################
                                    #   GAMEBOARD    #
##################################################################################################


    #Function which generates the gameboard.
    def gameboard(self):
        #Generates a list with numbers depening on rows and columns.
        ROOM_list = random.sample(range(1,self.rows*self.cols+1),self.rows*self.cols)
        self.grid = []
        #Puts the numbers into lists within a list. Creates a grid depening on set rows and columns.
        gridlist = []
        i = 0
        for x in range(self.rows):
            self.grid.append([])
            gridlist.append([])
            for y in range(self.cols):
                gridlist[x].append(ROOM_list[i])
                self.grid[x].append(Room(ROOM_list[i]))
                i += 1
        #Sets the connections for every room, for all directions.
        for x in range(self.rows):
            for y in range(self.cols):
                con_north = self.accessible_rooms(x, y, -1, 0)
                xn, yn = con_north
                room_north = self.grid[xn][yn].room_nr

                con_south = self.accessible_rooms(x, y, 1, 0)
                xs, ys = con_south
                room_south = self.grid[xs][ys].room_nr

                con_west = self.accessible_rooms(x, y, 0, -1)
                xw, yw = con_west
                room_west = self.grid[xw][yw].room_nr
                con_east = self.accessible_rooms(x, y, 0, 1)
                xe, ye = con_east
                room_east = self.grid[xe][ye].room_nr
                self.grid[x][y].set_connections(room_north, room_south, room_west, room_east, con_north, con_south, con_west, con_east)

        #Set the hero position at the start of the game.
        self.set_hero_start(random.randint(0,self.rows-1), random.randint(0,self.cols-1))

        #Set Wumpus position at the start of the game.
        while True:
            try:
                self.set_wumpus_start(random.randint(0,self.rows-1), random.randint(0,self.cols-1))
                break
            except:
                ##print("You and Wumpus spawned in the same room!, dev-team will fix that for you!")
                continue

        #Set the bats' positions at the start of the game.
        amount_bats = round(min(self.rows*self.cols-4 , self.rows*self.cols*(self.difficulty_nr-1)*0.15))
        while amount_bats > 0:
            try:
                self.set_bats_start(random.randint(0,self.rows-1), random.randint(0,self.cols-1))
                amount_bats -= 1
            except:
                ##print("Wumpus dont like bats.")
                continue

        #Set the hole positions at the start of the game.
        amount_holes = round(min(self.rows*self.cols-4 , self.rows*self.cols*(self.difficulty_nr-1)*0.1))
        while amount_holes > 0:
            try:
                self.set_hole_start(random.randint(0,self.rows-1), random.randint(0,self.cols-1))
                amount_holes -= 1
            except:
                continue

    ########################### POSITIONAL METHODS ########################


    #The corner rooms needs to be associated with the room at the other end.
    #This function makes the association to that room, depening on if an element in the gridlist is nonexcistent
    def accessible_rooms(self, x, y, dirx, diry):
        xcord = x + dirx
        ycord = y + diry
        try:
            self.grid[xcord][ycord]
        except:
            if dirx == -1:
                xcord = self.rows-1
            if dirx == 1:
                xcord = 0
            if diry == -1:
                ycord = self.cols-1
            if diry == 1:
                ycord = 0        
        return  (xcord, ycord)  

    #Prints the position of the hero after the player has moved it.
    def print_position(self):
        s = "You are in room: "+ str(self.grid[self.x_hero][self.y_hero].room_nr)
        s += "\nFrom here you can access rooms: "
        s += str(self.grid[self.x_hero][self.y_hero].room_north) + " "# +"(" + str(self.grid[self.x_hero][self.y_hero].x_north) +","+str(self.grid[self.x_hero][self.y_hero].y_north)+ ")| "
        s += str(self.grid[self.x_hero][self.y_hero].room_south) + " "# +"(" + str(self.grid[self.x_hero][self.y_hero].x_south) +","+str(self.grid[self.x_hero][self.y_hero].y_south)+ ")| "
        s += str(self.grid[self.x_hero][self.y_hero].room_west)  + " "# +"(" + str(self.grid[self.x_hero][self.y_hero].x_west) +","+str(self.grid[self.x_hero][self.y_hero].y_west)+ ")| "
        s += str(self.grid[self.x_hero][self.y_hero].room_east)  + " "# +"(" + str(self.grid[self.x_hero][self.y_hero].x_east) +","+str(self.grid[self.x_hero][self.y_hero].y_east)+ ")| "
        self.action_quote(s)


    ########################### BATS ########################

    #Generates bats in random rooms. If the room if already full it tries again.
    def set_bats_start(self, x_bat, y_bat):
        if self.grid[x_bat][y_bat].box_full == True:
            raise ValueError
        else:
            self.grid[x_bat][y_bat].figure_position(flag_bats = True, box_full=True)

    #Function is run when the hero steps into a room full with bats.
    #It puts the hero down in a random room which is empty from creatures and holes.
    def fly_hero(self):
        while True:
            rndm_x = random.randint(0,self.rows-1)
            rndm_y = random.randint(0,self.cols-1)
            if self.grid[rndm_x][rndm_y].box_full == True:
                continue
            else:
                self.action_quote("\nYou feel batwings on your cheek and are lifted upwards")
                self.action_quote("After a short flight the bats drop you at in room: "+str(self.grid[rndm_x][rndm_y].room_nr))
                self.set_hero_new(rndm_x, rndm_y, delete_hero=False)
                break




    ########################### HOLES ########################

    #Sets the holes at the start of the game. 
    #The function wont create a hole at a position which makes the hero become surrounded in all 4 directions
    def set_hole_start(self, x_hole, y_hole):
        if self.grid[self.x_hero][self.y_hero].check_hero_surrounded(self.grid) == True:
            self.grid[x_hole][y_hole].figure_position() #Fills in the the hole if it is placed so that the hero is surrounded by holes.
            raise ValueError
        if self.grid[x_hole][y_hole].box_full == True: #If the room contains something already.
            raise ValueError
        else:
            self.grid[x_hole][y_hole].figure_position(flag_hole=True, box_full=True)





    ########################### WUMPUS ########################

    #Sets wumpus at the start of the game at a random position. This position can not be that of the position of the hero.
    def set_wumpus_start(self, x_wumpus, y_wumpus):
        if self.x_hero == x_wumpus and self.y_hero == y_wumpus:
            raise ValueError
        else:
            self.x_wumpus = x_wumpus
            self.y_wumpus = y_wumpus
            #print("Wumpus is alive at: "+ str(self.x_wumpus)+", "+ str(self.y_wumpus))
            self.grid[self.x_wumpus][self.y_wumpus].figure_position(flag_wumpus=True, box_full=True)

    #Checks if the hero is at a greater or lower x- and y-coordiate respectivly.
    #Depening on said difference, wumpus is moved in one direction so that the difference is made smaller.
    def move_wumpus(self):
        w_can_move_N, w_can_move_S, w_can_move_W, w_can_move_E = self.grid[self.x_wumpus][self.y_wumpus].check_rooms_for_wumpus(self.grid)
        x_difference_HW = self.x_hero - self.x_wumpus
        y_difference_HW = self.y_hero - self.y_wumpus

        while True:
            #Wumpus is at a greater x position, possible move direction in x = "N"
            if x_difference_HW < 0 and w_can_move_N == True:
                self.set_wumpus_new(self.grid[self.x_wumpus][self.y_wumpus].x_north , self.grid[self.x_wumpus][self.y_wumpus].y_north)
                #print("Wumpus moved")
                break

            #Hero is at a greater x position, possible move direction in x = "S"
            elif x_difference_HW > 0 and w_can_move_S == True:
                self.set_wumpus_new(self.grid[self.x_wumpus][self.y_wumpus].x_south , self.grid[self.x_wumpus][self.y_wumpus].y_south)
                #print("Wumpus moved")
                break

            #Wumpus is at a greater y position, possible move direction in y = "W"
            if y_difference_HW < 0 and w_can_move_W == True:
                self.set_wumpus_new(self.grid[self.x_wumpus][self.y_wumpus].x_west , self.grid[self.x_wumpus][self.y_wumpus].y_west)
                #print("Wumpus moved")
                break

            #Hero is at a greater y position, possible move direction in y = "E"
            elif y_difference_HW > 0 and w_can_move_E == True:
                self.set_wumpus_new(self.grid[self.x_wumpus][self.y_wumpus].x_east , self.grid[self.x_wumpus][self.y_wumpus].y_east)
                #print("Wumpus moved")
                break
            #print("WUMPUS DIDNT MOVE")
            break

    #Removes Wumpus from the old room and associates it with the new.
    def set_wumpus_new(self, x_new_move, y_new_move):
        self.grid[self.x_wumpus][self.y_wumpus].figure_position()#despawns wumpus from selected room
        self.grid[x_new_move][y_new_move].figure_position(flag_wumpus=True, box_full=True)
        if self.AW_cheat == True and self.difficulty_nr == 3:
            self.button_list[x_new_move][y_new_move].configure(text="W", bg="maroon")
            self.button_list[self.x_wumpus][self.y_wumpus].configure(text=" ", bg="grey")
        self.x_wumpus = x_new_move
        self.y_wumpus = y_new_move

    #Runs the room-object-method to check what's inside the nearby rooms of the hero
    def check_nearby(self):
        danger_nearby = self.grid[self.x_hero][self.y_hero].check_nearby_rooms(self.grid, self.textbox, self.position_print)
        self.button_list[self.x_hero][self.y_hero].configure(bg=danger_nearby)

        

    ########################### ARROW ########################

    #Sets the position of the arrow as the same as the hero's when the player selects to shoot with the bow.
    def set_arrow_start(self):
        self.x_arrow = self.x_hero
        self.y_arrow = self.y_hero
        self.hidden_box_full = True
    
    #Moves the arrow and checks if you've killed something.
    def move_arrow(self, direction):
        #Updates the score.
        if self.score > 0:
            self.score-=1
        self.score_label.configure(text = "Score:"+str(self.score))
        #Removes an indicator depending on how many arrows you got left.
        self.arrows_left_radio_list[self.arrows_left-1].configure(state=DISABLED, disabledforeground="White")
            #Moves the arrow in selected direction
        self.move_arrow_dir(direction)
        if self.shot == 3:#Three shots left
            self.shot-=1
            if self.killed_W == False:
                self.action_quote("The arrow leaves the second room: Which direction?")
        elif self.shot == 2:#Two shots left.
            self.shot-=1
            if self.killed_W == False:
                self.action_quote("The arrow leaves the third room: Which direction?")
        elif self.shot == 1:#One shots left. If the player has no arrows left. Game ends.
            self.arrows_left-=1
            if self.arrows_left==0:
                self.action_quote("You have run out off arrows, GAME OVER")
                self.dead_buttons("YOU RAN OUT OF ARROWS")  
            else:
                self.shotb.configure(relief=RAISED, state=NORMAL)
                self.moveb.configure(relief=RAISED, state=NORMAL)
                self.shot=3
                self.action_quote("\nDo you want to move or shoot with the bow?")

            self.nrthb.configure(state=DISABLED)
            self.sothb.configure(state=DISABLED)
            self.westb.configure(state=DISABLED)
            self.eastb.configure(state=DISABLED)

    #Moves the arrow in a selected direction 
    def move_arrow_dir(self, move_dir):
        if move_dir == "N":
            self.set_arrow_new(self.grid[self.x_arrow][self.y_arrow].x_north , self.grid[self.x_arrow][self.y_arrow].y_north, shot)
        if move_dir == "S":
            self.set_arrow_new(self.grid[self.x_arrow][self.y_arrow].x_south , self.grid[self.x_arrow][self.y_arrow].y_south, shot)
        if move_dir == "W":
            self.set_arrow_new(self.grid[self.x_arrow][self.y_arrow].x_west , self.grid[self.x_arrow][self.y_arrow].y_west, shot)
        if move_dir == "E":
            self.set_arrow_new(self.grid[self.x_arrow][self.y_arrow].x_east , self.grid[self.x_arrow][self.y_arrow].y_east, shot)

    #Removes the arrow from the old room and associates it with the new.
    def set_arrow_new(self, x_new_arrow, y_new_arrow, shot):
        self.killed_W= False
        self.grid[self.x_arrow][self.y_arrow].set_hidden_box(self.hidden_box_full)
        self.hidden_box_full = self.grid[x_new_arrow][y_new_arrow].box_full
        #When the amount of shots left are less than two the arrow will disappear from the current mark.
        if self.shot <= 2:
            self.button_list[self.x_arrow][self.y_arrow].configure(text=" ")
        self.x_arrow = x_new_arrow
        self.y_arrow = y_new_arrow
        self.button_list[self.x_arrow][self.y_arrow].configure(text="+") #Adds a display of the arrow.
        if self.shot == 1:
            self.button_list[self.x_arrow][self.y_arrow].configure(text=" ") #Removes the arrow at last shot.
        #Checks if the arrow killed the hero or Wumpus.
        check_value_arrow = self.check_after_shot()
        if check_value_arrow == "wumpus_death":
            self.action_quote("YOU KILLED WUMPUS")
            self.victory()
            self.killed_W = True
        if check_value_arrow == "hero_death":
            self.button_list[self.x_hero][self.y_hero].configure(text="X", fg="Red")
            self.dead_buttons("YOU SHOT YOURSELF")
            self.killed_W = True



    #Checks what's inside the room which the arrow was shot into.
    #Returns different values depening on if the room had wumpus, the hero or something else inside.
    def check_after_shot(self):
        if self.grid[self.x_arrow][self.y_arrow].wumpus == True:
            return "wumpus_death"
        elif self.grid[self.x_arrow][self.y_arrow].hero == True:
            return "hero_death"
        else:
            return None



    ########################### HERO ########################

    #Sets the x and y position of the hero at the start of the game.
    #After the grid have been constructed
    def set_hero_start(self,x_hero, y_hero):
        #print(x_hero, y_hero)
        self.grid[x_hero][y_hero].figure_position(flag_hero=True, box_full=True)
        self.x_hero = x_hero
        self.y_hero = y_hero


    #Depending on which direction the player wants to move the hero, a new room will be associated with the hero.
    def move_hero(self, move_dir):
        if self.score > 0:
            self.score -=1
            
        self.score_label.configure(text = "Score:"+str(self.score))
        self.shotb.config(relief=RAISED, state=NORMAL)

        if move_dir == "N":
            self.set_hero_new(self.grid[self.x_hero][self.y_hero].x_north , self.grid[self.x_hero][self.y_hero].y_north)
        if move_dir == "S":
            self.set_hero_new(self.grid[self.x_hero][self.y_hero].x_south , self.grid[self.x_hero][self.y_hero].y_south)
        if move_dir == "W":
            self.set_hero_new(self.grid[self.x_hero][self.y_hero].x_west , self.grid[self.x_hero][self.y_hero].y_west)
        if move_dir == "E":
            self.set_hero_new(self.grid[self.x_hero][self.y_hero].x_east , self.grid[self.x_hero][self.y_hero].y_east)

    #Runs both if the bats flys the hero away and when the player moves the hero.
    #Removes the hero from the old room and associates it with the new.
    def set_hero_new(self, x_new_move, y_new_move, delete_hero=True):
        if delete_hero == True:
            self.grid[self.x_hero][self.y_hero].figure_position()#REMOVES THE HERO FROM THE ROOM.
            self.button_list[self.x_hero][self.y_hero].configure(text = " ", bg="grey")
        self.x_hero = x_new_move
        self.y_hero = y_new_move
        if self.difficulty_nr == 3:
            self.move_wumpus()
        #Checks if the hero walked into a room with Wumpus, a hole or bats inside.
        check_value_hero = self.check_after_move()
        if check_value_hero == "died_from_wumpus":
            self.button_list[self.x_hero][self.y_hero].configure(text="X", bg="Red", relief=SUNKEN)
            self.dead_buttons("YOU DIED")
        elif check_value_hero == "died_from_falldmg":
            self.button_list[self.x_hero][self.y_hero].configure(text="⚫", fg="Black", bg="darkslategray", relief=SUNKEN)
            self.dead_buttons("YOU FELL")
        elif check_value_hero == "fly":
            self.button_list[x_new_move][y_new_move].configure(text="^", bg="purple1", relief=SUNKEN)
            self.fly_hero()
        else: #Otherwise the hero will be displayed in the new room.
            self.grid[self.x_hero][self.y_hero].figure_position(flag_hero = True, box_full = True)
            self.button_list[self.x_hero][self.y_hero].configure(relief = SUNKEN, text="H")
            self.check_nearby()
            if self.position_print == True:
                self.print_position()


    #Checks what's inside the room which the hero has gone into.
    #Death if the new room has a hole or wumpus inside.
    #Fly if the new room has bats.
    def check_after_move(self):
        if self.grid[self.x_hero][self.y_hero].wumpus == True:
            return "died_from_wumpus"
        elif self.grid[self.x_hero][self.y_hero].hole == True:
            return "died_from_falldmg"
        elif self.grid[self.x_hero][self.y_hero].bats == True:
            return "fly"


cols = 10               #defines the number of columns of the gameboard grid.
rows = 10               #defines the number of rows for the gameboard grid.
arrows_left = 5         #defines the number of arrows. Needs to be > 0.
shot = 3                #defines the number of shots for a single arrow. CAN'T BE CHANGED.
position_print = True   #defines if the position rooms should be printed.
score = 100             #defines the startscore. Between 0 and 100.
root = Tk()
root.grid()
Game_menUI(root, cols, rows, arrows_left, shot, score, position_print)
root.mainloop()         #The mainloop of the entire progam.
#END OF PROGRAM
