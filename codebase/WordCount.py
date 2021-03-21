import os
from models.UserInput import UserInput
from codebase.StopWords import StopWords

class WordCount:

    # Variables
    _Counts = {}
    _MaxWordsInCloud = 20
    _StopWordObj = None

    def __init__(self, Inputs):
        #Set the vars
        self._Inputs = Inputs
        self._StopWordObj = StopWords(CaseInsensitive=True, LimitOnLength = False)

        if(self._Inputs == None or self._Inputs.SourceLocation is None or not os.path.exists(self._Inputs.SourceLocation)):
            raise Exception('No source location specified. Exiting program')

    # Begin processing the text from the word count file
    def ProcessWordCount(self):
        # Read in the file line by line, and process the data
        with open(self._Inputs.SourceLocation) as f:
            eof = False
            while(eof == False):
                NextLine = f.readline()
                if(NextLine):
                    self.SetWordCount(NextLine)
                else:
                    eof = True
        
        # Get the keys sorted by their counts in descending order
        # https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
        SortedTerms = sorted( self._Counts.items(), key = lambda kv: (-kv[1], kv[0]) )

        # Take the max number of words for the cloud, if any
        if(self._MaxWordsInCloud != None):
            SortedTerms = SortedTerms[0:self._MaxWordsInCloud]
        



        print(SortedTerms)

    # Process an individual line of data, and set the word counts
    def SetWordCount(self, Line):
        for x in Line.split(' '):
            x = x.strip()
            if(0 < len(x) and not self._StopWordObj.IsStopWord(x)):
                # Attempt to: check if 'x' is a key in the dictionary, and return the value
                # If there is no value, return a default
                self._Counts[x]  = self._Counts.get(x, 0) + 1