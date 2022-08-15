# https://www.aparat.com/akradi/playlists
#import

from random import choice
from tkinter import *

#var & list

functionha=['python',"list","dict","set","tuple","print","input",'for','while','if','else','elif','and','in','not','range','exit','break','continue','type','import','is','def','from','int','str','float','False','True','len','remove','class','var','randint','random','turtle']
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
randfank=choice(functionha)
jakhali=[]

#set win

win=Tk()
win.geometry("1000x600")
win.configure(bg="#cc99ff")
win.title("game")

#for

for ja in range(len(randfank)):
    jakhali.append("_")

#tozih

hello=Label(win,text="hello",font=("","30"),bg="#99ccff",fg="#660066").pack()
fasele1=Label(win,font=("","1"),bg="#cc99ff").pack()
jadval=Label(win,text="a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8,i:9,j:10,k:11,L:12,m:13,n:14,o:15,P:16,Q:17,r:18,s:19,t:20,u:21,v:22,w:23,x:24,y:25,z:26",bg='#99ccff',fg='#660066',font=("","10")).pack()

#chand

fasele2=Label(win,font=("","1"),bg="#cc99ff").pack()
chand=Label(win,text=jakhali,font=("","15"),fg="#660066",bg="#99ccff")
chand.pack()

#textbox

fasele3=Label(win,font=("","1"),bg="#cc99ff").pack()
txt=Entry(win,width=20)
txt.pack()
txt.config(bg="#99ccff")
txt.config(fg="#660066")

#fonc

def getme ():
    shomare=0
    harf=txt.get()
    harf=list1[int(harf)-1]
    for torf in randfank:
        shomare+=1
        if harf==torf:
            jakhali[shomare-1]=harf
            chand.config(text=jakhali)
    
#btn

fasele4=Label(win,font=("","1"),bg="#cc99ff").pack()
btn=Button(win,text="enter",font=("",15),command=getme)
btn.pack()
btn.config(bg="#99ccff")
btn.config(fg="#660066")

#mainloop

win.mainloop()
