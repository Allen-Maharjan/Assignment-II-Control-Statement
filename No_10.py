#changing camelcase to snake case and kebab case1

def transformer(sample,seperator):
    final_answer = ''
    if seperator == 1:
        for i in sample:
            if i.isupper() == True:
                final_answer += "_"
            final_answer += i.lower()
        print(f'Snakecase = {final_answer[1::]}')
    elif seperator == 2:
        for i in sample:
            if i.isupper() == True:
                final_answer += "-"
            final_answer += i.lower()
        print(f"keabab case= {final_answer[1::]}")

text = input("Enter a CamelCase string= ")
separator = int(input("Enter 1 for snakecase\nEnter 2 for kebab case: "))
if (separator == 1 or separator == 2):
    transformer(text,separator)
else:
    print("Error")
