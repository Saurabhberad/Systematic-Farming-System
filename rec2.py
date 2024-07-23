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
set3=set([])
cropList=[]
global cropList1
cropList1= ['Software Engineer', 'Web Developer','Data Analyst']

seasonList=[]


# for row in data1:
# 	if(row[0]=='maharashtra'):
# 		set2.add(row[1])
# 	districtList=list(set2)
# 	districtLen=len(districtList)
# print('DISTRICTS \n')
# print('districtList:',','.join(districtList))
# districtName=input('\nEnter a district :- ')
# districtName=districtName.lower()

file1=open("outmaha1.csv",'r')
data1=csv.reader(file1,delimiter=',')
for row in data1:
	if (row[0] == 'maharashtra'):
		set2.add(row[1])
	districtList = list(set2)
	districtLen = len(districtList)
file1.close()





def yearProductionCal(districtName,seasonchoice):

	for i in range(0, districtLen):
		if (districtName == districtList[i]):
			districtName = districtName + '.csv'
			file1 = open(districtName, 'r')
			file2 = open(districtName, 'r')
			file3 = open(districtName, 'r')
			# yearProductionCal()

	cnt=0
	# data1=csv.reader(file2,delimiter=',')

	# for row in data1:
	#
	# 	set3.add(row[3])
	# seasonList=list(set3)
	# print(seasonList)
	# print(len(seasonList[0]))
	# print('\nseasonList     :\n',','.join(seasonList))
	#
	# seasonchoice=input("Enter the season name :")
	# seasonchoice=seasonchoice.lower()
	# print(seasonchoice)
	data2=csv.reader(file3,delimiter=',')



	for row in data2:
		#print(seasonchoice)
		#print(row[3])
		if(row[3] == seasonchoice):
			# print("in if...............")
			set1.add(row[4])
	cropList=list(set1)

	cropList1=cropList

	# print('\ncropList     :\n', ','.join(cropList1))
	# print("Total Crops :", len(cropList1))
	global data
	data = csv.reader(file1, delimiter=',')
	# graph()

	return [cropList]

	# receive crop list
def graph(cropchoice,cropchoice1):
	# print(data)
	productiontotal = 0
	productiontotal1 = 0
	# cropchoice = input('\nEnter the crop name 1:')
	# cropchoice = cropchoice.lower()
	# cropchoice1 = input('\nEnter the crop name 2 :')
	# cropchoice1 = cropchoice1.lower()

	for row in data:
		if (row[4] == cropchoice):
			if (row[2] == '1997'):
				total[0] = int(float(row[6]))

			elif (row[2] == '1998'):
				total[1] += int(float(row[6]))

			elif (row[2] == '1999'):
				total[2] += int(float(row[6]))

			elif (row[2] == '2000'):
				total[3] += int(float(row[6]))

			elif (row[2] == '2001'):
				total[4] += int(float(row[6]))

			elif (row[2] == '2002'):
				total[5] += int(float(row[6]))

			elif (row[2] == '2003'):
				total[6] += int(float(row[6]))

			elif (row[2] == '2004'):
				total[7] += int(float(row[6]))

			elif (row[2] == '2005'):
				total[8] += int(float(row[6]))

			elif (row[2] == '2006'):
				total[9] += int(float(row[6]))

			elif (row[2] == '2007'):
				total[10] += int(float(row[6]))

			elif (row[2] == '2008'):
				total[11] += int(float(row[6]))

			elif (row[2] == '2009'):
				total[12] += int(float(row[6]))

			elif (row[2] == '2010'):
				total[13] += int(float(row[6]))

			elif (row[2] == '2011'):
				total[14] += int(float(row[6]))

			elif (row[2] == '2012'):
				total[15] += int(float(row[6]))

			elif (row[2] == '2013'):
				total[16] += int(float(row[6]))

			elif (row[2] == '2014'):
				total[17] += int(float(row[6]))
		if (row[4] == cropchoice1):
			if (row[2] == '1997'):
				total1[0] = int(float(row[6]))

			elif (row[2] == '1998'):
				total1[1] += int(float(row[6]))

			elif (row[2] == '1999'):
				total1[2] += int(float(row[6]))

			elif (row[2] == '2000'):
				total1[3] += int(float(row[6]))

			elif (row[2] == '2001'):
				total1[4] += int(float(row[6]))

			elif (row[2] == '2002'):
				total1[5] += int(float(row[6]))

			elif (row[2] == '2003'):
				total1[6] += int(float(row[6]))

			elif (row[2] == '2004'):
				total1[7] += int(float(row[6]))

			elif (row[2] == '2005'):
				total1[8] += int(float(row[6]))

			elif (row[2] == '2006'):
				total1[9] += int(float(row[6]))

			elif (row[2] == '2007'):
				total1[10] += int(float(row[6]))

			elif (row[2] == '2008'):
				total1[11] += int(float(row[6]))

			elif (row[2] == '2009'):
				total1[12] += int(float(row[6]))

			elif (row[2] == '2010'):
				total1[13] += int(float(row[6]))

			elif (row[2] == '2011'):
				total1[14] += int(float(row[6]))

			elif (row[2] == '2012'):
				total1[15] += int(float(row[6]))

			elif (row[2] == '2013'):
				total1[16] += int(float(row[6]))

			elif (row[2] == '2014'):
				total1[17] += int(float(row[6]))

	print("Sucessfuly Calculated....")

	j=1
	k=0
	production_total.clear()
	production_total1.clear()

	for i in range (0,18):
		productiontotal=productiontotal+total[i]
		production_total.append(total[i])
		bar_no.append(k)
		k=k+2
		production_total1.append(total1[i])
		productiontotal1=productiontotal1+total1[i]
		bar_no2.append(j)
		j=j+2
	print(productiontotal)
	print(productiontotal1)
	maxt1=productiontotal1
	maxt2=productiontotal
	mint=0
	if maxt1<maxt2:
		maxt=maxt2
		mint=maxt1
		cropMaxName = cropchoice
		cropMinName = cropchoice1
	else:
		maxt=maxt1
		mint=maxt2
		cropMaxName = cropchoice1
		cropMinName = cropchoice
	if(maxt==maxt1):
		cropMaxName=cropchoice
	else:
		cropMaxName=cropchoice1
	print('Max_Production',maxt)
	
	if(mint==maxt1):
		cropMinName=cropchoice
	else:
		cropMinName=cropchoice1
	print('Min_Production',mint)
	maxt=str(maxt)
	mint=str(mint)
	strTitle='Maximum Production Is : '
	str3='\nMinimum Production is : '
	str2='of  '
	str4='\nOUR SYSTEM RECOMMEND YOU :'
	str5='\nas production is less profit is more  '
	strTitle=strTitle+maxt+str3+mint+str2+cropMinName+str4+cropMinName+str5

		
	
	# plt.bar(bar_no,production_total,label=cropchoice)
	# plt.bar(bar_no2,production_total1,label=cropchoice1)
	# plt.xticks(bar_no, years, rotation='vertical')
	# plt.title(strTitle)
	# plt.legend()
	# plt.xlabel('Years')
	# plt.ylabel('Production in Quintal')
	# # cropchoice1 = None
	# # cropchoice = None
	# plt.show()
	print("Production1",production_total)
	print("production2",production_total1)

	return [production_total1,production_total,years,cropchoice,cropchoice1,maxt,cropMaxName,mint,cropMinName]
	#print(production_total)
	#print(len(production_total))







