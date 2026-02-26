def exp4(): 
    n = int(input("Enter the Number for to add Until that from 1:"))
    total = 0
    for i in range(1, n+1):
        total = total + i

    print(total)

#reversing a String
def exp5():
    string = input("Enter your Name:")
    print(string[::-1])

#Volwels in a String
def exp6():
    string = input("ENter your Name:").lower()
    vowels = ['a','e','i','o','u']
    count=0
    for i in range(len(string)):
        if string[i] in vowels:
            count  += 1
    print(count)

#largest number in a List
def exp7():
    num = [1,2,3,6,5,4]
    largest= num[0]
    for i in range(len(num)):
        if num[i] > largest:
            largest = num[i]
    print(largest)

#fibanocci Series
def exp8():
       n = int(input("Enter the number:"))
       series = []
       a,b = 0,1
       for i in range(n):
           series.append(a)
           a,b = b, a+b
        
       print(series)

#Dictonaries
def exp9():
    base = {"manoj":{"marks":29},
            "sai":{"marks":26},
            "kiran":{"marks":27},
            "mukesh":{"marks":28}}
    highest_marks = 0
    topper = ""
    for name in base:
        if base[name]["marks"] > highest_marks:
            highest_marks = base[name]["marks"]
            topper = name

    print("topper:",topper ,"," "marks:" , highest_marks)

#Prime Number
def exp10(n):
    if n <= 1:
        return(False)
    for i in range(2,n):
        if n %i == 0:
            return(False)
    return(True)

# number = int(input("Enter the Number:"))
# if exp10(number):
#     print("prime number")
# else:
#     print("Not a prime number")