# !/usr/bin/python3  
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image,ImageTk
from PIL import Image, ImageFilter
import csv

def visualization1(): 
	import DWTCProduction
	

'''
def visualization2():
	import ProductionOfPerticularCropinYears
	districtName=variable1.get()
	cropchoice=variable2.get()
	#file1=open("ProductionOfPerticularCropinYears.py",'r')		
print(districtName)
print(cropchoice)
'''	
	
	#ProductionOfPerticularCropinYears.compare_district(selected_district)
	
	#ProductionOfPerticularCropinYears.compare_district(selected_crop)
	
	#print ("crop is",selected_crop)
	#print ("district is",variable1.get())
def visualization2():
	districtName=variable1.get()
	cropchoice=variable2.get()
	
	print(districtName)
	print(cropchoice)
	
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
	bar_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	districtList=["outmaha1 ","ahmednagar","akola","amravati ","aurangabad ","beed","bhandara","buldhana","chandrapur ","dhule ","gadchiroli ","gondia ","hingoli ","jalgaon ","jalna ","kolhapur ","latur ","nagpur ","nanded ","nandurbar ","nashik ","osmanabad ","parbhani ","pune ","raigad ","ratnagiri ","sangli ","satara ","sindhudurg ","solapur ","thane ","wardha ","washim ","yavatmal "]
	production_total=[]
	print('DISTRICTS \n')
	print('districtList:',','.join(districtList))
	#districtName=input('Enter a district :- ')
	#districtName=districtName.lower()

