import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
'''
TODO list: 
    develop calculation methods
    develop main loop that breaks CSV file into 28500 event lengths

'''

# Array for on/off neuromorphic camera values
on = []
# Array for on[] arrays
metaChunk = []
# Array for timestamp value of camera samples
timestamp = []


class dataChunk:
    def __init__(self, on, timestamp):
        self.duration = self.calcDuration()
        self.density = self.calcDensity()
        self.covariance = self.calcCovariance()
        self.dict = zip(on, timestamp)
        self.length = 28500


    def getDur(self):
        return

    def getDens(self):
        return

    def getCov(self):
        return

    def calcDuration(self):
        """Time covered by the entire CSV file"""
        return
    def calcDensity(self):
        """Density of events. Do on a per-chunk and whole-file basis"""
        return
    def calcCovariance(self):
        """Covariance of one chunk vs another"""
        return


# csvLocation = 'C:/Users/Admin/Desktop/WaveletAnalysis/wheelTest.csv'
csvLocation = 'wheelTest.csv'
normalizeTimestamps = True

with open(csvLocation) as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',')
    eventCount = 0          # How many events have been processed since last chunk creation
    chunkTemp = []          # Where partial chunks are stored during creation
    chunkLength = 28500     # Number of events in a chunk
    headerInfo = []         # Header titles

    for row in spamReader:
        if eventCount == chunkLength:   # Finalize chunk & append to metaChunk

            # Make timestamps in chunk start at 0
            if normalizeTimestamps:
                firstTime = chunkTemp[0][1]
                for i, _ in enumerate(chunkTemp):
                    chunkTemp[i][1] = chunkTemp[i][1] - firstTime

            metaChunk.append([chunkTemp])
            chunkTemp.clear()
            eventCount = 0

        try:
            chunkTemp.append([int(row[0]) == 1, int(row[1])])
            eventCount += 1
        except ValueError:
            # Header Info
            headerInfo = [row[0], row[1]]

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

print("Chunk count = " + str(len(metaChunk)))

for chunk in metaChunk:
    print("Printing chunk")
    print(chunk)
    for val in chunk:
        print(val)
