'''
the search for stars in the field of view proceeds from the following logic, I assumed that the camera matrix is a
rectangle and its dimensions are fov_h and fov_v, respectively, and the direction of the telescope is the center
of this rectangle
'''



def search_stars(star_array,ra_user,dec_user,fov_v,fov_h):
    stars_in_fov=[]
    for star in star_array:
        try:
            if (ra_user-fov_v/2)<float(star.ra)<(ra_user+fov_v/2) and (dec_user-fov_h/2)<float(star.dec)<(dec_user+fov_h/2):
                stars_in_fov.append(star)
        except ValueError:
            pass
    return stars_in_fov