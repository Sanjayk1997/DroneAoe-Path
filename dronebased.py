import os
import pysrt
import xlsxwriter
from collections import OrderedDict
from coordinates import extractCoord
from dist import calcDist
from progressbar import ProgressBar


aoe = float(input("Enter the Area of Effect(metres):"))

bar = ProgressBar()


videolist = os.listdir("videos")
videolist.sort()
count = len(videolist)

class vidData:
    vidName = "default"
    timestamp = OrderedDict()
    data = OrderedDict()



vidObjs = [vidData() for i in range(50)]


for index in range(count):
    subs = pysrt.open('videos/' + videolist[index])
    vidObjs[index].vidName = videolist[index]
    for content in subs:
        content = str(content)
        content = content.split('\n')
        id = content[0]
        ts = content[1]
        dt = content[2][:-2]
        vidObjs[index].timestamp[id] = []
        vidObjs[index].timestamp[id].append(ts)
        vidObjs[index].data[id] = []
        vidObjs[index].data[id].append(dt)






filenames = os.listdir("images")

filenames.sort()
imgCoord = []


print ("Accessing SRT file/s ")

for name in filenames:
    if name.endswith(".JPG") or name.endswith(".jpg"):
        individualData = extractCoord(name)
        imgCoord.append(individualData)

workbook = xlsxwriter.Workbook('excel data/dronePath.xlsx')
path = workbook.add_worksheet()
row = 0
col = 0
count = 0

print ("Computing")


print ("Writing Data to file ")

for object in vidObjs:
    if(object.vidName != "default"):
        path.write(row,col,object.vidName)
        row +=1
        for i in bar(object.data):
            path.write(row,col,str(object.timestamp[i]))
            for imagepts in imgCoord:
                distance = calcDist(object.data[i],imagepts[1],imagepts[2])
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
