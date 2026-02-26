import matplotlib.pyplot as plt
import random
import time

def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generateList(n):
    return [random.randint(0, 1000) for _ in range(n)]
def measurreTime(n):
    arr = generateList(n)
    start_time = time.time()
    insertionsort(arr)
    end_time = time.time()
    return end_time - start_time
def plotGraph(nList):
    timeList = [measurreTime(n) for n in nList]
    plt.plot(nList, timeList,'o-')
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.title('Insertion Sort')
    plt.show()
    
nList =[100,500,1000,2000,5000,10000]
plotGraph(nList)