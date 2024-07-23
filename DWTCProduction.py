import matplotlib.pyplot as plt
import csv
def main():
	file1 = open("outmaha1.csv", 'r')
	data = csv.reader(file1, delimiter=',')
	production_total = []
	total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	bar_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
			  30, 31, 32, 33]
	# bars=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
	cnt = 0
	bars = ["ahmednagar ", "akola ", "amravati ", "aurangabad ", "beed ", "bhandara ", "buldhana ", "chandrapur ",
			"dhule ", "gadchiroli ", "gondia ", "hingoli ", "jalgaon ", "jalna ", "kolhapur ", "latur ", "nagpur ",
			"nanded ", "nandurbar ", "nashik ", "osmanabad ", "parbhani ", "pune ", "raigad ", "ratnagiri ", "sangli ",
			"satara ", "sindhudurg ", "solapur ", "thane ", "wardha ", "washim ", "yavatmal "]
	for row in data:
		if (row[1] == 'ahmednagar'):
			total[0] += int(float(row[6]))
			cnt = cnt + 1
		elif (row[1] == 'akola'):
			total[1] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'amravati'):
			total[2] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'aurangabad'):
			total[3] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'beed'):
			total[4] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'bhandara'):
			total[5] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'buldhana'):
			total[6] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'chandrapur'):
			total[7] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'dhule'):
			total[8] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'gadchiroli'):
			total[9] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'gondia'):
			total[10] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'hingoli'):
			total[11] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'jalgaon'):
			total[12] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'jalna'):
			total[13] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'kolhapur'):
			total[14] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'latur'):
			total[15] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'nagpur'):
			total[16] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'nanded'):
			total[17] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'nandurbar'):
			total[18] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'nashik'):
			total[19] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'osmanabad'):
			total[20] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'parbhani'):
			total[21] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'pune'):
			total[22] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'raigad'):
			total[23] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'ratnagiri'):
			total[24] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'sangli'):
			total[25] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'satara'):
			total[26] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'sindhudurg'):
			total[27] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'solapur'):
			total[28] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'thane'):
			total[29] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'wardha'):
			total[30] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'washim'):
			total[31] += float(row[6])
			cnt = cnt + 1
		elif (row[1] == 'yavatmal'):
			total[32] += float(row[6])
			cnt = cnt + 1
		print("Hello")
	for i in range(0, 33):
		production_total.append(total[i])
	maxt = max(production_total)
	maxindex = production_total.index(maxt)
	# print(maxt)

	maxt = str(maxt)
	strTitle = 'DISTRICT WISE PRODUCTION\nMaximum Production Is Of ' + bars[maxindex] + '=' + maxt
	strTitle = strTitle + maxt
	plt.bar(bar_no, production_total, color='r')
	plt.xticks(bar_no, bars, rotation='vertical')
	plt.title(strTitle)
	plt.xlabel('categories')
	plt.ylabel('values')
	# plt.show()
	print(production_total)
	print(len(production_total))
	file1.close()
	return [production_total,bars]

