#binary search

def binary_search(data,number,maximum,minimum):
    if maximum > minimum:
        mid = int((maximum+minimum)/2)
        if (data[mid] == number):
            print(f"index position={data.index(number)}")
        elif (data[mid]>number):
            return binary_search(data,number,mid-1,minimum)
        else:
            return binary_search(data,number,maximum,mid+1)
    else:
        print(-1)

data = [1,2,3,4,5,6,7,8,9,10]
number = 9
binary_search(data,number,len(data),0)
