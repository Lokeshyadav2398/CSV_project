import csv 
import pdb

def open_csv_file(filename):
    new_list = []
    fd = open(filename)
    fdata = csv.reader(fd)
        
    for row in fdata:
        #print(row)
        new_list.append(row)
        
    print("")
        
    temp = 0
    pdb.set_trace()
    for i in range(0,len(new_list)):
        for j in range(i+1, len(new_list)):
            if(int(new_list[i][0]) > int(new_list[j][0])):
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
        
    for line in new_list:
        print(line)
                        
def main():
    filename = "data.csv"
    data = open_csv_file(filename)
    return
        
if(__name__=="__main__"):
        main()
