
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image,ImageTk
from PIL import Image, ImageFilter
import csv
master =Tk()

w = Label(master, text="MAHARASHTRA CROP ANALYSIS",fg="red",font=("Arial Bold", 40),
			 bg = "light green")
w.config(width='900',height='1')
w.place(x=60, y=40)

w.pack()

#___________________________________________________

w=Label(master,text="SELECT DISTRICT",fg="blue",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=200)
	
 
variable3 = StringVar(master)
variable3.set("SELECT DISTRICT") # default value


w=OptionMenu(master,variable3,"ahmednagar","akola","amravati",
"aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane","wardha","washim","yavatmal")

w.pack() 
	#w.place(x=400,y=550)
w.place(x=500,y=200)
#_______________________________________________________


w=Label(master,text="SELECT YEAR",fg="blue",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=300)


variable4 = StringVar(master)
variable4.set("SELECT YEAR") # default value


w=OptionMenu(master,variable4,"1997","1998","1999","2000","2001","2002",
"2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")

w.pack() 

w.place(x=500,y=300)

def visualization4():
	districtName=variable3.get()
	yearChoice=variable4.get()
	import specificYearCropsProduction as tmp
	tmp.main(districtName,yearChoice)
#__________________________________________________________

def link():
	def change_case(event=None):
		w=Label(master,text="This Graph Show's the Maximum and minimum production of crops\nOf a Particular District",fg="RED",font=("ROMAN",16),bg="pink")
		w.pack()
		w.place(x=300,y=430)
		g.plot()
		w.config(g)
	
	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w= Button(master, text = "!!! SHOW VISUALIZATION !!!",activeforeground = "BLUE",activebackground = "YELLOW",command=visualization4)  

	
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=500,y=390)
link()






























master.geometry('1500x1500')
master.configure(bg='pink')



def close_window(): 
	master.destroy()

def quit():

	btn = Button(master, text = "BACK",activeforeground = "RED",command=close_window)  

	btn.place(x=1000,y=650)  
quit()

mainloop()
