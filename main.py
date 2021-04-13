'''

'''
import  math
import  datetime
import  sort_module
import  star_search

datafile='/home/davit/Documents/Projects/Astronomy_task_python/cleaned_stars.tsv'
fov_v=100
fov_h=70
ra_user=50
dec_user=50
n=20

index_id=2
index_ra=38
index_dec=39
index_mag=35
index_flux=32

def open_tsv():
    with open(datafile) as fd:
        list_of_DB=[]
        for row in fd:
            #if len(row.split('\t')) !=1:
            list_row=row[:-1].split('\t')
            list_of_DB.append([list_row[index_id],list_row[index_ra],list_row[index_dec], list_row[index_mag], list_row[index_flux]])
    return list_of_DB

def n_high_mag(array, n):
    n_high_mag_list=[]
    for i in range(n):
        n_high_mag_list.append(array[i])
    return n_high_mag_list


def calc_distanc_append_in_tab(array,index_mag):
    dist_sirius=8.64
    for row in array:
        dist=dist_sirius * math.sqrt(2.72**(-0.4*(-1.47-float(row[index_mag]))))
        row.append(dist)
    return array


def append_header(array):
    outpt_array_final=[[open_tsv()[0][0],open_tsv()[0][1],open_tsv()[0][2],open_tsv()[0][3],open_tsv()[0][4],'distance']]
    for row in array:
        outpt_array_final.append(row)
    return outpt_array_final



def creat_result(array):
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:

        for i in array:
            for j in i:
                csv_temp.write(f'{j}\t')
            csv_temp.write('\n')






tsv_to_list=open_tsv()
searched_stars=star_search.search_stars(tsv_to_list,ra_user,dec_user,fov_v,fov_h,index_ra=1,index_dec=2)
sort_by_mag=sort_module.quicksort(searched_stars,3)
n_sorted=n_high_mag(sort_by_mag,n)
calc_dist_append=calc_distanc_append_in_tab(n_sorted,3)
final_list=append_header(calc_dist_append)



creat_result(final_list)


