import csv 

file1=open("cropsmaha1.csv",'r')
file2=open("outmaha1.csv",'w')
data=csv.reader(file1,delimiter=',')
for row in data:
	
	row[2]=row[2].replace('yr','')
	row[4]=row[4].replace('Arhar/','')	
	row[4]=row[4].replace('(lint)','')
	row[4]=row[4].replace('(Green Gram)','')
	if(len(row[6])==0):
		row[6]=row[6].replace('','0')	
	for i in range(0,7):
		row[i]=row[i].lower()
	
	
	
	file2.write(",".join(row))
	file2.write('\n')
	print(".")
print("DATA CLEAN SUCESSFULLY.......")
file1.close()
file2.close()
