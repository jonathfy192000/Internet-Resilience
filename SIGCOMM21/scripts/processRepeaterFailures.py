import os
import sys
import random
import numpy


def processNodeAndLinkFailures (
        nodeToCablesDict, cableToLevelDict, cabRepCount, filePrefix, 
        level_1_fail_prob, level_2_fail_prob, level_3_fail_prob ):

    allDataFilename = filePrefix + "-allData.txt"
    print(cabRepCount)
    with open(allDataFilename, 'w') as allDataFile:
        #open txt file for failed cable IDs
        if os.path.exists("Failed Cables/failedCables.txt"):
            os.remove("Failed Cables/failedCables.txt")

        thisfailedCables = open("Failed Cables/failedCables.txt", "w")
        #set for not including duplicate cables
        setFailed = set()
        #end block

        # Tests for 3 repeater distances 50, 100, and 150
        #testing
        for dist in range(0,3): 
            currStatsFilename = filePrefix + "-stats-" + str((dist+1) * 50) + ".txt"
            with open(currStatsFilename, 'a') as currStatsFile:
                linksPerc = []
                nodesPerc = []
                for i in range(10):
                    failedDict = {}
                    failedCables = 0
                    for cable in cabRepCount:
                        failedDict[cable] = 0
                        repCount = cabRepCount[cable][dist]
                        level = cableToLevelDict[cable]
                        prob = 0.0
                        if (level == 1):                # 60-90 degree latitude
                            prob = level_1_fail_prob
                        elif (level == 2):              # 40-60 degree latitude
                            prob = level_2_fail_prob
                        else:                           # 0-40 degree latitude
                            prob = level_3_fail_prob
        
                        # for each repeater in the cable, we check if it fails under the given probability
                        if repCount > 0: 
                            for rep in range(repCount):
                                rand = random.uniform(0, 1)
                                if rand < prob:
                                    failedDict[cable] = failedDict[cable] + 1
        
                        # if at least one repeater fails, the cable is marked as failed
                        if failedDict[cable] > 0:
                            setFailed.add(cable)#add unique cable IDs that failed to set
                            failedCables = failedCables + 1
            
                    disconNodes = 0
                    for node in nodeToCablesDict:
                        totalConnect = len(nodeToCablesDict[node])
                        currConnect = totalConnect
                        for cable in nodeToCablesDict[node]:
                            if (cable in failedDict):
                                if failedDict[cable] > 0:
                                    currConnect = currConnect - 1
        
                        # if all connected links fail, the node is disconnected
                        if currConnect == 0:
                            disconNodes = disconNodes + 1
            
                    allDataFile.write('{} {} {} {} {} {} {} {}\n'.format((dist+1) * 50, prob, failedCables, len(cabRepCount), 
                        failedCables*1.0/len(cabRepCount), disconNodes, len(nodeToCablesDict), disconNodes*1.0/len(nodeToCablesDict)))
                    linksPerc.append(failedCables*1.0/len(cabRepCount))
                    nodesPerc.append(disconNodes*1.0/len(nodeToCablesDict))

                currStatsFile.write('{} {} {} {} {} {}\n'.format((dist+1) * 50, prob, 
                    numpy.mean(linksPerc), numpy.std(linksPerc), numpy.mean(nodesPerc), numpy.std(nodesPerc)))

        #write all the ID's to the .txt file
        for elem in setFailed:
            thisfailedCables.write(str(elem) + "\n")  # My Code: add the cable to the failedCables IDs
        thisfailedCables.close()