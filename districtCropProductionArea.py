import matplotlib.pyplot as plt
import csv
def plot():
	file1 = open("outmaha1.csv", 'r')
	data = csv.reader(file1, delimiter=',')
	production_total = []
	area_total = []
	total1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	bar_no = []
	bar_no2 = []
	bars = ["ahmednagar ", "akola ", "amravati ", "aurangabad ", "beed ", "bhandara ", "buldhana ", "chandrapur ",
			"dhule ", "gadchiroli ", "gondia ", "hingoli ", "jalgaon ", "jalna ", "kolhapur ", "latur ", "nagpur ",
			"nanded ", "nandurbar ", "nashik ", "osmanabad ", "parbhani ", "pune ", "raigad ", "ratnagiri ", "sangli ",
			"satara ", "sindhudurg ", "solapur ", "thane ", "wardha ", "washim ", "yavatmal "]

	print("  \n\n   DISTRICT WISE VARIOUS CROPS PRODUCTION  ")

	for row in data:
		if (row[1] == 'ahmednagar'):
			total[0] += float(row[6])
			total1[0] += float(row[5])
		elif (row[1] == 'akola'):
			total[1] += float(row[6])
			total1[1] += float(row[5])
		elif (row[1] == 'amravati'):
			total[2] += float(row[6])
			total1[2] += float(row[5])
		elif (row[1] == 'aurangabad'):
			total[3] += float(row[6])
			total1[3] += float(row[5])
		elif (row[1] == 'beed'):
			total[4] += float(row[6])
			total1[4] += float(row[5])
		elif (row[1] == 'bhandara'):
			total[5] += float(row[6])
			total1[5] += float(row[5])
		elif (row[1] == 'buldhana'):
			total[6] += float(row[6])
			total1[6] += float(row[5])
		elif (row[1] == 'chandrapur'):
			total[7] += float(row[6])
			total1[7] += float(row[5])
		elif (row[1] == 'dhule'):
			total[8] += float(row[6])
			total1[8] += float(row[5])
		elif (row[1] == 'gadchiroli'):
			total[9] += float(row[6])
			total1[9] += float(row[5])
		elif (row[1] == 'gondia'):
			total[10] += float(row[6])
			total1[10] += float(row[5])
		elif (row[1] == 'hingoli'):
			total[11] += float(row[6])
			total1[11] += float(row[5])
		elif (row[1] == 'jalgaon'):
			total[12] += float(row[6])
			total1[12] += float(row[5])
		elif (row[1] == 'jalna'):
			total[13] += float(row[6])
			total1[13] += float(row[5])
		elif (row[1] == 'kolhapur'):
			total[14] += float(row[6])
			total1[14] += float(row[5])
		elif (row[1] == 'latur'):
			total[15] += float(row[6])
			total1[15] += float(row[5])
		elif (row[1] == 'nagpur'):
			total[16] += float(row[6])
			total1[16] += float(row[5])
		elif (row[1] == 'nanded'):
			total[17] += float(row[6])
			total1[17] += float(row[5])
		elif (row[1] == 'nandurbar'):
			total[18] += float(row[6])
			total1[18] += float(row[5])
		elif (row[1] == 'nashik'):
			total[19] += float(row[6])
			total1[19] += float(row[5])
		elif (row[1] == 'osmanabad'):
			total[20] += float(row[6])
			total1[20] += float(row[5])
		elif (row[1] == 'parbhani'):
			total[21] += float(row[6])
			total1[21] += float(row[5])
		elif (row[1] == 'pune'):
			total[22] += float(row[6])
			total1[22] += float(row[5])
		elif (row[1] == 'raigad'):
			total[23] += float(row[6])
			total1[23] += float(row[5])
		elif (row[1] == 'ratnagiri'):
			total[24] += float(row[6])
			total1[24] += float(row[5])
		elif (row[1] == 'sangli'):
			total[25] += float(row[6])
			total1[25] += float(row[5])
		elif (row[1] == 'satara'):
			total[26] += float(row[6])
			total1[26] += float(row[5])
		elif (row[1] == 'sindhudurg'):
			total[27] += float(row[6])
			total1[27] += float(row[5])
		elif (row[1] == 'solapur'):
			total[28] += float(row[6])
			total1[28] += float(row[5])
		elif (row[1] == 'thane'):
			total[29] += float(row[6])
			total1[29] += float(row[5])
		elif (row[1] == 'wardha'):
			total[30] += float(row[6])
			total1[30] += float(row[5])
		elif (row[1] == 'washim'):
			total[31] += float(row[6])
			total1[31] += float(row[5])
		elif (row[1] == 'yavatmal'):
			total[32] += float(row[6])
			total1[32] += float(row[5])
	j = 1
	k = 0
	for i in range(0, 33):
		production_total.append(total[i])
		bar_no.append(k)
		k = k + 2
		area_total.append(total1[i])
		bar_no2.append(j)
		j = j + 2
	# print(bar_no)
	# print(bar_no2)
	maxt = max(production_total)
	maxindex=production_total.index(maxt)

	# print("\nMaximum Production :", maxt)
	maxa = max(area_total)
	# print(maxa)
	districtmx = ''
	# for i in range(0, 18):
	# 	if (maxt == total[i]):
	# 		districtmx = str(bars[i])

	maxt = str(maxt)
	strTitle = '\nDISTRICT WISE PRODUCTION\nMaximum Production Is Of  '
	strTitle = strTitle + bars[maxindex] + 'is  ' + maxt
	# plt.bar(bar_no,production_total,color='b',label='Production')
	# plt.bar(bar_no2,area_total,color='r',label='area')
	# plt.stackplot(bar_no, area_total, production_total)
	# plt.xticks(bar_no, bars, rotation='vertical')
	# plt.legend()
	# plt.title(strTitle)
	# plt.xlabel('categories')
	# plt.ylabel('values')
	# plt.show()
	print("\nproduction_total of all district   :\n\n", production_total)
	print(len(production_total))
	file1.close()
	return [bar_no,area_total,production_total,bars]
	#return [bars]
