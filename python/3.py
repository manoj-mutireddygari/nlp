#Secong largest Number in a list
def exp1():
    numbers = [1,2,3,4,5,6]
    largest = 0
    Second_largest = 0
    for i in range(len(numbers)):
        if numbers[i] > largest:
            Second_largest = largest
            largest = numbers[i]
        elif numbers[i] > Second_largest and numbers[i] != largest:
            Second_largest = numbers[i]

    print("Largest:", largest)
    print("Second Largest:", Second_largest)

#count wors in a sentence
def exp2():
    sentence = input("Enter the Sentence:")
    print(len(sentence.split()))

#remove duplicates
def exp3():
    num = [1,2,3,3,4,4,5]
    result = []
    for i in range(len(num)):
        if num[i] not in result:
            result.append(num[i])
    print(result)

#palindrom Number
def exp4():
    num = int(input("Enter the number:"))
    b = str(num)
    c = b[::-1]
    if b == c:
        print("Given number is palindrom")
    else:
        print("Not a palindrom Number")

#palindrom string
def exp5():
    a = input("enter the palindrom string:")
    if a == a[::-1]:
        print("palindrom")
    else:
        print("Not a palindrom")
exp5()