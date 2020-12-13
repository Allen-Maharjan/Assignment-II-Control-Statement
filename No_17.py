#basic calculator

class Calculator():

    def calculate(self,a,b,op):
        self.value1 = a
        self.value2 = b
        self.op = op
        try :
            if (self.op == '+'):
                return self.value1 + self.value2
            elif (self.op == '-'):
                return self.value1 - self.value2
            elif (self.op == '*'):
                return self.value1 * self.value2
            elif (self.op == '/'):
                return self.value1 / self.value2
        except ZeroDivisionError :
            return "Divisivle by zero is undetermined."


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator: ")
except (ValueError,NameError):
    print("Please enter intergers only")

a1 = Calculator()
print(a1.calculate(a,b,op))
