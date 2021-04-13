import json
import os
import sys

from models.UserInput import UserInput
from codebase.WordCount import WordCount
from codebase.CloudBuilder import CloudBuilder
from codebase.FileBuilder import FileBuilder
from codebase.ReadInputs import ReadInputs

# Parse the inputs either from the command line or via the package.json
if(__name__ == '__main__'):
    # Read in the input data
    InputReader = ReadInputs()
    InputData = InputReader.ReadInputs()

    # Check if Source is valid. If so, send the source file to the word count algorithm
    # If not, throw an exception
    if(InputData != None and os.path.exists(InputData.SourceLocation)):

        # Pass to word count algorithm
        WordCountGenerator = WordCount(InputData)
        CountData = WordCountGenerator.ProcessWordCount()

        # Build the word cloud based on the counts
        ConstructCloud = CloudBuilder(CountData)
        ConstructCloud.BuildCloud()

        # Build the word cloud file to display to the user
        if(ConstructCloud.DoesCloudDataExist()):
            ConstructFile = FileBuilder(InputData)
            ConstructFile.BuildWordCloudFile(ConstructCloud.GetCloudModel())
        else:
            print('No words processed. Word cloud was not created.')
    else:
        raise Exception('Unable to read inputs to generate word cloud.')
