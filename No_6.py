#finding john

class Find():
    def __init__(self,*args):
        self.list_of_names = args[0]
        if args[1] in self.list_of_names:
            print("John is one of my friend")
        else:
            print("Not found")


names = ["Allen","Rajesh","Ram","Shyam","Saugat","Samir"]
Find(names,"john")
