class CloudRow:

    # Variables
    _Count = 0
    _RowItems = None
    _InsertBefore = True
    
    # Remember the max importance value 
    _MaxImportance = 0

    def __init__(self):
        self._RowItems = []

    # Pass in the word, and how important it is in the cloud
    def AddItem(self, Word, Importance):
        # Set the max importance value
        self._MaxImportance = max(self._MaxImportance, Importance)

        # Set a value to know how less important the word is compared to _MaxImportance
        _LessImportance = self._MaxImportance - Importance

        #Insert the data either at the beginning or end of the array
        _WordData = (Word, _LessImportance)
        if(self._InsertBefore):
            self._RowItems.insert(0, _WordData)
        else:
            self._RowItems.append(_WordData)

        #Flip the flag for the next insertion
        self._InsertBefore = not self._InsertBefore

        #Update the count
        self._Count += 1
    
    def GetItemList(self):
        return self._RowItems