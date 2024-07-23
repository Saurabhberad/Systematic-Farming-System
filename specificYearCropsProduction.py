import matplotlib.pyplot as plt
import csv
def main(districtName,yearChoice):
	print("\n     SPECIFIC YEAR CROP PRODUCTION\n")
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bar_no=[]
	districtList=[]
	production_total=[]
	set1=set([])
	set2=set([])
	cropList=[]
	cropLen =0
	districtLen=0

	file1=open("outmaha1.csv",'r') 
	data1=csv.reader(file1,delimiter=',')
	for row in data1:
		if(row[0]=='maharashtra'):
			set2.add(row[1])
		districtList=list(set2)
		districtLen=len(districtList)
	print('\nDISTRICTS \n')
	print('\ndistrictList :',','.join(districtList))
	
	for i in range (0,districtLen):
		if(districtName ==districtList[i]):
			districtName=districtName+'.csv'
			file1=open(districtName,'r') 
			file2=open(districtName,'r')
			result_data=cropCal(districtName,yearChoice,file1,file2)
			file1.close()
	return result_data




def cropCal(districtName,yearChoice,file1,file2):
	total=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bar_no=[]
	districtList=[]
	production_total=[]
	set1=set([])
	set2=set([])
	cropList=[]
	cropLen =0
	districtLen=0	

	cnt=0
	data1=csv.reader(file2,delimiter=',')
	for row in data1:
		if(row[2]==yearChoice):
			set1.add(row[4])
	cropList=list(set1)
	#print(cropList)
	cropLen =len(cropList)
	file2.close()

	print('\nCropLIst    :\n  ',','.join(cropList))
	data=csv.reader(file1,delimiter=',')
	for row in data:
		if(row[2]==yearChoice):
			for i in range(0,cropLen ):
				if(row[4]==cropList[i]):
					total[i]=total[i]+float(row[6])
	
	for i in range (0,cropLen ):
		production_total.append(total[i])
		bar_no.append(i)
	maxt=max(production_total)
	mint=min(production_total)
	print('\n\nMax_Production',maxt)
	print('\nMIN_Production',mint)
	cropmx=''
	cropmn=''
	for i in range (0,cropLen ):
		if(maxt==total[i]):
			cropmx=str(cropList[i])
	for i in range (0,cropLen ):
		if(mint==total[i]):
			cropmn=str(cropList[i])
		
	maxt=str(maxt)
	mint=str(mint)
	strTitle=' CROPS PRODUCTION FOR YEAR  '
	str2='\nMaximum Production of : '
	str3='  is :'
	str4='\nMinimum Production is : '
	strTitle=strTitle+yearChoice+str2+cropmx+str3+maxt+str4+cropmn+str3+mint
	plt.bar(bar_no,production_total,color='r')
	plt.xticks(bar_no, cropList, rotation='vertical')
	plt.title(strTitle)
	plt.xlabel('Crops')
	plt.ylabel('Production in Quintal')
	# plt.show()
	#print(production_total)
	#print(len(production_total))
	print(cropList)
	return [production_total,cropList,yearChoice,cropmx,maxt,cropmn,mint]

