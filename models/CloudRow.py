class CloudRow:

    # Variables
    _Count = 0
    _RowItems = None
    _InsertBefore = True

    def __init__(self):
        self._RowItems = []

    def AddItem(self, Value):
        #Insert the data either at the beginning or end of the array
        if(self._InsertBefore):
            self._RowItems.insert(0, Value)
        else:
            self._RowItems.append(Value)

        #Flip the flag for the next insertion
        self._InsertBefore = not self._InsertBefore

        #Update the count
        self._Count += 1