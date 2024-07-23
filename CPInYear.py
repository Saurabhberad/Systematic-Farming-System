import matplotlib.pyplot as plt
import csv

def main(districtName):
	print("\n\nYEAR PRODUCTION DISTRICT\n")
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
	bar_no=[]
	districtList=[]
	production_total=[]
	districtLen=0
	set2=set([])
	set1=set([])

	file1=open("outmaha1.csv",'r') 
	data1=csv.reader(file1,delimiter=',')
	for row in data1:
		if(row[0]=='maharashtra'):
			set2.add(row[1])
		districtList=list(set2)
		districtLen=len(districtList)
	print('DISTRICTS \n')
	print('districtList:',','.join(districtList))
	#districtName=input('\nEnter a district :- ')
	#districtName=districtName.lower()
	file1.close()

	for i in range (0,districtLen):
		if(districtName ==districtList[i]):
			districtName=districtName+'.csv'
			file1=open(districtName,'r') 
			file2=open(districtName,'r')
			result_year=yearProductionCal(districtName,file2,file1)
			file1.close()
	return result_year


def yearProductionCal(districtName,file2,file1):
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
	bar_no=[]
	districtList=[]
	production_total=[]
	districtLen=0
	set2=set([])
	set1=set([])

	data=csv.reader(file1,delimiter=',')
	for row in data:
		if(row[2]=='1997'):	
			total[0]+=int(float(row[6]))
	
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

	print("\nSucessfuly Calculated....\n")
	for i in range (0,18):
		production_total.append(total[i])
		bar_no.append(i+1)
	maxt=max(production_total)
	print('\nMax_Production',maxt)
	
	year=''
	for i in range (0,18):
		if(maxt==total[i]):
			year=str(years[i])
		
	maxt=str(maxt)
	strTitle='YEARWISE TOTAL PRODUCTION\nMaximum Production Is '
	str2=' in year : '
	strTitle=strTitle+maxt+str2+year
	plt.bar(bar_no,production_total,color='r')
	plt.xticks(bar_no, years, rotation='vertical')
	plt.title(strTitle)
	plt.xlabel('Years')
	plt.ylabel('Production in Quintal')
	# plt.show()
	return [production_total,years,districtName,maxt,year]
	#print(production_total)
	#print(len(production_total))