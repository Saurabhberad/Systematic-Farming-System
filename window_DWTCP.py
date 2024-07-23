
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



def link():
	def change_case(event=None):
		w=Label(master,text="This Graph Show's the District name which having \nmaximum crop production including all years",fg="blue",font=("ROMAN",15),bg="pink")
		w.pack()
		w.place(x=300,y=530)
		import DWTCProduction  as c
		w.config(c)
	
	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w=Label(master,text="(click here) !! SEE  THE VISUALIZATION OF DISTRICT WISE TOTAL CROP PRODUCTION",fg="blue",font=("ROMAN",14),bg="pink")

	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=300,y=320)

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
