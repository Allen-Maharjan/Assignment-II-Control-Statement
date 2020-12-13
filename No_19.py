#validity of a sting of parenthese

class Validity_string():

    def check(self,string):
        self.strings = string
        checking_strings,checking_strings1 = [],[]
        for i in self.strings:
            if (i == "{" or  i== '(' or i == '['):
                checking_strings.append(i)
            if(i=='}'):
                checking_strings1.append('{')
            if(i==']'):
                checking_strings1.append('[')
            if(i ==')'):
                checking_strings1.append('{')
        i,j = 0,len(checking_strings1)-1
        while i< len(checking_strings):
            if (checking_strings[i] != checking_strings1[j]):
                print("invalid")
                break
            i += 1
            j -= 1
        else:
            print("valid")


a = Validity_string()
a.check("{[(]}")
