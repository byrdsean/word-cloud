import json
import os.path

class FileBuilder:

    def __init__(self, Inputs):
        self._Inputs = Inputs

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
        with open(self._Inputs.HtmlTemplate) as f:
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
        _DestinationFile = self._Inputs.OutputLocation + '\\wordcloud.html'
        _WriteMode = 'w' if os.path.exists(_DestinationFile) else 'x'
        with open(_DestinationFile, _WriteMode) as d:
            d.write(_html)

        # Read in the contents of the css file
        with open(self._Inputs.CssLocation) as f:
            _css = ''
            eof = False
            while(eof == False):
                _NextLine = f.readline()
                if(_NextLine):
                    _css += _NextLine.strip()
                else:
                    eof = True

        # Save the css to a file.
        _DestinationFileCss = self._Inputs.OutputLocation + '\\cloud.css'
        _WriteMode = 'w' if os.path.exists(_DestinationFileCss) else 'x'
        with open(_DestinationFileCss, _WriteMode) as d:
            d.write(_css)