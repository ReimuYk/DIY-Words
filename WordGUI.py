from string import *
import random
def handlerAdaptor(fun,**kwds):
    return lambda event,fun=fun,kwds=kwds: fun(event,**kwds)

from tkinter import *
root=Tk()

f=open('word.txt','r')
word=f.readlines()
f.close()

for i in range(len(word)):
    word[i]=word[i].split('|')

def highlight(label):
    label['font']=('黑体',10,'bold')

def select(event,th,co,bl):
    highlight(th)
    co['text']=bl

def randomWord():
    random.shuffle(word)
    return word[0:4]

def packWord(lst):
    l = Label(root,text=lst[0])
    l.pack()

def randomSol(lst):
    r = list(range(len(word)))
    random.shuffle(r)
    res={}
    for i in range(4):
        res[word[r[i]][2]]='n'
    res[lst[2]]='y'
    return res

def packSol(lst):
    d = randomSol(lst)
    sel = list(d)
    random.shuffle(sel)
    fm = Frame(root,width=600,height=20)
    co = Label(fm,text='',font=('黑体',10,'bold'))
    co.place(x=500,y=0)
    for i in range(5):
        t = str(i+1)+':'+sel[i]
        l = Label(fm,text=t)
        if d[sel[i]]=='y':
            l.bind("<Button-1>",handlerAdaptor(select,th=l,co=co,bl='√'))
        else:
            l.bind("<Button-1>",handlerAdaptor(select,th=l,co=co,bl='X'))
        l.place(x=100*i,y=0)
    fm.pack()

group = randomWord()
for item in group:
    packWord(item)
    packSol(item)



root.mainloop()
