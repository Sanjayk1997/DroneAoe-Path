import csv
import os
import xlsxwriter
from collections import OrderedDict
from coordinates import extractCoord
from progressbar import ProgressBar
from dist import calcPOI

aoe = float(input("Enter the Area of Effect(metres):"))

bar = ProgressBar()

assetlist = os.listdir("poiassets")

filenames = os.listdir("images")
filenames.sort()
imgCoord = []

print ("Computing")

for name in filenames:
    if name.endswith(".JPG") or name.endswith(".jpg"):
        individualData = extractCoord(name)
        imgCoord.append(individualData)

workbook = xlsxwriter.Workbook('excel data/dronePOI.xlsx')
path = workbook.add_worksheet()
row = 0
col = 0
count = 0



print ("Writing to File")

for assets in assetlist:
    poi = csv.reader(open('poiassets/' + assets, 'r'))
    poilist = list(poi)
    path.write(row,col,assets)
    row += 1

    for each in bar(poilist[1:]):
        path.write(row,col,str(each[0]))
        for imagepts in imgCoord:
            distance = calcPOI(each[2],each[1],imagepts[1],imagepts[2])
            if (distance<aoe):
                col+=1
                path.write(row,col,imagepts[0])
                count += 1
        row += 1
        col = 0

workbook.close()
print ("Done")
print ("Entries Made :")
print (count)