############################## POPCIY ############################  Ahmednagar####################
	if(districtName == 'ahmednagar'):
		file1=open("ahmednagar.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show() 

	############################## POPCIY ############################  Akola#####################

	elif(districtName == 'akola'):
		file1=open("akola.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show() 

############################## POPCIY ############################  Amravati####################
	
	elif(districtName == 'amravati'):
		file1=open("amravati.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show() 
############################## POPCIY ############################  Ahurangabad####################

		
	elif(districtName == 'aurangabad'):
		file1=open("aurangabad.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show() 		

############################## POPCIY ############################  beed ####################
	elif(districtName == 'beed'):
		file1=open("beed.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show() 


############################## POPCIY ############################  bhandara ####################
	elif(districtName == 'bhandara'):
		file1=open("bhandara.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()

############################## POPCIY ############################  buldhana ####################
	elif(districtName == 'buldhana'):
		file1=open("buldhana.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()

############################## POPCIY ############################  chandrapur ####################
	elif(districtName == 'chandrapur'):
		file1=open("chandrapur.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ dhule ####################
	elif(districtName == 'dhule'):
		file1=open("dhule.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()

############################## POPCIY ############################  gadchiroli ####################
	elif(districtName == 'gadchiroli'):
		file1=open("gadchiroli.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ gondia ####################
	elif(districtName == 'gondia'):
		file1=open("gondia.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ hingoli ####################
	elif(districtName == 'hingoli'):
		file1=open("hingoli.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ jalgaon ####################
	elif(districtName == 'jalgaon'):
		file1=open("jalgaon.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  jalna ####################
	elif(districtName == 'jalna'):
		file1=open("jalna.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  latur ####################
	elif(districtName == 'latur'):
		file1=open("latur.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ nagpur ####################
	elif(districtName == 'nagpur'):
		file1=open("nagpur.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  nanded ####################
	elif(districtName == 'nanded'):
		file1=open("nanded.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ nandurbar ####################
	elif(districtName == 'nandurbar'):
		file1=open("nandurbar.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  nashik ####################
	elif(districtName == 'nashik'):
		file1=open("nashik.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  osmanabad ####################
	elif(districtName == 'osmanabad'):
		file1=open("osmanabad.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ parbhani ####################
	elif(districtName == 'parbhani'):
		file1=open("parbhani.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  pune ####################
	elif(districtName == 'pune'):
		file1=open("pune.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  raigad ####################
	elif(districtName == 'raigad'):
		file1=open("raigad.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  ratnagiri ####################
	elif(districtName == 'ratnarigri'):
		file1=open("ratnagiri.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  sangli ####################
	elif(districtName == 'sangli'):
		file1=open("sangli.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  satara ####################
	elif(districtName == 'satara'):
		file1=open("satara.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################ sindhudurg ####################
	elif(districtName == 'sindhudurg'):
		file1=open("sindhudurg.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  solapur ####################
	elif(districtName == 'solapur'):
		file1=open("solapur.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  thane ####################
	elif(districtName == 'thane'):
		file1=open("thane.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  wardha ####################
	elif(districtName == 'wardha'):
		file1=open("wardha.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  washim ####################
	elif(districtName == 'washim'):
		file1=open("washim.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  yavatmal ####################
	elif(districtName == 'yavatmal'):
		file1=open("yavatmal.csv",'r') 
		data=csv.reader(file1,delimiter=',')
		for row in data:
			if(row[4] == cropchoice):
				if(row[2]=='1997'):	
					total[0]=int(float(row[6]))			

				elif(row[2]=='1998'):	
					total[1]+=int(float(row[6]))
			
				elif(row[2]=='1999'):	
					total[2]+=int(float(row[6]))
			
				elif(row[2]=='2000'):	
					total[3]+=int(float(row[6]))
				
				elif(row[2]=='2001'):	
					total[4]+=int(float(row[6]))
			
				elif(row[2]=='2002'):	
					total[5]+=int(float(row[6]))
			
				elif(row[2]=='2003'):	
					total[6]+=int(float(row[6]))
			
				elif(row[2]=='2004'):	
					total[7]+=int(float(row[6]))

				elif(row[2]=='2005'):	
					total[8]+=int(float(row[6]))

				elif(row[2]=='2006'):	
					total[9]+=int(float(row[6]))

				elif(row[2]=='2007'):	
					total[10]+=int(float(row[6]))
		
				elif(row[2]=='2008'):	
					total[11]+=int(float(row[6]))

				elif(row[2]=='2009'):	
					total[12]+=int(float(row[6]))

				elif(row[2]=='2010'):	
					total[13]+=int(float(row[6]))

				elif(row[2]=='2011'):	
					total[14]+=int(float(row[6]))
			
				elif(row[2]=='2012'):	
					total[15]+=int(float(row[6]))

				elif(row[2]=='2013'):	
					total[16]+=int(float(row[6]))

				elif(row[2]=='2014'):	
					total[17]+=int(float(row[6]))

		print("Sucessfuly Calculated....")
		for i in range (0,18):
			production_total.append(total[i])
		maxt=max(production_total)
		mint=min(production_total)
		print('Max_Production',maxt)
		print('MIN_Production',mint)
		yearmx=''
		yearmn=''
		for i in range (0,18):
			if(maxt==total[i]):
				yearmx=str(years[i])
		for i in range(0,18):
			if(mint==total[i]):
				yearmn=str(years[i])
			
		maxt=str(maxt)
		mint=str(mint)
		strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2=' in year : '
		str3='\nMinimum Production is : '
		str4=districtName
		str5=cropchoice
		strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+str5
		plt.pie(production_total,labels=years,shadow=True,autopct='%1.1f%%')
		plt.title(strTitle)
		plt.show()
############################## POPCIY ############################  Ahmednagar####################

############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################
############################## POPCIY ############################  Ahmednagar####################




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------ G U I ----------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def close_window(): 
	master.destroy()



#import ProductionOfPerticularCropinYears

	
master =Tk()

scrollbar = Scrollbar(master)
scrollbar.pack( side = RIGHT, fill=Y )

#***************************************************************************************************************************

explanation = """At present, only GIF and PPM/PGM
exists to allow additional image file
formats to be added easily."""
w = Label(master, text="CROP ANLYASIS",fg="red",font=("Arial Bold", 40),
		 bg = "light green")
w.config(width='900',height='1')
w.place(x=60, y=40)

w.pack()

# photo = PhotoImage(file="sam1.png")
# w = Label(master, image=photo)
# w.photo = photo
w.pack(side=TOP,fill=BOTH,expand=TRUE)
w.place(x=300,y=70)

w=Label(master,text="DISTRICT WISE TOTAL CROP PRODUCTION",fg="blue",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=530)

w=Label(master,text="PRODUCTION OF A PERTICULAR CROP IN YEAR",fg="blue",font=("ROMAN",15),bg="pink")
w.pack()
w.place(x=300,y=570)

w=Label(master,text="Select District",fg="red",font=("ROMAN",13))
w.pack()
w.place(x=320,y=600)


w=Label(master,text="Select crop",fg="red",font=("ROMAN",13))
w.pack()
w.place(x=320,y=650)

w=Label(master,text="",fg="blue",font=("ROMAN",15))
w.pack()
w.place(x=300,y=200)

#*************************************************************************************************************
variable1 = StringVar(master)
variable1.set("SELECT DISTRICT") # default value


w = OptionMenu(master,variable1,"ahmednagar","akola","amravati","aurangabad","beed","bhandara","buldhana","chandrapur","dhule","gadchiroli","gondia","hingoli","jalgaon","jalna","kolhapur","latur","nagpur","nanded","nandurbar","nashik","osmanabad","parbhani","pune","raigad","ratnagiri","sangli","satara","sindhudurg","solapur","thane ","wardha ","washim ","yavatmal")

w.pack() 
#w.place(x=400,y=550)
w.place(x=450,y=600)



variable2 = StringVar(master)
variable2.set("SELECT CROP") # default value
#________________________________________________________________________________________________________

w = OptionMenu(master,variable2,"tur","bajra","gram","jowar","maize","moong","pulses total","ragi","rice","sugarcane","total foodgrain","urad","jowar","maize","other rabi pulses","wheat","maize","cotton","tur","bajra","castor seed","cotton","groundnut","jowar","maize","moong","niger seed","other cereals & millets","other kharif pulses"
"ragi","rice","sesamum","soyabean","sugarcane","sunflower","urad","gram","jowar","linseed","maize","other rabi pulses","other cereals","millets","rapeseed &mustard","safflower","sesamum","sunflower","wheat""groundnut","maize","sunflower","tur","bajra",
"castor seed","cotton","groundnut","jowar","maize","moong","niger seed")

w.pack() 
#w.place(x=400,y=550)
w.place(x=450,y=650)


master.geometry('300x200')
master.configure(bg='pink')
#w.pack()

#__________________________________________________________________________________________________________
btn = Button(master, text = "->",activebackground = "red",activeforeground = "blue",command=visualization1)  

btn.place(x=800,y=530)  
#btn.place(relheight=0.6)

btn = Button(master, text = "->",activebackground = "red",activeforeground = "blue",command=visualization2)  

btn.place(x=800,y=600)  

btn = Button(master, text = "QUIT",activebackground = "BLUE",activeforeground = "RED",command=close_window)  

btn.place(x=1000,y=650)  


#___________________________________________________________________________________________________
mainloop()













































































































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
'''
