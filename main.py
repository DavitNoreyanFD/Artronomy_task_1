import csv
import  datetime

datafile='/home/davit/Documents/Projects/Astronomy_task_python/337.all(1).tsv'
def open_tsv():
    with open(datafile) as fd:
        list_of_DB=[]
        for row in fd:
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
    pass

def sort_stars():
    pass

def creat_result():
    pass
for row in open_tsv():
    print(len((row)))