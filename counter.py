# by https://www.facebook.com/UncleEngineer/

from tkinter import ttk
from tkinter import *


def countall():
	total = int(Res1.get()) + int(Res2.get())
	v_total.set('รวมคะแนนทั้งหมด: '+str(total))


def LungTu():

	old = int(Res1.get())
	new = old + 1
	Res1.set(new)
	countall()

def Tanatorn():
	old = int(Res2.get())
	new = old + 1
	Res2.set(new)
	countall()


def SetLung(event=None):

	def CountL(event=None):
		Res1.set(getlung.get())
		countall()
		Popup1.withdraw()




	Popup1 = Toplevel()
	Popup1.geometry('500x150')

	FP1 = Frame(Popup1)
	FP1.place(x=20,y=50)

	SL1 = ttk.Label(FP1,text='เซ็ตคะแนนให้ลุงตู่',font=('Angsana New',20),foreground='red')
	SL1.grid(row=0,column=0)

	getlung = StringVar()

	SE1 = ttk.Entry(FP1,textvariable=getlung,font=('Angsana New',20),foreground='red')
	SE1.grid(row=0,column=1)
	SE1.bind('<Return>',CountL)
	SE1.focus()

	SB1 = ttk.Button(FP1,text='Set Count',command=CountL)
	SB1.grid(row=0,column=2,ipadx=20,ipady=10)

	Popup1.mainloop()



def SetTanatorn(event=None):

	def CountL(event=None):
		Res2.set(gettanatorn.get())
		countall()
		Popup1.withdraw()



	Popup1 = Toplevel()
	Popup1.geometry('500x150')

	FP1 = Frame(Popup1)
	FP1.place(x=20,y=50)

	SL2 = ttk.Label(FP1,text='เซ็ตคะแนนให้ธนาธร',font=('Angsana New',20),foreground='green')
	SL2.grid(row=0,column=0)

	gettanatorn = StringVar()

	SE2 = ttk.Entry(FP1,textvariable=gettanatorn,font=('Angsana New',20),foreground='green')
	SE2.grid(row=0,column=1)
	SE2.bind('<Return>',CountL)
	SE2.focus()

	SB1 = ttk.Button(FP1,text='Set Count',command=CountL)
	SB1.grid(row=0,column=2,ipadx=20,ipady=10)

	Popup1.mainloop()


GUI = Tk()
GUI.title('Counter Candidate by Uncle Engineer')
GUI.geometry('700x250+50+50')

GUI.bind('<F2>',SetLung)
GUI.bind('<F3>',SetTanatorn)

v_total = StringVar()
v_total.set('รวมคะแนนทั้งหมด: '+'0')

LTotal = ttk.Label(GUI,textvariable=v_total,font=('Angsana New',30),foreground='blue')
LTotal.place(x=100,y=200)

SetLabel = ttk.Label(GUI,text='เซ็ตคะแนนให้ลุงตู่กดปุ่ม F2 เซ็ตคะแนนให้ธนาธรกดปุ่ม F3',font=('Angsana New',20))
SetLabel.place(x=100,y=15)


F1 = Frame(GUI)
F1.place(x=100,y=50)

L1 = ttk.Label(F1,text='ลุงตู่',font=('Angsana New',30),foreground='red')
L1.grid(row=0,column=0)

B1 = ttk.Button(F1,text='Lung Tu',command=LungTu)
B1.grid(row=0,column=1,ipadx=20,ipady=10)

Res1 = StringVar()
Res1.set('0')

LR1 = ttk.Label(F1,textvariable=Res1,font=('Angsana New',30),foreground='red')
LR1.grid(row=0,column=2,padx=50)

###############################

L1 = ttk.Label(F1,text='ธนาธร',font=('Angsana New',30),foreground='green')
L1.grid(row=1,column=0)

B2 = ttk.Button(F1,text='Tanatorn',command=Tanatorn)
B2.grid(row=1,column=1,ipadx=20,ipady=10)

Res2 = StringVar()
Res2.set('0')

LR2 = ttk.Label(F1,textvariable=Res2,font=('Angsana New',30),foreground='green')
LR2.grid(row=1,column=2,padx=50)


GUI.mainloop()