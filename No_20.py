#sum to zero

class Sum_to_zero():

    def output(self,list_of_numbers):
        result1,result = [],[]
        for i in list_of_numbers:
            for j in list_of_numbers:
                for k in list_of_numbers:
                    if (j==k or i==k or i==j):
                        continue
                    else:
                        result = []
                        if i+j+k == 0:
                            result.append(i)
                            result.append(j)
                            result.append(k)
                            list_of_numbers.remove(i)
                            list_of_numbers.remove(j)
                            list_of_numbers.remove(k)
                            result1.append(result)
        print(result1)

a = Sum_to_zero()
a.output([-25, -10, -7, -3, 2, 4, 8, 10])
