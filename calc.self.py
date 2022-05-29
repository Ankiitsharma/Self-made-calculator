from tkinter import Tk,Button,Label

root = Tk()

root.title("My Self Calculator")

exp=""
def calc(data):
    global exp
    if(exp=="0"):
        exp=data
    else:
        exp=exp+data
    op.config(text=exp[-20:])
def solution(event=None):
    global exp
    try:
        exp=str(eval(exp))
    
        op.config(text=exp[-20:])
    except:
        op.config(text="Invalid Expression")
def clear():
    global exp
    exp=""
    op.config(text="Output Screen @Ankiit...")

def back(event=None):
    global exp
    exp=exp[:-1]
    op.config(text=exp)


def sqrt():
    try:
        global exp
        exp=str(float(exp)**0.5)
        op.config(text=exp)
    except:
        op.config(text="Invalid Expression")



op=Label(root,text="Output Screen",font=("impact",30))

b0=Button(root,text="0",height=1,width=7,
          font=("impact",30),command=lambda:calc("0"))
b1=Button(root,text="1",height=1,width=7,
          font=("impact",30),command=lambda:calc("1"))
b2=Button(root,text="2",height=1,width=7,
          font=("impact",30),command=lambda:calc("2"))
b3=Button(root,text="3",height=1,width=7,
          font=("impact",30),command=lambda:calc("3"))
b4=Button(root,text="4",height=1,width=7,
          font=("impact",30),command=lambda:calc("4"))
b5=Button(root,text="5",height=1,width=7,
          font=("impact",30),command=lambda:calc("5"))
b6=Button(root,text="6",height=1,width=7,
          font=("impact",30),command=lambda:calc("6"))
b7=Button(root,text="7",height=1,width=7,
          font=("impact",30),command=lambda:calc("7"))
b8=Button(root,text="8",height=1,width=7,
          font=("impact",30),command=lambda:calc("8"))
b9=Button(root,text="9",height=1,width=7,
          font=("impact",30),command=lambda:calc("9"))



bAdd=Button(root,text="+",height=1,width=7,
          font=("impact",30),command=lambda:calc("+"))
bSub=Button(root,text="-",height=1,width=7,
          font=("impact",30),command=lambda:calc("-"))
bMul=Button(root,text="*",height=1,width=7,
          font=("impact",30),command=lambda:calc("*"))
bDiv=Button(root,text="/",height=1,width=7,
          font=("impact",30),command=lambda:calc("/"))

bMod=Button(root,text="%",height=1,width=7,
          font=("impact",30),command=lambda:calc("%"))
bDot=Button(root,text=".",height=1,width=7,
          font=("impact",30),command=lambda:calc("."))

bEqual=Button(root,text="=",height=1,width=7,
          font=("impact",30),command=solution)

bClear=Button(root,text="C",height=1,width=7,
          font=("impact",30),command=clear)

bBack=Button(root,text="B",height=1,width=7,
          font=("impact",30),command=back)

bSqrt=Button(root,text="SQ",height=1,width=7,
          font=("impact",30),command=sqrt)


op.grid(row=0,column=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
bAdd.grid(row=1,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bSub.grid(row=2,column=3)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
bMul.grid(row=3,column=3)

bBack.grid(row=4,column=0)
b0.grid(row=4,column=1)
bDot.grid(row=4,column=2)
bDiv.grid(row=4,column=3)


bClear.grid(row=5,column=0)
bEqual.grid(row=5,column=1)
bSqrt.grid(row=5,column=2)
bMod.grid(row=5,column=3)




def eventcalculator(event):
    key=event.char
    if (key>="0" and key<="9" or key=="+" or key=="-" or key =="*" or key=="/" or key =="%" or key=="."):
        calc(key)
    elif (key=="="):
        solution()
        
    


root.bind("<Key>",eventcalculator)
root.bind("<Return>",solution)
root.bind("<BackSpace>",back)

root.mainloop() 
