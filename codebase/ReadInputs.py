import json
import os

from models.UserInput import UserInput

class ReadInputs:

    #Model to contain the input data
    _Inputs = None

    #Variables to contain the name of the source properties
    _source = 'source'
    _html = 'html'
    _css = 'css'
    _outputLocation = 'outputLocation'
    _stopwords = 'stopwords'
    _maxWordsInCloud = 'MaxWordsInCloud'
    _maxStopwordLen = 'MaxStopwordLen'

    def __init__(self):
        self._Inputs = UserInput()

    # Get source location from package.json
    def ReadInputs(self):
        with open('package.json') as f:
            ConfigData = json.load(f)

            if('assests' in ConfigData.keys()):
                AssestsDict = ConfigData["assests"]

                # #Set the variables
                self._Inputs.SourceLocation = self.GetDictData(AssestsDict, self._source)
                self._Inputs.HtmlTemplate = self.GetDictData(AssestsDict, self._html)
                self._Inputs.CssLocation = self.GetDictData(AssestsDict, self._css)
                self._Inputs.OutputLocation = self.GetDictData(AssestsDict, self._outputLocation)
                self._Inputs.Stopwords = self.GetDictData(AssestsDict, self._stopwords)
                self._Inputs.MaxWordsInCloud = self.GetDictData(AssestsDict, self._maxWordsInCloud)
                self._Inputs.MaxStopwordLength = self.GetDictData(AssestsDict, self._maxStopwordLen)

        return self._Inputs

    # Get dictionary data
    def GetDictData(self, AssestsDict, key):
        return AssestsDict[key] if key in AssestsDict.keys() else None