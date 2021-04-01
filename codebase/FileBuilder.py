import json
import os.path

class FileBuilder:

    # Location of the base html
    _BaseHtmlLocation = None

    def __init__(self):
        self.SetBaseHtmlLocation()

    def SetBaseHtmlLocation(self):
        with open('package.json') as f:
            ConfigData = json.load(f)
            if ('html' in ConfigData.keys()):
                self._BaseHtmlLocation = ConfigData["html"]
            else:
                raise Exception('No base html file was specified. Unable to build cloud.')

    # Build the file to display the word cloud to the user
    def BuildWordCloudFile(self, _CloudData):
        # Build a string to contain the cloud as an html
        _CloudStr = ''
        for Row in _CloudData:
            _RowStr = ''

            # Insert the words into a new row
            for WordData in Row.GetItemList():
                _RowStr += '<span class="word step-{Step}">{Word}</span>'.format(Word = WordData[0], Step = WordData[1])

            # Insert the row in the _CloudStr
            _CloudStr += '<div class="wordRow">{WordList}</div>'.format(WordList = _RowStr)

        # Read in the html contents
        _FinalWordCloud = ''
        with open(self._BaseHtmlLocation) as f:
            _html = ''
            eof = False
            while(eof == False):
                _NextLine = f.readline()
                if(_NextLine):
                    _html += _NextLine.strip()
                else:
                    eof = True

        # Insert the data into the cloud
        _html = _html.replace('<!--CloudInsertion-->', _CloudStr)
        
        # Save the html to a file. Set the code to overwrite any existing data
        _DestinationFile = 'C:\\Users\\Sean\\Desktop\\output\\wordcloud.html'
        _WriteMode = 'w' if os.path.exists(_DestinationFile) else 'x'
        with open(_DestinationFile, _WriteMode) as d:
            d.write(_html)