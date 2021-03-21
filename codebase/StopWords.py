import json

class StopWords:

    # Variables
    _MaxStopwordLen = 3
    _StopWordList = set()
    _CaseInsensitive = False
    _LimitOnLength = False

    def __init__(self, CaseInsensitive, LimitOnLength):
        self._CaseInsensitive = CaseInsensitive
        self._LimitOnLength = LimitOnLength

        # Load the stop words from package.json
        with open('package.json') as p:
            PackageDict = json.load(p)

            # Add the stopwords to the list
            for word in PackageDict["stopwords"]:
                #Set variable to know if we should check the length of the work
                ValidLength = True
                if(self._LimitOnLength):
                    ValidLength = len(word) <= self._MaxStopwordLen

                # Insert the data if there is a valid length
                if(ValidLength):
                    InsertWord = word.lower() if self._CaseInsensitive else word
                    self._StopWordList.add(InsertWord)

    # Check if a word is a stopword
    def IsStopWord(self, value):
        CheckValue = value.lower() if self._CaseInsensitive else value
        return True if CheckValue in self._StopWordList else False