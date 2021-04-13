'''

'''

import  datetime
import  sort_module
import  star_search

datafile='/home/davit/Documents/Projects/Astronomy_task_python/337.all(1).tsv'
fov_v=100
fov_h=70
ra_user=50
dec_user=50
n=20

def open_tsv():
    with open(datafile) as fd:
        list_of_DB=[]
        for row in fd:
            if len(row.split('\t')) !=1:
                list_of_DB.append(row[:-1].split('\t'))
    return list_of_DB

def n_high_mag(array, n):
    n_high_mag_list=[]
    for i in range(n):
        n_high_mag_list.append(array[i])
    return n_high_mag_list


def creat_result(array):
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        for i in array:
            csv_temp.write(f'{i}\n')



with open('text.txt', 'w') as wt:
    for i in n_high_mag(sort_module.quicksort(star_search.search_stars(open_tsv(),ra_user,dec_user,fov_v,fov_h), index_sort=22), n):
        wt.write(f'{i}\n')


creat_result(([open_tsv()[0]]+n_high_mag(sort_module.quicksort(star_search.search_stars(open_tsv(),ra_user,dec_user,fov_v,fov_h), index_sort=22), n)))