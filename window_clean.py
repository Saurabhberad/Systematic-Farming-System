
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


w=Label(master,text="!!!!!!!!!  DATA CLEAN SUCCESSFULLY !!!!!!!!!",fg="BLUE",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=350)



master.geometry('1500x1500')
master.configure(bg='pink')



def close_window(): 
	master.destroy()

def quit():

	btn = Button(master, text = "BACK",activeforeground = "RED",command=close_window)  

	btn.place(x=1000,y=650)  
quit()

mainloop()
