import csv 

def open_csv_file(filename):
	new_list = []
	fd = open(filename)
	fdata = csv.reader(fd)
	
	for row in fdata:
		#print(row)
		new_list.append(row)
	
	print("")
	
	#print(new_list)
	temp = 0
	for i in range(0,len(new_list)):
		for j in range(i+1,len(new_list)):
			if(new_list[i][0]>new_list[j][0]):
				temp = new_list[i]
				new_list[i] = new_list[j]
				new_list[j] = temp
	
	print(new_list)	
			
def main():
	filename = "data.csv"
	data = open_csv_file(filename)
	return
	
if(__name__=="__main__"):
	main()