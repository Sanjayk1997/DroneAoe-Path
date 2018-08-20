def calcDist(s1,d1,d2):
    import geopy.distance

    source = s1[0]
    source = source.split(",")

    coords_1 = (float(source[1]),float(source[0]))
    coords_2 = (d1, d2)


    distance = geopy.distance.distance(coords_1, coords_2).m

    return distance

def calcPOI(s1,s2,d1,d2):
    import geopy.distance


    coords_1 = (float(s1),float(s2))
    coords_2 = (d1, d2)


    distance = geopy.distance.distance(coords_1, coords_2).m

    return distance
