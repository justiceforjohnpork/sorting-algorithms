def selectionSort(intList):
        for index in range(len(intList)):
            swapped = False
            smallestIndex = index
            for i in range (index,len(intList)):
                if intList[smallestIndex] > intList[i]:
                    smallestIndex = i
                    swapped = True

                
            if swapped == True:
                temp = intList[index]
                intList[index] = intList[smallestIndex]
                intList[smallestIndex] = temp
        
        return intList
    

        
