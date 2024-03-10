from urllib.request import urlopen
import sys
import csv

link = "" #insert link "here"
f = urlopen(link)
fileName = f.read()
# print(type(myfile))
s = str(fileName, encoding='utf-8')
# print(type(s))
# print(s)
arr = ""
for x in s:
    while x != '/r/n':
        arr += x

#uncomment to use alternate method
        
# with open('nycCensus1.csv', 'w') as file:
#     writer = csv.writer(file)
#     for row in s:
#         if row == 'Close\n':
#             break
#         else:
#             x = row.rstrip().split(",")
#             writer.writerow(x)