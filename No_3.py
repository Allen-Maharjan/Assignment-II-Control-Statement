#finding anagram

def is_anagram(string1,string2):
    if len(string1)==len(string2):
        string1_sorted = sorted(string1)
        string2_sorted = sorted(string2)

        for i in range(len(string1_sorted)):
            if string1_sorted[i] != string2_sorted[i]:
                return False
            return True
    else:
        return False


paragraph = " Python is a great language!, said Fred. I don't ever remember having this much fun before that hatt"
list_paragraph = paragraph.split(" ")
for i in list_paragraph:
    if i.isalpha()==True:
        for j in list_paragraph:
            if i == j:
                continue
            else:
                if is_anagram(i,j):
                    print(f"{i} and {j} are anagrams")
                else:
                    print(f"{i} and {j} are not anagrams")
