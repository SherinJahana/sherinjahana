
from tkinter import *

root=Tk()
root.geometry('500x520')

#file bar

menubar= Menu()
filemenu= Menu(menubar, tearoff=False)
menubar.add_cascade(label= "File",underline=0, menu= filemenu)
filemenu.add_command(label="New file", underline= 1)
filemenu.add_command(label="Open file", underline= 1)
filemenu.add_command(label="Save", underline= 1)
filemenu.add_command(label="Save as", underline= 1)
filemenu.add_command(label="Quit", underline= 1, command= exit, accelerator= "Ctrl+Q")
root.config(menu= menubar)
filemenu.bind_all("<Control-q>", exit)

#help bar

Helpmenu= Menu(menubar, tearoff=False)
menubar.add_cascade(label= "Help",underline=0, menu= Helpmenu)
Helpmenu.add_command(label="Get started", underline= 1)
Helpmenu.add_command(label="Keyboard shortcuts", underline= 1)
Helpmenu.add_command(label="View license", underline= 1)
Helpmenu.add_command(label="About", underline= 1)
root.config(menu= menubar)
self=Frame(root,bg="#EEF2E6",height="130",width="500")

hd=Label(self,text="General information",bd=3,bg="beige").place (x=10,y=10)

hd=Label(self,text="Name").place (x=80,y=60)
hd=Entry(self,bd=3,).place (x=120,y=60)
hd=Label(self,text="ID no").place (x=260,y=60)
hd=Entry(self,bd=3).place (x=300,y=60)
self.pack()

secframe=Frame(root,bg="#D6CDA4",height="130",width="500")
hd=Label(secframe,text="Selection",bg="beige").place (x=10,y=10)
hd=Checkbutton(secframe,text="ok bruh").place (x=50,y=60)
hd=Checkbutton(secframe,text="bye bruh").place (x=150,y=60)
hd=Checkbutton(secframe,text="thenks bruh").place (x=260,y=60)
hd=Checkbutton(secframe,text="go bruh").place (x=380,y=60)
secframe.pack()

thframe=Frame(root,bg="#EEF2E6",height="130",width="500")
hd=Label(thframe,text="Results",bg="beige").place (x=10,y=10)
Var1 = StringVar()
 
RBttn = Radiobutton(thframe, text = "Option1", variable = Var1,
                    value = 1).place(x=50,y=60)
RBttn2 = Radiobutton(thframe, text = "Option2", variable = Var1,
                     value = 2).place(x=150,y=60)
RBttn3 = Radiobutton(thframe, text = "Option3", variable = Var1,
                    value = 3).place(x=250,y=60)
RBttn4 = Radiobutton(thframe, text = "Option4", variable = Var1,
                     value = 4).place(x=350,y=60)
thframe.pack()

ftframe=Frame(root,bg="#D6CDA4",height="130",width="500")
hd=Label(ftframe,text="STATUS",bd=3,bg="beige").place (x=10,y=10)
text_box = Text(ftframe,
height=3,width=50,
    font=(12)).place(y=50,x=20)
sb = Scrollbar(
    ftframe,
    orient=VERTICAL
    ).pack(text_box)


ftframe.pack()

Button(root,text="click here").pack

root.mainloop()