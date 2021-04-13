
'''the quicksort sorting algorithm is used to sort the data, the reason for this is that quicksort is, in most cases, 
very optimal in large amounts of data and the complexity is in average O (nlogn). Since my logic we get a matrix of 
data and we must sort by a specific column, then our sorting function gets an array and a column index to sort
'''
from random import randint
def quicksort(array, index_sort):
    for row in array:
        row[index_sort]=float(row[index_sort])
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)][index_sort]
    for item in array:
        if item[index_sort] < pivot:
            low.append(item)
        elif item[index_sort] == pivot:
            same.append(item)
        elif item[index_sort] > pivot:
            high.append(item)

    return quicksort(low,index_sort) + same + quicksort(high,index_sort)