import json
import os
import sys

from models.UserInput import UserInput
from codebase.WordCount import WordCount
from codebase.CloudBuilder import CloudBuilder

# Get source location from package.json
def _GetSourceLocationFromConfig():
    Source = None
    with open('package.json') as f:
        ConfigData = json.load(f)

        if('assests' in ConfigData.keys()):
            AssestsDict = ConfigData["assests"]
            Source = AssestsDict['source'] if 'source' in AssestsDict.keys() else None

    return Source

# Get source location from argv
def _GetSourceLocationFromArgv():
    Source = None
    if(1 < len(sys.argv)):
        Source = sys.argv[1]
    return Source

# Parse the inputs either from the command line or via the package.json
if(__name__ == '__main__'):
    # Try reading the source from command line
    Source = _GetSourceLocationFromArgv()

    # If Source = None, try reading the Source from the package
    if(Source == None):
        Source = _GetSourceLocationFromConfig()

    # Check if Source is valid. If so, send the source file to the word count algorithm
    # If not, throw an exception
    if(Source != None and os.path.exists(Source)):
        # print('{Source} exists!'.format(Source = Source))
        
        # Create input data
        InputData = UserInput()
        InputData.SourceLocation = Source

        # Pass to word count algorithm
        WordCountGenerator = WordCount(InputData)
        CountData = WordCountGenerator.ProcessWordCount()

        # Build the word cloud based on the counts
        ConstructCloud = CloudBuilder(CountData)
        ConstructCloud.BuildCloud()
    else:
        raise Exception('"{Source}" does not exist. Please enter a valid file location'.format(Source = Source))
