import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image,ImageTk
from PIL import Image, ImageFilter
import csv
master =Tk()

	
	


def visualization1(): 
	import DWTCProduction
	

def visualization2():
	districtName=variable1.get()
	cropchoice=variable2.get()

	import temp1 as tmp
	tmp.main(districtName,cropchoice)
	

def visualization3():
	import districtCropProductionArea

#&&&&&&&&&&&&&&&&&&& FUNCTION INSIDE SPECIFIC YEAR CROP PRODUCTION

def visualization4():
	districtName=variable3.get()
	yearChoice=variable4.get()
	import specificYearCropsProduction as tmp
	tmp.main(districtName,yearChoice)	

def visualization5():
	districtName=variable5.get()
	print(districtName)
	import CPInYear as tmp
	tmp.main(districtName)


def data_clean():
	import clean1
	w=Label(master,text="DATA CLEAN SUCCESFULLY !!! ",fg="RED",font=("ROMAN",8))
	w.pack()
	w.place(x=840,y=300)
	
	
	
	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------ G U I ----------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def close_window(): 
	master.destroy()



#import ProductionOfPerticularCropinYears

	

'''
scrollbar = Scrollbar(master)
scrollbar.pack( side = RIGHT, fill=Y )
'''
'''
w=Label(master,text="A).DISTRICT WISE TOTAL CROP\nBAHSUIEKOLG DRYU BGDR VGHT\n",fg="RED",font=("ITALIC",12),bg="pink")
w.pack()
w.place(x=10,y=500)
'''

#***************************************************************************************************************************


explanation = """At present, only GIF and PPM/PGM
exists to allow additional image file
formats to be added easily."""
def title():
	w = Label(master, text="MAHARASHTRA CROP ANALYSIS",fg="red",font=("Arial Bold", 40),
			 bg = "light green")
	w.config(width='900',height='1')
	w.place(x=60, y=40)

	w.pack()
'''
photo = PhotoImage(file="sam1.png")
w = Label(master, image=photo)
w.photo = photo
w.pack(side=TOP,fill=BOTH,expand=TRUE)
w.place(x=300,y=70)
'''
def DWTCP():
	def change_case(event=None):

		import window_DWTCP as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")
	w=Label(master,text="DISTRICT WISE TOTAL CROP PRODUCTION",fg="blue",font=("ROMAN",12),bg="pink")
	
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=300,y=520)	
	


	#btn = Button(master, text = "->",command=visualization1)  

	#btn.place(x=800,y=520)  
	#btn.place(relheight=0.6)
def POPCIY():
	def change_case(event=None):

		import window_POPCIY as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w=Label(master,text="PRODUCTION OF A PERTICULAR CROP IN YEAR",fg="blue",font=("ROMAN",12),bg="pink")
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.pack()
	w.place(x=300,y=560)

	
	'''variable1 = StringVar(master)
	variable1.set("SELECT DISTRICT") # default value


	w = OptionMenu(master,variable1,"ahmednagar","akola","amravati","aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane ","wardha ","washim ","yavatmal")

	w.pack() 
	#w.place(x=400,y=550)
	w.place(x=450,y=590)



	variable2 = StringVar(master)
	variable2.set("SELECT CROP") # default value
	#________________________________________________________________________________________________________

	w = OptionMenu(master,variable2,"tur","bajra","gram","jowar","maize","moong","pulses total","ragi","rice","sugarcane","total foodgrain","urad","jowar","maize","other rabi pulses","wheat","maize","cotton","tur","bajra","castor seed","cotton","groundnut","jowar","maize","moong","niger seed","other cereals & millets","other kharif pulses"
	"ragi","rice","sesamum","soyabean","sugarcane","sunflower","urad","gram","jowar","linseed","maize","other rabi pulses","other cereals","millets","rapeseed &mustard","safflower","sesamum","sunflower","wheat""groundnut","maize","sunflower","tur","bajra",
	"castor seed","cotton","groundnut","jowar","maize","moong","niger seed")

	w.pack() 
	#w.place(x=400,y=550)
	w.place(x=300,y=590)

		
	btn = Button(master, text = "->",command=visualization2)  

	btn.place(x=800,y=590)

'''

