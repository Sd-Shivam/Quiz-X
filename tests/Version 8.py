from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import time,os,ss,glob
from PIL import ImageTk

class Questions:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        #quiz= Questions(**data)
        

#def fileExplore():
   # filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select ShivamQuiz Quiz file",filetypes = (("ss files","*.ss"),("all files","*.*")))
    ##print (filename)
    #loadQuiz(filename)
    
#global Quiz
#data = {"meta":{"title":"Computer Quiz","author":"Joshua Boag","length":3},"questions":{"Q1":{"question":"How many Bits are in a Byte?","choices":["8 Bits","2 Bits","6 Bits","4 Bits"],"answer":1},"Q2":{"question":"Where many","choices":["1","2","three","4"],"answer":4},"Q3":{"question":"How much","choices":["one","2","3","4"],"answer":3}}}
#Quiz= Questions(**data)



class QuizGUI:
    def default(self):
        self.sidelist.selection_clear(0, END)
        self.sidelist.selection_set( first = 0 )
        self.titlevar.set(self.__quiz.questions["Q1"]['question'])
        self.choiceOneVar.set(self.__quiz.questions["Q1"]['choices'][0])
        self.choiceTwoVar.set(self.__quiz.questions["Q1"]['choices'][1])
        self.choiceThreeVar.set(self.__quiz.questions["Q1"]['choices'][2])
        self.choiceFourVar.set(self.__quiz.questions["Q1"]['choices'][3])
        self.__answersCorrect=[]
        for i in range(1,int(self.__quiz.meta['length'])+1):
            self.sidelist.itemconfig(i-1, {'fg': 'black'})
        self.questionsAnswered=[]
        self.displayQuesiton(self,1)

    def displayFrame(self):
        if self.itemsPacked == False:
            self.title = Label(self.master, text="ShivamQuiz", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
            self.title.pack(fill="x")
            self.mainarea = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
            self.mainarea.pack(expand=True, fill='both', side='right')

            self.errortitle = Label(self.mainarea, textvar=self.errortitlevar, bg="#F0F0F0", fg="red",font=('Helvetica Neue',12,"bold"),wraplength=700,pady=5)
            self.errortitle.grid(row=0,column=0,sticky="we",columnspan=4)


            maintitle = Label(self.mainarea, textvar=self.titlevar, bg="#F0F0F0", fg="black",font=('Helvetica Neue',18),wraplength=700,pady=5)
            maintitle.grid(row=1,column=0,sticky="we",columnspan=4)
            self.mainarea.grid_columnconfigure(0, weight=1)
            self.mainarea.grid_columnconfigure(1, weight=1)

            self.choiceFont = font.Font(family="Montserrat", size=24, weight='bold')
            self.choiceWidth= 350
            self.choiceHeight= 200
            self.choicePadX= 10
            self.choicePadY= 10

            self.choiceOne = Button(self.mainarea,textvar=self.choiceOneVar,relief="flat", bg="#c01733",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(1))
            self.choiceOne.config(image= self.choiceOneImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceOne.grid(row=2,column=0,sticky="W",padx=self.choicePadX, pady=30)

            self.choiceTwo = Button(self.mainarea,textvar=self.choiceTwoVar,relief="flat",  bg="#1368ce",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(2))
            self.choiceTwo.config(image= self.choiceTwoImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceTwo.grid(row=2,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.choiceThree = Button(self.mainarea, textvar=self.choiceThreeVar,relief="flat",  bg="#d89e00", fg="white",width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(3))
            self.choiceThree.config(image= self.choiceThreeImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceThree.grid(row=4,column=0,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.choiceFour = Button(self.mainarea,image=self.choiceFourImg, textvar=self.choiceFourVar,relief="flat", bg="#298f0d",fg="white", width=self.choiceWidth,height=self.choiceHeight, highlightcolor="red", font=self.choiceFont,command=lambda: self.answercheck(4))
            self.choiceFour.config(image= self.choiceFourImg, compound = LEFT,width=self.choiceWidth,height=self.choiceHeight,padx=10)
            self.choiceFour.grid(row=4,column=1,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.skip= Button(self.mainarea, text="Skip",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.skip)
            self.skip.grid(row=5,column=0,sticky="W",padx=self.choicePadX, pady=self.choicePadY)

            self.finish= Button(self.mainarea, text="Finish",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.quizComplete)
            self.finish.grid(row=5,column=1,sticky="E",padx=self.choicePadX, pady=self.choicePadY)
            self.itemsPacked= True
        else:
            pass

    def quizComplete(self):
        self.menubar.destroy()
        self.sidebar.pack_forget()
        self.scrollbar.pack_forget()
        self.mainarea.pack_forget()
        self.finishText= StringVar(self.master)
        finishTitle= Label(self.master, textvar=self.finishText, bg="#F0F0F0", fg="black",font=('Helvetica Neue',24),wraplength=700,pady=10)
        finishTitle.pack(fill='x')

        c_width = 600
        c_height = 340
        c_linewidth=4
        c_padY=c_width/10
        c_padX=c_width/10
        c_barwidth=c_width/3
        c = Canvas(self.master, width=c_width, height=c_height,bd=0)
        c.pack()
        print(self.__answersCorrect)
        correct= len(self.__answersCorrect)
        wrong=int(self.meta['meta']['length'])- correct

        graphY1=((c_height/(correct+wrong)))*correct
        graphY2=((c_height/(correct+wrong)))*wrong

        if len(self.questionsAnswered) == 0:
            print("No Questions Answered")
            self.finishText.set("Uhm, did you even try?!")
            graphY1= c_padX
            graphY2= c_padX
        elif len(self.__answersCorrect) == 0:
            self.finishText.set("Better Luck Nextime!")
            graphY1= c_padX
            graphY2= c_height-c_padX
        if len(self.__answersCorrect) == int(self.meta['meta']['length']):            
            print("None Wrong")
            self.finishText.set("Congratulations!")
            graphY1= c_height-c_padX
            graphY2= c_padX
        elif len(self.questionsAnswered) != 0:
            print("Normal")
            self.finishText.set("Well Done!")
        
        c.create_rectangle(c_padX, c_height-graphY1, c_barwidth+c_padX, c_height-c_padY, fill="green",outline="green")
        c.create_text(c_padX+(c_barwidth/2), c_height-graphY1-(c_padY/2), text="Correct: "+str(correct),font=('Helvetica Neue',16,"bold"))
        c.create_rectangle((c_padX*2)+c_barwidth, c_height-graphY2, c_barwidth*2+c_padX*2, c_height-c_padY, fill="red",outline="red")
        c.create_text((c_padX*2)+(c_barwidth*1.5), c_height-graphY2-(c_padY/2), text="Wrong: "+str(wrong),font=('Helvetica Neue',16,"bold"))
        c.create_line(0, c_height-c_padY, c_width, c_height-c_padY,width=4)

        self.resetHome= Button(self.master, text="Home",relief="flat", bg="#46178f", fg="white", width=10,height=2, highlightcolor="red", font=("Montserrat", '12','bold'),command=self.resetAll)
        self.resetHome.pack()

    def resetAll(self):
        self.itemsPacked= False
        self.preload()

    def clearFrame(self):
        self.itemsPacked= False
        self.mainarea.pack_forget()

    def clearMaster(self):
        self.homescreen.pack_forget()
    
    def __init__(self, master):
        # sidebar
        self.master=master
        self.home()

    def preload(self):
        self.sidebar = tk.Frame(self.master, width=200, bg='#F0F0F0', height=500, relief='sunken', borderwidth=0)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack( side = LEFT, fill = Y )
        self.sidelist = Listbox(self.sidebar,height=700,width=15,bg="#F0F0F0",fg="#757515",font=("Montserrat",16),selectmode="tk.BROWSE",activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.sidelist.pack(padx=5,pady=50)

        self.itemsPacked= False

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        fileMenu = Menu(self.menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Reset", command=self.default)
        fileMenu.add_command(label="Clear Frame", command=self.clearFrame)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        #Main content area
        self.titlevar= StringVar(self.master)
        self.errortitlevar= StringVar(self.master)
        self.choiceOneImg=PhotoImage(file="images/tri.png")
        self.choiceOneVar= StringVar(self.master)

        self.choiceTwoImg=PhotoImage(file="images/dia.png")
        self.choiceTwoVar= StringVar(self.master)
        self.choiceThreeImg=PhotoImage(file="images/cir.png")
        self.choiceThreeVar= StringVar(self.master)
        self.choiceFourImg=PhotoImage(file="images/squ.png")
        self.choiceFourVar= StringVar(self.master)
        for i in range(1,int(self.__quiz.meta['length'])+1):
            self.sidelist.insert(END,"Question "+str(i))
            self.sidelist.bind('<<ListboxSelect>>', self.select)
            self.sidelist.curselection()
        
        self.sidelist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.sidelist.yview)

    def home(self):
        self.homescreen = tk.Frame(self.master, background='#F0F0F0', width=500, height=500)
        self.homescreen.pack(expand=True, fill='both', side='right')
        self.homescreen.grid_columnconfigure(0, weight=1,uniform="yes")
        self.homescreen.grid_columnconfigure(1, weight=1,uniform="yes")
        self.homescreen.grid_columnconfigure(2, weight=1,uniform="yes")
        self.homescreen.grid_rowconfigure(1, weight=0,uniform="yes")
        self.homescreen.grid_rowconfigure(2, weight=2,uniform="yes")
        self.homescreen.grid_rowconfigure(3, weight=0,uniform="yes")
        self.homescreen.grid_rowconfigure(4, weight=1,uniform="yes")
        self.title = Label(self.homescreen, text="ShivamQuiz", bg="#46178f", fg="white",font=('Helvetica Neue',24,"bold"),wraplength=700,pady=5)
        self.title.grid(row=0,column=0,sticky="we",columnspan=3)

        self.selectedFileVar= StringVar(self.master)
        self.selectedFileVar.set("Select a Built-in Quiz or click 'Open' to Play your Own")
        self.selectedFile = Label(self.homescreen, textvar=self.selectedFileVar, bg="lightgrey", fg="Black",font=('Helvetica Neue',14,"normal"),wraplength=700,pady=10)
        self.selectedFile.grid(row=3,column=0,sticky="we",columnspan=3)

        self.browseQuiz = Listbox(self.homescreen,bg="lightgrey",fg="#757515",bd=1,height=2,font=("Montserrat",16),activestyle='none',borderwidth=0,relief="flat",highlightthickness=0)
        self.browseQuiz.grid(row=2, column=0, sticky="NWES",columnspan=3,padx=150,pady=10,rowspan=1)
        self.scrollbar = tk.Scrollbar(self.browseQuiz)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        self.metaVar= StringVar(self.master)
        self.meta = Label(self.homescreen, textvar=self.metaVar, bg="lightgrey", fg="Black",font=('Helvetica Neue',14,"normal"),wraplength=700,pady=10)
        self.meta.grid(row=1,column=0,sticky="we",columnspan=3)

        #for i in range(0,len(glob.glob1(os.getcwd(),"*.ss"))):
        #os.chdir(os.getcwd())
        for file in glob.glob("*.ss"):
            self.browseQuiz.insert(END,file.split(".")[0])
        self.browseQuiz.bind('<<ListboxSelect>>', self.selectQuiz)
        #self.sidelist.curselection()
        
        self.browseQuiz.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.browseQuiz.yview)

        self.buttonWidth=20
        self.buttonHeight=2
        self.buttonPadY=10
        self.buttonFont= font.Font(family="Montserrat", size=16, weight='bold')
        self.button1 = tk.Button(self.homescreen, text = 'Start',state=DISABLED, command = self.startQuiz,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button1.grid(row=4,column=0,pady=self.buttonPadY)
        self.button2 = tk.Button(self.homescreen, text = 'Open', command = self.fileExplore,relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button2.grid(row=4,column=1,pady=self.buttonPadY)
        self.button3 = tk.Button(self.homescreen, text = 'Create',relief="flat", bg="#c01733",fg="white",width=self.buttonWidth,height=self.buttonHeight,font=self.buttonFont)
        self.button3.grid(row=4,column=2,pady=self.buttonPadY)

    def select(self,other):
        a = int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        print("a=",a)
        self.displayQuesiton(self,a)

    def startQuiz(self):
        print(self.filename)
        self.__quiz= Questions(**(ss.load(open(self.filename))))
        self.browseQuiz.destroy()
        self.clearMaster()
        self.preload()
        #print(self.filename)
        self.displayFrame()
        self.default()

    def displayQuesiton(self,other=None,Qnum=None):
        print("Qnum ",Qnum)
        self.displayFrame()
        self.mainarea.configure(background='#F0F0F0')
        
        if self.isDisabled() == True:
            self.errortitlevar.set("You have already answered this Question!")
            self.choiceOne.configure(state=DISABLED)
            self.choiceTwo.configure(state=DISABLED)
            self.choiceThree.configure(state=DISABLED)
            self.choiceFour.configure(state=DISABLED)
        elif Qnum != None:
            self.errortitlevar.set("")
            self.choiceOne.configure(state=NORMAL)
            self.choiceTwo.configure(state=NORMAL)
            self.choiceThree.configure(state=NORMAL)
            self.choiceFour.configure(state=NORMAL)

        if Qnum == None:
            Qnum= self.getval()
        else:
            pass

        self.titlevar.set(self.__quiz.questions["Q"+str(Qnum)]['question'])
        self.choiceOneVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][0])
        self.choiceTwoVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][1])
        self.choiceThreeVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][2])
        self.choiceFourVar.set(self.__quiz.questions["Q"+str(Qnum)]['choices'][3])
    
    def onExit(self):
        self.master.quit()

    def debug(self):
        print("Debugging")

    def getval(self,other=None):
        try:
            return int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        except:
            print("Auto Question")
            

    def answercheck(self,choice):
        getquestionnum= int(str(self.sidelist.get(self.sidelist.curselection())).split(" ")[1])
        answer= self.__quiz.questions["Q"+str(getquestionnum)]['answer']
        if answer == choice:
            self.__answersCorrect.append(getquestionnum)
            print("Correct:",len(self.__answersCorrect))
            self.sidelist.itemconfig(getquestionnum-1, {'fg': '#66bf39'})
            self.mainarea.configure(background='#66bf39')
        else:
            print("Incorrect")
            self.sidelist.itemconfig(getquestionnum-1, {'fg': 'red'})
        self.disableQuestion()
        self.next()

    def isDisabled(self):
        if self.getval() in self.questionsAnswered:
            return True
        else:
            return False

    def disableQuestion(self):
        self.questionsAnswered.append(self.getval())
        self.displayQuesiton()

    def skip(self):
        if self.getval() == (int(self.__quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(self.__quiz.meta['length'])+1):
            if i not in self.questionsAnswered:
                if i == self.getval():
                    continue
                else:
                    print(i)
                    self.displayQuesiton(Qnum=i)
                    self.sidelist.selection_clear(0, END)
                    self.sidelist.selection_set( first = i-1 )
                    return
    def next(self):
        if len(self.questionsAnswered) == int(self.__quiz.meta['length']):
            self.quizComplete()
        if self.getval() == (int(self.__quiz.meta['length'])):
            start=1
        else:
            start=self.getval()
        for i in range(start,int(self.__quiz.meta['length'])+1):
            if i not in self.questionsAnswered:
                if i == self.getval():
                    continue
                else:
                    print(i)
                    self.sidelist.selection_set( first = i-1 )
                    self.displayQuesiton(Qnum=i)
                    self.sidelist.selection_clear(0, END)
                    self.sidelist.selection_set( first = i-1 )
                    return
    def selectQuiz(self,other):
        #print(self.filename)
        self.button1.config(state=NORMAL)
        try:
            self.filename=str(self.browseQuiz.get(self.browseQuiz.curselection())+".ss")
        except:
            pass
        
        self.meta= (ss.load(open(str(self.browseQuiz.get(self.browseQuiz.curselection())+".ss"))))
        self.metaVar.set("Made by: "+self.meta['meta']['author']+"\tQuestions: "+str(self.meta['meta']['length']))
        self.selectedFileVar.set("Selected: "+str(self.browseQuiz.get(self.browseQuiz.curselection())))


    def fileExplore(self):
        self.metaVar.set("")
        self.selectedFileVar.set("")
        self.browseQuiz.selection_clear(0,END)
        self.filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select ShivamQuiz Quiz file",filetypes = [("ShivamQuiz Quiz Files","*.ss")])
        if self.filename: # If correct fuke us sekected
            print("File Selected")
            self.meta= (ss.load(open(str(self.filename))))
            self.metaVar.set("Made by: "+self.meta['meta']['author']+"\tQuestions: "+str(self.meta['meta']['length']))
            self.selectedFileVar.set("Selected: "+str(self.filename))
            self.button1.config(state=NORMAL)
        else:
            print("No File Selected")
            self.button1.config(state=DISABLED)
            self.selectedFileVar.set("No File Selected! Try Again!")

def init():   
    root = Tk()
    root.minsize("1000","750")
    root.maxsize("1000","750")
    homescreen=QuizGUI(root)
    root.mainloop()

init()
