#sorting list

class NameList():

    def __init__(self,*args,**kwargs):
        print(id(args))
        a = args[0]
        a.sort()
        print(f" first name = {a[0]} and second name = {a[1]}")

a= ['Ram','Shyam','Hari','Sita','Gita','Balram']
print(id(a))
NameList(a)
