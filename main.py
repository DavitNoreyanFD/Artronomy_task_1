'''
the script works functionally, the necessary attributes are taken and
placed in the attributes of the Stars class to avoid unwanted use of a lot of index
'''
import configparser
import math
import datetime
import sort_module
import star_search
import stars

config = configparser.ConfigParser()
config.read('config.ini')

datafile = config['USER']['datafile']
fov_v = float(config['USER']['fov_v'])
fov_h = float(config['USER']['fov_h'])
ra_user = float(config['USER']['ra_user'])
dec_user = float(config['USER']['dec_user'])
n = int(config['USER']['n'])

INDEX_ID = 7
INDEX_RA = 0
INDEX_DEC = 1
INDEX_MAG = 22
INDEX_FLUX = 20


def open_tsv():
    with open(datafile) as fd:
        list_of_DB = []
        next(fd)

        for row in fd:
            list_row = row[:-1].split('\t')
            try:
                list_of_DB.append(
                    stars.Stars(
                        float(list_row[INDEX_ID]),
                        float(list_row[INDEX_RA]),
                        float(list_row[INDEX_DEC]),
                        float(list_row[INDEX_MAG]),
                        float(list_row[INDEX_FLUX]),
                    )
                )
            except ValueError:
                pass


        return list_of_DB


def n_high_mag(array, n):
    '''the function returns the n brightest stars in the field of view'''
    n_high_mag_list = []
    for i in range(n):
        n_high_mag_list.append(array[i])
    return n_high_mag_list


def calc_distanc_append_in_tab(star_array):
    '''the calculation logic comes from the principle m1-m2 = -2.5lg (l1 / l2) I took the
    famous star Sirius and compared it with the stars in our database'''
    dist_sirius = 8.64
    for star in star_array:
        star.distance = dist_sirius * math.sqrt(2.72 ** (-0.4 * (-1.47 - float(star.mag))))

    return star_array


def creat_result(star_array):
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        csv_temp.write('id \t ra\t dec\t mag\t flux \t distance \n')
        for star in star_array:
            csv_temp.write(f'{star.id}\t{star.ra}\t{star.dec}\t{star.mag}\t{star.flux}\t{star.distance}\n')


my_key = lambda s: -s.mag

tsv_to_list = open_tsv()
searched_stars = star_search.search_stars(tsv_to_list, ra_user, dec_user, fov_v, fov_h)
sort_by_mag = sort_module.quicksort(searched_stars, key=my_key)
n_sorted = n_high_mag(sort_by_mag, n)
calc_dist_append = calc_distanc_append_in_tab(n_sorted)

if __name__ == "__main__":
    creat_result(calc_dist_append)