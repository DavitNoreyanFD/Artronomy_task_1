'''
the search for stars in the field of view proceeds from the following logic, I assumed that the camera matrix is a
rectangle and its dimensions are fov_h and fov_v, respectively, and the direction of the telescope is the center
of this rectangle
'''

def search_stars(array,ra_user,dec_user,fov_v,fov_h,index_ra,index_dec):
    stars_in_fov=[]
    for row in array:
        try:
            if (ra_user-fov_v/2)<float(row[index_ra])<(ra_user+fov_v/2) and (dec_user-fov_h/2)<float(row[index_dec])<(dec_user+fov_h/2):
                stars_in_fov.append(row)
        except ValueError:
            pass
    return stars_in_fov