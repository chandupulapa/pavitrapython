from tkinter import *
mw = Tk()
#mw.iconbitmap("images/mario.ico")
mw.title("project4 ")

mylable1 = Label(mw,text="vidyavaradhi",font=("Arial",18),fg='red')
mylable3 = Label(mw,text="i love python",font=("Arial",18),fg='blue')

mybutton=Button(mw,text='click me!',font=('Arial',20),fg='white',bg='#024cf7')
mylable1.grid(row=0,column=0)
mylable3.grid(row=0,column=2)
mybutton.grid(row=2,column=1,pady=20)



mw.mainloop()  # app created