import os
import re
from models.UserInput import UserInput
from codebase.StopWords import StopWords

class WordCount:

    # Variables
    _Counts = {}
    _CaseInsensitive = True
    _StopWordObj = None         # Object to parse stop words
    _NonAlpha = None            # Regular expression to find non-alphanumeric characters
    _MaxClassCount = 10         # Maximum count used as a class in the cloud

    def __init__(self, Inputs):
        #Set the vars
        self._Inputs = Inputs
        self._StopWordObj = StopWords(Inputs, LimitOnLength = False)
        self._NonAlpha = re.compile('[^a-z0-9]', flags = re.IGNORECASE)

        if(self._Inputs == None or self._Inputs.SourceLocation is None or not os.path.exists(self._Inputs.SourceLocation)):
            raise Exception('No source location specified. Exiting program')

    # Begin processing the text from the word count file
    def ProcessWordCount(self):
        # Keep a count of the total words processed, and the maximum number of count seen
        Total = 0
        MaxCount = 0

        # Read in the file line by line, and process the data
        with open(self._Inputs.SourceLocation) as f:
            eof = False
            while(eof == False):
                NextLine = f.readline()
                if(NextLine):
                    CountNumbers = self.SetWordCount(NextLine)
                    Total += CountNumbers[0]
                    MaxCount = max(MaxCount, CountNumbers[1])
                else:
                    eof = True
        
        # Get the keys sorted by their counts in descending order
        # https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
        SortedTerms = sorted( self._Counts.items(), key = lambda kv: (-kv[1][1], kv[0]) )

        # Take the max number of words for the cloud, if any
        if(self._Inputs.MaxWordsInCloud != None):
            SortedTerms = SortedTerms[0:self._Inputs.MaxWordsInCloud]
        
        # Set the cloud classes
        CloudClass = self._MaxClassCount
        Previous = None
        for x in SortedTerms:
            if(Previous == None):
                Previous = x[1][1]

            # If the current importance is less that the previous, decrement the class
            if(x[1][1] < Previous):
                Previous = x[1][1]
                CloudClass = CloudClass - 1
                if(CloudClass < 0):
                    CloudClass = 0
            
            # Set the class
            x[1][2] = CloudClass

        # Store the data into an object to return
        CountData = {
            "TotalWords" : Total,
            "MaxCount" : MaxCount,
            "SortedTerms" : SortedTerms
        }
        return CountData

    # Process an individual line of data, and set the word counts
    def SetWordCount(self, Line):
        WordsSeen = 0
        MaxCount = 0
        for x in Line.split(' '):
            
            # Parse the word:
            # 1. Remove leading and trailing spaces
            # 2. Remove non-alphanumeric characters
            x = x.strip()
            x = self._NonAlpha.sub('', x)
            
            if(0 < len(x) and not self._StopWordObj.IsStopWord(x)):
                key = x.lower() if self._CaseInsensitive else x

                # Attempt to: check if 'x' is a key in the dictionary, and return the value
                # If there is no value, return a default
                toUpdate = self._Counts.get(key, [x, 0, 0])
                toUpdate[1] += 1
                self._Counts[key] = toUpdate
                MaxCount = max(MaxCount, toUpdate[1])

                # Increment the number of words seen
                WordsSeen += 1
        
        return WordsSeen, MaxCount