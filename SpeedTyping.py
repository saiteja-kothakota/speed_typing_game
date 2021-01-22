from tkinter import *
import random
from tkinter import messagebox

def clock():
    global time,score,miss
    if(time>0):
        time-=1
        timeleftLabel.configure(text='{} Sec'.format(time))
        timeleftLabel.after(1000,clock)
    else:
        hintLabel.configure(text='TOTAL SCORE: {} / {}'.format(score,score+miss))
        rr=messagebox.askyesno('Time Up','Wanna Try Again.?')
        if(rr):
            score=0
            miss=0
            time=60
            hintLabel.configure(text='')
            timeleftLabel.configure(text='{} Sec'.format(time))
            scorecardLabel.configure(text=score)
            inputbox.configure(text='')
            wordLabel.configure(text=words[0])
        else:
            global root
            root.quit()

def startGame(event):
    global score,miss
    if(time==60):
        clock()
    hintLabel.configure(text='')
    if(inputbox.get()==wordLabel['text']):
        score+=1
        scorecardLabel.configure(text=score)
    else:
        miss+=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    inputbox.delete(0,END)


######################################## ROOT METHOD

root = Tk()
root.title("Speed Typing Game")
root.geometry('800x600+250+80')
root.configure(bg='light blue')

######################################## Variables

score=0
miss=0
time=60
words=['abundance', 'abundant', 'accomplished', 'admire', 'adore', 'adorable', 'adventure', 'affectation', 'agape', 'alive', 'aloha', 'altruistic', 'amazing', 'angel', 'angelic', 'apologize', 'appreciate', 'beacon', 'beam', 'beautiful', 'beauty', 'befriend', 'begin', 'behold', 'being', 'bejewel', 'believe', 'belong', 'beloved', 'calm', 'camaraderie', 'capable', 'carefree', 'careful', 'caretaker', 'catnap', 'celebrate', 'celebration', 'centered', 'change', 'chant', 'charitable', 'charming', 'chat', 'cheer', 'cheerful', 'cheery', 'cherish', 'chirpy', 'clarity', 'clean', 'clear', 'dance', 'darling', 'dazzle', 'dear', 'delight', 'delightful', 'deserve', 'deserving', 'devoted', 'dignity', 'discover', 'divine', 'do', 'donate', 'doting', 'dream', 'elegant', 'embark', 'embrace', 'emotion', 'empathetic', 'empathize', 'empathy', 'empower', 'empowered', 'empowering', 'enchanted', 'enchanting', 'encourage', 'encouraged', 'encouraging', 'endearing', 'endeavor', 'energetic', 'energize', 'genius', 'genuine', 'gift', 'gifted', 'give', 'glad', 'gladness', 'glamorous', 'glee', 'gleeful', 'glory', 'glowing', 'goal', 'good', 'goodwill', 'gorgeous', 'grace', 'graceful', 'grateful', 'great', 'gregarious', 'groovy', 'grow', 'happy', 'harmonious', 'haven', 'heal', 'healed', 'healing', 'health', 'healthy', 'heart', 'illuminate', 'immaculate', 'imagine', 'imaginative', 'improve', 'include', 'inclusive', 'individual', 'infinite', 'innocence', 'innocent', 'inspiration', 'joke', 'jolly', 'jovial', 'joy', 'joyful', 'jubilant']
random.shuffle(words)

######################################## Creating Labels

headingLabel=Label(root,text='Welcome to Speed Typing Game.!',font=('Tempus Sans ITC',25,'italic bold'),bg='light blue',fg='dark red')
headingLabel.place(x=100,y=20)

wordLabel=Label(root,text=words[0],font=('Lucida',30),bg='light blue',fg='dark blue')
wordLabel.place(x=320,y=300)

scoreLabel=Label(root,text='Your Score:',font=('Lucida  Handwriting',15,'italic bold'),bg='light blue',fg='black')
scoreLabel.place(x=50,y=150)

scorecardLabel=Label(root,text=score,font=('Lucida',20,'italic bold'),bg='light blue',fg='green')
scorecardLabel.place(x=50,y=200)

timerLabel=Label(root,text='Time Left:',font=('Lucida',15,'italic bold'),bg='light blue',fg='black')
timerLabel.place(x=630,y=150)

timeleftLabel=Label(root,text='{} Sec'.format(time),font=('Lcuida',20,'italic bold'),bg='light blue',fg='red')
timeleftLabel.place(x=630,y=200)

hintLabel=Label(root,text='Type word and Hit ENTER',font=('Lcuida',20,'italic bold'),bg='light blue',fg='grey')
hintLabel.place(x=215,y=400)

######################################## Input 

inputbox=Entry(root,font=('arial',20,'italic'),bd=5,justify='center')
inputbox.place(x=230,y=360)
inputbox.focus_set()

root.bind('<Return>',startGame)

root.mainloop()