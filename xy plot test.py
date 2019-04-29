import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
'''
TODO list: 
    develop calculation methods
    develop main loop that breaks CSV file into 28500 event lengths

'''

#array for on/off neuromorphic camera values
on=[]
#array for on[] arrays
metaOn={}
#array for timestamp value of camera samples
timestamp=[]

class dataChunk:
    def __init__(self, on, timestamp):
        duration=calcDuration()
        density=calcDensity()
        covariance=calcCovariance()
        dict=zip(on, timestamp)
        length=28500

    def getDur():
        return self.duration

    def getDens():
        return self.density

    def getCov():
        return self.covariance

    def calcDuration():
        return duration
    def calcDensity():
        return density
    def calcCovariance(): 
        return covariance



with open('C:/Users/Admin/Desktop/WaveletAnalysis/wheelTest.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     myCount=0
     loopCount=0
     innerOn={}
     for row in spamreader:
        if myCount==28500:
            metaOn[loopCount]=[innerOn]
            myCount=0
            loopCount+=1 
            
        #on.append(row[0])
        #timestamp.append(row[1])
        try:
            innerOn[myCount]=[int(row[0]), int(row[1])]
        except:
            continue
        
        myCount+=1
        '''
        try:
            on[-1]=int(on[-1])
            timestamp[-1]=int(timestamp[-1])
            metaOn[-1]=[int(row[0]), int(row[1])]
        except:
            continue
        '''

# grab header values from csv
#eventTitle=on.pop(0)
#timeStampTitle=timestamp.pop(0)

# remove stray startup value
#del on[0:2]
#del timestamp[0:2]

# normalize time stamps
'''
TODO test loop functionality with dictionary metaOn
firstTime=timestamp[0]
for x in range(len(timestamp)):
    timestamp[x]=timestamp[x]-firstTime

timestampslice=timestamp[0:60]
onslice=on[0:60]
plt.scatter(timestampslice, onslice)
plt.show()
'''
for x in metaOn:
    print (x)
    for y in metaOn[x]:
        print(y,':', metaOn[x][y])