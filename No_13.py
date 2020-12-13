#writing a csv filename

def making_csv(sample):
    sample_str = ''
    for i in sample:
        sample_str += str(i)+","
    file.write(sample_str[0:-1]+'\n')




file = open("file1.csv","w")
file.write("name, address, age"+'\n')
sample_test = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',21)]
for i in range(len(sample_test)):
    making_csv(sample_test[i])
file.close()
