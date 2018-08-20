def extractCoord(name):
    from PIL import Image
    from PIL.ExifTags import TAGS

    metaData = {}
    latitude = []
    longitude = []
    individualData = []

    imgFile = Image.open("images/" + name)
    info = imgFile._getexif()

    for (tag, value) in info.items():
        tagname = TAGS.get(tag, tag)
        metaData[tagname] = value


    for n in metaData["GPSInfo"][2]:
        latitude.append(n[0])


    for n in metaData["GPSInfo"][4]:
        longitude.append(n[0])

    coordinateLat = float(latitude[0]) + float(latitude[1])/60 + float(latitude[2])/36000000
    coordinateLon = float(longitude[0]) + float(longitude[1])/60 + float(longitude[2])/36000000

    individualData.append(name)
    individualData.append(coordinateLat)
    individualData.append(coordinateLon)

    return individualData
