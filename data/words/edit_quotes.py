import csv

csv_file = open("./quotes.csv", "r" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
quotes_list = []
for line in f:
	quotes_list.append(line[1])
	#print(len(line[1]))
#print(quotes_list)
#print("original length", len(quotes_list))

length = 35
quotes_list = list(filter(lambda quote: len(quote) < length , quotes_list))
#print("filtered by length <", length, ":", len(quotes_list))
print(quotes_list)