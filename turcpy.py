import matplotlib.pyplot as plt
import csv
total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
bar_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
districtList=["outmaha1 ","ahmednagar ","akola ","amravati ","aurangabad ","beed ","bhandara ","buldhana ","chandrapur ","dhule ","gadchiroli ","gondia ","hingoli ","jalgaon ","jalna ","kolhapur ","latur ","nagpur ","nanded ","nandurbar ","nashik ","osmanabad ","parbhani ","pune ","raigad ","ratnagiri ","sangli ","satara ","sindhudurg ","solapur ","thane ","wardha ","washim ","yavatmal "]

production_total=[]
print('DISTRICTS \n')
print('districtList:',','.join(districtList))
'''districtName=input('Enter a district :- ')
districtName=districtName.lower()
'''
cropchoice=input('Enter the crop name :')
cropchoice=cropchoice.lower()
data=csv.reader(file1,delimiter=',')
	
for row in data:
	
	if(row[4] == cropchoice):
		file2=open("outmaha1.csv",'r')
		total[0]+=int(float(row[6]))
		print(total)
		file2.close()
			
	
			
	
'''
file1=open("outmaha1.csv",'r') 
yearProductionCal()
file1.close()


file1=open("ahmednagar.csv",'r') 
yearProductionCal()
file1.close()

file1=open("akola.csv",'r') 
yearProductionCal()
file1.close()
print(production_total)

for i in range (0,18):
	production_total.append(total[i])

maxt=max(production_total)
print('Max_Production',maxt)
'''	
