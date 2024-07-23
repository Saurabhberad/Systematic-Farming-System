
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image,ImageTk
from PIL import Image, ImageFilter
import csv
master =Tk()

w = Label(master, text="MAHARASHTRA CROP ANALYSIS1",fg="red",font=("Arial Bold", 40),
			 bg = "light green")
w.config(width='900',height='1')
w.place(x=60, y=40)

w.pack()

w=Label(master,text="SELECT DISTRICT",fg="blue",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=200)


variable5 = StringVar(master)

variable5.set("SELECT DISTRICT") # default value
w=OptionMenu(master,variable5,"ahmednagar","akola","amravati",
"aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane","wardha","washim","yavatmal")
w.pack() 
w.place(x=500,y=200)

def visualization5():
	districtName=variable5.get()
	print(districtName)
	import CPInYear as tmp
	tmp.main(districtName)
#__________________________________________________________

def link():
	def change_case(event=None):
		w=Label(master,text="This Graph Show's the Particular District Production in all years",fg="RED",font=("ROMAN",16),bg="pink")
		w.pack()
		w.place(x=300,y=430)
		g.plot()
		w.config(g)
	
	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w= Button(master, text = "!!! SHOW VISUALIZATION !!!",activeforeground = "BLUE",activebackground = "YELLOW",command=visualization5)  

	
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
