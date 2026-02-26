def bubble_sort(array):

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                print('for the element',j+1,'and',j+2,'compare the elements',array[j+1],'and',array[j],'then after swap to',array[j],'and',array[j+1])
                print('pass',i+1,'after sorted array',array)

data =[-2,45,0,11,-9]
print('before sorted array',data)
bubble_sort(data)
print('sorted array in Ascending order',data)