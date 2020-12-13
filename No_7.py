#finding average age

class AverageAge():

    def __init__(self,*args):
        self.age_average = 0
        exceptions = 0
        for i in range(len(args[0])+1):
            if (args[i][2] == None):
                exceptions += 1
                continue
            else:
                self.age_average += args[i][2]
        self.average = self.age_average/(len(args) - exceptions)
        print(self.average)
        for i in range(len(args[0])+1):
            if (args[i][2] == None):
                print(f"{args[i][0]} age is not defined")
                continue
            elif args[i][2] < self.average:
                print(f"{args[i][0]} is young ")
            else:
                print(f"{args[i][0]} is old")


me = ("Allen","Maharjan",None)
ram = ("Ram","Shah",30)
shyam = ("Shyam","Shretha",25)
hari = ("hari","ram",50)
AverageAge(me,ram,shyam,hari)
