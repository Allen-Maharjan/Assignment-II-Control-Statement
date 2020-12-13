#creating tuple and add in list

class Discription():
    def sorting (*args,**kwargs):
        changing_to_list= list(args)
        print(f"unsorted = {changing_to_list}")
        changing_to_list.sort(key=lambda x:x[2])
        return changing_to_list



me = ("Allen","Maharjan",20)
ram = ("Ram","Shah",30)
shyam = ("Shyam","Shretha",25)

print(f"sorted = {Discription.sorting(me,ram,shyam)}")
