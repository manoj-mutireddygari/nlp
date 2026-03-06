#week:1 day:1
#even
def even():
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")

#largest
def largest():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a>b:
        print("a is greater")
    elif b>a:
        print("b is greater")
    elif a == b:
        print("both are equal")
    
#pos neg neutral
def check():
    num = int(input("Enter the number: "))
    if num == 0:
        print("ZERO")
    elif num >0:
        print("Positive")
    elif num < 0:
        print("Negative")

#largest of three
def largest_of_three():
    a, b, c = map(int, input("Enter three numbers separated by space: ").split())
    if a>=b and a>=c:
        print(a ," is greater")
    elif b>=a and b>=c:
        print(b , "is greater")
    else:
        print(c , "is greater")

#week:1 day:2
#loops
#multiplication table

def multiplication_table():
    num = int(input("enter the number: "))
    for i in range(1,11):
        print(num , "x" , i , "=" , num*i)


#string and number palindrom
def palindrom():
    num = input("enter the number:")
    a = num[::-1]
    if a == num:
        print("palindrom")
    else:
        print("not palindrom")

#pattern *
def patterns():
    num =int(input("enter the number:"))
    for i in range(1, num + 1):
        for s in range(num-i):
            print(" ",end="")
        for j in range(1, i + 1):
            print("*", end=" ")
        print() 

def reverse_integer():
    num = int(input("enter the number: "))
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    print("Reversed number:", rev)

def reverse_integer2():
    num = input("enter the number: ")
    rev = num[::-1]
    rev = int(rev)
    print("Reversed string:", rev)

#finding length of a integer without len()
def len_of_integer():
    num = int(input("Enter a number: "))
    count = 0
    while num > 0:
        count += 1
        num //= 10
    print("length of the value is:", count)

#sum of the digits
def sum_of_digits():
    num = int(input("Enter a number: "))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print("Sum of digits:", total)

#Armstrong Number
def Armstrong_Number():
    num = int(input("Enter a number: "))
    original =num
    count =len(str(num))
    total=0
    while num>0:
        digit = num%10
        total += digit**count
        num //= 10
    if total==original:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")



#week1-Day-3
#counting vowels in the sting
def count_vowels():
    string = input("Enter a string: ").strip().lower()
    vowels=['a','e','i','o','u']
    count =0
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1
    print("Number of vowels:", count)

#largest number in the list
def largest_in_list():
    numbers = list(map(int, input("enter the number seperated by space:").split()))
    largest = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    print("Largest number:", largest)

#reverse a list
def reverse_a_list():
    num = list(map(int ,input("enter the numbers seperate them by space:").split()))
    reverse = []

    for i in range(len(num)-1, -1, -1):
        reverse.append(num[i])

    print("Reversed list:", reverse)

#remove duplicate from the list
def remove_duplicate_num_in_list():
    lst = list(map(int ,input("Enter the numbers separate them by space:").split()))
    clean_lst =[]
    for num in lst:
        if num not in clean_lst:
            clean_lst.append(num)
    print("List after removing duplicates:", clean_lst)


#week1- Day4
#count frequency of string
def count_frequency():
    string = input("Enter the string:")
    frequency ={}
    for i in range(len(string)):
        if string[i] in frequency:
            frequency[string[i]] += 1
        else:
            frequency[string[i]] = 1
    print("frequency of the word" , frequency)

#count frequency of string method-2
def count_frequency2():
    text = input("Enter the string: ")
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    print(freq)

#finding max frequency letter in string
def max_frequency():
    text = input("Enter the string: ")
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1
    high_frequency =max(freq.items(), key=lambda item: item[1])
    print(high_frequency)

#two sum problem
def two_sum():
    lst = list(map(int,input("Enter the numbers seperate them by space").split()))
    target = int(input("Enter the target:"))
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                print("indexes",i,j)
                print("values",lst[i],lst[j])

#two sum method 2
def two_sum2():
    lst = list(map(int,input("Enter the numbers seperate them by space").split()))
    target = int(input("Enter the target:"))
    hashmap ={}
    for i,num in enumerate(lst):
        comp = target-num
        if comp in hashmap:
            print("indexes",hashmap[comp],i)
            print("values",comp,num)
        hashmap[num]=i

two_sum2()




