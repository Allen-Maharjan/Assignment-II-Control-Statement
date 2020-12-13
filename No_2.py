#to see the given year is leap year or not

class Year():
    def __init__(self,year):
        self.year = year

    def checking_leap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year% 400 == 0:
                    print(f"{self.year} is a leap year")
                else:
                    print(f"{self.year} is not a leap year")
            else:
                print(f"{self.year} is a leap year")
        else:
            print(f"{self.year} is not a leap year")

year_1 = Year(1904)
year_2 = Year (1905)
year_3 = Year(2020)
year_1.checking_leap()
year_2.checking_leap()
year_3.checking_leap()
