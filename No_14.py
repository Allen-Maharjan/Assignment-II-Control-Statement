#reading a csv file

def read_csv(list_file):
    print(len(list_file))
    my_dict = {}
    output = []
    y = list_file[0].split(',')
    for i in range(1,len(list_file)):
        x = list_file[i].split(',')
        my_dict[y[0]]= x[0]
        my_dict[y[1]]= x[1]
        my_dict[y[2]]= x[2]
        output.append(my_dict)
    print(output)


file = open("file1.csv","r")
list_file = file.readlines()
read_csv(list_file)
