import matplotlib.pyplot as plt
import csv
def main(districtName,cropchoice):
	print(' \n     PRODUCTION OF PERICULAR CROP IN YEARS\n')
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	flag=0
	flag2=1
	years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
	bar_no=[]
	districtList=[]
	production_total=[]
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
#	districtName=input('\nEnter a district :- ')
#	districtName=districtName.lower()
	file1.close()

	
	for i in range (0,districtLen):
		if(districtName ==districtList[i]):
			districtName=districtName+'.csv'
			file1=open(districtName,'r') 
			file2=open(districtName,'r')
			result_list=yearProductionCal(districtName,cropchoice,file1,file2)
			file1.close()
	return result_list

def yearProductionCal(districtName,cropchoice,file1,file2):
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	years=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
	bar_no=[]
	districtList=[]
	production_total=[]
	districtLen=0
	set2=set([])
	set1=set([])
	cropList=[]
	cnt=0
	data1=csv.reader(file2,delimiter=',')
	for row in data1:
		set1.add(row[4])
	cropList=list(set1)
	print('\ncropList     :\n',','.join(cropList))
	print("Total Crops :", len(cropList))
	#cropchoice=input('\nEnter the crop name :')
	#cropchoice=cropchoice.lower()
	data=csv.reader(file1,delimiter=',')
	for row in data:
		if(row[4] == cropchoice):
			flag=1
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


	if flag==1:
		print("Sucessfuly Calculated....")
		for i in range(0, 18):
			production_total.append(total[i])
			bar_no.append(i + 1)
		print("Total Pie :", len(bar_no))
		maxt = max(production_total)
		mint = min(production_total)
		print('Max_Production', maxt)
		print('MIN_Production', mint)
		yearmx = ''
		yearmn = ''
		for i in range(0, 18):
			if (maxt == total[i]):
				yearmx = str(years[i])
		for i in range(0, 18):
			if (mint == total[i]):
				yearmn = str(years[i])

		maxt = str(maxt)
		mint = str(mint)
		strTitle = 'YEARWISE TOTAL PRODUCTION\nMaximum Production Is : '
		str2 = ' in year : '
		str3 = '\nMinimum Production is : '
		strTitle = strTitle + maxt + str2 + yearmx + str3 + mint + str2 + yearmn
		plt.pie(production_total, labels=years, shadow=True, autopct='%1.1f%%')
		plt.title(strTitle)
		# plt.show()
		print(production_total)
		# print(len(production_total))
		return [production_total, years,maxt,yearmx,mint,yearmn]

	else:
		return [["NONE"], ["NONE"]]
