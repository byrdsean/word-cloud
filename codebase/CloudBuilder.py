import random
from models.CloudRow import CloudRow

class CloudBuilder:

    # Stores the processed word data
    _CloudData = None

    # Model containing the words from the cloud
    # Will be an expanding 2D array
    _ModelCloud = None

    def __init__(self, CloudData):
        self._CloudData = CloudData
        self._ModelCloud = []

    def BuildCloud(self):
        if(self._CloudData != None and 0 < len(self._CloudData["SortedTerms"])):
            #Randomly sort the array, then insert the data
            random.shuffle(self._CloudData["SortedTerms"])

            _CurrentIndex = 0
            _InsertBefore = True
            for x in self._CloudData["SortedTerms"]:
                #Insert the word
                #1. Check if the code is at the end of ModelCloud. 
                #   If so, insert a new array either at the beginning or end
                #2. Insert the a word into the current array
                #3. Loop to the next word

                _NextWord = x[1][0]
                _Importance = x[1][1]

                #1. Check if the code is at the end of ModelCloud. 
                #   If so, insert a new array either at the beginning or end
                if(_CurrentIndex == len(self._ModelCloud)):
                    _UpdateRow = CloudRow()

                    if(_InsertBefore):
                        self._ModelCloud.insert(0, _UpdateRow)
                    else:
                        self._ModelCloud.append(_UpdateRow)
                    
                    #Insert the value
                    _UpdateRow.AddItem(_NextWord, _Importance)

                    #Update the variables for the next iteration
                    _InsertBefore = not _InsertBefore
                    _CurrentIndex = 0
                else:
                    #Insert the data, then update the index for the next iteration
                    self._ModelCloud[_CurrentIndex].AddItem(_NextWord, _Importance)
                    _CurrentIndex = (_CurrentIndex % len(self._ModelCloud)) + 1

    # Check if cloud model data exists
    def DoesCloudDataExist(self):
        _Exists = True if self._ModelCloud != None and 0 < len(self._ModelCloud) else False
        return _Exists

    # Returns the process cloud data
    def GetCloudModel(self):
        return self._ModelCloud