#______________________ districtCropProductionArea
def AADWCP():
	def change_case(event=None):

		import AADWCP_window as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")


	w=Label(master,text="AREA AND DISTRICT WISE CROP PRODUCTION",fg="blue",font=("ROMAN",12),bg="pink")
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=300,y=320)

	

	#btn = Button(master, text = "->",command=visualization3)  

	#btn.place(x=800,y=320) 
#---------------------- Clean
def clean():
	def change_case(event=None):

		import window_clean as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")


	w=Label(master,text="DATA CLEANING AND PRE-PROCESSING",fg="blue",font=("ROMAN",12),bg="pink")
	
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=300,y=280)	
	
	#btn = Button(master, text = "clean",command=data_clean)  

	#btn.place(x=800,y=280)


	


	 

#-------------------- Specifice YearCropProduction
def SYCP():
	
	def change_case(event=None):

		import window_SYCP as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w=Label(master,text="SPECIFIC YEAR CROP PRODUCTION",fg="blue",font=("ROMAN",12),bg="pink")

	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	
	w.pack()
	#----------------
	w.place(x=300,y=360)



	'''
	btn = Button(master, text = "->",command=visualization4)  

	btn.place(x=800,y=390) 
	variable3 = StringVar(master)
	variable3.set("SELECT DISTRICT") # default value


	w=OptionMenu(master,variable3,"ahmednagar","akola","amravati",
"aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane","wardha","washim","yavatmal")

	w.pack() 
	#w.place(x=400,y=550)
	w.place(x=300,y=385)
	#_______________________
	variable4 = StringVar(master)
	variable4.set("SELECT YEAR") # default value


	w=OptionMenu(master,variable4,"1997","1998","1999","2000","2001","2002",
"2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")

	w.pack() 

	w.place(x=500,y=385)'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ YEAR PRODUCTION DISTRICT
def CPIEY():
	def change_case(event=None):

		import window_CPIEY as c
		w.config(c)

	def red_text(event=None):

		w.config(fg="red")

	def black_text(event=None):
	
		w.config(fg="black")

	w=Label(master,text="CROP PRODUCTION IN EACH YEAR",fg="blue",font=("ROMAN",12),bg="pink")
	w.bind("<Button-1>",change_case)
	
	w.bind("<Enter>",red_text)
	w.bind("<Leave>",black_text)
	w.pack()
	w.place(x=300,y=430)
	'''variable5 = StringVar(master)

	variable5.set("SELECT DISTRICT") # default value
	w=OptionMenu(master,variable5,"ahmednagar","akola","amravati",
"aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane","wardha","washim","yavatmal")
	w.pack() 
	w.place(x=300,y=460)

	btn = Button(master, text = "->",command=visualization5)  

	btn.place(x=800,y=460)  

'''
#*************************************************************************************************************
def geometry():

	master.geometry('1500x1500')
	master.configure(bg='pink')
#w.pack()

#__________________________________________________________________________________________________________

def quit():

	btn = Button(master, text = "QUIT",activeforeground = "RED",command=close_window)  

	btn.place(x=1000,y=650)


#___________________________________________________________________________________________________













































































































'''
from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    print ("value is:" + variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
print(dict(comboExample)) 
comboExample.grid(column=0, row=1)
comboExample.current(1)

#print(comboExample.current(), comboExample.get())

app.mainloop()

from tkinter import *  
root = Tk()  
root.geometry("200x200")  
      
def open():  
	top = Toplevel(root)  
	top.mainloop()  
      
btn = Button(root, text = "open", command = open)  
btn.place(x=75,y=50)  
root.mainloop()  
'''



''' 
from tkinter import *  
  
top = Tk()  
  
top.geometry("200x250")  
  
menubutton = Menubutton(top, text = "Language", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
  
menubutton.pack()  
  
top.mainloop() 
from tkinter import *



top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
top.mainloop()
'''# !/usr/bin/python3  



#w = Label(master,text="CROP ANALYSIS", width=300, height=60,x=600,y=300)
#w.pack()

#***************************************************************************************************************************


#root = tk.Tk()
#logo = master.PhotoImage(file="sam2.png")














































































