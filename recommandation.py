import matplotlib.pyplot as plt
import csv

print(' \n     PRODUCTION OF PERICULAR CROP IN YEARS\n')
total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
bar_no=[]
bar_no2=[]
districtList=[]
production_total=[]
production_total1=[]
districtLen=0
set2=set([])
set1=set([])
cropList=[]

file1=open("outmaha1.csv",'r') 
data1=csv.reader(file1,delimiter=',')
for row in data1:
	if(row[0]=='maharashtra'):
		set2.add(row[1])
	districtList=list(set2)
	districtLen=len(districtList)
print('DISTRICTS \n')
print('districtList:',','.join(districtList))
districtName=input('\nEnter a district :- ')
districtName=districtName.lower()
file1.close()
def yearProductionCal():
	cnt=0
	data1=csv.reader(file2,delimiter=',')
	for row in data1:
		set1.add(row[4])
	cropList=list(set1)
	print('\ncropList     :\n',','.join(cropList))
	print("Total Crops :", len(cropList))
	cropchoice=input('\nEnter the crop name 1:')
	cropchoice=cropchoice.lower()
	cropchoice1=input('\nEnter the crop name 2 :')
	cropchoice1=cropchoice1.lower()
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

		if(row[4] == cropchoice1):
			if(row[2]=='1997'):	
				total1[0]=int(float(row[6]))			

			elif(row[2]=='1998'):	
				total1[1]+=int(float(row[6]))
		
			elif(row[2]=='1999'):	
				total1[2]+=int(float(row[6]))
		
			elif(row[2]=='2000'):	
				total1[3]+=int(float(row[6]))
			
			elif(row[2]=='2001'):	
				total1[4]+=int(float(row[6]))
		
			elif(row[2]=='2002'):	
				total1[5]+=int(float(row[6]))
		
			elif(row[2]=='2003'):	
				total1[6]+=int(float(row[6]))
		
			elif(row[2]=='2004'):	
				total1[7]+=int(float(row[6]))

			elif(row[2]=='2005'):	
				total1[8]+=int(float(row[6]))

			elif(row[2]=='2006'):	
				total1[9]+=int(float(row[6]))

			elif(row[2]=='2007'):	
				total1[10]+=int(float(row[6]))
	
			elif(row[2]=='2008'):	
				total1[11]+=int(float(row[6]))

			elif(row[2]=='2009'):	
				total1[12]+=int(float(row[6]))

			elif(row[2]=='2010'):	
				total1[13]+=int(float(row[6]))

			elif(row[2]=='2011'):	
				total1[14]+=int(float(row[6]))
		
			elif(row[2]=='2012'):	
				total1[15]+=int(float(row[6]))

			elif(row[2]=='2013'):	
				total1[16]+=int(float(row[6]))

			elif(row[2]=='2014'):	
				total1[17]+=int(float(row[6]))
	
	print("Sucessfuly Calculated....")
	
	
	j=1
	k=0	
	for i in range (0,18):
		production_total.append(total[i])
		bar_no.append(k)
		k=k+2
		production_total1.append(total1[i])
		bar_no2.append(j)
		j=j+2
	print(bar_no)
	print(bar_no2)	
	
	print("Total Pie :",len(bar_no))
	maxt1=max(production_total)
	maxt2=max(production_total1)
	if maxt1<maxt2:
		maxt=maxt2
	else:
		maxt=maxt1
	mint1=min(production_total)
	mint2=min(production_total1)
	if mint1<mint2:
		mint=mint2
	else:
		mint=mint1
	
	if(maxt==maxt1):
		cropMaxName=cropchoice
	else:
		cropMaxName=cropchoice1
		
	
	
		
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
	str4='\nOUR SYSTEM RECOMMEND YOU :'
	strTitle=strTitle+maxt+str2+yearmx+str3+mint+str2+yearmn+str4+cropMaxName
		
	
	plt.bar(bar_no,production_total)
	plt.bar(bar_no2,production_total1)
	plt.xticks(bar_no, years, rotation='vertical')
	plt.title(strTitle)
	plt.xlabel('categories')
	plt.ylabel('values')
	plt.show() 
	
	 
	#print(production_total)
	#print(len(production_total))

for i in range (0,districtLen):
	if(districtName ==districtList[i]):
		districtName=districtName+'.csv'
		file1=open(districtName,'r') 
		file2=open(districtName,'r')
		yearProductionCal()
		file1.close()





