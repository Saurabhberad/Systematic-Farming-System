import csv
list1=[]
cnt=0
file1=open('pune.csv','r')
data=csv.reader(file1,delimiter=',')
for row in data:
	if row[4] not in list1:
		list1=list1.append(row[4])
		cnt+=1
	
print(list1)
print(len(list1))
print(cnt)

		

		
