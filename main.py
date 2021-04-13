import csv
import  datetime

datafile='/home/davit/Documents/Projects/Astronomy_task_python/337.all(1).tsv'
fov_v=100
fov_h=70
ra_user=50
dec_user=50

def open_tsv():
    with open(datafile) as fd:
        list_of_DB=[]
        for row in fd:
            if len(row.split('\t')) !=1:
                list_of_DB.append(row.split('\t'))
    return list_of_DB

def list_of_dec():
    list_of_dec_l=[]
    for row in open_tsv():
        try:
            list_of_dec_l.append(float(row[0]))
        except ValueError:
            pass
    return  list_of_dec_l

def list_of_RA():
    list_of_RA_l=[]
    for row in open_tsv():
        try:
            list_of_RA_l.append(float(row[1]))
        except ValueError:
            pass
    return  list_of_RA_l


def search_stars():
    stars_in_fov=[]
    for row in open_tsv():
        try:
            if (ra_user-fov_v/2)<float(row[0])<(ra_user+fov_v/2) and (dec_user-fov_h/2)<float(row[1])<(dec_user+fov_h/2):
                stars_in_fov.append(row)
        except ValueError:
            pass
    return stars_in_fov
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i][0]
        j = i - 1
        while j >= left and array[j][0] > key_item:
            array[j + 1][0] = array[j][0]
            j -= 1

        array[j + 1][0] = key_item
    return array
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2
    return array

def creat_result():
    pass
#print(len(list_of_dec()))
#print((search_stars()))
print(len((search_stars())))
print(timsort(search_stars()))
print(len((search_stars())))