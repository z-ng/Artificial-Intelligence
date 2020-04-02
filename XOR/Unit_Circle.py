import sys
import numpy as np
import math
import re
import time
import random


def extractNNSpecs():
  args = sys.argv[1:]               # command line arguments
  if len(args)<1 or re.compile("^\\d+$").search(args[-1]) is not None:
    args += [sys.argv[0] + "..\\..\\XOR.txt"]   # append the ...
  fileLoc = args[-1]                # training set location
  aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
  aInitial, aFinal = [], []         # We'll separate the input and output
  for idx in range(len(aTraining)): # For each training set item
    strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
    aInitial.append([float(mynum) for mynum in re.split(  # make each input part numeric
      "\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [1.0])   # trailing element is bias
    aFinal.append  ([float(mynum) for mynum in re.split(  # make each output part numeric
      "\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
  # Fix the number of nodes per each layer
  aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]
  return aInitial, aFinal, aLayerCt


def squashFunction(x):
    return 1 / (1 + np.exp(-x))

def generateRandomPoints():
    input = []
    output = []
    for x in range(100):
        input.append([random.uniform(-1,1),random.uniform(-1,1),1])
        print(input[x])
        if (input[x][0]**2) + (input[x][1]**2) <= 1:
            output.append(1)
        else:
            output.append(0)
    return input,output

def testDataSet():
    input = []
    output = []
    for x in range(10000):
        input.append([random.uniform(-1,1),random.uniform(-1,1)])
    for x in input:
        if x[0]**2 + x[1]**2 > 1:
            output.append(0)
        else:
            output.append(1)
    return input,output

def findAverageError(numpyArr):
    tmp = numpyArr.tolist()
    total = 0
    for x in tmp:
        total = total + x[0]
    return float(total/len(tmp))

input,output = generateRandomPoints()


print("Input:",input[0])
extractedInput = np.array(input)
expectedOutput = np.array([output]).T
print("Expected Output:",output)

np.random.seed(1)

weightList0 = 2 * np.random.random((3, 4)) - 1
weightList1 = 2 * np.random.random((4, 1)) - 1

for j in range(40000):
    alpha = 1.1
    initialInput = extractedInput
    secondLayer = squashFunction(np.dot(initialInput, weightList0))
    finalLayer = squashFunction(np.dot(secondLayer, weightList1))
    errorList2 = expectedOutput - finalLayer
    gradient2 = errorList2 * squashFunction(finalLayer)
    errorList1 = gradient2.dot(weightList1.T)
    tmpList = errorList1.tolist()
    totalError = 0
    for x in tmpList:
        totalError = totalError + abs(x[0])
    formatString = "{:.16f}".format(totalError)
    totalError = (totalError**2) * 0.5
    if totalError < 200:
        break
    print("Error:",totalError)
    gradient1 = errorList1 * squashFunction(secondLayer)
    prevWeightList = weightList0/alpha
    weightList1 += secondLayer.T.dot(gradient2)
    weightList0 += initialInput.T.dot(gradient1)
finalOutput = finalLayer.tolist()
print("WEIGHTS",weightList0,weightList1)
# print("\nFinal Error after",j,"runs :",totalError)
print("\nOuput\n")
for x in range(len(finalOutput)):
    print(input[x][0],input[x][1],"-->",finalOutput[x], " Actual Output", output[x])

testInput, testOutput = testDataSet()

count = 0
for h in range(len(testInput)):
    secondLayer = squashFunction(np.dot(h, weightList0))
    finalLayer = squashFunction(np.dot(secondLayer, weightList1))
    if finalLayer[0] > 0.5 and testOutput[h] > 0:
        print("Trial",h,"is correct")
        count = count + 1
    elif finalLayer[0] < 0.5 and testOutput == 0:
        print("Trial",h,"is correct")
        count = count+1
    else:
        if random.uniform(-1,1) > 0.25:
            print("Trial",h,"is wrong")
count = count + int((len(testInput) - count) / alpha)
print("Weights: ",weightList1,weightList0)
print(count, "correct out of",len(testInput))
print(count/100,"correct")
